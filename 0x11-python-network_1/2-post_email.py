#!/usr/bin/python3
"""
Takes in URL and email, sends POST request using given parameters,
displays body of response decoded in utf-8
"""
if __name__ == "__main__":
    from urllib import parse, request
    from sys import argv

    value = {'email': argv[2]}
    data = parse.urlencode(value)
    data = data.encode('utf-8')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
