from chatbot import llm
from langchain_core.prompts import PromptTemplate
email_prompt="""
You are an AI Email Writer Agent.
Create a professional personalized cold email.
Company Information:
{research}
Sales Analysis:
{sales_analysis}
Generate:
Subject:
Email Body:
Rules:
- Professional tone
- Short and convincing
- Mention company name
- Mention AI solutions
- Add meeting request
"""
prompt=PromptTemplate(template=email_prompt, input_variables=["research", "sales_analysis"])
def generate_email(research, sales_analysis):
    chain=prompt | llm
    response=chain.invoke({"research": research, "sales_analysis": sales_analysis})
    return response.content