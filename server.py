from fastmcp import FastMCP
from tools import (
    get_course_info,
    calculate_final_grade,
    days_until_deadline,
    gpa_to_letter,
)

mcp = FastMCP(name="Course Assistant MCP Server")

mcp.tool()(get_course_info)
mcp.tool()(calculate_final_grade)
mcp.tool()(days_until_deadline)
mcp.tool()(gpa_to_letter)

if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=8000)
