

# AI Research Assistant & Data Analyzer 
An intelligent document processing pipeline that combines traditional data analysis with modern Natural Language Processing (NLP). This tool can analyze structured data (CSV/JSON) and perform deep-dive analysis on unstructured text (PDF/Docx) using Transformer models.

##  Key Features
- **Intelligent Q&A:** Ask specific questions about uploaded documents using a `distilbert-base-uncased` SQuAD model.
- **Automated Summarization:** Generates concise abstracts of long-form text using the `DistilBART` CNN model.
- **Multi-Format Support:** - **Structured:** CSV/JSON analysis (Mean calculations, unique value extraction, empty row cleaning).
  - **Unstructured:** PDF and Word (.docx) text extraction and processing.
- **Keyword Extraction:** Uses **TF-IDF Vectorization** to identify the most statistically significant terms in a document.
- **REST API:** Includes a **Flask** backend for handling file uploads and metadata logging.

## Tech Stack
- **NLP/AI:** Hugging Face Transformers, Scikit-learn (TF-IDF), PyPDF2, Python-Docx
- **Data Science:** NumPy, Pandas, Collections
- **Backend:** Flask (REST API), Logging
- **Configuration:** JSON/JSON5 for metadata management

## Requirements
To run this project, you will need to install:
```bash
pip install flask transformers torch scikit-learn numpy pandas PyPDF2 python-docx json5
