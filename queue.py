class Queue:
   def __init__(self):
       self.items = []

   def is_empty(self):              # Проверка очереди на пустоту
       return self.items == []

   def enqueue(self, item):         # Добавление элемента в очередь
       self.items.insert(0, item)

   def dequeue(self):               # Удаление нижнего (первого) элемента из очереди
       return self.items.pop()

   def size(self):                  # Размер очереди
       return len(self.items)

queue = Queue()

print("Проверка очереди на пустоту:", queue.is_empty())
print("Добавление 4-х элементов в очередь")
queue.enqueue( 1)
queue.enqueue("слово")
queue.enqueue("дороже")
queue.enqueue(2)

print("Проверка очереди на пустоту:", queue.is_empty())

print('\n"Вытолкнем" все элементы очереди')
for i in range(queue.size()):
    print("\nРазмер очереди:", queue.size())
    print(f"Выполним удаление нижнего (первого) элемента из очереди - '{queue.dequeue()}'")
