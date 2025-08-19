def create_binary_file(test):
    data = bytes([0, 1, 2, 3, 4, 5])
    with open(test, 'wb') as file:
        file.write(data)
create_binary_file('binary_sample.bin')
print('binary files created successfully')
def read_binary_file(test):
  with open(test, 'rb') as file:
    content = file.read
    print('binary content:', content)
read_binary_file('binary_sample.bin')
def append_to_binary_file(test, data):
    with open(test, 'ab') as file:
        file.write(data)
append_to_binary_file('binary_sample.bin', bytes([6, 7, 8, 9]))
print('bytes appended to binary file')
read_binary_file('binary_sample.bin')