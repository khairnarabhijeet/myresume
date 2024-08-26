
import streamlit as st

#This code block is used for AI CHatbot
import openai

about_me = """
I'm Abhijeet K, a Program Manager with over 18 years of experience in the IT industry, specializing in banking domain programs.
I have managed large teams, driven enterprise-level application development and deployment, and I hold certifications in AWS Cloud Practitioner, 
SAFe 5.0, Scrum Master, Salesforce Developer, and Zend PHP.
"""
#Function to get AI response
def get_ai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Streamlit app configuration
st.title("AI Chatbot - About Abhijeet")

# User input
user_input = st.text_input("Ask me anything about Abhijeet:")
openai.api_key = "sk-CyuTvgjWvDO4Bj7hdBUmzuWGbmYCtSRlTKILwDRt73T3BlbkFJ95bUA_EIYbuCdbGk1hSqBIm8vG-c-LuJd_VJcWW9kA"
# Response generation


if user_input:
    prompt = f"User asked: {user_input}\n\nProvide a response based on the following details:\n\n{about_me}\n\nResponse:"
    response = get_ai_response(prompt)
    st.write(response)

#End of code block used for AI Chatbot 

# Streamlit App Interface
st.title("Abhijeet K - Program Manager")

# Resume Section
st.header("About Me")
st.write("""
I am an experienced Program Manager offering more than 18 years of IT experience. 
I have held strong and dynamic leadership roles in Service & Solution Delivery, 
Program Management, Consulting, IT Transformation, and Engagement Management. 
I have led the development and deployment of enterprise-level applications 
pertaining to web and mobile applications with expertise in cloud technologies, 
micro-service design, CI/CD, and scalable fault-tolerant platform design.
""")

st.write("""
### Experience
- **Program Manager** at Wipro, India (August 2021 – Current)
  - Managing HSBC Financial Services Program with budgets up to $10 million.
  - Leading a team of 250+ members across various projects.
  - Implementing Scaled Agile Framework in a multi-domain ecosystem.
  
- **Project Manager** at Fulcrum Digital, India (June 2019 – August 2021)
  - Engaged in MasterCard Financial Services Projects with team sizes of up to 65.
  - Managed Scrum of Scrums in Scaled Agile Framework.
  - Specialized in payment services including Cards, POS, and mobile payments.

### Certifications
- AWS Cloud Practitioner
- SAFe 5.0 Certified Professional
- Scrum Master Certification
- Salesforce Developer Certified
- Zend PHP Certified Professional

### Awards
- HSBC Best Project Award ACS 2023
- Best Project Mastercard Web & Mobile Pay By Bank App 2020
- Best Project Mastercard Bill Pay 2019
""")

st.write("""
### Technical Skills
- Java, Spring Boot, Spring Integration
- LAMP, Xamarin
- Angular 6, Oracle, Hadoop Integration
- Android & iOS Mobile Development
- CI/CD Jenkins, SonarQube, Sonatype
- AWS EC2, Amazon Lambda, AWS SQS
- Qlik Sense, UI Path Robotic Process Automation
""")

# Chatbot Section
#st.header("Chat with Me!")
#user_input = st.text_input("Ask a question about me:")

#if user_input:
 #   response = get_chatbot_response(user_input)
  #  st.write(response)

#st.write("Feel free to ask any question related to my experience, skills, or anything you'd like to know!")
