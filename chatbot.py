from langchain_groq import ChatGroq
llm=ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key="YOUR_GROQ_API_KEY"
)