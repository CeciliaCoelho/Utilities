import os
import arxiv
import datetime
import glob
from PyPDF2 import PdfFileReader


def main():

    pdfFileList = glob.glob("*.pdf")

    for pdfFile in pdfFileList:

        try:
            search = arxiv.Search(id_list=[pdfFile[:-4]])
            paper = next(search.results())
            title = paper.title
            year = paper.published.year

        except:
            try:
                f = open(pdfFile , 'rb')
                paper = PdfFileReader(f, strict=False).getDocumentInfo()
                title = paper.title
                year = paper['/CreationDate'][2:6]
                f.close()
            except:
                pass




        if title is not None: 
            title = title.translate({ord(i): None for i in '<>:"/\\|?*'})
            os.rename(pdfFile , str(year)+"-"+title+".pdf")


if __name__ == '__main__':
    main()
