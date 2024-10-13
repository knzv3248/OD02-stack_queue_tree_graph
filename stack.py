class Stack:
   def __init__(self):
       self.items = []

   def is_empty(self):          # Проверка стека на пустоту
       return self.items == []

   def push(self, item):        # Добавление элемента в стек
       self.items.append(item)

   def pop(self):               # Удаление верхнего (последнего) элемента из стека
       return self.items.pop()

   def peek(self):              # Просмотр верхнего (последнего) элемента без его удаления
       return self.items[-1]

   def size(self):              # Размер стека
       return len(self.items)


stack = Stack()

print(stack.is_empty())

stack.push(1)
stack.push('слово')
stack.push('python')

print(stack.is_empty())
print('Размер стека:', stack.size())
print('Верхний элемент стека:', stack.peek())

print('Выполним удаление верхнего элемента из стека: ', stack.peek())
stack.pop()

print('Новый размер стека:', stack.size())
print('Новый верхний элемент стека:', stack.peek())


