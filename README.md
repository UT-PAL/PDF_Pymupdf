# PDF Text Analysis and Highlighting(getinfo_fitz.py)

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
result = get_info("input.pdf", "output.pdf", "old")
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

# PDF Text Replacement Tool (pdf_text_replace.py)

## Overview
This Python script allows you to replace specific text in a PDF file while preserving the original font style and color as closely as possible. The script uses `PyMuPDF` (also known as Fitz) for text extraction and manipulation, and `pdf2image` for rendering pages when needed.

## Features
- Extracts text and font details from a PDF file.
- Replaces occurrences of specified text with new text.
- Preserves original font style and color.
- Saves the modified PDF as a new file.

## Requirements
Ensure you have the following Python libraries installed:

```sh
pip install pymupdf numpy pdf2image 
```

Additionally, for `pdf2image`, you may need to install `poppler`:

- **Windows**: Download and install `poppler` from [this link](https://github.com/oschwartz10612/poppler-windows/releases).
- **Linux/macOS**: Install using package manager:
  ```sh
  sudo apt install poppler-utils   # Ubuntu/Debian
  brew install poppler            # macOS
  ```

## Usage

### Running the Script
To run the script, use the following command:

```sh
python script.py
```

Make sure to modify the `replace_text()` function call with the correct file paths and text to be replaced.

### Example Usage in Code
```python
replace_text("input.pdf", "output.pdf", "old_text", "new_text")
```

### Parameters
- `input_pdf`: Path to the original PDF file.
- `output_pdf`: Path to save the modified PDF file.
- `old_text`: The text in the PDF that needs to be replaced.
- `new_text`: The new text that will replace the old text.

## Known Limitations
- If the text in the PDF is embedded as an image, this method won't work directly.
- The script assumes uniform character spacing, which may not work perfectly with some fonts.

## License
This project is open-source and free to use under the MIT License.


