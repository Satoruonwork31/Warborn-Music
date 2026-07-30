"""/start — welcome card with configurable branding and links.

Everything shown here (bot name, banner image, and the Support / Updates
/ Owner / Add-me buttons) comes from config.py, which reads the .env
file. Nothing is hardcoded: a button whose link is left blank in .env is
simply omitted, so a freshly forked bot works with only the required
credentials filled in.
"""

from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.config import (
    BOT_NAME,
    BOT_USERNAME,
    OWNER_URL,
    START_IMAGE,
    SUPPORT_CHAT,
    UPDATE_CHANNEL,
    normalize_link,
)


def _start_caption(user) -> str:
    mention = user.mention
    user_id = user.id
    return (
        f"✦  <b>Welcome to {BOT_NAME}</b> 🎵\n\n"
        f"Hey {mention}!\n"
        f"I'm {BOT_NAME}, your music companion for Telegram voice chats.\n\n"
        "⚡ Fast  •  🎶 High-quality audio\n"
        "🧠 Smart queue  •  🔥 Powerful playback\n"
        "👥 Group friendly  •  🎧 24/7 music\n\n"
        "━━━━━━━━━━━━━━\n\n"
        "👤 <b>Your Profile</b>\n"
        f"❤️‍🔥 User: {mention}\n"
        f"🆔 ID: <code>{user_id}</code>\n\n"
        "Use /help to view all available commands."
    )


async def _resolve_add_url(client) -> str:
    """Build the 'Add me to your group' deep-link.

    Prefers the BOT_USERNAME override; otherwise resolves the bot's own
    username at runtime so this works without any configuration.
    """
    username = BOT_USERNAME
    if not username:
        try:
            me = await client.get_me()
            username = me.username or ""
        except Exception:
            username = ""
    return f"https://t.me/{username}?startgroup=true" if username else ""


async def _start_keyboard(client) -> InlineKeyboardMarkup:
    """Assemble the inline keyboard from configured links only.

    Each optional link is rendered as a button when set and skipped when
    blank, so no dead/placeholder buttons appear on an unconfigured fork.
    """
    rows: list[list[InlineKeyboardButton]] = []

    updates_url = normalize_link(UPDATE_CHANNEL)
    support_url = normalize_link(SUPPORT_CHAT)
    owner_url = normalize_link(OWNER_URL)

    top: list[InlineKeyboardButton] = []
    if updates_url:
        top.append(InlineKeyboardButton("📢 Updates", url=updates_url))
    if support_url:
        top.append(InlineKeyboardButton("💬 Support", url=support_url))
    if top:
        rows.append(top)

    if owner_url:
        rows.append([InlineKeyboardButton("👑 Owner", url=owner_url)])

    add_url = await _resolve_add_url(client)
    if add_url:
        rows.append([InlineKeyboardButton("➕ Add Me to Your Group", url=add_url)])

    rows.append(
        [InlineKeyboardButton("📚 Help & Commands", callback_data="help:0:home")]
    )
    return InlineKeyboardMarkup(rows)


@Client.on_message(filters.command("start") & filters.private)
async def start_command(client, message):
    from bot.utils.logchannel import log_bot_started
    await log_bot_started(client, message.from_user)
    await message.reply_photo(
        photo=START_IMAGE,
        caption=_start_caption(message.from_user),
        parse_mode=ParseMode.HTML,
        reply_markup=await _start_keyboard(client),
    )


@Client.on_callback_query(filters.regex(r"^start:home$"))
async def start_home_callback(client, callback_query):
    # Restore the welcome message — the "Back" button on the /help page.
    try:
        await callback_query.edit_message_caption(
            caption=_start_caption(callback_query.from_user),
            parse_mode=ParseMode.HTML,
            reply_markup=await _start_keyboard(client),
        )
    except Exception as exc:
        if "MESSAGE_NOT_MODIFIED" in str(exc).upper():
            await callback_query.answer()
            return
        await callback_query.answer(f"Update failed: {exc}", show_alert=True)
        return
    await callback_query.answer()
