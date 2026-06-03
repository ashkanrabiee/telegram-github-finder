"""GitHub API service for repository search."""

import logging
from typing import List, Dict, Any
import httpx
from config import Config

logger = logging.getLogger(__name__)


class GitHubService:
    """Service to interact with GitHub REST API."""

    def __init__(self):
        self.headers = {
            "Authorization": f"token {Config.GITHUB_TOKEN}",
            "Accept": "application/vnd.github.v3+json",
        }
        self.per_page = Config.GITHUB_SEARCH_PER_PAGE

    async def search_repositories(self, query: str) -> List[Dict[str, Any]]:
        """
        Search GitHub repositories using the provided query.

        Args:
            query: GitHub search query string.

        Returns:
            List of repository dictionaries with relevant fields.

        Raises:
            Exception: On rate limit or other API errors.
        """
        url = f"{Config.GITHUB_API_BASE_URL}/search/repositories"
        params = {"q": query, "per_page": self.per_page, "sort": "stars", "order": "desc"}

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, headers=self.headers, params=params)
                response.raise_for_status()

                data = response.json()
                items = data.get("items", [])

                # Parse and format repository data
                repositories = []
                for repo in items:
                    # Construct ZIP download URL using default branch
                    default_branch = repo.get("default_branch", "main")
                    zip_url = f"https://github.com/{repo['full_name']}/archive/refs/heads/{default_branch}.zip"

                    repositories.append({
                        "name": repo.get("name", "بدون نام"),
                        "full_name": repo.get("full_name", ""),
                        "description": repo.get("description") or "توضیحاتی وجود ندارد",
                        "stars": repo.get("stargazers_count", 0),
                        "language": repo.get("language") or "نامشخص",
                        "url": repo.get("html_url", ""),
                        "zip_url": zip_url,
                    })

                logger.info(f"Found {len(repositories)} repositories for query: '{query}'")
                return repositories

            except httpx.HTTPStatusError as e:
                if e.response.status_code == 403:
                    # Check for rate limit message
                    if "rate limit" in str(e.response.text).lower():
                        logger.error("GitHub API rate limit exceeded")
                        raise Exception("محدودیت درخواست‌های گیت‌هاب به پایان رسیده است. لطفاً چند دقیقه دیگر تلاش کنید.")
                logger.error(f"GitHub API error: {e}")
                raise Exception(f"خطا در ارتباط با گیت‌هاب: {e.response.status_code}")
            except httpx.RequestError as e:
                logger.error(f"Network error calling GitHub API: {e}")
                raise Exception("خطای شبکه. لطفاً اتصال اینترنت خود را بررسی کنید.")

    async def get_repository_details(self, full_name: str) -> Dict[str, Any]:
        """
        Get detailed information about a single repository (for future features).

        Args:
            full_name: Repository full name (owner/repo).

        Returns:
            Repository details.
        """
        url = f"{Config.GITHUB_API_BASE_URL}/repos/{full_name}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()