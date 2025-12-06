from ddgs import DDGS

def perform_search(query: str) -> str:
    """
    Perform a web search and return the results using DDGS directly.
    """
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=5))
            if not results:
                return "No results found."
            
            # Format results
            formatted_results = []
            for r in results:
                formatted_results.append(f"Title: {r['title']}\nLink: {r['href']}\nSnippet: {r['body']}")
            
            return "\n\n".join(formatted_results)
    except Exception as e:
        return f"Error performing search: {str(e)}"
