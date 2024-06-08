import streamlit as st
import base64
import pptx
from pptx.util import Inches, Pt
import os
from model.model import AIModel


class SlideGenerator:
    def __init__(self):
        self.TITLE_FONT_SIZE = Pt(30)
        self.SLIDE_FONT_SIZE = Pt(16)
        self.slide_titles = ["About Us", "Market Analysis",
                             "Competitor", "Key Difference", "Expected Fundings & ROI"]

    def generate_slide_content(self, messages):
        slides_ai = AIModel()
        full_response = ""  # Initialize full_response before using it
        for chunk in slides_ai.loadChatCompletion(messages):
            full_response += chunk.choices[0].delta.content or ""
        return full_response

    def create_presentation(self, slide_titles, slide_contents):
        prs = pptx.Presentation()
        slide_layout = prs.slide_layouts[1]

        title_slide = prs.slides.add_slide(prs.slide_layouts[0])
        title_slide.shapes.title.text = "Pitch Deck"

        for slide_title, slide_content in zip(slide_titles, slide_contents):
            slide = prs.slides.add_slide(slide_layout)
            slide.shapes.title.text = slide_title
            slide.shapes.placeholders[1].text = slide_content

            # Customize font size for titles and content
            slide.shapes.title.text_frame.paragraphs[0].font.size = self.TITLE_FONT_SIZE
            for shape in slide.shapes:
                if shape.has_text_frame:
                    text_frame = shape.text_frame
                    for paragraph in text_frame.paragraphs:
                        paragraph.font.size = self.SLIDE_FONT_SIZE
         # Check if directory exists and create it if not
        if not os.path.exists("generated_ppt"):
            os.makedirs("generated_ppt")
        prs.save(f"generated_ppt/_presentation.pptx")

    def get_ppt_download_link(self):
        ppt_filename = f"generated_ppt/_presentation.pptx"

        with open(ppt_filename, "rb") as file:
            ppt_contents = file.read()

        b64_ppt = base64.b64encode(ppt_contents).decode()
        return f'<a href="data:application/vnd.openxmlformats-officedocument.presentationml.presentation;base64,{b64_ppt}" download="{ppt_filename}">Download the PowerPoint Presentation</a>'
