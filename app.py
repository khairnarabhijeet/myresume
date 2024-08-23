
import streamlit as st
import openai

# Set up OpenAI API key
openai.api_key = 'sk-5MknObkALbU79x97jWp0bjOWn8TQiDmOhJDyo5UK7KT3BlbkFJfIEptkb0O2ERJDBX7pnrZ0gGipCgWE372Pa4anrzQA'

# Function to generate response
def generate_response(user_input):
    personal_info = """
    Abhijeet K is an experienced Program Manager with over 18 years of experience in IT, specializing in Service & Solution Delivery, Program Management, Consulting, IT Transformation, and Engagement Management. He has led the development and deployment of Enterprise-level Applications, has expertise in cloud technologies, micro-service design, CI/CD, and more. He has worked with HSBC, MasterCard, and Wipro, managing large teams and budgets up to $10 million. Abhijeet is also certified in AWS Cloud Practitioner, SAFe 5.0, Scrum Master, Salesforce Developer, and Zend PHP.
    """
    prompt = f"{personal_info}\n\nUser: {user_input}\nChatbot:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
    )
    return response.choices[0].text.strip()



# Set up Streamlit app
st.title("Abhijeet's Personal Chatbot")

st.write("This is a chatbot that answers questions about Abhijeet K. Feel free to ask anything!")

# Input box for user to ask a question
user_input = st.text_input("You: ", "Who is Abhijeet K?")

# Generate a response when the user submits a question
if user_input:
    prompt = f"You are a chatbot that knows everything about Abhijeet K. Answer the following question: {user_input}"
    response = generate_response(prompt)
    st.text_area("Abhijeet's Chatbot:", value=response, height=150)




#from transformers import AutoModelForCausalLM, AutoTokenizer
#import torch

# Load the pre-trained model and tokenizer
#model_name = "microsoft/DialoGPT-medium"
#model = AutoModelForCausalLM.from_pretrained(model_name)
#tokenizer = AutoTokenizer.from_pretrained(model_name)

# Function to generate chatbot responses
#def get_chatbot_response(user_input):
    # Encode the user input and add the EOS token
    #inputs = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
    
    # Create an attention mask: 1 for tokens that are not padding
    #attention_mask = torch.ones(inputs.shape, dtype=torch.long)
    
    # Generate the response with attention_mask
    #response_ids = model.generate(inputs, attention_mask=attention_mask, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    
    # Decode and return the response
    #response = tokenizer.decode(response_ids[:, inputs.shape[-1]:][0], skip_special_tokens=True)
    #return response

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
