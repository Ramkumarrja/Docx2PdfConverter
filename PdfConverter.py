from docx2pdf import convert

class Docx2Pdf:
    def Doc2PdfConverter(self,docx_path,pdf_path):
        self.Docx=docx_path
        self.Pdf=pdf_path
        print("pdf file converter sucssfully")
        return(convert(self.Docx,self.Pdf))
