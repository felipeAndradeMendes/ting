from .file_management import txt_importer

# from queue import Queue


def process(path_file, instance):
    file_data = txt_importer(path_file)
    processed_text = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_data),
        "linhas_do_arquivo": file_data,
    }

    file = "nome_do_arquivo"

    for i in range(instance.__len__()):
        if instance.search(i)[file] == processed_text[file]:
            return None

    instance.enqueue(processed_text)
    print(processed_text)


def remove(instance):
    if instance.__len__() == 0:
        return print("Não há elementos")
    removed_element = instance.dequeue()
    print(f"Arquivo {removed_element['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


# fila01 = Queue()
# process('news_file.txt', fila01)
# print('FILA 01:', vars(fila01))
# remove(fila01)
# print('FILA APOS REMOÇÃO:', vars(fila01))
