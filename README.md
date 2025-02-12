# Data_moduler_helper
**Problem:**
  Traditional methods involve manual drawing using software like Microsoft Visio, which can be time- consuming and prone to human error in complex databases. We can avoid this with help of my POC Data modeler Helper.

**Solution:**
  We used google generative ai GEMINI to generate ER diagram from business requirements. Gemini LLM excels in natural language understanding, generating highly accurate diagrams from textual data inputs, thereby streamlining the creation of **ER diagrams.** 
  
**Process:**
  The Natural Language Processing (NLP) techniques involve using algorithms to extract meaningful information from textual data, aiding in the construction of ER diagrams.
  Parsing and segmentation break down the text into manageable parts, helping to identify entities and relationships within sentences and phrases efficiently.
  
**Steps:**

**1. Identifying Entities and Relationships:**
     This step focuses on determining the main entities and their interrelations, essential for structuring an accurate database model.
     
**2. Attributes Extraction:**
     Attributes extraction involves pinpointing specific properties or characteristics of entities that need representation in the ER diagram.
   
**System Requirements:**
1.	Python and Microsoft VS build tool.
2.	Python package:
   1. google.generativeai
   2. streamlit
   3. matplotlib
   4. eralchemy
   5. sqlalchemy
   6. graphviz
3.	GEMINI API Key.

**How to run python script:**
1.	you need to install python (from software center) and above packages into you system with help of below comment in cmd.
a.	Pip install google.generativeai
2.	Get your API key from Get API key | Google AI Studio.
3.	Download the code from https://github.com/venkatesaan/Data_moduler_helper.git
4.	From CMD you can run with help of below comment:
a.	python -m streamlit run path_to_main.py
Once the program runs successfully. Streamlit will initials link(http://localhost:8501) for your program. 

