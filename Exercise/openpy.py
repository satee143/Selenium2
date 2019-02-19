__author__ = 'AMMA'
from selenium import webdriver
import time,openpyxl
d=[]
wk=openpyxl.load_workbook('C:/Users\satheesh/PycharmProjects/Selenium/abcd.xlsx')
ws=wk['Sheet1']
rows=ws.max_row
column=ws.max_column

for i in range(1,rows+1):
    d.clear()
    for j in range(1,column+1):
        d.append(ws.cell(i,j).value)
        c=ws.cell(i,j)
        #print(c.value)
        #print(c[i].value)

# for i in ws.iter_rows():
#     for cell in i:
#         print(str(cell.value))
# #print('\n')