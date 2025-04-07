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

# PDF Text Replacement Tool more control (Folder: custom editor)

A Python tool for searching and replacing text in PDF documents using the `PyMuPDF` (fitz) library. This tool supports the detection and modification of specific text spans based on color boxes marked on the document. It allows users to replace text in the selected areas with custom input.

## Features

- **Text Replacement**: Search and replace text in a PDF file.
- **Font Support**: Works with basic fonts like "helv" (Helvetica) and "cour" (Courier).
- **Text Detection**: Identifies text spans and allows you to manually approve or reject replacements.
- **Transparency Support**: Handles text with transparency, preserving the original appearance of the document.
- **Color Box Marking**: Supports marking areas of the PDF with colored boxes for text replacement.

## Prerequisites

- Python 3.x
- Required Python Libraries:
  - `PyMuPDF` (for PDF manipulation)
  - `pdf2image` (for converting PDF pages to images)
  - `opencv-python` (for image processing)
  - `fitz_marker` (custom library for marking text)
  
To install the required dependencies, run:

```bash
pip install fitz pdf2image opencv-python
```

If you don’t have `fitz_marker`, make sure it is available or replace it with a similar functionality for marking the text.

## How to Use

1. **Run the script**:
   - Open a terminal and execute the script.
   
2. **Enter the input PDF**:
   - When prompted, enter the name of the PDF file where you want to replace text.

3. **Mark the PDF**:
   - The script will first create a marked version of the input PDF by drawing colored boxes around selected areas. You’ll see a saved PDF (`fitz_marker.pdf`) that shows these marked areas.

4. **Select Text to Replace**:
   - Once the marked PDF is ready, input the text you want to replace. The tool will detect this text and prompt you to confirm replacements.

5. **Replace the Text**:
   - If you want to replace the detected text, enter "y" and provide the new text. The replacement will maintain the font, color, and transparency.

6. **Save the Edited PDF**:
   - After performing the replacements, the tool will save the updated PDF as `utpal_newcv_edited.pdf`.

## Example Usage

```bash
python replace_text.py
```

You will be prompted to:

1. Enter the input PDF filename (e.g., `input.pdf`).
2. View the marked PDF (`fitz_marker.pdf`) and input the text to replace.
3. Confirm replacements and input the new text.

The final output will be saved as `utpal_newcv_edited.pdf`.

## File Structure

- **replace_text.py**: The main script to run the PDF text replacement.
- **fitz_marker.py**: Custom module used to mark text areas (ensure it's available).
- **input.pdf**: The original PDF file.
- **utpal_newcv_edited.pdf**: The edited PDF output after text replacement.

## Supported Fonts

- **helv** (Helvetica)
- **cour** (Courier)

## Limitations

- Only text spans marked with colored boxes will be considered for replacement.
- The replacement text should not exceed the length of the original text span to avoid layout issues.

## License

This project is open-source and free to use under the MIT License.

