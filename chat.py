from model import QASystem
import pandas as pd
import csv

def chatbot(input):
    qa = QASystem('clean_dataset.csv')
    try:
        qa_response = qa.get_response(input)
        print("Try")
    except:
        qa_response = "I can't answer this question."
        print("Except")
    return qa_response
