from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PDFReader
def main():
    load_dotenv()
    st.set_page_config(page_title='Ask your PDF')
    st.header("Ask your pdf")
    
    pdf = st.file_uploader('Upload your pdf', type="PDF")
    
    if pdf is not None:
        pdf_reader = PDFReader(pdf)

if __name__ == '__main__':
    main()