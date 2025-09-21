from mcp.server.fastmcp import FastMCP

mcp = FastMCP('weather')

@mcp.tool()
async def get_weather(location:str)->str:
    return 'New York weather is pleasant.'


if __name__=='__main__':
    mcp.run(transport='streamable-http')