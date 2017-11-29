import openpyxl


class FileProcessor:

    def __init__(self, file):
        self.file = file

    def process(self):
        wb = openpyxl.load_workbook(self.file)
        sheet = wb.get_sheet_by_name('Sheet1')

        for row in range(1, sheet.max_row + 1):
            print(sheet['A' + str(row)].value + '::' + sheet['C' + str(row)].value)
            print('[ END ROW ]')
