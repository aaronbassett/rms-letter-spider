import httpx
from bs4 import BeautifulSoup

github_usernames = []
response = httpx.get('https://rms-support-letter.github.io/')

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.select('ol li a'):
        url = link.get('href')

        if url.find("https://github.com") != -1:
            github_usernames.append(url.strip("/").split("/")[-1])

print(sorted(github_usernames))
