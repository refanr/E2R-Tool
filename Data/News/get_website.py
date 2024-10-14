from urllib.request import urlopen
import re

def get_website(url):
    response = urlopen(url)
    return response.read()

def get_urls(website):
    lst = re.findall(r'(https:\/\/nyr\.ruv\.is\/frettir\/innlent\/[^, ]+?)"', str(website))
    return lst

new_urls = []

with open("Data/News/urls.txt") as file:
    urls = file.readlines()
    for url in urls:
        website = get_website(url)
        new_url = get_urls(website)
        if len(new_url) > 0:
            new_urls.append(new_url[0])
        else:
            urls.remove(url)
    print(len(urls))

with open("Data/News/new_urls.txt", "a") as file:
    for url in new_urls:
        file.write(url + "\n")


