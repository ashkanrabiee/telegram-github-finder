"""Persian text formatting utilities."""

from typing import Dict, Any


def format_repository_message(repo: Dict[str, Any], index: int, total: int) -> str:
    """
    Format a single repository as a Persian message.

    Args:
        repo: Repository dictionary containing name, description, stars, etc.
        index: Current index (1-based for display).
        total: Total number of repositories.

    Returns:
        Formatted Persian message string.
    """
    message = f"""
🔍 **نتیجه {index} از {total}**

📁 **نام:** {repo['name']}
📝 **توضیحات:** {repo['description']}
⭐ **ستاره‌ها:** {repo['stars']:,}
💻 **زبان:** {repo['language']}
🔗 **لینک پروژه:** {repo['url']}
📦 **لینک دانلود ZIP:** {repo['zip_url']}
"""
    return message.strip()


def format_welcome_message() -> str:
    """Return Persian welcome message for /start command."""
    return """
🤖 به **ربات جستجوی پروژه گیت‌هاب** خوش آمدید!

من با استفاده از هوش مصنوعی به شما کمک می‌کنم بهترین پروژه‌های گیت‌هاب را پیدا کنید.

🔍 **چطور کار می‌کند؟**
1. یک درخواست خود را به فارسی یا انگلیسی ارسال کنید
2. هوش مصنوعی آن را به یک کوئری بهینه گیت‌هاب تبدیل می‌کند
3. من پروژه‌های مرتبط را از گیت‌هاب جستجو می‌کنم
4. می‌توانید بین نتایج جابجا شوید و پروژه‌ها را دانلود کنید

✨ **مثال‌ها:**
• `laravel ecommerce`
• `react dashboard با دارک مود`
• `python telegram bot template`

از `/help` برای راهنمایی بیشتر استفاده کنید.
"""


def format_help_message() -> str:
    """Return Persian help message."""
    return """
📚 **راهنمای استفاده از ربات**

**دستورات:**
/start - شروع مجدد ربات و مشاهده پیام خوش‌آمدگویی
/help - نمایش این راهنما
/about - اطلاعات درباره ربات

**نحوه جستجو:**
متن دلخواه خود را ارسال کنید. مثال:
• `قالب مدیریت react`
• `سیستم احراز هویت laravel`
• `اسکرپر پایتون`

**دکمه‌های تعاملی:**
• ⬅️ پروژه قبلی - رفتن به پروژه قبلی در نتایج
• ➡️ پروژه بعدی - رفتن به پروژه بعدی
• 🌐 مشاهده در گیت‌هاب - باز کردن پروژه در مرورگر
• 📦 دانلود ZIP - دانلود مستقیم سورس کد پروژه

**نکات:**
• نتایج بر اساس تعداد ستاره مرتب می‌شوند
• هر جستجو حداکثر ۳۰ پروژه را نمایش می‌دهد
• برای جستجوی جدید، کافی است متن جدیدی ارسال کنید

در صورت بروز مشکل، بعد از چند دقیقه دوباره تلاش کنید.
"""


def format_about_message() -> str:
    """Return Persian about message."""
    return """
ℹ️ **درباره ربات**

نسخه: 1.0.0
توسعه‌دهنده: تیم هوش مصنوعی

این ربات با استفاده از:
• **python-telegram-bot** - کتابخانه ارتباط با تلگرام
• **OpenAI GPT-4** - هوش مصنوعی تبدیل درخواست
• **GitHub REST API** - جستجوی پروژه‌ها

✨ **امکانات آینده:**
• ذخیره پروژه‌های مورد علاقه
• تاریخچه جستجوها
• آمار دانلود
• پشتیبانی از زبان‌های دیگر

**لینک‌های مفید:**
• [مخزن پروژه در گیت‌هاب](https://github.com/example/project)
• [گزارش مشکل](https://github.com/example/project/issues)

از استفاده شما سپاسگزاریم! ❤️
"""