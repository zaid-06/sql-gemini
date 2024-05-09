from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

## Congigure Genai key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
