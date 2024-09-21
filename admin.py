import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QIntValidator
from connect_database import ConnectDatabase
from admin_ui import Ui_Form  # Import the UI class from admin_ui.py

class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = ConnectDatabase()
        self.connectSignalsSlots()
        
        # Set validators
        self.studentid.setValidator(QIntValidator())
        self.studentsalary.setValidator(QIntValidator())
        self.studentage.setValidator(QIntValidator())

    def connectSignalsSlots(self):
        self.add_btn.clicked.connect(self.add_student)
        self.update_btn.clicked.connect(self.update_student)
        self.search_btn.clicked.connect(self.search_student)
        self.select_btn.clicked.connect(self.select_student)
        self.delete_btn.clicked.connect(self.delete_student)
        self.cleare_btn.clicked.connect(self.clear_form_info)
        self.exit_btn.clicked.connect(self.close)

    def get_student_info(self):#it not built in function -_-
        return {
            "id": self.studentid.text().strip(),
            "name": self.studentname.text().strip(),
            "salary": self.studentsalary.text().strip(),
            "age": self.studentage.text().strip(),
        }

    def add_student(self):
        student_info = self.get_student_info()

        if student_info["id"] and student_info["name"]:
            try:
                add_result = self.db.add_info(id=int(student_info["id"]),
                                              name=student_info["name"],
                                              salary=student_info["salary"],
                                              age=student_info["age"])

                if add_result:
                    QMessageBox.warning(self, "Warning", f"Add failed: {add_result}. Please try again.", QMessageBox.Ok)
                else:
                    QMessageBox.information(self, "Success", "Student added successfully.", QMessageBox.Ok)
                    self.search_student()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "Warning", "Please input student ID and name", QMessageBox.Ok)
        self.clear_form_info()
    def update_student(self):
        student_info = self.get_student_info()

        if student_info["id"]:
            try:
                update_result = self.db.update_info(
                    id=student_info["id"],
                    name=student_info["name"],
                    salary=student_info["salary"],
                    age=student_info["age"]
                )

                if update_result:
                    QMessageBox.warning(self, "Warning", f"Failed to update the information: {update_result}. Please try again.", QMessageBox.Ok)
                else:
                    QMessageBox.information(self, "Success", "Student information updated successfully.", QMessageBox.Ok)
                    self.search_student()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "Warning", "Please select a student to update.", QMessageBox.Ok)
        self.clear_form_info()

    def search_student(self):
        student_info = self.get_student_info()#this is not built in function
        try:
            # Pass the specific id and allow partial matches for other fields
            student_result = self.db.search_info(
                id=student_info["id"] if student_info["id"] else None,  # Only search by ID if provided
                name=student_info["name"],
                salary=student_info["salary"],
                age=student_info["age"]
            )
            self.show_data(student_result)  # Display search results
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while searching: {str(e)}", QMessageBox.Ok)

    def select_student(self):
        select_row = self.tableWidget.currentRow()
        if select_row != -1:
            self.studentid.setEnabled(False)
            id = self.tableWidget.item(select_row, 0).text().strip()
            name = self.tableWidget.item(select_row, 1).text().strip()
            salary = self.tableWidget.item(select_row, 2).text().strip()
            age = self.tableWidget.item(select_row, 3).text().strip()

            self.studentid.setText(id)
            self.studentname.setText(name)
            self.studentsalary.setText(salary)
            self.studentage.setText(age)
        else:
            QMessageBox.warning(self, "Warning", "Please select one student from the table.", QMessageBox.Ok)

    def delete_student(self):
        select_row = self.tableWidget.currentRow()
        if select_row != -1:
            reply = QMessageBox.question(self, "Warning", "Are you sure you want to delete this student?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                id = self.tableWidget.item(select_row, 0).text().strip()
                try:
                    delete_result = self.db.delete_info(id=id)
                    if not delete_result:
                        QMessageBox.information(self, "Success", "Student deleted successfully.", QMessageBox.Ok)
                        self.search_student()
                    else:
                        QMessageBox.warning(self, "Warning", f"Failed to delete the student: {delete_result}. Please try again.", QMessageBox.Ok)
                except Exception as e:
                    QMessageBox.critical(self, "Error", f"An error occurred while deleting: {str(e)}", QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "Warning", "Please select a student to delete.", QMessageBox.Ok)

    def clear_form_info(self):
        self.studentid.clear()
        self.studentid.setEnabled(True)
        self.studentname.clear()
        self.studentsalary.clear()
        self.studentage.clear()

    def show_data(self, result):
        self.tableWidget.setRowCount(100)
        if result and isinstance(result, list):
            self.tableWidget.setRowCount(len(result))
            for row, info in enumerate(result):
                for column, (key, value) in enumerate(info.items()):
                    item = QTableWidgetItem(str(value))
                    self.tableWidget.setItem(row, column, item)
        else:
            if isinstance(result, str):
                QMessageBox.warning(self, "Error", f"Database error: {result}", QMessageBox.Ok)
            else:
                QMessageBox.information(self, "Info", "No matching records found.", QMessageBox.Ok)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()