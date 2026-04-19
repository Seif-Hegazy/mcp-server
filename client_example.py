from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

response = client.responses.create(
    model="gpt-4o-mini",
    input="What is the course info for AI and how many credit hours is it?",
    tools=[
        {
            "type": "mcp",
            "server_label": "course_server",
            "server_url": "YOUR_PUBLIC_MCP_SERVER_URL",
            "allowed_tools": [
                "get_course_info",
                "calculate_final_grade",
                "days_until_deadline",
                "gpa_to_letter"
            ],
            "require_approval": "never"
        }
    ]
)

print(response.output_text)
