import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tabel Sederhana")
        self.setGeometry(100, 100, 600, 400)

        self.table = QTableWidget(self)
        self.table.setGeometry(50, 50, 500, 300)
        self.table.setColumnCount(3)
        self.table.setRowCount(5)

        # Mengatur judul header kolom
        self.table.setHorizontalHeaderLabels(["Nama", "NIM", "Jurusan"])

        # Mengisi data tabel
        data = [
            ["John Doe", "123456", "Informatika"],
            ["Jane Smith", "789012", "Manajemen"],
            ["Alice Johnson", "456789", "Elektro"],
            ["Bob Brown", "987654", "Teknik Sipil"],
            ["Eva Davis", "654321", "Kimia"],
        ]

        for row_index, row_data in enumerate(data):
            for col_index, cell_data in enumerate(row_data):
                item = QTableWidgetItem(cell_data)
                self.table.setItem(row_index, col_index, item)

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
