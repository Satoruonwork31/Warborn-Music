<div align="center">

# ⚡ Raiden Music Bot

A modern, high-performance Telegram music bot built for speed, quality, and reliability.

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Telegram-26A5E4.svg)

</div>

---

## ✨ Features

- 🎵 High-quality music playback
- 🔎 Fast song search
- 📃 Queue management
- ⏯️ Play, Pause, Resume & Skip
- 🔁 Loop support
- 🎚️ Volume control
- 🖼️ Beautiful UI cards
- ⚡ Fast response times
- 🔒 Stable and reliable
- 🛠️ Regular updates

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/Satoruonwork31/Raiden-Music-Bot.git
cd Raiden-Music-Bot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure your environment variables and start the bot.

---

## ⚙️ Configuration

Create a `.env` file and add your credentials.

```env
API_ID=
API_HASH=
BOT_TOKEN=
STRING_SESSION=
MONGO_URI=
OWNER_ID=
```

---

## 🎧 Commands

| Command | Description |
|---------|-------------|
| `/play` | Play a song |
| `/pause` | Pause playback |
| `/resume` | Resume playback |
| `/skip` | Skip current song |
| `/stop` | Stop playback |
| `/queue` | Show queue |
| `/volume` | Change volume |
| `/ping` | Check bot latency |
| `/help` | Show help menu |

---

## 📂 Project Goals

Raiden Music Bot aims to provide a fast, elegant, and feature-rich music experience on Telegram while maintaining clean code and an easy-to-use interface.

Future updates may include:

- Smart recommendations
- Playlist support
- Lyrics
- Audio filters
- Web Dashboard
- Multi-language support
- Enhanced queue UI
- Better streaming performance

---

## 🤝 Contributing

Contributions, feature requests, and bug reports are welcome.

Feel free to open an Issue or submit a Pull Request.

---

## 📜 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for details.

---

## ❤️ Credits

Developed and maintained by **Satoruonwork31**.

Special thanks to everyone who supports the project.

---

<div align="center">

### ⭐ If you like this project, don't forget to leave a star!

Made with ❤️ for the Telegram community.

</div>

# 🚀 Getting Started

Follow these steps to set up and run Raiden Music Bot.

---

## 1. Clone the Repository

```bash
git clone https://github.com/Satoruonwork31/Raiden-Music-Bot.git
cd Raiden-Music-Bot
```

---

## 2. Install Dependencies

Make sure you have **Python 3.10 or newer** installed.

Install all required packages:

```bash
pip install -r requirements.txt
```

---

## 3. Create a Telegram Bot

1. Open **@BotFather** on Telegram.
2. Send `/newbot`.
3. Follow the instructions.
4. Copy the **Bot Token**.

Example:

```
BOT_TOKEN=1234567890:AA...
```

---

## 4. Get Telegram API Credentials

Visit:

https://my.telegram.org

Login using your Telegram account.

Go to:

**API Development Tools**

Create a new application and copy:

- API_ID
- API_HASH

Example:

```
API_ID=12345678
API_HASH=0123456789abcdef0123456789abcdef
```

---

## 5. Generate a String Session

Generate a Pyrogram String Session using any trusted session generator compatible with your Pyrogram version.

Copy the generated session.

Example:

```
STRING_SESSION=AQF...
```

---

## 6. Create a MongoDB Database

Create a free MongoDB cluster.

Copy your connection URI.

Example:

```
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/database
```

---

## 7. Create the Environment File

Inside the project folder create a file named:

```
.env
```

Paste the following:

```env
# Telegram
API_ID=
API_HASH=
BOT_TOKEN=
STRING_SESSION=

# Database
MONGO_URI=

# Owner
OWNER_ID=

# Optional
LOG_GROUP_ID=
SUPPORT_CHAT=
UPDATE_CHANNEL=
```

Fill every value with your own credentials.

---

## 8. Start the Bot

Run:

```bash
python main.py
```

or

```bash
python3 main.py
```

If your project uses another startup file, replace `main.py` with the correct filename.

---

# ☁️ Hosting

Raiden Music Bot can be hosted on:

- VPS (Recommended)
- Railway
- Koyeb
- Render
- Pella
- Docker
- Local Machine (24/7 PC)

Simply copy the same environment variables from your `.env` file into your hosting provider's Environment Variables section.

---

# 🔑 Environment Variables

| Variable | Description |
|----------|-------------|
| API_ID | Telegram API ID |
| API_HASH | Telegram API Hash |
| BOT_TOKEN | Telegram Bot Token |
| STRING_SESSION | Pyrogram User Session |
| MONGO_URI | MongoDB Database URL |
| OWNER_ID | Telegram User ID of the Bot Owner |
| LOG_GROUP_ID | Group where bot logs are sent (Optional) |
| SUPPORT_CHAT | Support group username (Optional) |
| UPDATE_CHANNEL | Updates channel username (Optional) |

---

# 🛠 Troubleshooting

### Bot doesn't start

- Make sure Python version is supported.
- Install all requirements.
- Verify every environment variable.
- Ensure your MongoDB URI is valid.

---

### Invalid Bot Token

Create a new token from **@BotFather** and update your `.env` file.

---

### Database Error

Check your MongoDB URI and verify that your IP/network has access to the database.

---

### String Session Invalid

Generate a new String Session using the same Telegram account that will act as the assistant account.

---

# ❤️ Need Help?

If you encounter any issues while setting up the bot, open a GitHub Issue or join the support group for
