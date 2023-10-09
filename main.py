import sys
from PyQt6.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QPushButton, QStackedLayout, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QFormLayout, QLineEdit, QPlainTextEdit, QComboBox, QDateEdit, QSlider, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.data = [];
        self.setWindowTitle("My App")

        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stacklayout = QStackedLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(self.stacklayout)

        btn = QPushButton("Form")
        btn.pressed.connect(self.activate_tab_form)
        button_layout.addWidget(btn)

        btn = QPushButton("Tabel")
        btn.pressed.connect(self.activate_tab_table)
        button_layout.addWidget(btn)

        #  tab Form
        form_tab = QWidget()
        form_layout = QFormLayout()
        self.input_nama = QLineEdit()
        form_layout.addRow("Nama:", self.input_nama)
        self.input_nim = QLineEdit()
        form_layout.addRow("Nim:", self.input_nim)
        self.input_alamat = QPlainTextEdit()
        form_layout.addRow("Alamat:", self.input_alamat)
        combobox = QComboBox()
        combobox.addItem("Laki-laki")
        combobox.addItem("Perempuan")
        self.kelamin = combobox
        form_layout.addRow("Jenis Kelamin:", self.kelamin)
        self.input_tgl = QDateEdit()
        form_layout.addRow("Tanggal Lahir:", self.input_tgl)
        form_tab.setLayout(form_layout)
        self.input_hobi = QPlainTextEdit()
        form_layout.addRow("Hobi:", self.input_hobi)
        slider = QSlider()
        slider.setMinimum(50)
        slider.setMaximum(200)
        self.tinggi = slider
        form_layout.addRow("Tinggi Badan:", self.tinggi)
        self.btn_submit = QPushButton("Submit")
        self.btn_submit.clicked.connect(self.on_submit)
        form_layout.addRow(self.btn_submit)
        self.stacklayout.addWidget(form_tab)

        #  tab Tabel
        table_tab = QWidget()
        table_layout = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setRowCount(7)
        self.table.setHorizontalHeaderLabels(["Nama", "Nim", "Alamat", "Jenis Kelamin", "Tanggal Lahir", "Hobi", "Tinggi Badan"])

        # for row_index, row_data in enumerate(self.data):
        #     for col_index, cell_value in enumerate(row_data):
        #         item = QTableWidgetItem(cell_value)
        #         self.table.setItem(row_index, col_index, item)


        table_layout.addWidget(self.table)
        table_tab.setLayout(table_layout)
        self.stacklayout.addWidget(table_tab)

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    def add_item_table(self):
        for row_index, row_data in enumerate(self.data):
            for col_index, cell_value in enumerate(row_data):
                item = QTableWidgetItem(cell_value)
                self.table.setItem(row_index, col_index, item)


    def on_submit(self):
            nama = self.input_nama.text()
            nim = self.input_nim.text()
            alamat = self.input_alamat.toPlainText()
            jenis_kelamin = self.kelamin.currentText()
            tanggal_lahir = self.input_tgl.date().toString("yyyy-MM-dd")
            hobi = self.input_hobi.toPlainText()
            tinggi_badan = str(self.tinggi.value()) 
            # newData = {
            #     "nama": nama,
            #     "nim": nim,
            #     "alamat": alamat,
            #     "jenis_kelamin": jenis_kelamin,
            #     "tanggal_lahir": tanggal_lahir,
            #     "hobi": hobi,
            #     "tinggi_badan": tinggi_badan
            # }
            newData = [
                nama,
                nim,
                alamat,
                jenis_kelamin,
                tanggal_lahir,
                hobi,
                tinggi_badan
            ]

            self.data.append(newData)
            self.add_item_table()
            self.input_nama.clear()
            self.input_nim.clear()
            self.input_alamat.clear()
            self.input_hobi.clear()
            # print (nama, nim, alamat, jenis_kelamin, tanggal_lahir, hobi, tinggi_badan)
                # self.input_line.setText(str(result))

    def activate_tab_form(self):
        self.stacklayout.setCurrentIndex(0)

    def activate_tab_table(self):
        self.stacklayout.setCurrentIndex(1)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
