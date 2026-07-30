<div align="center">

# ⚡ Warborn Music

### 🎵 Powered by Raiden Music Bot

A modern, high-performance Telegram music bot framework built for speed, stability, and a beautiful user experience.

[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Telegram-26A5E4.svg)

⭐ If you enjoy this project, consider leaving a star!

</div>

---

# ✨ Features

- 🎵 High-quality audio playback
- 🔎 Fast YouTube search
- 📃 Interactive queue management
- ⏯️ Play, Pause, Resume & Skip
- 🔁 Loop support
- 🎚️ Volume control
- 🖼️ Beautiful media cards
- ⚡ Optimized performance
- 🔒 Stable and reliable
- 🌍 Multi-platform hosting support
- 🛠️ Regular updates
- 📦 Easy deployment

---

# 🚀 Getting Started

Follow these steps to set up **Warborn Music**.

---

## 1. Clone the Repository

```bash
git clone https://github.com/Satoruonwork31/Warborn-Music.git
cd Warborn-Music
```

---

## 2. Install Dependencies

Make sure **Python 3.10 or newer** is installed.

Install all required packages:

```bash
pip install -r requirements.txt
```

---

## 3. Create a Telegram Bot

1. Open **@BotFather**
2. Send:

```
/newbot
```

3. Follow the instructions.
4. Copy your **Bot Token**.

Example:

```
BOT_TOKEN=1234567890:AAxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## 4. Get Telegram API Credentials

Visit:

```
https://my.telegram.org
```

Log in using your Telegram account.

Go to:

```
API Development Tools
```

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

Generate a **Pyrogram String Session** using any trusted Pyrogram Session Generator compatible with your Pyrogram version.

Copy the generated session.

Example:

```
STRING_SESSION=AQFxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## 6. Create a MongoDB Database

Create a free MongoDB Atlas cluster.

Copy your MongoDB connection URI.

Example:

```
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/database
```

---

## 7. Configure Environment Variables

Create a file named:

```
.env
```

inside the project directory.

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

Fill in all required values before running the bot.

---

## 8. Run the Bot

```bash
python main.py
```

or

```bash
python3 main.py
```

If your project uses another startup file, replace **main.py** with the correct filename.

---

# ☁️ Hosting

Warborn Music is designed to run on a variety of hosting platforms.

### Officially Supported

- 🚄 Railway
- 💜 Heroku
- ☁️ Koyeb
- 🌐 Render
- 🐳 Docker
- 🖥️ VPS (Ubuntu/Debian recommended)
- 💻 Local Machine (Windows/Linux/macOS)
- ☁️ Any Linux server with Python support

Simply copy all values from your `.env` file into your hosting provider's **Environment Variables** section.

For Docker deployments, you can either use a `.env` file or pass the environment variables directly to your container.

---

## 📦 Deploy on Railway

1. Fork this repository.
2. Create a new Railway project.
3. Connect your GitHub repository.
4. Add all required Environment Variables.
5. Deploy the project.

---

## 💜 Deploy on Heroku

1. Fork this repository.
2. Create a new Heroku application.
3. Connect your GitHub repository.
4. Go to **Settings → Config Vars**.
5. Add all required Environment Variables.
6. Deploy the application.

---

## ☁️ Deploy on Koyeb

1. Create a Koyeb service.
2. Import your GitHub repository.
3. Configure the Environment Variables.
4. Deploy.

---

## 🌐 Deploy on Render

1. Create a new **Web Service**.
2. Connect your GitHub repository.
3. Configure the Environment Variables.
4. Deploy.

---

## 🖥️ Deploy on VPS

```bash
git clone https://github.com/Satoruonwork31/Warborn-Music.git
cd Warborn-Music

pip install -r requirements.txt

python main.py
```

For production deployments, it's recommended to use **systemd**, **PM2**, or **Docker** so the bot restarts automatically if it stops.

---

# 🔑 Environment Variables

| Variable | Description |
|-----------|-------------|
| API_ID | Telegram API ID |
| API_HASH | Telegram API Hash |
| BOT_TOKEN | Telegram Bot Token |
| STRING_SESSION | Pyrogram Assistant Session |
| MONGO_URI | MongoDB Database URI |
| OWNER_ID | Telegram User ID of the Bot Owner |
| LOG_GROUP_ID | Log Group ID (Optional) |
| SUPPORT_CHAT | Support Group Username (Optional) |
| UPDATE_CHANNEL | Updates Channel Username (Optional) |

---

# 🎧 Commands

| Command | Description |
|---------|-------------|
| `/play` | Play music |
| `/pause` | Pause playback |
| `/resume` | Resume playback |
| `/skip` | Skip current song |
| `/stop` | Stop playback |
| `/queue` | Show queue |
| `/loop` | Toggle loop mode |
| `/volume` | Adjust volume |
| `/ping` | Check bot latency |
| `/help` | Display help menu |

---

# 📂 Roadmap

Upcoming features include:

- 🎼 Spotify support
- 🎧 Apple Music support
- 📜 Lyrics
- ❤️ Favorites
- 📂 Playlists
- 🌍 Multi-language support
- 🖼️ Premium queue interface
- 🎨 Enhanced artwork generation
- 📊 Web Dashboard
- 🔔 Update notifier
- ⚡ Performance improvements

---

# 🤝 Contributing

Contributions are always welcome.

If you discover a bug, have a feature request, or would like to improve the project, feel free to open an **Issue** or submit a **Pull Request**.

---

# 🛠 Troubleshooting

### Bot doesn't start

- Verify Python version.
- Install all dependencies.
- Check every environment variable.
- Verify your MongoDB connection.
- Restart the bot after updating the configuration.

---

### Invalid BOT_TOKEN

Generate a new Bot Token using **@BotFather** and update your `.env` file.

---

### Invalid STRING_SESSION

Generate a new Pyrogram String Session using the same Telegram account that will act as the assistant account.

---

### Database Connection Failed

Check your MongoDB URI and ensure your database is accessible.

---

# 📜 License

This project is licensed under the **MIT License**.

See the **LICENSE** file for more information.

---

# ❤️ Credits

**Warborn Music** is maintained by **Satoruonwork31**.

Powered by **Raiden Music Bot**.

Special thanks to the open-source community and everyone who contributes to improving this project.

---

<div align="center">

## ⭐ Star this repository if you find it useful!

Made with ❤️ for the Telegram community.

</div>- 🔒 Stable and reliable
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
