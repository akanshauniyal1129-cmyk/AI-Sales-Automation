from duckduckgo_search import DDGS

def search_company(company_name):
    query=f"{company_name} latest news technology awards"
    results=[]
    with DDGS() as ddgs:
        search_results=ddgs.text(query, max_results=5)
        for result in search_results:
            results.append({"title": result["title"], "link": result["href"], "snippet": result["body"]})
    return results