from docx import Document


# Функция для чтения данных из анкеты
def read_anketa(file_path):
    doc = Document(file_path)
    data = {}

    # Чтение всех параграфов в документе
    for paragraph in doc.paragraphs:
        text = paragraph.text.strip()

        if text.startswith("Время приема:"):
            data["time"] = text.split(":")[1].strip()
        elif text.startswith("Способ применения:"):
            data["condition"] = text.split(":")[1].strip()
        elif text.startswith("Лекарство принято:"):
            # Проверяем, есть ли галочка (☒) в тексте
            data["taken"] = "☒" in text
        elif text.startswith("Комментарий:"):
            data["comment"] = text.split(":")[1].strip()

    return data


# Основная логика программы
if __name__ == "__main__":
    # Чтение данных из анкеты
    anketa_data = read_anketa("anketa.docx")

    # Вывод данных
    print("Данные из анкеты:")
    print(f"Время приема: {anketa_data.get('time')}")
    print(f"Способ применения: {anketa_data.get('condition')}")
    print(f"Лекарство принято: {'Да' if anketa_data.get('taken') else 'Нет'}")
    print(f"Комментарий: {anketa_data.get('comment')}")