def dict_to_xml(data):
    def build_xml(obj, indent_level=0):
        lines = []
        indent = "  " * indent_level  # 2 пробела на уровень вложенности

        for key, value in obj.items():
            if isinstance(value, dict):
                # Если значение — словарь, создаем открывающий тег,
                # вызываем функцию рекурсивно и закрываем тег
                lines.append(f"{indent}<{key}>")
                lines.append(build_xml(value, indent_level + 1))
                lines.append(f"{indent}</{key}>")
            else:
                # Если значение — примитив, записываем в одну строку
                lines.append(f"{indent}<{key}>{value}</{key}>")

        return "\n".join(lines)

    # Формируем итоговое содержимое с XML-декларацией
    xml_content = build_xml(data)

    # Записываем в файл student.xml в кодировке UTF-8
    with open("student.xml", "w", encoding="utf-8") as f:
        f.write(xml_content)

if __name__ == "__main__":
    data = {
        "Students": [
            {"Имя": "Алиса", "Возраст": "25"},
            {"Имя": "Борис", "Возраст": "27"},
        ]
    }

    dict_to_xml(data)

    with open("students.xml", "r", encoding="utf-8") as file:
        print(file.read())