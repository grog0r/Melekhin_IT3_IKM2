class BallGame:
    def __init__(self): # создаем пустой стек и счетчик удаленных шариков
        self.stack = []
        self.removed_count = 0

    def add_ball(self, color): # добавление шарика в цепочку и обработка удаления последовательностей, цвет шариков
        self.stack.append(color) # добавляем текущий шарик в стек
        
        while len(self.stack) >= 3: # проверяем есть ли последовательность из 3-х и более шариков
            last_three = self.stack[-3:] # берем 3 последних шарика
            
            if last_three[0] == last_three[1] == last_three[2]: # проверяем одинаковые ли 3 последних шарика
                self.stack = self.stack[:-3] # если одинаковые - удаляем их из стека
                self.removed_count += 3 # увеличиваем счетчик
                
                if len(self.stack) >= 2 and self.stack[-1] == self.stack[-2]: # проверяем образовалась ли новая последовательность при удалении шариков
                    # если два последних шарика одинаковые - продолжаем проверку
                    continue
            else:
                # если последовательности нет - выходим
                break


import sys
    
try:
    print("Введите количество шариков, затем последовательность шариков в виде их цветов (0-9): ")
    input_line = sys.stdin.readline() # считываем введенную строку
        
    if not input_line.strip(): # проверка, что строка не пустая
        raise ValueError("Ошибка: отсутствуют входные данные")
        
    try:
        data = list(map(int, input_line.split())) # разбиваем строку на числа
    except ValueError as e:
        raise ValueError("Ошибка: входные данные должны быть целыми числами") from e
        
    if len(data) < 2: # проверка на достаточное количество шариков
        raise ValueError("Ошибка: недостаточно данных (нужно количество и хотя бы один шарик)")
        
    n = data[0]
    balls = data[1:]
        
    if n != len(balls): # проверяем совпадение количества шариков
       raise ValueError(f"Ошибка: заявлено {n} шариков, а получено {len(balls)}")
        
    for ball in balls: # проверяем диапазон цветов шариков
        if not 0 <= ball <= 9:
            raise ValueError(f"Ошибка: цвет шарика должен быть от 0 до 9, получено {ball}")
        
    game = BallGame()
        
    for ball in balls:
        game.add_ball(ball)
        
    print("Количество шариков, которые будут уничтожены =", game.removed_count)
        
except ValueError as e: # обработка ошибок
    print(f"Ошибка ввода: {e}")
    sys.exit(1)
