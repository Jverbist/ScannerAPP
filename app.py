from flask import Flask, request, render_template, redirect, url_for, jsonify
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


@app.route('/input', methods=['GET'])
def input_items():
    return render_template('input_live.html')

@app.route('/guide', methods=['GET'])
def guide():
    return render_template('guide.html')


@app.route('/live-sort', methods=['POST'])
def live_sort():
    global parsed_data
    if not parsed_data:
        return jsonify({"error": "No data uploaded"}), 400

    input_numbers = request.json.get("input_numbers", [])
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

    # Group matched items by PO Number and count them
    grouped_matched = {}
    counts = {}
    for item in matched:
        po_number = item["PO Number"]
        if po_number not in grouped_matched:
            grouped_matched[po_number] = []
            counts[po_number] = 0
        grouped_matched[po_number].append(item)
        counts[po_number] += 1

    return jsonify(
        {"grouped_matched": grouped_matched, "counts": counts, "unmatched": unmatched}
    )



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
