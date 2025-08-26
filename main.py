# main.py
import csv
import numpy as np
from collections import Counter
from config import project_metadata
from utils.json_loader import load_json
from utils.data_cleaner import clean_empty_rows, convert_to_float
import pandas as pd
from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
import PyPDF2
from docx import Document
import os

# ---- Windows fixes ----
os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"  # disables symlink warning

print("Project Author:", project_metadata["author"])
print("Version:", project_metadata["version"])
print("Features:", ", ".join(project_metadata["features"]))

# ---- CSV Analyzer ----
def load_csv(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            data = list(csv.reader(csvfile))
            return data
    except FileNotFoundError:
        print("File not found!")
        return []

def column_mean(data, col_idx):
    values = [float(row[col_idx]) for row in data[1:] if row[col_idx]]
    return np.mean(values)

class DataAnalyzer:
    def __init__(self, data):
        self.data = data
    
    def preview(self, rows=5):
        print("\n--- Data Preview ---")
        for row in self.data[:rows]:
            print(row)

    def unique_values(self, col_idx):
        if not self.data:
            return set()
        return set(row[col_idx] for row in self.data[1:] if len(row) > col_idx and row[col_idx])

    def summarize_column(self, col_idx):
        values = [float(row[col_idx]) for row in self.data[1:] if row[col_idx]]
        return {"min": min(values), "max": max(values), "mean": np.mean(values)}

# ---- Load and clean CSV ----
data = load_csv("sample.csv")
data = clean_empty_rows(data)
data = convert_to_float(data, 1)

analyzer = DataAnalyzer(data)
analyzer.preview()
print("Average Age:", column_mean(data, 1))

# ---- Word Frequency & Keyword Search ----
words = []
for row in data:
    for cell in row:
        words.extend(str(cell).split())
freq = Counter(words)
print("\nTop 10 Word Frequencies:", freq.most_common(10))

sentences = [" ".join(str(cell) for cell in row) for row in data]
keyword = input("Enter keyword to search: ")
matches = [s for s in sentences if keyword.lower() in s.lower()]
print(f"Found {len(matches)} matches:")
for m in matches:
    print("-", m)

print("\nUnique Ages:", analyzer.unique_values(1))
print("Unique Cities:", analyzer.unique_values(2))

# ---- JSON Data Handling ----
json_data = load_json("sample.json")
print("\nLoaded JSON data:", json_data)

# ---- PDF/Doc Summarization ----
def read_pdf(file_path):
    text = ""
    with open(file_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()
    return text

def read_docx(file_path):
    doc = Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

# Load document (PDF or DOCX or TXT)
doc_text = read_pdf("sample.pdf")  # or read_docx("sample.docx") or open("sample.txt").read()

# ---- Smaller summarization model for Windows ----
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")  # smaller model
summary = summarizer(doc_text[:1000], max_length=150, min_length=50, do_sample=False)
print("\nDocument Summary:", summary[0]['summary_text'])

# Keyword extraction
vectorizer = TfidfVectorizer(stop_words='english', max_features=10)
X = vectorizer.fit_transform([doc_text])
keywords = vectorizer.get_feature_names_out()
print("Top Keywords in Document:", keywords)

# Q&A
qa = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")  # small QA model
question = input("Ask a question about the document: ")
answer = qa(question=question, context=doc_text[:2000])
print("Answer:", answer['answer'])
