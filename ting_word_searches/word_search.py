def set_ocorrencias(linha, conteudo, has_conteudo):
    if has_conteudo:
        return {"linha": linha, "conteudo": conteudo}
    else:
        return {"linha": linha}


def search_in_fila(word, instance, has_conteudo):
    word_lower = word.lower()
    size = instance.__len__()
    qtd_lin = "qtd_linhas"
    lin_arq = "linhas_do_arquivo"
    nom_arq = "nome_do_arquivo"

    returned_list = []

    for i in range(size):
        item = instance.search(i)
        ocorrencias = []
        for j in range(int(item[qtd_lin])):
            if word_lower in item[lin_arq][j].lower():
                ocorrencias.append(
                    set_ocorrencias(j + 1, item[lin_arq][j], has_conteudo)
                )
        if len(ocorrencias):
            returned_list.append(
                {
                    "palavra": word,
                    "arquivo": item[nom_arq],
                    "ocorrencias": ocorrencias,
                }
            )

    return returned_list


def exists_word(word, instance):
    search_result = search_in_fila(word, instance, False)
    return search_result


def search_by_word(word, instance):
    search_result = search_in_fila(word, instance, True)
    return search_result
