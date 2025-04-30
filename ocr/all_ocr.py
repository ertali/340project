from datetime import datetime, timedelta
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import os
import numpy as np
import csv
import json

# Optional: if tesseract is not in PATH
pytesseract.pytesseract.tesseract_cmd = '/share/pkg.7/tesseract/4.1.3/install/bin/tesseract'

import ollama  # assuming this is imported and works

start_date = datetime.strptime("2013-01-26", "%Y-%m-%d")
end_date = datetime.strptime("2023-08-27", "%Y-%m-%d")
current_date = start_date

output_path = '/projectnb/ds340/students/samc/340project/output.csv'

# Make sure header is written once if file doesn't exist
if not os.path.exists(output_path):
    with open(output_path, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Date', 'Text', 'Embedding'])

while current_date <= end_date:
    filename = f"{current_date.strftime('%Y-%m-%d')}.pdf"
    filepath = "/projectnb/ds340/students/samc/340project/pdf/" + filename
    print(f"Trying {filepath}")
    
    try:
        pages = convert_from_path(filepath)
        first_page = pages[0]
        text = pytesseract.image_to_string(first_page)
        print(f"OCR result (preview): {text[:10]!r}")
        
        try:
            embedding = ollama.embeddings(model='nomic-embed-text', prompt=text)
            print(f"Got embedding for {filename}")
        except Exception as embed_err:
            print(f"Embedding failed for {filename}: {embed_err}")
            embedding = {"embedding": []}

        # Write result to CSV immediately
        with open(output_path, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([current_date.strftime('%Y-%m-%d'), text, json.dumps(embedding['embedding'])])
            f.flush()
            os.fsync(f.fileno())
            print(f"Wrote row for {filename}")

    except Exception as e:
        print(f"Failed to process {filename}: {e}")
    
    try:
        # os.remove(filepath)
        print(f"Finished {filename}")
    except Exception as e:
        print(f"Could not delete {filename}: {e}")
    
    current_date += timedelta(days=1)

print("Done. All processed entries saved to output.csv")
