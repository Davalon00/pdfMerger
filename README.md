# PDF Merger Script

This Python script merges multiple PDF files from a specified folder into a single PDF file. It uses the `PyPDF2` library to handle the merging process.

## Prerequisites

- Python 3.x
- `PyPDF2` library

You can install the required library using pip:

```bash
pip install PyPDF2
```

## How It Works

1. The script reads all files in a folder named `files`.
2. It filters and selects only the files with the `.pdf` extension.
3. These PDF files are merged into one using `PyPDF2.PdfMerger`.
4. The merged PDF is saved as `finalPDF.pdf` in the current working directory.

## Script Workflow

- **Step 1**: List all files in the `files` folder and sort them.
- **Step 2**: Check if each file has a `.pdf` extension.
- **Step 3**: Append the PDFs in sorted order to the merger instance.
- **Step 4**: Save the resulting merged PDF as `finalPDF.pdf`.
- **Step 5**: Output a confirmation message indicating the final file has been saved.

## Usage

1. Place the PDF files you want to merge in a folder named `files` in the same directory as the script.
2. Run the script:
   ```bash
   python merge_pdfs.py
   ```
3. After running the script, a file named `finalPDF.pdf` will be created containing the merged PDFs.

## Example Directory Structure

```
your_project/
│
├── merge_pdfs.py
├── files/
│   ├── file1.pdf
│   ├── file2.pdf
│   └── file3.pdf
└── finalPDF.pdf (generated after running the script)
```

## Notes

- The script assumes that the `files` directory exists and contains PDF files.
- The PDF files are merged in the sorted order of filenames.
- If the `files` directory contains any non-PDF files, they are ignored.
