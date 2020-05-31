from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

class Parse:
    # получение исходной страницы
    def get_content(self, url):
        html = urlopen(url)
        bsObj = BeautifulSoup(html.read(), "html.parser")
        links = []
        # Выборка ссылок со страницы
        for link in bsObj.find_all('a'):
            link_name = get_link_name(link)
            link = link.get('href')
            if link.startswith("http"):
                links.append([link, link_name])
            else:
                break
        return links

# Удаление тегов из <a></a>
def get_link_name(tag):
    try:
        regex = re.compile(".*?>(.*)<")
        result = re.findall(regex, str(tag))
        if "<" in result[0]:
            result[0] = '???'
        if not result[0]:
            result[0] = '???'
        return result[0]
    except Exception:
        pass
