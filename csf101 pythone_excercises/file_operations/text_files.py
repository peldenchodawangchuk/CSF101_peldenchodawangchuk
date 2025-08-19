def create_and_write_file(test):
    with open(test, 'w') as file:
        file.write('this is the first line./n')
        file.write('this is the second line./n')
        file.write('this is the third line./n')

create_and_write_file('text.txt')
print('file created and written successfully')

def read_and_print_file(test):
    with open(test, 'r') as file:
        content = file.read()
        print(content)
read_and_print_file('text.txt')

def append_to_file(test, new_line):
    with open(test, 'a') as file:
        file.write(new_line + '/n')
append_to_file('text.txt', 'this is and appended line')
print('line appended successfully')
read_and_print_file('text.txt')

def print_lines_with_numbers(test):
    with open(test, 'r') as file:
        for index, line in enumerate(file, start=1):
            print(f'{index}: {line.strip()}')
print_lines_with_numbers('text.txt')

def count_words(test):
    with open(test, 'r') as file:
        content = file.read()
        words = content.split()
        return len(words)
word_count = count_words('text.txt')
print(f'the file contains {word_count} words')