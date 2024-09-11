calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    result = {len(string), string.upper(), string.lower()}
    return result


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    for i in range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    key = string in list_to_search
    return key

print(string_info('Шоколадка'))
print(string_info('Трапеция'))
print(is_contains('Красный', ['ЖелтыЙ', 'ЗеЛеНыЙ', 'КраСныЙ']))
print(is_contains('Воробей', ['ЖелтыЙ', 'ЗеЛеНыЙ', 'КраСныЙ']))
print(calls)