cat > README.md << 'EOF'
# 🤖 AI-Powered GitHub Project Finder Telegram Bot

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://python.org)
[![python-telegram-bot](https://img.shields.io/badge/Telegram-Bot-blue.svg)](https://github.com/python-telegram-bot/python-telegram-bot)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991.svg)](https://openai.com)
[![GitHub API](https://img.shields.io/badge/GitHub-API-181717.svg)](https://docs.github.com/en/rest)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A smart Telegram bot that finds GitHub repositories using natural language (Persian/English), powered by **OpenAI GPT-4o-mini** and **GitHub REST API**.  
The bot speaks Persian by default, making it easy for Persian-speaking developers to discover open-source projects.

---

## 📖 Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Windows](#windows)
  - [Ubuntu / Linux](#ubuntu--linux)
- [Configuration](#configuration)
- [Running the Bot](#running-the-bot)
- [Usage](#usage)
- [Commands](#commands)
- [Project Structure](#project-structure)
- [Future Enhancements](#future-enhancements)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Persian Guide (راهنمای فارسی)](#persian-guide-راهنمای-فارسی)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🧠 **AI-Powered Query** | Converts your natural language (Persian/English) into an optimized GitHub search query using OpenAI |
| 🔍 **GitHub Search** | Searches repositories, sorted by stars, via GitHub REST API |
| 📦 **Rich Results** | Shows: name, description, stars, language, repository URL, ZIP download link |
| ⬅️➡️ **Navigation** | Inline buttons in Persian to browse results without re-searching |
| 💾 **In-Memory Cache** | Stores results per user – no repeated API calls while navigating |
| 🗣️ **Persian UI** | All messages, menus, buttons, help texts are in Persian (Farsi) |
| 🛡️ **Error Handling** | Manages rate limits, empty results, network failures, invalid API keys |
| 📝 **Logging** | Full logging system for monitoring and debugging |
| ⚡ **Async Architecture** | Non-blocking, fast responses |

---

## 🎬 Demo

**User sends:**  


**Bot replies (first result):**  
```text
🔍 نتیجه 1 از 24

📁 نام: laravel-ecommerce
📝 توضیحات: A complete e-commerce platform built with Laravel and Vue.js
⭐ ستاره‌ها: 1,234
💻 زبان: PHP
🔗 لینک پروژه: https://github.com/example/laravel-ecommerce
📦 لینک دانلود ZIP: https://github.com/example/laravel-ecommerce/archive/main.zip


📋 Prerequisites
Python 3.9 or higher

Telegram Bot Token – get it from @BotFather

OpenAI API Key – get it from OpenAI Platform

GitHub Personal Access Token – create at GitHub Settings → Tokens
Required scopes: repo, public_repo


🔧 Installation
1-Windows

Clone the repository

git clone https://github.com/yourusername/telegram-github-finder.git
cd telegram-github-finder


2-Create a virtual environment

python -m venv venv
venv\Scripts\activate

3-Install dependencies

pip install -r requirements.txt

4-Create .env file (see Configuration)

5-Run the bot

python bot.py

Ubuntu / Linux


1-Update system & install Python & Git

sudo apt update
sudo apt install python3 python3-pip python3-venv git -y

2-Clone the repository

git clone https://github.com/yourusername/telegram-github-finder.git
cd telegram-github-finder

3-Create a virtual environment

python3 -m venv venv
source venv/bin/activate

4-Install dependencies

pip install -r requirements.txt

5-Create .env file (see below)

6-Run the bot

python3 bot.py

⚙️ Configuration
Create a .env file in the project root with the following content:

```bash
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
OPENAI_API_KEY=your_openai_api_key_here
GITHUB_TOKEN=your_github_personal_access_token_here
```

⚠️ Never commit .env to version control. Add it to .gitignore.

🚀 Running the Bot
After configuration, simply run:

python bot.py

2025-01-15 10:00:00 - root - INFO - Bot is starting...


Now open Telegram, find your bot, and start chatting!

📱 Usage
Commands
Command	Description
/start	Welcome message and introduction
/help	Detailed usage guide
/about	Information about the bot


Searching
Send any text describing the project you need – Persian or English.

Examples:

react dashboard with dark mode

python telegram bot template

قالب مدیریت لاراول

admin panel django

What happens behind the scenes:

1-OpenAI generates an optimized GitHub query (e.g., react dashboard topic:dashboard stars:>50)

2-GitHub API returns matching repositories (sorted by stars)

3-Bot displays the first result with interactive buttons

4-You can navigate without re-searching


📂 Project Structure

```bash
telegram-github-finder/
├── bot.py                 # Main entry point
├── config.py              # Environment variables & validation
├── ai_service.py          # OpenAI API wrapper
├── github_service.py      # GitHub API wrapper
├── handlers/
│   ├── __init__.py
│   ├── commands.py        # /start, /help, /about
│   ├── search.py          # Text message handler
│   └── callbacks.py       # Inline button callbacks
├── keyboards/
│   └── inline.py          # Keyboard builder
├── utils/
│   ├── __init__.py
│   └── formatters.py      # Persian text formatting
├── requirements.txt
├── .env.example
└── README.md
```

🔮 Future Enhancements
The code is designed to be easily extended. Planned features:

🗄️ Database support (SQLite / PostgreSQL) – save search history, user favorites

⭐ User favorites – let users star repositories they like

📊 Download statistics – track most downloaded projects

🌍 Multi-language support – add English/Arabic interfaces

🔔 Scheduled searches – notify users about new repositories

To add a database, simply create a database.py module and integrate it in search.py and callbacks.py.


🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository

Create a feature branch (git checkout -b feature/amazing-feature)

Commit your changes (git commit -m 'Add amazing feature')

Push to the branch (git push origin feature/amazing-feature)

Open a Pull Request

Please ensure type hints and docstrings are included.

📄 License
Distributed under the MIT License. See LICENSE file for more information.


