import requests

def get_status(url):
    response = requests.get(url)
    return response.status_code

if __name__ == "__main__":
    print(get_status("https://example.com"))
