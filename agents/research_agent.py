from loader import load_website
from splitter import split_documents
from vectorstore import create_vectorstore
from embedding import embeddings
from retriever import get_retriever
from chatbot import llm

from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate


research_prompt = """
You are an AI Research Agent.

Your job is to analyze a company's website and collect business information.

Use the given website context.

Context:
{context}

Question:
{question}


Provide information in this format:

Company Name:
Industry:
Products:
Services:
Target Customers:
Business Summary:
Possible Pain Points:
Current Business Challenges:


If information is not available write:
Not Available
"""


PROMPT = PromptTemplate(
    template=research_prompt,
    input_variables=["context", "question"]
)



def research_company(url):

    # Load website
    docs = load_website(url)


    # Split documents
    chunks = split_documents(docs)


    # Create vector database
    vectorstore = create_vectorstore(
        chunks,
        embeddings
    )


    # Retriever
    retriever = get_retriever(vectorstore)


    # QA Chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={
            "prompt": PROMPT
        }
    )


    question = """
    Analyze this company completely.
    Provide company details,
    industry,
    services,
    products,
    customers,
    pain points.
    """


    response = qa_chain.invoke(
        {
            "query": question
        }
    )


    return response["result"]