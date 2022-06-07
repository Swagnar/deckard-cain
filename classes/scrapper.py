from bs4 import BeautifulSoup
from more_itertools import first
from requests_html import AsyncHTMLSession

# initialize helper class
asession = AsyncHTMLSession()

class Scrapper:
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0'}

    async def return_page(self, url):
        
        print('miele')
        response = await asession.get(url)
        await response.html.arender(timeout=15, sleep=5)
        #article = response.html.find('#filter-results', first=True)
        print(response.html.html)
        return response

    async def return_build_articles(self, userClass, instance):
        
        url = f"https://immortal.maxroll.gg/category/build-guides#classes%3D%5Bdi-{userClass}%5D%26metas%3D%5Bdi-{instance}%5D"

        
        
        articles = await self.return_page(url)

        #print(articles.html.links)
        # articlesLink = articles.html.find('#filter-results', first=True)

        # print(articlesLink.absolute_links)
        
        
        
        
        # response = requests.get(url, headers=self.headers)
        # content = response.content

        # soup = BeautifulSoup(content, 'html.parser')
        # results = soup.find_all('div', id='filter-results')
        # print(results)