import fitz
import random
import re


def marker(input_pdf, output_pdf):
    doc = fitz.open(input_pdf)
    matches = []
    j=0
    for page_num, page in enumerate(doc):
        text_info = page.get_text("dict")
        
        #print(page.get_fonts())
        for block in text_info["blocks"]:
            if block.get("oc", False):  # Ignore hidden layers
                continue
            for lines in block.get("lines", []):
                for span in lines.get("spans", []): 
                    color = span.get("color", 0)  # Default to black if missing
                    alpha = span.get("alpha", 1)  # Get transparency
                    font_size = span["size"]
                    font_color = span["color"]
                    font_name = span['font']
                    bbox = span["bbox"]
                    text = span['text']
                    
                    rect = fitz.Rect(span['bbox'])
                    random_color =(random.random(),random.random(),random.random())
                    word_bbox = fitz.Rect(bbox)
                    page.draw_rect(word_bbox,color=random_color)
                        
                        # Convert color to (R, G, B)
                    r = (font_color >> 16) & 255
                    g = (font_color >> 8) & 255
                    b = font_color & 255
                    font_color = (r, g, b)

                    match_data = {
                            'page_num': page_num,
                            'font_size': font_size,
                            'font_color': font_color,
                            'bbox': bbox,
                            'text': text,
                            'font_name':font_name,
                            'alpha':span.get('alpha',1),
                                        } 
                    print(f"item: {j} ,Alpha: {span.get('alpha',1)},page num: {match_data['page_num']+1}\n Text:{match_data['text']}\n Font size:{match_data['font_size']} Font color:{match_data['font_color']} Font name:{match_data['font_name']}\n Bboxes:{match_data['bbox']}\n")
                    matches.append(match_data)
                    j+=1
                        
    
    matches.sort(key=lambda x: (x["page_num"], x["bbox"][1], x["bbox"][0]))  # Sort by page, then y, then x
    doc.save(output_pdf)
    doc.close()
    print("PDF saved successfully")
    return matches






