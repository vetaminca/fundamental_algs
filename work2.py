# Решение криптарифма:
#     DONALD
#   + GERALD
#   --------
#     ROBERT
#
# Условия:
#   - D = 5
#   - Каждая буква — уникальная цифра 0–9
#   - Ведущие буквы D, G, R ≠ 0
#   - Сложение выполняется по правилам обычной арифметики с переносом разрядов

import itertools

# Определим буквы, участвующие в уравнении
# DONALD + GERALD = ROBERT
letters = list("DONALDGERALDROBERT")
# Уберём дубликаты — всего 10 уникальных букв
letters = sorted(set(letters))
print("Уникальные буквы:", letters)

# Мы знаем, что D = 5 по условию
fixed = {'D': 5}

# Ведущие буквы (первые в словах): D, G, R — не могут быть нулём
leading_letters = {'D', 'G', 'R'}

# Определим оставшиеся буквы (те, для которых нужно подобрать цифры)
remaining_letters = [l for l in letters if l not in fixed]
print("Неизвестные буквы:", remaining_letters)

# Все возможные цифры 0–9, кроме уже занятых
digits = set(range(10)) - set(fixed.values())

# Вспомогательная функция для подстановки букв в число
def word_to_num(word, mapping):
    """Преобразует слово из букв в число, подставляя цифры согласно mapping."""
    return int("".join(str(mapping[ch]) for ch in word))

# Перебираем все возможные комбинации цифр для оставшихся букв
# Поскольку всего 10 букв, а D уже фиксировано, остаётся 9! = 362880 вариантов.
# Это всё ещё выполнимо для Python (занимает пару секунд).

for perm in itertools.permutations(digits, len(remaining_letters)):
    # permutations - все возможные комбинации из различных цифр без повторений.

    # Формируем словарь подстановки для данного варианта
    mapping = dict(zip(remaining_letters, perm))
    # Добавляем фиксированные значения
    mapping.update(fixed)

    # Проверим, что ведущие буквы не равны 0
    if any(mapping[l] == 0 for l in leading_letters):
        continue

    # Вычислим числовые значения слов
    DONALD = word_to_num("DONALD", mapping)
    GERALD = word_to_num("GERALD", mapping)
    ROBERT = word_to_num("ROBERT", mapping)

    # Проверим уравнение
    if DONALD + GERALD == ROBERT:
        print("✅ Найдено решение!")
        for k in sorted(mapping.keys()):
            print(f"{k} = {mapping[k]}")
        print(f"\nDONALD = {DONALD}")
        print(f"GERALD = {GERALD}")
        print(f"ROBERT = {ROBERT}")
        break
    else:
        print("❌ Решений не найдено.")