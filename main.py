from research_agent import ResearchAgent
from summarize_agent import SummarizerAgent


if __name__=='__main__':
    research_agent = ResearchAgent()
    summ_agent = SummarizerAgent()

    query = input("Введите тему для поиска: ")
    articles = research_agent.search(query, 0, 1)

    result = summ_agent.run(articles=articles)
    print(result)

    # for i, art in enumerate(result, 1):
    #     print(f"\n{i}. {art['title']}")
    #     print(f"Ссылка: {art['link']}")
    #     print(f"Аннотация: {art['summary']}") 