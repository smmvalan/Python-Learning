import openpyxl
path="C:\\python\\data\\abc.xlsx" # excel is not created yet
workbook=openpyxl.load_workbook(path)
sheet=workbook.active #(only one sheet)
# Method2: sheet=workbook.get_sheet_by_name("sheet1") multiple sheet
for r in range (1,3):
    for c in (1,2):
        sheet.cell(row=r,column=c).value="welcome"
workbook.save(path)