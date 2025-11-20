import sys
import os
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QComboBox, QLineEdit, QPushButton, QMessageBox, 
    QSpacerItem, QSizePolicy, QCheckBox
)

class SearchApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("КонтрЗакупки · Поиск")
        self.setMinimumWidth(400)
        self.setMinimumHeight(550)  # Увеличили высоту для новых элементов

        # Загрузка стилей
        self.load_styles()

        layout = QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(12)

        self.region_label = QLabel("Регион")
        layout.addWidget(self.region_label)
        self.region_combo = QComboBox()
        regions = ["Москва", "Санкт-Петербург", "Новосибирск", "Красноярск", "Ростов-на-Дону", "Воронеж"]
        self.region_combo.addItems(regions)
        layout.addWidget(self.region_combo)

        self.keywords_label = QLabel("Ключевые слова")
        layout.addWidget(self.keywords_label)
        self.keywords_edit = QLineEdit()
        self.keywords_edit.setPlaceholderText("Например: мужские джинсы")
        layout.addWidget(self.keywords_edit)

        # Добавляем чекбоксы
        self.only_actual_checkbox = QCheckBox("Только актуальные закупки")
        self.only_actual_checkbox.setChecked(True)
        layout.addWidget(self.only_actual_checkbox)

        self.with_electronic_signature_checkbox = QCheckBox("Только с электронной подписью")
        layout.addWidget(self.with_electronic_signature_checkbox)

        self.include_archive_checkbox = QCheckBox("Включая архивные")
        layout.addWidget(self.include_archive_checkbox)

        self.search_button = QPushButton("🔍 Найти закупки")
        self.search_button.clicked.connect(self.handle_search)
        layout.addWidget(self.search_button)

        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        self.setLayout(layout)

    def load_styles(self):
        """Загрузка CSS стилей из файла"""
        # Определяем путь к файлу стилей
        current_dir = os.path.dirname(os.path.abspath(__file__))
        css_path = os.path.join(current_dir, "styles.css")
        # Читаем файл стилей
        with open(css_path, "r", encoding="utf-8") as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)
            print("Стили успешно загружены из файла")


    def handle_search(self):
        region = self.region_combo.currentText()
        keywords = self.keywords_edit.text()
        only_actual = self.only_actual_checkbox.isChecked()
        with_electronic_signature = self.with_electronic_signature_checkbox.isChecked()
        include_archive = self.include_archive_checkbox.isChecked()
        
        message = (f"Регион: {region}\n"
                  f"Ключевые слова: {keywords}\n"
                  f"Только актуальные: {'Да' if only_actual else 'Нет'}\n"
                  f"С электронной подписью: {'Да' if with_electronic_signature else 'Нет'}\n"
                  f"Включая архивные: {'Да' if include_archive else 'Нет'}")
        
        QMessageBox.information(self, "Результаты поиска", message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = SearchApp()
    window.show()
    sys.exit(app.exec())