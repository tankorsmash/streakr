# streakr
Scrapes Github for a user's contributions total and streak. 

I don't think there's an API to use, and calculating it up by hand would take too much work.

### Usage
    python streakr.py streak tankorsmash
    >>> tankorsmash's current streak: 2 days

    python streakr.py contribs tankorsmash
    >>> tankorsmash's contributions: 123 total


### Requirements

BeautifulSoup4, python-requests, argh

    pip install beautifulsoup4 requests argh
