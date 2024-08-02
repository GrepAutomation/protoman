from flask import Flask, request, render_template
import fitz  # PyMuPDF
import pandas as pd
import os

app = Flask(__name__)

# Load the Excel sheet with default refrigeration system mappings
df = pd.read_excel('refrigeration_systems.xlsx')

def extract_data_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def match_refrigeration_system(dimensions):
    match = df[df['Box Size'] == dimensions]
    if not match.empty:
        return match.iloc[0]['Refrigeration System']
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_upload', methods=['POST'])
def process_upload():
    walkin_box_file = request.files['walkinBox']
    refrigeration_file = request.files.get('refrigeration')

    # Save the uploaded PDFs
    walkin_box_path = os.path.join('uploads', walkin_box_file.filename)
    walkin_box_file.save(walkin_box_path)
    
    if refrigeration_file:
        refrigeration_path = os.path.join('uploads', refrigeration_file.filename)
        refrigeration_file.save(refrigeration_path)
    else:
        refrigeration_path = None

    # Extract data from PDFs
    walkin_box_data = extract_data_from_pdf(walkin_box_path)
    refrigeration_data = extract_data_from_pdf(refrigeration_path) if refrigeration_path else None

    # Extract dimensions and refrigeration system
    dimensions = extract_dimensions(walkin_box_data)  # Implement your extraction logic here
    refrigeration_system = extract_refrigeration_system(refrigeration_data) if refrigeration_data else None

    if not refrigeration_system:
        refrigeration_system = match_refrigeration_system(dimensions)
        if not refrigeration_system:
            return "No matching refrigeration system found."

    # Generate the quote
    quote = f"{walkin_box_data['Customer Name']}\n"
    quote += f"Indoor Walk-In Freezer/Floor: {dimensions} with a {refrigeration_system}\n"
    quote += "$55,450.00 No Taxes (Includes Shipping) Bush Refrigeration\n"
    quote += "\nCurrent lead time for equipment is 6 weeks\n"
    quote += "Quote is good for 15 days\n"
    quote += "\nAdditional Information:\n\n"
    quote += "Shipping Included, No Installation\n"
    quote += "We are exclusively an equipment company. Installation is always done third party by whomever you choose."

    return quote

def extract_dimensions(walkin_box_data):
    # Implement the logic to extract dimensions from the walk-in box data
    return "26’ x 6’ 10” x 7’ 6”"

def extract_refrigeration_system(refrigeration_data):
    # Implement the logic to extract refrigeration system information from the refrigeration data
    return "4.5HP Low Temp Refrigeration System"

if __name__ == '__main__':
    app.run(debug=True)
