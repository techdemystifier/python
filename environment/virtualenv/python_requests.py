import requests

if __name__ == '__main__':
    r = requests.get('https://reqbin.com/echo')
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.text)
