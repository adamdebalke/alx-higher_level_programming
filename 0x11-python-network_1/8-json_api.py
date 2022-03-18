#!/usr/bin/python3
"""
Takes a letter and sends POST request to
http://0.0.0.0:5000/search_user with letter as parameter
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    q = "" if len(argv) == 1 else argv[1]
    payload = {"q": q}

    rq = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        res = rq.json()
        if not res:
            print("No result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
