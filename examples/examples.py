import os
from os import path

def get_py(current_dir):
    all_path = []
    for file_or_dir in os.listdir(current_dir):
        path_ = path.join(current_dir, file_or_dir)
        if path.isfile(path_):
            if path_.endswith('.py'):
                all_path.append(path_)
        else:
            all_path.extend(get_py(path_))
    return all_path

if __name__ == '__main__':
    current_path = path.dirname(__file__)
    all_py_path = []
    for file_or_dir in os.listdir(current_path):
        path_ = path.join(current_path, file_or_dir)
        if path.isdir(path_):
            all_py_path.extend(get_py(path_))
    
    for py in all_py_path:
        
        print(f'\nPython file: {py}')
        os.system(f'python {py}')
        print('.' * 110)
        