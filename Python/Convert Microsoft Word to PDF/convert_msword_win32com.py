import os
import win32com.client
import time

format_code = 17

time_start = time.time()

# create the MS word app
word_app = win32com.client.Dispatch('Word.Application')

# conversion
file_input = os.path.abspath('./sample_data/sample_file1.doc')
file_output = os.path.abspath('./sample_data/sample_file1.pdf')
word_file = word_app.Documents.Open(file_input)
word_file.SaveAs(file_output,FileFormat=format_code)
word_file.Close()

file_input = os.path.abspath('./sample_data/sample_file2.docx')
file_output = os.path.abspath('./sample_data/sample_file2.pdf')
word_file = word_app.Documents.Open(file_input)
word_file.SaveAs(file_output,FileFormat=format_code)
word_file.Close()

# close file and application
word_app.Quit()

time_end = time.time()

print(f'Time used for conversion {time_end - time_start}')