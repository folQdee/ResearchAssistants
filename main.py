import urllib.request
import re
import xml.etree.ElementTree as ET


class ResearchAgent:
    def __init__(self):
      self.base_url = 'http://export.arxiv.org/api/query'
      self.ns = {'arxiv':'http://www.w3.org/2005/Atom'}
    
    def search(self, query, start=0, max_results=1):
        # Кодируем query для URL
        query_safe = urllib.parse.quote(query)

        # Формируем URL с параметрами
        url = f"{self.base_url}?search_query=all:{query_safe}&start={start}&max_results={max_results}"

        # Запрос к arxiv
        data = urllib.request.urlopen(url)
        unfiltered = data.read().decode('utf-8')
        root = ET.fromstring(unfiltered)

        results = []
        for entry in root.findall('arxiv:entry', self.ns):
            title = entry.find('arxiv:title', self.ns).text.strip()
            summary = entry.find('arxiv:summary', self.ns).text.strip()
            link = entry.find('arxiv:id', self.ns)
            if link is not None:
                link = link.text
            results.append({
                "title": title,
                "summary": summary,
                "link": link
            })
        return results


if __name__=='__main__':
    agent = ResearchAgent()
    query = input("Введите тему для поиска: ")
    result = agent.search(query, 0, 1)
    for i, art in enumerate(result, 1):
        print(f"\n{i}. {art['title']}")
        print(f"Ссылка: {art['link']}")
        print(f"Аннотация: {art['summary'][:300]}...") 