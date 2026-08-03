#io:PDF ko hard disk mai save krega & RAM mai Memory Buffer file bnayga
import io
# canvas: reportlab ka robot jo print krega AI text
from reportlab.pdfgen import canvas

def create_pdf(AItext_content):
    # 1.RAM mai Memory Buffer file bnayga (blank)
    buf = io.BytesIO()

    # 2.Robot canvas ko buffer(blank) file dena
    c = canvas.Canvas(buf)
    
    # 3.PDF ke heading ka font set krna
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800, "AKGEC AI Notes Summarizer - Exam Ready - by Anmol Shah 👈😎")
    c.setLineWidth(1)
    c.line(50, 785, 550, 785) #boder lines
    
    # 4.printing AItext_content
    c.setFont("Helvetica", 12)
    y_position = 750           # first line set at height 750

    # 5.change page if height kamm bache 50 se (mtlb page complete)
    for line in AItext_content.split('\n'):
        if y_position < 50:
            c.showPage()                      #open next page
            c.setFont("Helvetica", 12)        #again set font for that page
            y_position = 750
        c.drawString(50, y_position, line)    #print bachi hui lines
        y_position -= 20                      #spacing 20 lines downward for next page
    c.save()                                  #robot save the file
    buf.seek(0)                               #return back to first page for reading the content to user
    return buf.getvalue()                     #return this pdf to website