"""
На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
Первый список ваш лотерейный билет
Второй список содержит список чисел, которые выпали в лотерею.
Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.
Напишите класс LotteryGame, который будет иметь метод compare_lists, который будет 
сравнивать числа из вашего билета из list1 со списком выпавших чисел list2
Если совпадающих чисел нет, то выведите на экран:
Совпадающих чисел нет

list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()

Совпадающие числа: [3, 12, 8, 41, 9, 14, 5]
Количество совпадающих чисел: 7
"""

class LotteryGame:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def compare_lists(self):
        res = []
        for i in self.list1:
            for j in self.list2:
                if i == j:
                    res.append(i)
                    break

        return f'Совпадающие числа: {res}\nКоличество совпадающих чисел: {len(res)}'

list1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()
print(matching_numbers)















