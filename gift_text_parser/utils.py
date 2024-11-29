"""Utility functions for parsing text."""

import re

RE_SEP = re.compile(r"\n\n+")


def parse_text(text: str) -> list[dict[str, str | None]] | None:
    # Split into separate gift ideas based on consecutive newlines.
    if len(text) == 0:
        return None
    else:
        entries = RE_SEP.split(text)

    gifts = []

    # For each gift idea entry:
    for gift in entries:
        # Split off the "what"
        gift = gift.split("\n", maxsplit=1)
        what = gift[0]

        #   Verify it is < 256 characters.
        if len(what) > 255:
            what = what[0:255]

        # Are there additional lines?
        if len(gift) == 1:  # No.
            link = None
            details = None
        else:  # Yes.
            link, details = parse_extra(gift[1])

        gifts.append({"what": what, "link": link, "details": details})

    return gifts if len(gifts) > 0 else None


def parse_extra(text: str) -> tuple[str | None, str | None]:
    """Returns the link and details portions of the gift entry."""
    if text.startswith("https://"):
        # Includes a link, so split it off from the rest.
        text = text.split("\n", maxsplit=1)
        link = text[0]

        if len(text) > 1 and text[1].rstrip():
            details = text[1]
        else:
            details = None
    else:
        link = None
        text = text.rstrip()
        details = text if text else None

    return (link, details)
