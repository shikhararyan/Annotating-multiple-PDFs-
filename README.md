# Annotating-multiple-PDFs-
This project aims to automate the process of highlighting specific keywords within PDF documents. Leveraging the PyMuPDF library (fitz module), along with pandas for handling keyword data stored in CSV format, the script systematically searches through each page of the PDF documents, identifies the keywords, and highlights them.

# Highlight Keywords in PDFs

This Python script highlights specified keywords in PDF documents. It reads a list of keywords from a CSV file, searches for these keywords in each page of the input PDFs, and highlights them. The processed PDFs are saved in an output folder.

## Requirements

- Python 3.x
- pandas
- PyMuPDF (fitz)

You can install the required packages using pip:

pip install pandas pymupdf

Retrieve Processed Files: The processed PDF files with highlighted keywords will be saved in the processed_files folder.

## Script Description

1. Highlight Keywords in PDFs
The function highlight_keywords_in_pdf reads a PDF file, searches for specified keywords, and highlights them in the document. It utilizes the PyMuPDF library (fitz) to handle PDF manipulation.

2. Read Keywords from CSV
The script reads the list of keywords from the CSV file filtered_keywords.csv using pandas. It converts the keywords to lowercase and stores them in a set for efficient lookup.

3. Input and Output Folders
The input PDF files are expected to be placed in the input_files folder. The processed PDFs with highlighted keywords will be saved in the processed_files folder. If the output folder doesn't exist, it will be created.

4. Iterate Through PDF Files
The script iterates through each PDF file in the input folder (input_files). For each PDF file, it highlights the keywords and saves the processed file in the output folder (processed_files).

Note
Make sure to have proper permissions to read from/write to the input and output folders.
Ensure that the required Python packages are installed before running the script.
