"""Premium Now-Playing / queue thumbnail generator.

Composites the fetched song artwork into a FIXED circular placeholder on a
locally-stored template (bot/assets/now_playing_template.png). The template is
loaded from disk once and cached in memory; it is NEVER fetched at runtime and
NEVER modified — only the circular artwork region changes.

The placeholder circle was measured ONCE from the template and hard-coded below
(_ART_X/_ART_Y/_ART_D); it is not recomputed per song. Artwork is centre-cropped
to a square (object-fit: cover), masked to a smooth circle, resized to the exact
placeholder diameter, and pasted at the fixed coordinates — sitting inside the
template's decorative rim.
"""
from __future__ import annotations

import asyncio
import io
import logging
import os

import aiohttp
from PIL import Image, ImageDraw

logger = logging.getLogger("WarbornMusic.thumbnail")

_TEMPLATE_PATH = os.path.join(
    os.path.dirname(__file__), "..", "assets", "now_playing_template.png"
)

# Fixed artwork circle inside the template's rim (top-left X/Y + diameter),
# measured once from the 640x360 template. Do NOT recompute per song.
_ART_X, _ART_Y, _ART_D = 4, 60, 218
_SS = 4  # mask supersampling → smooth anti-aliased circle edge

_template = None  # cached RGBA Image, loaded once


def _load_template() -> Image.Image:
    global _template
    if _template is None:
        _template = Image.open(_TEMPLATE_PATH).convert("RGBA")
    return _template


def _circular(art_bytes: bytes) -> Image.Image:
    """Centre-crop artwork to a square, resize to the placeholder diameter, and
    apply a smooth circular alpha mask (object-fit: cover, no borders)."""
    art = Image.open(io.BytesIO(art_bytes)).convert("RGBA")
    w, h = art.size
    s = min(w, h)
    left, top = (w - s) // 2, (h - s) // 2
    art = art.crop((left, top, left + s, top + s))
    big = _ART_D * _SS
    art = art.resize((big, big), Image.LANCZOS)
    mask = Image.new("L", (big, big), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, big - 1, big - 1), fill=255)
    art = art.resize((_ART_D, _ART_D), Image.LANCZOS)
    mask = mask.resize((_ART_D, _ART_D), Image.LANCZOS)
    art.putalpha(mask)
    return art


def _compose(art_bytes) -> bytes:
    """Paste the circular artwork onto a fresh copy of the cached template and
    export high-quality PNG bytes. Template-only when art_bytes is falsy."""
    tpl = _load_template().copy()
    if art_bytes:
        try:
            tpl.alpha_composite(_circular(art_bytes), (_ART_X, _ART_Y))
        except Exception:
            logger.exception("thumbnail: artwork composite failed — template only")
    out = io.BytesIO()
    tpl.save(out, "PNG")
    return out.getvalue()


def _yt_candidates(url: str):
    """For an i.ytimg URL, prefer max resolution then fall back to the sizes
    that always exist. Any other URL is used as-is."""
    if "i.ytimg.com" in url:
        base = url.rsplit("/", 1)[0]
        return [f"{base}/maxresdefault.jpg", f"{base}/sddefault.jpg", f"{base}/hqdefault.jpg"]
    return [url]


async def _fetch(url):
    if not url:
        return None
    for cand in _yt_candidates(url):
        try:
            async with aiohttp.ClientSession() as sess:
                async with sess.get(cand, timeout=aiohttp.ClientTimeout(total=8)) as resp:
                    if resp.status == 200:
                        data = await resp.read()
                        if len(data) > 1000:  # skip YouTube's tiny 404 placeholder
                            return data
        except Exception as exc:
            logger.debug("thumbnail fetch %s failed: %s", cand, exc)
    return None


async def generate(artwork_url):
    """Return a BytesIO PNG of the composited thumbnail (named for Telegram
    upload). Falls back to the template-only image when artwork can't be
    fetched. Never raises; returns None only if even the template fails."""
    try:
        art = await _fetch(artwork_url)
        data = await asyncio.to_thread(_compose, art)
    except Exception:
        logger.exception("thumbnail.generate failed — trying template only")
        try:
            data = await asyncio.to_thread(_compose, None)
        except Exception:
            logger.exception("thumbnail.generate: template load failed")
            return None
    bio = io.BytesIO(data)
    bio.name = "now_playing.png"
    return bio
