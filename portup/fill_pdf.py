import csv
from fdfgen import forge_fdf
import os
import sys

sys.path.insert(0, os.getcwd())

def process_csv(file):
    headers = []
    data =  []
    csv_data = csv.reader(open(file))
    for i, row in enumerate(csv_data):
        if i == 0:
            headers = row
            continue;
        field = []
        for i in range(len(headers)):
            field.append((headers[i], row[i]))
        data.append(field)
    return data

def form_fill(fields, pdf_form, file_prefix, output_dir):
    tmp_file = "tmp.fdf"
    fdf = forge_fdf("",fields,[],[],[])
    fdf_file = open(tmp_file,"w")
    fdf_file.write(fdf)
    fdf_file.close()
    output_file = '{0}{1}{2}.pdf'.format(output_dir, file_prefix, fields[0][1])
    cmd = 'pdftk "{0}" fill_form "{1}" output "{2}" flatten'.format(pdf_form, tmp_file, output_file)
    os.system(cmd)
    os.remove(tmp_file)

## Set the file name
filename_prefix = "pay_slip_"
csv_file = "sample2.csv"
pdf_file = "form.pdf"
output_folder = '../output/'

## Run the code

data = process_csv(csv_file)
print('Generating Forms:')
print('-----------------------')
for i in data:
    #if i[0][1] == 'Yes':
    #    continue
    print('{0}{1} created...'.format(filename_prefix, i[0][1]))
    form_fill(i, pdf_file, filename_prefix, output_folder)