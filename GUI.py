import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
import webbrowser

class SearchEngineApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Web Search Engine")

        self.label = QLabel("Enter your search query:", self)
        self.entry = QLineEdit(self)
        self.button = QPushButton("Search", self)
        self.button.clicked.connect(self.search)

        self.label.move(10, 10)
        self.entry.move(10, 40)
        self.button.move(10, 80)

        self.setGeometry(100, 100, 300, 120)

    def search(self):
        query = self.entry.text()
        if query:
            search_url = f"https://search.brave.com/search?q={query}"
            webbrowser.open(search_url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SearchEngineApp()
    window.show()
    sys.exit(app.exec_())
