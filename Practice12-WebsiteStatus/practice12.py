import urllib.request
website = input("Enter a website (example: https://google.com): ")

try:
    response = urllib.request.urlopen(website, timeout=5)
    print(website, "is working. Status code:", response.status)
except Exception:
   print(website, "is not working or cannot be reached.")
