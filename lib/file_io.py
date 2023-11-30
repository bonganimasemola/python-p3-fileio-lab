
def write_file(file_name, file_content):
    with open(f'{file_name}.txt', 'w', encoding='utf-8') as f:
        f.write(file_content)

def append_file(file_name, append_content):
    with open(f'{file_name}.txt', 'a', encoding='utf-8') as f:
        f.write(append_content)

def read_file(file_name):
    with open(f'{file_name}.txt', 'r', encoding='utf-8') as f:
        return f.read()
