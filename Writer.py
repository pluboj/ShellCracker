from openpyxl import Workbook
from openpyxl.compat import range
from openpyxl.utils import get_column_letter


class Writer:
    def __init__(self, file, destination):
        self.file = file
        self.destination = destination

    def create_file(self):
        wb = Workbook()
        dest_filename = self.destination
        print(dest_filename)
