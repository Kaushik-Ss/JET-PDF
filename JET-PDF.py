from PyPDF2 import PdfFileWriter, PdfFileReader
import os
from tqdm import tqdm

        
def extract_information(pdf_path):
        try:
                with open(pdf_path,'rb') as f:
                        pdf=PdfFileReader(f)
                        information=pdf.getDocumentInfo()
                        number_of_pages = pdf.getNumPages()
                # print(information)
                txt = f"""
            Information about {pdf_path}: 
            Author: {information.author}
            Title: {information.title}
            Number of pages: {number_of_pages}
            """
                print(txt)
        except:
                return "Can't open pdf"

        return 'successfully opened'
def get_duplicates(path):
        print('The duplicates are: ')
        with open(path,'rb') as f:
                pdf=PdfFileReader(f)
                number_of_pages = pdf.getNumPages()
                for page_1 in range(number_of_pages):
                        for page_2 in range(page_1+1,number_of_pages):
                                pageObj1 = pdf.getPage(page_1)
                                pageObj2 = pdf.getPage(page_2)
                                if pageObj1==pageObj2:
                                        print(page_1,page_2)



def get_duplicates_dir(path):
        dupli={}
        try:
                with open(path,'rb') as f:
                        pdf=PdfFileReader(f)
                        print('The duplicates are: ')
                        number_of_pages = pdf.getNumPages()
                        tqdm_bar= list(range(number_of_pages))
                        for page_1 in tqdm.tqdm(tqdm_bar):
                                for page_2 in range(page_1+1,number_of_pages):
                                        pageObj1 = pdf.getPage(page_1)
                                        p1=pageObj1.extractText()
                                        pageObj2 = pdf.getPage(page_2)
                                        p2=pageObj2.extractText()
                                        try:
                                                if p1==p2:
                                                        if (min(page_1,page_2),max(page_1,page_2)) not in dupli:
                                                                dupli[(min(page_1,page_2),max(page_1,page_2))]=1
                                        except:
                                                print("{page_1} and {page_2} Can't be compared")
                duplicates=[]
                if len(duplicates)==0:
                        print('None')
                for rep in dupli:
                        duplicates.append(rep[1])
                        print(rep)
                return duplicates
        except:
                return "Can't open file"


def delete_duplicate(old_path,duplicates,new_path='new pdf.pdf'):
        try:
                print('Pages to delete are')
                print(duplicates)
                infile = PdfFileReader(old_path, 'rb')
                number_of_pages = infile.getNumPages()
                pages_to_keep = [item for item in range(number_of_pages) if item not in duplicates]
                output = PdfFileWriter()

                
                for i in tqdm(pages_to_keep):
                    p = infile.getPage(i)
                    output.addPage(p)

                with open(new_path, 'wb') as f:
                    output.write(f)
                return new_path+' has been successfully created at location '+os.path.abspath(new_path)
        except:
                return new_path+' failed to create'

print('Welcome to Jet-PDF')

if __name__=='__main__':
        print('Enter Absoulte pdf location to remove duplicate pages [with .pdf at end]?')
        path=input()
        info=extract_information(path)
        print(info)
        if info!="Can't open pdf":
                duplicates=get_duplicates_dir(path)
                if duplicates!="Can't open file":
                                print('Enter new file name? don"t add .pdf at end')
                                new_path=input()
                                new_path+='.pdf'
                                print(delete_duplicate(path,duplicates,new_path))
        print('Thank you for using Jet-PDF')
        print('If you felt this application was helpful please star this repository')
        print('Made with love 💚 by Kaushik')






