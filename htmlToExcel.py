from bs4 import BeautifulSoup
import os, openpyxl


def write_to_xl(func_flag, *contents_for_xl):
    if func_flag == 0:
        with open('Result.xls', 'w') as Rd:
            Rd.write('Citation, Title')
            Rd.write('\n')
            for content in contents_for_xl:
                Rd.write(str(content))
                Rd.write('\n')
    else:
        with open('Result.xls', 'a') as Rd:
            for content in contents_for_xl:
                Rd.write(str(content))
                Rd.write('\n')


# root_path = input('Enter the Path of the folder where HTML files/folders exist: ')
root_path = r'D:\PharmSource\PharmSourceDocuments'
no_of_files_parsed = 0
flag = 0
all_files = []
parsed_files = []
for i in os.listdir(root_path):
    if os.path.isfile(i):
        filename, file_ext = os.path.splitext(i)
        if file_ext == '.html':
            with open(i, 'r') as html_file:
                try:
                    # all_files(flag, i)
                    all_files.append(i)
                    contents = html_file.read()
                    soup = BeautifulSoup(contents, 'html.parser')
                    fir_p, sec_p, fin_p = soup.find('p'), soup.find_next_sibling('p'), soup.find_next_siblings('p')
                    write_to_xl(flag, fir_p, sec_p, fin_p)
                    # for each_p in fin_p:
                    #     write_to_xl(each_p, flag)
                    no_of_files_parsed += 1
                    # parsed_file_names(flag, i)
                    parsed_files.append(i)
                    flag += 1
                except Exception as e:
                    print('Something has been mapped to undefined', e)

print(no_of_files_parsed)

for file in all_files:
    if file not in parsed_files:
        print(file)
# TODO : Learn Flask and build a normal website
