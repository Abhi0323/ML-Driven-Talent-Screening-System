# ML-Driven Talent Screening System

* **Purpose:** Designed to enhance HR capabilities by automating the resume screening process, this application leverages Machine Learning and NLP to efficiently categorize resumes, saving time and improving recruitment accuracy.

## Technical Stack:

* **Data Science & Machine Learning:** Developed using Python, with Scikit-learn for building and evaluating models, and spaCy for Natural Language Processing.
* **Text Processing:** Implemented advanced text preprocessing techniques to extract meaningful features from complex datasets, including TF-IDF vectorization and lemmatization.
* **Model Development:** Employed multiple classification algorithms (K-Nearest Neighbors initially) with a structured pipeline approach for scalable experimentation of various classifiers.
* **Evaluation & Optimization:** Achieved an impressive model accuracy of 97.4%, backed by a robust testing framework using stratified data splits and a comprehensive evaluation using confusion matrices and classification reports.
* **Web Application:** Built with Streamlit, allowing users to upload resumes in different formats (text, PDF, docx). Integrated PyMuPDF and python-docx for file handling and WordCloud for visual analytics.
* **Deployment:** Deployed the machine learning model using Hugging Face Spaces for easy accessibility and integration into HR workflows.
  
## Application Features:

* **Multi-Format Support:** Accepts resumes in various file formats, increasing the application's versatility.
* **Dynamic Predictions:** Uses machine learning to predict the job category based on resume content, with immediate visual feedback through an interactive word cloud representation of key terms.
* **User-Friendly Interface:** Designed for ease of use, the app includes features like file uploaders and text input for direct analysis, catering to both tech-savvy and non-technical users.
  
## Impact:

* **Efficiency in Recruitment:** Automates the initial stages of the recruitment process, significantly reducing the manual effort and time required in resume screening.
* **Enhanced Decision-Making:** Provides HR professionals with data-driven insights, enabling more informed decision-making and improving the quality of hires.
  
## Looking Forward:

Plans to incorporate feedback mechanisms to continuously improve the model based on user input and expand the model to include multi-language support to cater to diverse demographics.
🔗 Explore More: [Link to the application/demo]
