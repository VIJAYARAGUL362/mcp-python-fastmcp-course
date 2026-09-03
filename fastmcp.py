import feedparser
from fastmcp import FastMCP
from typing import Dict,Any
mcp = FastMCP(name="fast_mcp_feed_search")


@mcp.tool(
    name="search_feed",
    description="Searches a feed for a given query and returns the results."
)
def search_web_feed(query:str,feed_url:str,max_results:int=5)->list[Dict[str,Any]]:
    """Searches a feed for a given query and returns the results."""
    feed = feedparser.parse(feed_url)
    results = []
    for entry in feed.entries:
        title = entry.get("title","")
        description = entry.get("description","")
        if query.lower() in title.lower() or query.lower() in description.lower():
            results.append({
                "title":title,
                "description":description,
                "link":entry.get("link","")
            })

        if len(results) >= max_results:
            break

    if not results:
        return [{"message":"No results found"}]


    return results

@mcp.tool(
    name="get_youtube_feed",
    description="get the relevant feed based on your query"
)
def get_youtube_feed(query:str,channel_id:str,max_results:int=5)->list[Dict[str,Any]]:
    """Get the relevant feed based on your query on the channel_id you are proviing"""
    if not channel_id:
        return [{"message":"please provide a channel_id"}]
    if not query:
        return [{"message":"please provide a query"}]

    feed_url = f"https://www.youtube.com/feeds/videos.xml?channel_id={channel_id}"
    feed = feedparser.parse(feed_url)
    if not feed:
        return [{"message":"provide a valide channel_id"}]
    results = []
    for entry in feed.entries:
        title = entry.get("title","")
        if query.lower() in title.lower():
            results.append({
                "title":title,
                "link":entry.get("link","")
            })
        if len(results) >= max_results:
            break

    return results if results else [{"message":"latest videos","videos":[{"title":entry.get("title",""),"link":entry.get("link","")} for entry in feed.entries[:max_results]]}]


if __name__ == "__main__":
    mcp.run(transport="http")