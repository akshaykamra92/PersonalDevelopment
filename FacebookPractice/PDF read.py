import PyPDF2

# creating a pdf file object
pdfFileObj = open("PDFread.pdf", 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page()
test = pageObj.extractText()
# print(pageObj.extractText())
print(test)

# closing the pdf file object
pdfFileObj.close()