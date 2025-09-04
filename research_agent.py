from base_agent import Agent
import urllib.request
import xml.etree.ElementTree as ET


class ResearchAgent(Agent):
    def __init__(self):
      self.base_url = 'http://export.arxiv.org/api/query'
      self.ns = {'arxiv':'http://www.w3.org/2005/Atom'}

    def run():
        pass
    
    def search(self, query, start=0, max_results=1):
        query_safe = urllib.parse.quote(query)

        url = f"{self.base_url}?search_query=all:{query_safe}&start={start}&max_results={max_results}"

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
