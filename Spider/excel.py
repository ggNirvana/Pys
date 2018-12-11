import xlrd
import xlsxwriter
book = xlsxwriter.Workbook('result.xlsx')
sheet = book.add_worksheet()
sheet.write(0, 0, '名称')
sheet.write(0,1,'连接')
sheet.write(0,2,'分类')
