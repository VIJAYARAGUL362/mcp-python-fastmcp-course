# FastMCP Feed Search Server 📡

An open-standard [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server built in Python using **FastMCP**. This server enables AI assistants (such as Claude Desktop, Cursor, and GitHub Copilot) to search web RSS/Atom feeds and retrieve YouTube channel video updates dynamically.

---

## 🛠️ Features

* **Web Feed Search (`search_feed`):** Parses and searches any RSS/Atom web feed by query term, stripping raw HTML tags for clean LLM context.
* **YouTube Feed Integration (`get_youtube_feed`):** Queries or retrieves the latest public videos from any YouTube channel using its Channel ID.
* **Dual Transport Ready:** Configured for local `STDIO` execution or network-accessible `HTTP/SSE` streaming.
* **FastMCP Cloud Compatible:** Ready for serverless continuous deployment via FastMCP Cloud.

---

## 📦 Tech Stack & Prerequisites

* **Python 3.10+**
* **[FastMCP](https://github.com/jlowin/fastmcp):** Python framework for building MCP servers.
* **[feedparser](https://github.com/kurtmckee/feedparser):** RSS/Atom parsing library.

---

## 🚀 Getting Started Locally

### 1. Clone the repository
```bash
git clone [https://github.com/VIJAYARAGUL362/mcp-python-fastmcp-course.git](https://github.com/VIJAYARAGUL362/mcp-python-fastmcp-course.git)
cd mcp-python-fastmcp-course
