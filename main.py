from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P",unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
df = pd.read_csv("topics.csv")


for index,row in df.iterrows():
    for i in range(row['Pages']):
        pdf.add_page()
        #set header
        pdf.set_font(family="Times",style="B", size=24)
        pdf.set_text_color(0,80,100)
        pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1 , border=0)
        pdf.line(10,21,200,21)
        #set footer
        pdf.ln(250)
        pdf.set_font(family="Times",style="I", size=10)
        pdf.set_text_color(0,20,20)
        pdf.cell(w=0,h=12, txt=row['Topic'], align='R', ln=1 , border=0 )

pdf.output('output.pdf')