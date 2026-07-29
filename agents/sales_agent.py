from chatbot import llm
from langchain_core.prompts import PromptTemplate
sales_prompt="""
You are an AI Sales Strategy Agent.
Analyze the company research information.
Company Research:
{research}
Find:
1. Business Problems
2. Pain Points
3. Automation Opportunities
4. Recommended AI Solutions
5. Expected Business Benefits
Answer in structured format.
"""
prompt=PromptTemplate(template=sales_prompt, input_variables=["research"])
def analyze_sales(research):
    chain=prompt | llm
    response=chain.invoke({"research":research})
    return response.content