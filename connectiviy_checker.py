import requests

def main(url:str):
    if url.startswith("http://") or url.startswith("https://"):
        response = requests.get(url)
    else:
        try:
            response = requests.get("https://"+url)
        except:
            response = requests.get("http://"+url)
    return response.url, response.status_code

if __name__ == '__main__':
    print("Hello, This is a connectivity checker ....")
    url_input = input("Enter your url > ")
    print("Checking connectivity...")
    url, code = main(url_input)
    print(f"your connection code for {url} is : {code}")