# TODO  Напишите функцию count_letters
def count_letters(text):
    new_low_text = text.lower()
    dictionary = {}
    for symbol in new_low_text:
        if (symbol not in dictionary) and (symbol.isalpha()):
            count_symbol = new_low_text.count(symbol)
            dictionary[symbol] = count_symbol
    return dictionary
# TODO Напишите функцию calculate_frequency


def calculate_frequency(dictionary_symbol):
    total = sum(dictionary_symbol.values())
    for key in dictionary_symbol:
        dictionary_symbol[key] = round(dictionary_symbol[key]/total, 2)
    return dictionary_symbol


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""


# TODO Распечатайте в столбик букву и её частоту в тексте
dictionary_filtered = count_letters(main_str)
result = calculate_frequency(dictionary_filtered)
for keys in result:
    print(f'{keys}: {result[keys]:.2f}')
