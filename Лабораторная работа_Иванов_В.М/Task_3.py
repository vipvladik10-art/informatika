list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

center_list = len(list_players) // 2 #Делим список поровну

first_team = list_players[:center_list] #С помощью срезов создаём список для первой команды
second_team = list_players[center_list:] #С помощью срезов создаём список для второй команды

print(first_team) #Выводим список первой команды
print(second_team) #Выводим список второй команды
