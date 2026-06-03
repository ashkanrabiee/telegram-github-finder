"""Command handlers for /start, /help, /about."""

import logging
from telegram import Update
from telegram.ext import ContextTypes
from utils.formatters import format_welcome_message, format_help_message, format_about_message

logger = logging.getLogger(__name__)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /start command."""
    user = update.effective_user
    welcome_msg = format_welcome_message()
    await update.message.reply_text(
        f"{welcome_msg}\n\n👋 سلام {user.first_name} عزیز!",
        parse_mode="Markdown",
    )
    logger.info(f"User {user.id} started the bot")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /help command."""
    help_msg = format_help_message()
    await update.message.reply_text(help_msg, parse_mode="Markdown")
    logger.info(f"User {update.effective_user.id} requested help")


async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle /about command."""
    about_msg = format_about_message()
    await update.message.reply_text(about_msg, parse_mode="Markdown", disable_web_page_preview=True)
    logger.info(f"User {update.effective_user.id} requested about info")