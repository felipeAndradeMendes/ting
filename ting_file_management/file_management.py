import sys


def txt_importer(path_file):
    invalid_format_error = "Formato inválido"
    file_not_found_error = f"Arquivo {path_file} não encontrado"

    if path_file.split(".")[1] != "txt":
        print(invalid_format_error, file=sys.stderr)

    try:
        with open(path_file, mode="r") as file:
            data = file.readlines()
    except FileNotFoundError:
        print(file_not_found_error, file=sys.stderr)

    else:
        list_of_news = [line.replace("\n", "") for line in data]
        return list_of_news
