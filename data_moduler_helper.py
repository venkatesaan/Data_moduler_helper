
import google.generativeai as genai
import os 
import streamlit as st


st.title("DATA MODULER HELPER - ER GENERATOR")
natural_text = st.text_area("Enter Context to convert into ER Diagram")
#natural_text = "A university has students, professors, and courses. Students enroll in courses, and professors teach courses. Each student can enroll in multiple courses, and each course can be taught by multiple professors" 

code_style = "sqlalchemy" # Press the green button in the gutter to run the script. 

 
PAML_API_KEY = "Your GEMINI API KEY" 
genai.configure(api_key=PAML_API_KEY) 
model = genai.GenerativeModel("gemini-1.5-flash") 
chat = model.start_chat() 

prompt = f""" You are a database expert, {natural_text} Return only a {code_style} python executeble code for all the entity and relationships such that all of them are connected with each other in the ER diagram in markdown format with out using any database like sqlite and the table name, attribute should not contains any space,uppercase and junk chartacters. you can use _ between the table and attribute name if required. Table and attribute name should be in signular. e.g.: for example in schema: import matplotlib.image as mpimg import pandas as pd from eralchemy import render_er from sqlalchemy import * from sqlalchemy import (MetaData, Table, Column) import matplotlib.pyplot as plt metadata = MetaData() # create your own model .... users = Table('users', metadata, Column('user_id', String(15), primary_key=True), Column('username', String(15), nullable=False, unique=True), ) orders = Table('orders', metadata, Column('order_id', String(15)), Column('user_id', ForeignKey('users.user_id')), ) # add your own table .... # Show ER model from here filename = 'mymodel.png' render_er(metadata, filename) imgplot = plt.imshow(mpimg.imread(filename)) plt.savefig(filename) """ 
	

response = chat.send_message(prompt)
filename = 'mymodel.png' 
if natural_text:
	exec(response.text.split("```")[1].replace('python', '#python code')) 
	#st.sidebar.write(response.text) 
	st.image(filename)
