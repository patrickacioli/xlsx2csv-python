import csv
import openpyxl
from os import listdir
from os.path import isfile, join

def read_files():
    return [f for f in listdir("input") if isfile(join("input", f))]

for file in read_files():
    wb = openpyxl.load_workbook(f"input/{file}", read_only=True)
    for worksheet in wb.worksheets:
        ws = wb[worksheet.title]
        with open(f'output/{file.replace(".xlsx", ".csv")}', "w") as out:
            writer = csv.writer(out)
            for row in ws:
                values = (cell.value for cell in row)
                writer.writerow(list(values))
