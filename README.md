# Details to QR Code Generator

A small Python script that reads people's details from a CSV file and generates a
QR code for each row. Every QR code encodes all of that row's column values, so
scanning it shows the full record (name, roll number, department, etc.).

The script is **incremental**: if a QR code already exists for a person, it decodes
the existing image and only regenerates the QR code when the data has actually
changed. Unchanged rows are skipped.

## How it works

1. Reads `Book1.csv` from the project directory.
2. Creates a `qr_codes/` folder (if it doesn't already exist).
3. For each row, builds the QR text as one `Column: Value` pair per line.
4. Saves the QR image as `qr_codes/<Name>_QR.png`.
   - If the file already exists, the current QR is decoded and compared.
   - Matching data → skipped. Changed data → regenerated.

The `Name` column is used to name the output files. If a row has no `Name`
column, a generic `Person_<index>` name is used instead.

## Requirements

- Python 3.7+
- Dependencies:

```bash
pip install pandas qrcode pillow pyzbar
```

> **Note:** `pyzbar` needs the ZBar shared library.
> - **Windows:** the ZBar DLLs ship with the `pyzbar` wheel, so `pip install pyzbar` is usually enough.
> - **macOS:** `brew install zbar`
> - **Debian/Ubuntu:** `sudo apt-get install libzbar0`

## Usage

1. Place your data in `Book1.csv` (a sample is included in this repo).
2. Run the script:

```bash
python DetailsToQR2.py
```

3. Find the generated QR codes in the `qr_codes/` folder.

## Input CSV format

The CSV can contain any columns you like — all of them are encoded into the QR
code. A `Name` column is recommended so the output files get readable names.

Example (`Book1.csv`):

```csv
Name,Roll No,Department,Email,Phone
Alice Sharma,CS001,Computer Science,alice.sharma@example.com,9876543210
Bob Verma,EC002,Electronics,bob.verma@example.com,9876501234
```

Each row above produces a QR code such as `qr_codes/Alice Sharma_QR.png` encoding:

```
Name: Alice Sharma
Roll No: CS001
Department: Computer Science
Email: alice.sharma@example.com
Phone: 9876543210
```

## Project structure

```
scanner/
├── DetailsToQR2.py   # Main script
├── Book1.csv         # Sample/input CSV data
├── README.md         # This file
└── qr_codes/         # Generated QR codes (created on first run)
```
