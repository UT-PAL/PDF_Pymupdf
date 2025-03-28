
import fitz 
import matplotlib.font_manager
import os
import cv2
import numpy as np
import re
from pdf2image import convert_from_path

def normalize_text(text):
    return re.sub(r'[^\w\s]', '', text)



def replace_text(input_pdf,output_pdf,old_text,new_text):
    doc = fitz.open(input_pdf)
    clean_old_text = " ".join(old_text.lower().split())
    print(clean_old_text)
    for page_num,page in enumerate(doc):
        fonts = page.get_fonts(full=True)
        for font in fonts:
            print(f"fontname,{font[3]},Embedded:{font[4]},Type:{font[2]}")
        text_info = page.get_text("dict")
        for block in text_info["blocks"]:
            #print(block)
            for lines in block.get("lines",[]):
            #print(lines)
                for span in lines.get("spans",[]):
                    #print(span)
                    clean_span_text = " ".join((span["text"].lower()).split())
                    if normalize_text(clean_old_text) in normalize_text(clean_span_text):
                        print(span["text"])
                        
                        rect = fitz.Rect(span["bbox"])
                        print(f"Orginal bbox:{rect}")
                        
                        text_width = rect.width
                        char_count = len(span['text'])
                        char_width = text_width/char_count
                        print("char width",char_width)

                        start_index = normalize_text(clean_span_text).find(normalize_text(clean_old_text))
                        end_index = start_index+len(old_text)
                        print(f"start_index:{start_index},end_index:{end_index}")
                        
                        word_x0 = rect.x0 +(start_index*char_width)
                        word_x1 = rect.x0 +(end_index*char_width)
                        print(f"word_x0:{word_x0},word_x1:{word_x1}")
                        word_bbox = fitz.Rect(word_x0, rect.y0, word_x1, rect.y1)
                        print(f"Word '{old_text}' bbox: {word_bbox}")
                        
                        font_size = span["size"]
                        font_color = span["color"]
                        font_name =span["font"]
                         # Convert color to (R, G, B)
                        r = (font_color >> 16) & 255
                        g = (font_color >> 8) & 255
                        b = font_color & 255

                        font_color=(r, g, b)
                        normalized_font_color = tuple(c / 255 for c in font_color)

                        print(font_name)
                        print(normalized_font_color)
                        print(font_size)
                        page.draw_rect(word_bbox,color=(1,1,1),fill=(1,1,1))
                        page.insert_text((word_bbox.x0,word_bbox.y1-2),new_text,
                        fontsize=font_size, fontname='helv', color=normalized_font_color)

    doc.save(output_pdf)
    doc.close()


replace_text("utpal.pdf","utpal_newcv_edited.pdf","Link"," utpal")

#supported fonts with pymupdf
#"helv" (Helvetica)
#"cour" (Courier)
#"times" (Times New Roman)
#"symbol" (Symbol)
#"zapfdingbats" (Zapf Dingbats)

