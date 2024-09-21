from openai import OpenAI

api_key = "sk-9FZknAIsf7vqPAZKM5L1GGBnyE1oCrKGe9qBV0U8vK7RfRdG"
client = OpenAI(api_key=api_key, base_url="https://api.deepbricks.ai/v1/")

chat_log = [{"role": "system", "content": "You are a helpful language translation (Chinese and English) assistant."}, ]
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=chat_log
)
print(response)

while True:
    user_input = input("User: ")
    if user_input.lower() == "exit":
        break
    user_msg = {"role": "user", "content": user_input}
    chat_log.append(user_msg)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=chat_log
    )
    assistant_msg = {"role": "assistant", "content": response.choices[0].message.content}
    chat_log.append(assistant_msg)
    print(f"Assistant: {response.choices[0].message.content}")
    print(f"Usage: {response.usage}")
