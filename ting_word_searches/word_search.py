# from ting_file_management.queue import Queue
# from ting_file_management.file_process import process


def exists_word(word, instance):
    word_lower = word.lower()
    size = instance.__len__()
    qtd = "qtd_linhas"
    line = "linhas_do_arquivo"
    nom_arq = "nome_do_arquivo"

    # archive_match = {
    #     "palavra": word,
    #     "arquivo": '',
    #     "ocorrencias": []
    # }

    returned_list = []

    for i in range(size):  # percorre cada item da lista
        print(f"PASSANDO PELO ITEM {i}", instance.search(i)[nom_arq])
        ocorrencias = []
        for j in range(
            int(instance.search(i)[qtd])
        ):  # percorre cada linha do item
            print(f"PASSANDO PELO linha {j}", instance.search(i)[line][j])
            if word_lower in instance.search(i)[line][j].lower():
                # print('MATCH!')
                ocorrencias.append({"linha": j + 1})
                # archive_match['arquivo'] = instance.search(i)[nom_arq]
                # archive_match['ocorrencias'].append({'linha': j + 1})
        # print('ARCHIVE MATCH:', archive_match)
        if len(ocorrencias):
            returned_list.append(
                {
                    "palavra": word,
                    "arquivo": instance.search(i)[nom_arq],
                    "ocorrencias": ocorrencias,
                }
            )
        print("RETURNED LIST::", returned_list)

    return returned_list


"""
Fazer uma função somente para checar se tem, na linha, a palavra procurada
"""


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


# fila01 = Queue()
# process("news_file2.txt", fila01)
# process("news_file3.txt", fila01)

# exists_word('de', fila01)
