from flask import Flask, request, render_template, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Global storage for parsed data
parsed_data = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    global parsed_data
    if 'file' not in request.files:
        return "No file uploaded", 400

    file = request.files['file']
    if file.filename.endswith('.xlsx'):
        df = pd.read_excel(file)
        # Store the parsed data in a dictionary for quick lookup
        parsed_data = {
            "POBE": df["PO Number"].tolist(),
            "Items": df["Item"].tolist(),
            "Serial Numbers": df["Serial Number"].tolist(),
        }
        return redirect(url_for('input_items'))
    else:
        return "Invalid file format. Please upload an Excel file.", 400

@app.route('/input', methods=['GET', 'POST'])
def input_items():
    global parsed_data
    if request.method == 'POST':
        # Get the inputted item numbers
        input_numbers = request.form.get("item_numbers").splitlines()
        # Match the input numbers to their PO Numbers
        matched = []
        unmatched = []
        for number in input_numbers:
            if number in parsed_data["Serial Numbers"]:
                index = parsed_data["Serial Numbers"].index(number)
                matched.append({
                    "Serial Number": number,
                    "PO Number": parsed_data["POBE"][index],
                    "Item": parsed_data["Items"][index],
                })
            else:
                unmatched.append(number)

        return render_template('results.html', matched=matched, unmatched=unmatched)

    return render_template('input.html')

if __name__ == '__main__':
    app.run(debug=True)

