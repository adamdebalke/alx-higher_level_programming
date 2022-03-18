#!/usr/bin/python3
"""
Takes in URL and email, sends POST request using given parameters,
displays body of response decoded in utf-8
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    response = requests.post(argv[1], data={'email': argv[2]})
    print(response.text)
