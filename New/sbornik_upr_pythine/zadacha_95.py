text = "привет.пока"
result = text[0].upper() + text[1:]  # Делаем первую букву заглавной
final = ""
i = 0
while i < len(result):
    if result[i] == '.':
        # Добавляем точку и следующую букву заглавной
        final += result[i] + result[i+1].upper()
        i += 2  # Переходим через обработанные символы
    else:
        final += result[i]
        i += 1
        
print(final)  # Выведет: Привет.Пока