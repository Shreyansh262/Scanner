import pandas as pd
import qrcode
import os
from pyzbar.pyzbar import decode
from PIL import Image

# Load the CSV file
df = pd.read_csv('Book1.csv')

# Create a folder to store the QR codes if it doesn't exist
output_folder = 'qr_codes'
os.makedirs(output_folder, exist_ok=True)

# Function to decode existing QR code data
def decode_qr(file_path):
    try:
        img = Image.open(file_path)
        decoded_objects = decode(img)
        if decoded_objects:
            return decoded_objects[0].data.decode("utf-8")
    except Exception as e:
        print(f"Error decoding QR code from {file_path}: {e}")
    return None

# Loop through each row in the DataFrame
for index, row in df.iterrows():
    # Dynamically construct the text that will be encoded in the QR code
    qr_data = "\n".join([f"{col}: {row[col]}" for col in df.columns])

    # Define a file name based on a unique identifier (use 'Name' column if available, else a generic one)
    name = row['Name'] if 'Name' in df.columns else f"Person_{index}"
    qr_file_path = os.path.join(output_folder, f"{name}_QR.png")

    # Check if the QR code file already exists
    if os.path.exists(qr_file_path):
        # Decode the existing QR code
        existing_data = decode_qr(qr_file_path)
        
        # Compare existing QR data with new QR data
        if existing_data == qr_data:
            print(f"No changes detected for {name}. Skipping QR code generation.")
            continue  # Skip if data hasn't changed

    # Generate the QR code if data is new or has changed
    qr = qrcode.make(qr_data)
    qr.save(qr_file_path)

    print(f"QR code for {name} saved as {qr_file_path}")
