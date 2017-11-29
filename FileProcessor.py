import openpyxl


class FileProcessor:

    def __init__(self, file):
        self.file = file

    def process(self):
        wb = openpyxl.load_workbook(self.file)
        sheet = wb.get_sheet_by_name('Sheet1')
        data_new_file = {}
        data_old_file = {}
        data_final = {}

        for row in range(1, sheet.max_row + 1):
            current_row = str(row)
            variable_a = sheet['A' + current_row].value
            variable_b = sheet['C' + current_row].value
            label_a = sheet['B' + current_row].value
            label_b = sheet['D' + current_row].value
            if variable_a and label_a:
                data_new_file[row] = {'var': variable_a, 'label': label_a}
            if variable_b and label_b:
                data_old_file[row] = {'var': variable_b, 'label': label_b}

        for item in data_new_file:
            label = data_new_file[item]['label']

            for row in data_old_file:
                if label == data_old_file[row]['label']:
                    print(row)
                    data_final[item] = {'updated': 1, 'var': data_old_file[item]['var'],
                                        'label': data_old_file[item]['label']}
                else:
                    data_final[item] = {'updated': 0, 'var': data_new_file[item]['var'],
                                        'label': data_new_file[item]['label']}

        for item in data_final:
            print(str(item) + ' :: ' + str(data_final[item]))
