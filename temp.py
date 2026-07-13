from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
# Initialize the model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,
    max_retries=2
)

# Invoke a response
response = llm.invoke("Explain Quantum Computing in one short sentence.")
print(response.content)
