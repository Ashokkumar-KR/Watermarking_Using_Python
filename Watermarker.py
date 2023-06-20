import PyPDF2
template = PyPDF2.PdfReader(open('Sample.pdf', 'rb'))   # Replace 'Sample.pdf' with the name of the PDF to be watermarked if it is present within the same folder; otherwise, provide its directory  
watermark = PyPDF2.PdfReader(open('Watermark.pdf', 'rb'))     # Replace 'wtr.pdf' with the name of watermark source pdf
output = PyPDF2.PdfWriter()

for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)

    with open('Watermarked Output.pdf', 'wb') as file: # Change 'Watermarked Output.pdf' with your desired output file name.
        output.write(file)
