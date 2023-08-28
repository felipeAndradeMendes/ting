from .file_management import txt_importer
# from .queue import Queue


def process(path_file, instance):
    file_data = txt_importer(path_file)
    processed_text = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_data),
        "linhas_do_arquivo": file_data,
    }

    instance.enqueue(processed_text)
    print(processed_text)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


# fila01 = Queue()
# process('news_file.txt', fila01)
# print('FILA 01:', vars(fila01))
