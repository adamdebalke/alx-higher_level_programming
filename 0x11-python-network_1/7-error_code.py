#!/usr/bin/python3
"""
Takes URL, sends request to URL,
displays body of response decoded in utf-8
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    response = requests.get(argv[1])
    code = response.status_code
    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(response.text)
