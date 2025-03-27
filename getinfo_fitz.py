import fitz
import random

def get_info(input_pdf, output_pdf,old_text):
    doc = fitz.open(input_pdf)
    clean_old_text = " ".join(old_text.lower().split())
    matches = []
    for page_num, page in enumerate(doc):
        text_info = page.get_text("dict")
        for block in text_info["blocks"]:
            for lines in block.get("lines", []):
                for span in lines.get("spans", []):
                    #if clean_old_text in span['text'].lower():
                        font_size = span["size"]
                        font_color = span["color"]
                        font_name = span['font']
                        bbox = span["bbox"]
                        text = span['text']
                        rect = fitz.Rect(span['bbox'])
                        text_width = rect.width
                        random_color =(random.random(),random.random(),random.random())
                        page.draw_rect(rect,color=random_color)
                        
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
                            'font_name':font_name
                        }
                        print(f"page num: {match_data['page_num']+1}\n Text:{match_data['text']}\n Font size:{match_data['font_size']} Font color:{match_data['font_color']} Font name:{match_data['font_name']}\n Bboxes:{match_data['bbox']}\n")
                        matches.append(match_data)
                        
    
    matches.sort(key=lambda x: (x["page_num"], x["bbox"][1], x["bbox"][0]))  # Sort by page, then y, then x
    doc.save(output_pdf)
    doc.close()
    return matches


result=get_info("input.pdf","output.pdf","old")

