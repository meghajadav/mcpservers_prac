from mcp.server.fastmcp import FastMCP

mcp = FastMCP('weather')

@mcp.tool
async def get_weather(location:str)->str:
    return 'New York weather is pleasant.'