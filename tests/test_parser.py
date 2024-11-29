"""Tests for the text parser."""

import pytest

from gift_text_parser.utils import parse_text


@pytest.mark.parametrize(
    ("input", "output"),
    (
        ["t-shirt", [{"what": "t-shirt", "link": None, "details": None}]],
        [
            "t-shirt\n\nSICP",
            [
                {"what": "t-shirt", "link": None, "details": None},
                {"what": "SICP", "link": None, "details": None},
            ],
        ],
        ["t-shirt\n", [{"what": "t-shirt", "link": None, "details": None}]],
        [
            "t-shirt\n\nSICP\n",
            [
                {"what": "t-shirt", "link": None, "details": None},
                {"what": "SICP", "link": None, "details": None},
            ],
        ],
    ),
)
def test_what(input: str, output: list[dict]):
    assert output == parse_text(input)


@pytest.mark.parametrize(
    ("input", "output"),
    (
        [
            "t-shirt\nhttps://example.com",
            [{"what": "t-shirt", "link": "https://example.com", "details": None}],
        ],
        [
            "t-shirt\n\nSICP\nhttps://bookshop.org/p/books/structure-and-interpretation-of-computer-programs-gerald-jay-sussman/11620466?ean=9780262510875",
            [
                {"what": "t-shirt", "link": None, "details": None},
                {
                    "what": "SICP",
                    "link": "https://bookshop.org/p/books/structure-and-interpretation-of-computer-programs-gerald-jay-sussman/11620466?ean=9780262510875",
                    "details": None,
                },
            ],
        ],
    ),
)
def test_what_link(input: str, output: list[dict]):
    assert output == parse_text(input)


@pytest.mark.parametrize(
    ("input", "output"),
    (
        [
            "t-shirt\nSize medium",
            [{"what": "t-shirt", "link": None, "details": "Size medium"}],
        ],
        [
            "t-shirt\nSize medium\nAny colors.",
            [{"what": "t-shirt", "link": None, "details": "Size medium\nAny colors."}],
        ],
        [
            "t-shirt\n\nSICP\n2nd ed.",
            [
                {"what": "t-shirt", "link": None, "details": None},
                {
                    "what": "SICP",
                    "link": None,
                    "details": "2nd ed.",
                },
            ],
        ],
    ),
)
def test_what_details(input: str, output: list[dict]):
    assert output == parse_text(input)


@pytest.mark.parametrize(
    ("input", "output"),
    (
        [
            "t-shirt\nhttps://example.com\nSize medium",
            [
                {
                    "what": "t-shirt",
                    "link": "https://example.com",
                    "details": "Size medium",
                }
            ],
        ],
        [
            "t-shirt\n\nSICP\nhttps://bookshop.org/p/books/structure-and-interpretation-of-computer-programs-gerald-jay-sussman/11620466?ean=9780262510875\n2nd ed.",
            [
                {"what": "t-shirt", "link": None, "details": None},
                {
                    "what": "SICP",
                    "link": "https://bookshop.org/p/books/structure-and-interpretation-of-computer-programs-gerald-jay-sussman/11620466?ean=9780262510875",
                    "details": "2nd ed.",
                },
            ],
        ],
        [
            "t-shirt\nhttps://example.com\nSize medium\n\nSICP\nhttps://bookshop.org/p/books/structure-and-interpretation-of-computer-programs-gerald-jay-sussman/11620466?ean=9780262510875\n2nd ed.",
            [
                {
                    "what": "t-shirt",
                    "link": "https://example.com",
                    "details": "Size medium",
                },
                {
                    "what": "SICP",
                    "link": "https://bookshop.org/p/books/structure-and-interpretation-of-computer-programs-gerald-jay-sussman/11620466?ean=9780262510875",
                    "details": "2nd ed.",
                },
            ],
        ],
    ),
)
def test_what_link_details(input: str, output: list[dict]):
    assert output == parse_text(input)
