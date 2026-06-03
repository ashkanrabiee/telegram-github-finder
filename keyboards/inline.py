"""Inline keyboard builders for repository navigation."""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_repo_navigation_keyboard(repo_url: str, zip_url: str) -> InlineKeyboardMarkup:
    """
    Create an inline keyboard with navigation and action buttons.

    Args:
        repo_url: GitHub repository URL.
        zip_url: Direct ZIP download URL.

    Returns:
        InlineKeyboardMarkup object.
    """
    keyboard = [
        [
            InlineKeyboardButton("⬅️ پروژه قبلی", callback_data="prev"),
            InlineKeyboardButton("➡️ پروژه بعدی", callback_data="next"),
        ],
        [
            InlineKeyboardButton("🌐 مشاهده در گیت‌هاب", url=repo_url),
            InlineKeyboardButton("📦 دانلود ZIP", url=zip_url),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)