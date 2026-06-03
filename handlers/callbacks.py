"""Callback query handler for navigation buttons."""

import logging
from telegram import Update
from telegram.ext import ContextTypes
from handlers.search import send_repository

logger = logging.getLogger(__name__)


async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handle inline keyboard button presses (prev/next).

    Updates the current index and refreshes the displayed repository.
    """
    query = update.callback_query
    user_id = update.effective_user.id
    data = query.data

    # Get current state
    repositories = context.user_data.get("search_results", [])
    current_index = context.user_data.get("current_index", 0)

    if not repositories:
        await query.answer("⚠️ نتیجه‌ای یافت نشد. لطفاً دوباره جستجو کنید.", show_alert=True)
        return

    # Update index based on button press
    if data == "prev":
        new_index = current_index - 1
        if new_index < 0:
            await query.answer("🔚 شما در اولین پروژه هستید!", show_alert=True)
            return
        context.user_data["current_index"] = new_index
    elif data == "next":
        new_index = current_index + 1
        if new_index >= len(repositories):
            await query.answer("🏁 شما در آخرین پروژه هستید!", show_alert=True)
            return
        context.user_data["current_index"] = new_index
    else:
        await query.answer()
        return

    # Send the updated repository (edit message)
    await send_repository(update, context, user_id, query.message.chat_id)
    logger.info(f"User {user_id} navigated to index {context.user_data['current_index']}")