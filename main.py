from re import sub, split
from pathlib import Path
import sys

characters_on_line = 84

choice = ''

while choice not in ['y', 'n']:
    choice = input(sub(r' +', ' ', '''
                This script will iterate all .txt files in current directory
                and will wrap the text to a new line at the earliest opportunity
                after the 84th character then the original file will be kept
                untouched and will be created a result file with name original_file_result.txt.
                Please press "y" to agree or "n" to decline.
                '''.strip()).strip())

if choice == 'n':
    sys.exit(0)


def read_file_and_prepare_content(input_file_path: str, input_characters_on_line: int) -> str:
    with open(input_file_path, 'r') as input_file:
        file_content_on_one_line = ' '.join(split(r'\s+', input_file.read()))
        result_data = sub(r'(.{%d}\S+)\s' % input_characters_on_line, r'\1\n', file_content_on_one_line)
        return result_data


def write_data_to_file(input_file_path: str, input_data: str):
    with open(input_file_path, 'a') as output_file:
        output_file.write(input_data)


p = Path('.')

text_files = [sub(r'\.txt$', '', x.name) for x in p.iterdir() if x.is_file() and x.name.endswith('.txt')]

for file in text_files:
    prepared_data = read_file_and_prepare_content(f'{file}.txt', characters_on_line)
    write_data_to_file(f'{file}_result.txt', prepared_data)

print(f'All done! {len(text_files)} files were processed.')
