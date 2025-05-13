from itertools import combinations

def comb_summa(candidates, target):
    resultat = set()  #чтоб  хранить ток уникальные комбо


    for numbers in candidates:
        if numbers == target:
            resultat.add((numbers,))

    # Генерируем комбинации разной длинн
    for i in range(2, len(candidates) + 1):  # Начинаем с 2 до длины списка
        for combo in combinations(candidates, i):  #i определит какого размера будут генериться комбинации
            if sum(combo) == target:
                resultat.add(combo)  # Добавляем комбинацию в множество

    return list(resultat)  #в список

candidates = [1, 2, 2, 4, 5]
target = 8
combinations_found = comb_summa(candidates, target)
print(combinations_found)