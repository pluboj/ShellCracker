from openpyxl import Workbook
from openpyxl.styles import Alignment


class Writer:
    def __init__(self, file, old_shell, destination):
        self.file = file
        self.old_shell = old_shell
        self.destination = destination

    def create_file(self):
        wb = Workbook()
        dest_filename = self.get_new_path()
        ws1 = wb.active
        ws1.title = "Updated shell"
        al = Alignment(horizontal="center")

        for row in self.file:
            a = ws1['A' + str(row)]
            b = ws1['B' + str(row)]
            a.value = self.file[row]['updated']
            a.alignment = al
            b.value = self.file[row]['var']
            if self.file[row]['updated'] == 1:
                b.style = "Good"
            else:
                b.style = "Bad"
            ws1['D' + str(row)] = self.file[row]['label']
            if row in self.old_shell:
                ws1['F' + str(row)] = self.old_shell[row]['var']
                ws1['H' + str(row)] = self.old_shell[row]['label']

        wb.save(filename=dest_filename)

    def get_new_path(self):
        path = self.destination.split('/')
        path[-1] = "SHELL.xlsx"
        return '/'.join(path)
