#!/usr/bin/python3
"""
Takes in URL, sends request,
displays the value of X-Request-Id found in header
"""
if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from sys import argv
    url = Request(argv[1])
    with urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))
