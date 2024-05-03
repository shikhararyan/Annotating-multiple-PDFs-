import fitz  # PyMuPDF
import os
import pandas as pd

def highlight_keywords_in_pdf(input_pdf_path, output_pdf_path, keywords):
    # Open the PDF file
    pdf_document = fitz.open(input_pdf_path)
    
    # Iterate through each page of the PDF
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        
        # Extract text from the page
        text = page.get_text()
        
        # Split text into words
        words = text.split()
        
        # Search for keywords and highlight them
        for word in words:
            if word.lower() in keywords:
                instances = page.search_for(word)
                for inst in instances:
                    page.add_highlight_annot(inst)
    
    # Save the modified PDF with highlighted keywords
    pdf_document.save(output_pdf_path)
    pdf_document.close()

# Read keywords from CSV
keywords_df = pd.read_csv("filtered_keywords.csv")
keywords = set(keywords_df["Keyword"].str.lower())

# Input and output folders
input_folder = "input_files"
output_folder = "processed_files"

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate through each PDF file in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".pdf"):
        input_pdf = os.path.join(input_folder, filename)
        output_pdf = os.path.join(output_folder, filename)
        
        # Highlight keywords in PDF and save the processed file
        highlight_keywords_in_pdf(input_pdf, output_pdf, keywords)

print("Processing completed!")
