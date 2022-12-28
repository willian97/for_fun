import PyPDF2
import re
pdf_file = open('dados.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()
page = read_pdf.getPage(0)
page_content = page.extractText()
parsed = ''.join(page_content)
print("Sem eliminar as quebras")
print(parsed)
parsed = re.sub('n', '', parsed)
print("Após eliminar as quebras")
print(parsed)
print("nPegando apenas as 20 primeiras posições")
novastring = parsed[0:20]
print(novastring)