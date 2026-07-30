"""Premium custom-emoji snippets (HTML) for message UIs.

Only IDs already proven to render for THIS bot (reused from start.py / help.py
/ play_actions, which display correctly) live here — an unknown custom-emoji
id makes Telegram reject the whole message. Each value is
``<emoji id="…">glyph</emoji>``; clients without premium show the glyph.

Use with ``parse_mode=ParseMode.HTML``. For status marks (✅/❌/🔒) use plain
unicode — always safe and needs no premium.
"""


import html as _html


def _e(eid: str, glyph: str) -> str:
    return f'<emoji id="{eid}">{glyph}</emoji>'


def mention(user) -> str:
    """HTML mention link. user.mention renders with the client's default parse
    mode, which isn't safe inside an explicit-HTML message, so build it here."""
    if user is None:
        return "someone"
    name = _html.escape(getattr(user, "first_name", None) or "user")
    return f'<a href="tg://user?id={user.id}">{name}</a>'


NOTE = _e("5994721794760642534", "🎵")
MUSIC = _e("5334653529741076580", "🎶")
HEAD = _e("5886268068035827289", "🎧")
BOLT = _e("6170427231802757303", "⚡")
FIRE = _e("5346334981792734939", "🔥")
BRAIN = _e("5278628322769654561", "🧠")
PEOPLE = _e("5861955787181525936", "👥")
USER = _e("5226810560250676186", "👤")
SHIELD = _e("4958900559139570572", "🛡")
CROWN = _e("6231116549919349944", "👑")
WAVE = _e("5816875690183631180", "👋")
GEAR = _e("5341715473882955310", "⚙️")
IDCARD = _e("5350427505805238170", "🆔")
DICE = _e("5972061723400605896", "🎲")
SPARKLE = _e("5271810272640643747", "🔮")
WAND = _e("5269617691836058799", "🪄")
CHAT = _e("5443038326535759644", "💬")
PLUS = _e("5030749344752468962", "➕")
MEGA = _e("4967957395331351254", "📢")
BOOK = _e("5033104253846029290", "📚")
