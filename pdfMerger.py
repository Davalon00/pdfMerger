import PyPDF2
import os

#create an instance of PyPDF
merger = PyPDF2.PdfMerger()

#reads files from folder
file_list = os.listdir("files")
file_list.sort()

print("The files in the folder are:", file_list)

#merges files if extension == .pdf
for file in file_list:
    if ".pdf" in file:
        merger.append(f"files/{file}")

#saves merged files
merger.write("finalPDF.pdf")

print("Final file saved")