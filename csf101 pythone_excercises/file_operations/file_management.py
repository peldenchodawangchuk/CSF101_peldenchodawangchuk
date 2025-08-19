# import os

# def file_exists(test):
#     return os.path.exists(test)
# print(f"'text.txt' exists: {file_exists('text.txt')}")
# print(f"'nonexistent.txt' exists: {file_exists('nonexxistent.txt')}")

# import os
# def rename_file(test, retest):
#     os.rename(test, retest)
#     lrename_file('text.txt', 'retext.txt')
# print('file renamed successfully')
# print(f"'retext.txt' exists: {file_exists('retext.txt')}")

# import os
# def delete_file(retest):
#     if os.path.exists(retest):
#         os.remove(retest)
#         print(f'{retest} has been deleted')
#     else:
#         print(f'{retest} doesnt exist')
# delete_file('binary_sample.bin')

# import os
# def create_directory(eminem):
#     if not os.path.exists(eminem):
#         os.makedirs(eminem)
#         print(f"directory '{eminem}' created successfully.")
#     else:
#         print(f"directory '{eminem}' already exists")

# create_directory('new_folder')

# import os
# def list_files(eminem):
#     files = os.listdir(eminem)
#     for file in files:
#         print(file)

# print('files in the current directory:')
# list_files('.')

import shutil

def copy_file(source, destination):
    shutil.copy2(source, destination)
    print(f"file copied from {source} to {destination}")
copy_file('retext.txt', 'new_folder/copied_text.txt')
