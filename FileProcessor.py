import openpyxl
from Writer import Writer


class FileProcessor:

    def __init__(self, file):
        self.file = file

    ''' 
    Excel format:
        column A: new file variable ID
        column B: new file label
        column C: old file variable ID
        column D: old file label
    '''

    def process(self):
        wb = openpyxl.load_workbook(self.file)
        sheet = wb.get_sheet_by_name('Sheet1')
        data_new_file = {}
        data_old_file = {}
        data_final = {}

        for row in range(1, sheet.max_row + 1):
            current_row = str(row)
            new_var = sheet['A' + current_row].value
            old_var = sheet['C' + current_row].value
            new_label = sheet['B' + current_row].value
            old_label = sheet['D' + current_row].value
            if new_var and new_label:
                data_new_file[row] = {'var': new_var, 'label': new_label}
            if old_var and old_label:
                data_old_file[row] = {'var': old_var, 'label': old_label}

        for item in data_new_file:
            label = data_new_file[item]['label']
            tmp_old_item = []

            for row in data_old_file:
                if label == data_old_file[row]['label']:
                    if item in data_old_file:
                        tmp_old_item.append({'updated': 1, 'var': data_old_file[row]['var'],
                                            'label': data_old_file[row]['label']})

            if len(tmp_old_item) == 1:
                data_final[item] = tmp_old_item[0]
            else:
                data_final[item] = {'updated': 0, 'var': data_new_file[item]['var'],
                                    'label': data_new_file[item]['label']}

        '''
        for item in data_final:
            print(str(item) + ' :: '
                  + str(data_final[item]['updated']) + ' : '
                  + str(data_final[item]['var']) + ' : '
                  + str(data_final[item]['label']))
        '''
        w = Writer(data_final, data_old_file, self.file)
        w.create_file()
        return data_final
