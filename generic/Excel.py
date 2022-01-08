import openpyxl
class Execl:
    def getData(path,sheet,row,col):
        wb = openpyxl.load_workbook(path)
        value = wb[sheet].cell(row, col).value
        print(value)
        return value
