"""OpenAI service for optimizing GitHub search queries."""

import logging
from openai import AsyncOpenAI
from config import Config

logger = logging.getLogger(__name__)


class AIService:
    """Service to interact with OpenAI API."""

    def __init__(self):
        self.client = AsyncOpenAI(api_key=Config.OPENAI_API_KEY)

    async def generate_github_query(self, user_input: str) -> str:
        """
        Convert natural language user request into an optimized GitHub search query.

        Args:
            user_input: The user's search request in Persian/English.

        Returns:
            A GitHub search query string.
        """
        system_prompt = """شما یک دستیار هوشمند هستید که درخواست کاربر برای پیدا کردن پروژه گیت‌هاب را به یک کوئری جستجوی بهینه‌شده گیت‌هاب تبدیل می‌کنید.
قوانین:
- فقط کوئری نهایی را برگردانید، بدون هیچ توضیح اضافی.
- از qualifierهای گیت‌هاب استفاده کنید: language, stars, topic, forks, etc.
- اگر کاربر زبان خاصی خواسته، از language استفاده کنید.
- اگر پروژه محبوب می‌خواهد، stars:>100 اضافه کنید.
- مثال: کاربر: "react dashboard" => "react dashboard topic:dashboard stars:>50"
- مثال: کاربر: "laravel ecommerce with payment" => "laravel ecommerce payment topic:ecommerce language:php stars:>50"
- کوئری نهایی باید به زبان انگلیسی باشد."""

        try:
            response = await self.client.chat.completions.create(
                model=Config.OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_input},
                ],
                temperature=Config.OPENAI_TEMPERATURE,
                max_tokens=100,
            )
            query = response.choices[0].message.content.strip()
            logger.info(f"OpenAI generated query: '{query}' from input: '{user_input}'")
            return query
        except Exception as e:
            logger.error(f"OpenAI API error: {e}")
            # Fallback: use the original user input as query
            return user_input