def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    i = ()
    i += len(string), string.upper(), string.lower()
    return i

def is_contains(string_, list_to_search):
    count_calls()
    a = True
    b = ' '.join(list_to_search).lower()
    if b.find(string_.lower()) == -1:
        a = False
    return a

calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)