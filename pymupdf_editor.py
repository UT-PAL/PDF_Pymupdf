
import fitz
from pdf2image import convert_from_path
import numpy as np
import re
from fitz_marker import marker
import cv2


def normalize_text(text):
    return re.sub(r'[^\w\s]', '', text).lower().strip()


def get_bgcolor(input_pdf, x_min, y_min):
    pages = convert_from_path(input_pdf)
    for page in pages:
        np_page = np.array(page)
        np_page = cv2.cvtColor(np_page, cv2.COLOR_RGB2BGR)

        if 0 <= y_min+2 < np_page.shape[0] and 0 <= x_min+2 < np_page.shape[1]:
            bg_color = tuple(int(c) for c in np_page[y_min+2, x_min+2])
        else:
            bg_color = (255, 255, 255)
        bg_color = (bg_color[2], bg_color[1], bg_color[0])
        normalized_bg_color = tuple(c / 255 for c in bg_color)
        return normalized_bg_color


def replace_text(input_pdf, output_pdf, old_text):
    doc = fitz.open(input_pdf)
    combined = ''
    for page_num, page in enumerate(doc):

        text_info = page.get_text("dict")
        for block in text_info["blocks"]:
            # print(block)
            for lines in block.get("lines", []):
                # print(lines)
                for span in lines.get("spans", []):
                    # print(span)
                    clean_span_text = normalize_text(span["text"])
                    if clean_span_text == '':
                        continue
                    clean_old_text = normalize_text(old_text)
                    start_index = clean_old_text.find(clean_span_text)

                    if start_index != -1:
                        end_index = start_index+len(clean_span_text)
                        print(
                            f"page num: {page_num} Found: '{clean_old_text[start_index:end_index]}' at [{start_index}:{end_index}] span {clean_span_text}\n")

                        if clean_old_text[start_index:end_index] == clean_span_text:
                            rect = fitz.Rect(span["bbox"])
                            print(f"Orginal bbox:{rect}\n")
                            print(
                                f"start_index:{start_index} end index:{end_index}\n")
                            combined += span['text']
                            print(
                                f"span text :{span['text']}")
                            print("combined text:\n", combined)
                            replay = input(
                                f"enter y or n to do the changes in the span text\n")
                            if replay.lower() == 'y':
                                new_text = input(
                                    f"Enter the text to be inserted  (text length should not exceed the {len(span['text'])}):\n")
                                # Get transparency
                                alpha = span.get("alpha", 1)
                                font_size = span["size"]
                                font_color = span["color"]
                                font_name = span['font']
                                bbox = span["bbox"]
                                text = span['text']
                            # Convert color to (R, G, B)
                                r = (font_color >> 16) & 255
                                g = (font_color >> 8) & 255
                                b = font_color & 255

                                font_color = (r, g, b)
                                normalized_font_color = tuple(
                                    c / 255 for c in font_color)

                                print(font_name)
                                print(normalized_font_color)
                                print(font_size)

                            #     Compute bounding box positions

                                x_min = int(bbox[0])
                                y_min = int(bbox[1])
                                x_max = int(bbox[2])
                                y_max = int(bbox[3])
                                print(f"bbox: {x_min, y_min, x_max, y_max}")

                                normalized_bg_color = get_bgcolor(
                                    input_pdf, x_min, y_min)
                                print("normalized bg color",
                                      normalized_bg_color)
                                word_bbox = fitz.Rect(
                                    rect.x0, rect.y0, rect.x1, rect.y1)
                                page.draw_rect(
                                    word_bbox, fill=normalized_bg_color, color=normalized_bg_color)

                                page.insert_text((word_bbox.x0, word_bbox.y1-2), new_text,
                                                 fontsize=font_size, fontname='helv', color=normalized_font_color)
                            else:
                                continue

                            '''
            text_width = rect.width
            char_count = len(span['text'])
            char_width = text_width/char_count

            word_x0 = rect.x0 +(start_index*char_width)
            word_x1 = rect.x0 +(end_index*char_width)
                            '''

    doc.save(output_pdf)
    doc.close()
    return True


if __name__ == '__main__':

    input_pdf = input("enter input pdf name\n")
    output_pdf = "utpal_newcv_edited.pdf"
    marked_pdf = "fitz_marker.pdf"
    print("Wellcome to pymupdf pdf editor(supported fonts):\n1. helv\n ")
    mark = marker(input_pdf, marked_pdf)
    if mark:
        print(f"see the saved pdf file {marked_pdf}")

    old_text = input(
        f"enter the text to be replaced (text should be in selected colored boxes) in the :{marked_pdf} :\n")

    result = replace_text(input_pdf, output_pdf, old_text)

    try:
        if result:
            print(f"{output_pdf} saved successfully\n")
    except Exception as e:
        print(f"Error: {e}")


# supported fonts with pymupdf
# "helv" (Helvetica)
# "cour" (Courier)
# "times" (Times New Roman)
# "symbol" (Symbol)
# "zapfdingbats" (Zapf Dingbats)
