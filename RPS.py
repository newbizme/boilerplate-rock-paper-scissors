import random

def player(prev_play, opponent_history=[]):
    # Сохраняем историю ходов противника
    if prev_play:
        opponent_history.append(prev_play)
    # Для первых ходов делаем последовательные попытки, чтобы собрать паттерн
    if len(opponent_history) < 3:
        return "R"
    # Анализ частоты ходов противника
    last = opponent_history[-1]
    freq = {"R": 0, "P": 0, "S": 0}
    for move in opponent_history:
        freq[move] += 1
    # Против частовстречающихся ходов выбираем победный
    if freq["R"] > freq["P"] and freq["R"] > freq["S"]:
        return "P"  # Побеждает камень
    if freq["P"] > freq["R"] and freq["P"] > freq["S"]:
        return "S"  # Побеждает бумагу
    if freq["S"] > freq["R"] and freq["S"] > freq["P"]:
        return "R"  # Побеждает ножницы
    # Если все одинаково — случайный ход
    return random.choice(["R", "P", "S"])
