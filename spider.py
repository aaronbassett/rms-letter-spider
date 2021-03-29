import httpx
from bs4 import BeautifulSoup

github_usernames = []
response = httpx.get('https://rms-open-letter.github.io/')


def find_github_username_end_index(string, start_index):
    i = start_index
    while i < len(string):
        if string[i] == ',' or string[i] == ')' or string[i] == ' ' or string[i] == '/' or string[i] == '\n':
            return i
        i = i + 1

    return None


if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.select('ol li a'):
        url = link.get('href')

        if url.find("https://github.com") != -1:
            github_usernames.append(url.strip("/").split("/")[-1])

    for text in soup.select('ol li:-soup-contains("@")'):
        raw_text = text.getText()
        github_username_start = raw_text.find('@')
        github_username_end = find_github_username_end_index(raw_text, github_username_start)
        github_usernames.append(raw_text[github_username_start + 1:github_username_end])

print(github_usernames)
