# Gift Text Parser

This is a microservice that uses a REST API to receive, parse, and return multiple
gift ideas submitted as a single string. It is intended to work with my wish list
web app.

## Setup and Usage

### Formatting the Submitted String

Each gift idea is separated by one or more blank lines, i.e. "\n\n".
A gift idea comprises three fields:

- what: required, it names the gift idea
- link: optional, a URL to the item or that explains it
- details: optional, additional information that may be relevant to the gift idea

Thus, an example submission string could be:

```
"""
t-shirt
size medium

Structure and Interpretation of Computer Programs
https://bookshop.org/p/books/structure-and-interpretation-of-computer-programs-gerald-jay-sussman/11620466?ean=9780262510875
2nd ed.
"""
```

The result would be:

```json
[
  { "what": "t-shirt", "link": null, "details": "size medium" },
  {
    "what": "Structure and Interpretation of Computer Programs",
    "link": "https://bookshop.org/p/books/structure-and-interpretation-of-computer-programs-gerald-jay-sussman/11620466?ean=9780262510875",
    "details": "2nd ed."
  }
]
```

The parser always treats the first line of a new paragraph as the "what".
It will determine whether the next additional non-blank line begins with "https://".
The rest of the lines will be included as details.
Thus, URLs may be included in the details portion of the gift idea as plain text.
