"""Handler for text messages (search requests)."""

import logging
from telegram import Update
from telegram.ext import ContextTypes
from ai_service import AIService
from github_service import GitHubService
from keyboards.inline import get_repo_navigation_keyboard
from utils.formatters import format_repository_message

logger = logging.getLogger(__name__)

# Initialize services
ai_service = AIService()
github_service = GitHubService()


async def search_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle user text messages as search queries.

    Stores results in user_data and displays the first result.
    """
    user_id = update.effective_user.id
    user_input = update.message.text.strip()

    # Send typing indicator
    await update.message.chat.send_action(action="typing")

    try:
        # Step 1: Generate optimized GitHub query using OpenAI
        logger.info(f"User {user_id} searching for: {user_input}")
        github_query = await ai_service.generate_github_query(user_input)
        await update.message.reply_text(f"🔍 در حال جستجوی پروژه‌های مرتبط با: `{github_query}`", parse_mode="Markdown")

        # Step 2: Search GitHub
        repositories = await github_service.search_repositories(github_query)

        # Step 3: Handle empty results
        if not repositories:
            await update.message.reply_text(
                "❌ هیچ پروژه‌ای با درخواست شما یافت نشد.\n"
                "لطفاً عبارت دیگری را امتحان کنید یا از کلمات عمومی‌تر استفاده کنید."
            )
            return

        # Step 4: Store results in user_data
        context.user_data["search_results"] = repositories
        context.user_data["current_index"] = 0

        # Step 5: Display first repository
        await send_repository(update, context, user_id=user_id, chat_id=update.effective_chat.id)

    except Exception as e:
        logger.error(f"Search error for user {user_id}: {e}")
        await update.message.reply_text(
            f"⚠️ خطا در انجام جستجو: {str(e)}\n"
            "لطفاً چند لحظه دیگر تلاش کنید یا با پشتیبانی تماس بگیرید."
        )


async def send_repository(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    user_id: int,
    chat_id: int,
) -> None:
    """
    Send the current repository to the user.

    Args:
        update: Update object (may be None for callback queries).
        context: Callback context.
        user_id: User ID for logging.
        chat_id: Chat ID to send message to.
    """
    repositories = context.user_data.get("search_results", [])
    current_index = context.user_data.get("current_index", 0)

    if not repositories:
        error_msg = "⚠️ نتیجه‌ای یافت نشد. لطفاً دوباره جستجو کنید."
        if update and update.callback_query:
            await update.callback_query.answer(error_msg)
            await update.callback_query.edit_message_text(error_msg)
        else:
            await context.bot.send_message(chat_id=chat_id, text=error_msg)
        return

    repo = repositories[current_index]
    message_text = format_repository_message(repo, current_index + 1, len(repositories))
    keyboard = get_repo_navigation_keyboard(repo["url"], repo["zip_url"])

    # Determine if we're editing an existing message or sending a new one
    if update and update.callback_query:
        # Edit existing message
        await update.callback_query.edit_message_text(
            text=message_text,
            reply_markup=keyboard,
            parse_mode="Markdown",
            disable_web_page_preview=True,
        )
        await update.callback_query.answer()
    else:
        # Send new message
        await context.bot.send_message(
            chat_id=chat_id,
            text=message_text,
            reply_markup=keyboard,
            parse_mode="Markdown",
            disable_web_page_preview=True,
        )