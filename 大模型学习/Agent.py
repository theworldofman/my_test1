# Agent就是一个可以自主行动的软件程序
import os
from openai import OpenAI
import json

client = OpenAI(
    api_key="sk-537f7b5a99eb453399552481f4486839",
    base_url="https://api.deepseek.com",
)

def weather_report(city):
    match city:
        case "beijing":return "qingtian";
        case "shanghai":return "yingtian";

tools = [{
    "type": "function",
    "function": {
        "name": "weather_report",
        "description": "Get weather report for a city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The city to get the weather report for",
                }
            },
            "required": ["city"],
            }
        }
}]

message=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "beijing 天气怎么样"},
    ]



while True:
    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=message,
        tools=tools,
        stream=False,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}},
    )
    msg = response.choices[0].message
    message.append(msg)
    if not msg.tool_calls:
        print(msg.content)
        break
    for tool_call in msg.tool_calls:
        if tool_call.function.name == "weather_report":
            args = json.loads(tool_call.function.arguments)
            result = weather_report(args["city"])
        message.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result,
            })
