from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

    def search(self, index):
        if index < 0 or index >= self.queue.__len__():
            raise IndexError("Índice Inválido ou Inexistente")
        return self.queue[index]


# if __name__ == "__main__":
    # queue_test = Queue()
    # print('FILA VAZIA:', vars(queue_test))
    # queue_test.enqueue("Jorge")
    # # queue_test.__len__()
    # print('FILA UM ITEM:', vars(queue_test))
    # queue_test.enqueue("Jurema")
    # # queue_test.__len__()
    # print('FILA DOIS ITENS:', vars(queue_test))
    # queue_test.dequeue()
    # # queue_test.__len__()
    # print('FILA MENOS PRIMEIRO ITEM:', vars(queue_test))
