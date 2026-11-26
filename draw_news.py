#!/usr/bin/env python3
"""Draw the 26 November 2026 news poster (1024x1024) from scratch.

A broadsheet front page: masthead, one lead story, a 2x2 grid of stories,
one bottom strip, and a source footer. All six stories were verified from
Reuters, BBC and The Hindu on 26 November 2026.
"""

import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 241, 229)
INK = (25, 23, 19)
RED = (166, 30, 30)
BLUE = (44, 74, 107)
GREY = (96, 90, 80)
RULE = (25, 23, 19)

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
SERIF_B = FONT_DIR + "DejaVuSerif-Bold.ttf"
SERIF = FONT_DIR + "DejaVuSerif.ttf"
SANS_B = FONT_DIR + "DejaVuSans-Bold.ttf"
SANS = FONT_DIR + "DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Wrap text to fit max_w pixels, word by word."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def tag_chip(draw, x, y, label):
    """Small filled tag with white bold text; returns width used."""
    fnt = font(SANS_B, 19)
    tw = draw.textlength(label, font=fnt)
    pad_x, pad_y = 10, 5
    draw.rounded_rectangle(
        [x, y, x + tw + 2 * pad_x, y + 30], radius=4, fill=BLUE
    )
    draw.text((x + pad_x, y + pad_y), label, font=fnt, fill=(255, 255, 255))
    return tw + 2 * pad_x

LEAD = {
    "tag": "SEOUL  |  RATES",
    "headline": "Bank of Korea lifts rate to 3.25%",
    "deck": "Resumes tightening after an October pause; AI exports keep "
            "growth brisk.",
    "source": "Reuters",
}

GRID = [
    {
        "tag": "ASIA  |  MARKETS",
        "headline": "Asian shares bounce back",
        "deck": "Nikkei up 1.6% and Kospi up 1.9% as Wall Street fights back "
                "from deep lows.",
        "source": "Reuters",
    },
    {
        "tag": "LONDON  |  EUROPE",
        "headline": "UK to publish new EU treaties",
        "deck": "Government set to publish the treaties agreed with the EU.",
        "source": "BBC",
    },
    {
        "tag": "HORMUZ  |  ENERGY",
        "headline": "Oil tops $94 as mines hit ships",
        "deck": "Brent at $94.71 after tankers strike Iranian mines in the "
                "Strait of Hormuz.",
        "source": "Reuters",
    },
    {
        "tag": "ARUNACHAL  |  DIPLOMACY",
        "headline": "India, China hold border talks",
        "deck": "High-level talks on border management and LAC issues, "
                "says the MEA.",
        "source": "The Hindu",
    },
]

BOTTOM = {
    "tag": "SYDNEY  |  BANKING",
    "headline": "ANZ dropped from NY Fed's FX list",
    "deck": "New York Fed removes ANZ from its foreign-exchange counterparties; "
            "CBA is now the only Australian lender on the list.",
    "source": "Reuters",
}


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead ------------------------------------------------------
    title = "THE WORLD TODAY"
    tf = font(SERIF_B, 82)
    tw = d.textlength(title, font=tf)
    d.text(((W - tw) / 2, 26), title, font=tf, fill=INK)
    date = "T H U R S D A Y   ·   2 6   N O V E M B E R   2 0 2 6"
    df = font(SANS_B, 26)
    dw = d.textlength(date, font=df)
    d.text(((W - dw) / 2, 122), date, font=df, fill=RED)
    d.line([(40, 162), (984, 162)], fill=RULE, width=4)
    d.line([(40, 170), (984, 170)], fill=RULE, width=1)

    # ---- lead story ----------------------------------------------------
    x0, y0 = 40, 192
    d.rectangle([x0, y0, x0 + 8, y0 + 118], fill=RED)
    tag_chip(d, x0 + 24, y0, LEAD["tag"])
    hf = font(SERIF_B, 46)
    y = draw_lines(
        d, wrap(d, LEAD["headline"], hf, 900), x0 + 24, y0 + 42, hf, INK, 54
    )
    sf = font(SANS, 22)
    y = draw_lines(
        d, wrap(d, LEAD["deck"], sf, 900), x0 + 24, y + 6, sf, GREY, 28
    )
    d.text((x0 + 24, y + 2), "— " + LEAD["source"], font=font(SANS_B, 19), fill=BLUE)
    d.line([(40, 356), (984, 356)], fill=RULE, width=2)

    # ---- 2x2 grid ------------------------------------------------------
    cols = [40, 524]
    rows = [378, 592]
    cell_w, cell_h = 460, 196
    for i, story in enumerate(GRID):
        cx = cols[i % 2]
        cy = rows[i // 2]
        tag_chip(d, cx, cy, story["tag"])
        hf2 = font(SANS_B, 31)
        y = draw_lines(
            d, wrap(d, story["headline"], hf2, cell_w), cx, cy + 42, hf2, INK, 37
        )
        sf2 = font(SANS, 20)
        y = draw_lines(
            d, wrap(d, story["deck"], sf2, cell_w), cx, y + 4, sf2, GREY, 26
        )
        d.text((cx, y + 2), "— " + story["source"], font=font(SANS_B, 18), fill=BLUE)
        if i % 2 == 0:
            d.line([(508, cy), (508, cy + cell_h)], fill=(200, 192, 172), width=1)
        if i < 2:
            d.line([(40, 576), (984, 576)], fill=(200, 192, 172), width=1)

    # ---- bottom strip --------------------------------------------------
    d.line([(40, 806), (984, 806)], fill=RULE, width=2)
    tag_chip(d, 40, 828, BOTTOM["tag"])
    hf3 = font(SANS_B, 32)
    y = draw_lines(
        d, wrap(d, BOTTOM["headline"], hf3, 944), 40, 870, hf3, INK, 38
    )
    sf3 = font(SANS, 21)
    draw_lines(
        d, wrap(d, BOTTOM["deck"], sf3, 944), 40, y + 4, sf3, GREY, 27
    )

    # ---- footer --------------------------------------------------------
    d.line([(40, 972), (984, 972)], fill=RULE, width=1)
    foot = "SIX STORIES VERIFIED FROM REUTERS  ·  BBC  ·  THE HINDU"
    ff = font(SANS_B, 17)
    fw = d.textlength(foot, font=ff)
    d.text(((W - fw) / 2, 984), foot, font=ff, fill=GREY)

    img.save("entry.png", "PNG", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
