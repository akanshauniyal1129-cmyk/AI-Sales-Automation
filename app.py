import streamlit as st
from agents.research_agent import research_company
from agents.sales_agent import analyze_sales
from agents.email_agent import generate_email
from tools.crm_tool import save_lead, create_database
from tools.gmail_tool import send_email

create_database()
st.set_page_config(page_title="AI Sales Automation Agent", layout="wide")
st.title("🤖 AI Sales Automation Agent")
st.write(
    """
    Enter a company website URL.
    AI will research the company,
    identify opportunities,
    generate personalized email,
    save lead and send email.
    """
)
if "research" not in st.session_state:
    st.session_state.research=None
if "sales_analysis" not in st.session_state:
    st.session_state.sales_analysis=None
if "email" not in st.session_state:
    st.session_state.email=None

website_url=st.text_input("Enter Company Website URL")
if st.button("Research Company"):
    if website_url:
        with st.spinner("Analyzing company website..."):
            research=research_company(website_url)
            st.session_state.research=research
            st.success("Company Research Completed")
    else:
        st.error("Please enter website URL")

if st.session_state.research:
    st.subheader("Company Research")
    st.write(st.session_state.research)

if st.session_state.research:
    if st.button("Find AI Opportunities"):
        with st.spinner("Analyzing business opportunities..."):
            sales=analyze_sales(st.session_state.research)
            st.session_state.sales_analysis=sales
            st.success("Sales Analysis Generated")

if st.session_state.sales_analysis:
    st.subheader("Sales Analysis")
    st.write(st.session_state.sales_analysis)
    
if(st.session_state.research and st.session_state.sales_analysis):
    if st.button("Generate Cold Email"):
        with st.spinner("Writing personalized email..."):
            email=generate_email(st.session_state.research, st.session_state.sales_analysis)
            st.session_state.email=email
            st.success("Email Generated")

if st.session_state.email:
    st.subheader("Generated Email")
    st.text_area("Email Content", st.session_state.email, height=300)

st.subheader("Save Lead")

company_name=st.text_input("Company Name", key="company_name")
industry=st.text_input("Industry", key="industry")
email_address=st.text_input("Company Email", key="company_email")
col1, col2=st.columns(2)

with col1:
    if st.button("Save Lead"):
        if not company_name or not industry or not email_address:
            st.error("Please fill all fields.")
        else:
            result=save_lead(company_name, industry, email_address)
            st.success(result)

with col2:
    if st.button("Send Email"):
        receiver=st.session_state.get("company_email", "").strip()
        if receiver=="":
            st.error("Please enter company email.")
        elif not st.session_state.email:
            st.error("Please generate the email first.")
        else:
            try:
                result=send_email(receiver, "AI Automation Solutions", st.session_state.email)
                st.success(result)
            except Exception as e:
                st.error(f"Email could not be sent.\n\n{e}")