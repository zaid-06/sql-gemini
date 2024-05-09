from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

## Congigure Genai key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## fUncctio  to load gemini model and provide queries as response

def get_gemini_response(question , prompt):
    model = genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0], question])
    return response.text

## Function to retrieve query from thr database

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur= conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()   
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
    """
    You are an expert in converting english to sql query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION
    \n\n For example, \nExample 1 - How many entries of records are present?,
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
    \n Example 2 - Tell me all students studying in Data Scince class?
    the SQL command will be something like this SELECT * FROM STUDENT where CLASS="Data Science";
    also the sql code should not have ''' in begining or end sql word in output
    """
]

## Streamlit APP 

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question= st.text_input("Input: ", key= "input")
submit = st.button("Ask the question")


# if submit is clicked

if submit:
    response = get_gemini_response(question , prompt)
    print(response)
    response = read_sql_query(response , "student.db")
    print(response)
    st.subheader("The response is")
    for row in response:
        print(row)
        st.header(row)
