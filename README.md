# PDF Text Analysis and Highlighting

## Overview
This script processes a PDF document to extract and analyze text, font properties, and bounding boxes. It highlights the detected text spans using randomly colored rectangles.

## Features
- Extracts text from a PDF file.
- Identifies font size, color, and font name for each text span.
- Highlights extracted text using randomly generated colors.
- Saves the modified PDF with highlights.
- Prints extracted text details for verification.

## Prerequisites
Ensure you have the following dependencies installed before running the script:

```sh
pip install pymupdf
```

## Usage

### Input Parameters
- `input_pdf` : The PDF file to process.
- `output_pdf` : The output file with highlighted text.
- `old_text` : The text to search for in the PDF.

### Running the Script
Execute the script with the required parameters:

```python
result = get_info("utpal_newcv.pdf", "output.pdf", "old")
```

### Output
- A new PDF (`output.pdf`) with highlighted text.
- Console output showing extracted text details, including:
  - Page number
  - Extracted text
  - Font size
  - Font color (RGB format)
  - Font name
  - Bounding box coordinates

## Code Breakdown
1. Opens the PDF file using `PyMuPDF`.
2. Extracts text, font properties, and bounding box information from each page.
3. Highlights each detected text span with a randomly colored rectangle.
4. Saves the modified PDF with highlights.
5. Prints extracted text details for verification.

## Example Console Output
```
Page num: 1
Text: Sample Text
Font size: 12.0
Font color: (0, 0, 0)
Font name: Times-Roman
Bboxes: (50.0, 100.0, 200.0, 120.0)
```

## Notes
- The script does **not** filter specific text by default but processes all text spans.
- If filtering is required, modify the `if` condition inside the loop to match specific text.

## License
This project is open-source and can be used freely with modifications as needed.

