import streamlit as st
import pickle
import spacy
from wordcloud import WordCloud
from docx import Document
import fitz  
import matplotlib.pyplot as plt

# Attempt to load the spaCy model, downloading it if necessary
try:
    nlp = spacy.load("en_core_web_sm")
except IOError:
    print("Downloading the spaCy language model...")
    spacy.cli.download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Define the text preprocessing function using spaCy
def preprocess_text(text):
    doc = nlp(text)
    clean = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct and token.is_alpha]
    return " ".join(clean)

# Load the model pipeline from file
with open('model_res.pkl', 'rb') as file:
    model_pipeline = pickle.load(file)

# Define the category mapping for prediction output
category_mapping = {
    15: "Java Developer",
    23: "Testing",
    8: "DevOps Engineer",
    20: "Python Developer",
    24: "Web Designing",
    12: "HR",
    13: "Hadoop",
    3: "Blockchain",
    10: "ETL Developer",
    18: "Operations Manager",
    6: "Data Science",
    22: "Sales",
    16: "Mechanical Engineer",
    1: "Arts",
    7: "Database",
    11: "Electrical Engineering",
    14: "Health and fitness",
    19: "PMO",
    4: "Business Analyst",
    9: "DotNet Developer",
    2: "Automation Testing",
    17: "Network Security Engineer",
    21: "SAP Developer",
    5: "Civil Engineer",
    0: "Advocate",
}

# Function to predict the category of a resume
def predict_category(text):
    cleaned_text = preprocess_text(text)
    prediction_id = model_pipeline.predict([cleaned_text])[0]
    return category_mapping.get(prediction_id, "Unknown")

# Function to extract text from a PDF file using PyMuPDF
def extract_text_from_pdf(pdf_file):
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text

def extract_text_from_docx(docx_file):
    doc = Document(docx_file)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def main():
    st.title("Advanced Resume Screening App", anchor=None)
    st.markdown('<p class="big-font">Welcome to the Advanced Resume Screening App!</p>', unsafe_allow_html=True)
    st.markdown("## Upload your resume or type in your details below:")

    # Using columns to layout the file uploader and text box
    col1, col2 = st.columns(2)
    
    with col1:
        uploaded_file = st.file_uploader("Upload Your Resume", type=["txt", "pdf", "docx"])
    
    with col2:
        resume_text_manual = st.text_area("Type your resume here:")

    resume_text = ""
    if uploaded_file is not None:
        if uploaded_file.type == "application/pdf":
            resume_text = extract_text_from_pdf(uploaded_file)
        elif uploaded_file.type == "text/plain":
            resume_text = uploaded_file.getvalue().decode("utf-8")
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            resume_text = extract_text_from_docx(uploaded_file)
    elif resume_text_manual:
        resume_text = resume_text_manual

    if resume_text and st.button("Analyze Resume"):
        with st.spinner("Analyzing..."):
            category = predict_category(resume_text)
            st.markdown(f"## Predicted Category: **{category}**")

            # Generate a word cloud from the cleaned resume text
            cleaned_text = preprocess_text(resume_text)
            wordcloud = WordCloud(width=800, height=400, background_color ='white').generate(cleaned_text)
            fig, ax = plt.subplots()
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis("off")
            st.pyplot(fig)

if __name__ == "__main__":
    main()
