from dotenv import load_dotenv
load_dotenv()
from email_sender import send_email
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

def isprime(n: int) -> str:
    """Check if a number is prime."""
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return f"{n} is not prime"
    return f"{n} is prime"

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=1.0,
)

agent = create_agent(
    model=model,
    tools=[get_weather,isprime,send_email],
    system_prompt="You are a helpful assistant",
)
print("before invoking")
# Run the agent
response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in mysore and is 2001 prime,and send an email to shreyavnadiger@gmail.com regarding this content and the result of prime?"}]}
)
print("after invoking")
# Print only the final AI response
final_msg = response["messages"][-1]
if isinstance(final_msg.content, list):
    for block in final_msg.content:
        if isinstance(block, dict) and block.get("type") == "text":
            print(block["text"])
else:
    print(final_msg.content)
print("after printing")