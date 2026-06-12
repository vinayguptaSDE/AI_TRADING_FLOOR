import os
from dotenv import load_dotenv
from market import is_paid_polygon, is_realtime_polygon

load_dotenv(override=True)

brave_env = {"BRAVE_API_KEY": os.getenv("BRAVE_API_KEY")}
polygon_api_key = os.getenv("POLYGON_API_KEY")

# The MCP server for the Trader to read Market Data

if is_paid_polygon or is_realtime_polygon:
    market_mcp = {
        "command": "python",
        "args": ["--from", "git+https://github.com/polygon-io/mcp_polygon@v0.1.0", "mcp_polygon"],
        "env": {"POLYGON_API_KEY": polygon_api_key},
    }
else:
    market_mcp = {"command": "python", "args": ["market_server.py"]}


# The full set of MCP servers for the trader: Accounts, Push Notification and the Market

trader_mcp_server_params = [
    {"command": "python", "args": ["accounts_server.py"]},
    {"command": "python", "args": ["push_server.py"]},
    market_mcp,
]

# The full set of MCP servers for the researcher: Fetch, Brave Search and Memory



