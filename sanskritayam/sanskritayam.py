import re
import sys
import os

# Define the mapping of Python keywords and operators to Sanskrit words in English script
keyword_mapping = {
    'print': 'printayam',
    'input': 'pravesham',
    'if': 'yadi',
    'else': 'anyatha',
    'for': 'krte',
    'while': 'jabtak',
    'def': 'paribhasha',
    'return': 'pratyahar',
    'and': 'cha',
    'or': 'va',
    'not': 'na',
    'True': 'satyam',
    'False': 'asatyam',
    'None': 'kimapi_na',
    'in': 'antargatam',
    'is': 'asti',
    '=': 'samam',
    '+': 'yogah',
    '-': 'viyogah',
    '*': 'gunanam',
    '/': 'bhagaharah',
    '//': 'poornabhagaharah',
    '%': 'sheshah',
    '**': 'ghatah',
    '<': 'nyoonam',
    '>': 'adhikam',
    '<=': 'nyoonasamam',
    '>=': 'adhikasamam',
    '==': 'tulyam',
    '!=': 'atulyam',
    'try': 'prayatnah',
    'except': 'apavadah',
    'finally': 'antatah',
    'raise': 'utthapanam',
    'import': 'ayatah',
    'from': 'tah',
    'as': 'yatha',
    'with': 'saha',
    'assert': 'pratijna',
    'class': 'vargah',
    'del': 'vilopanam',
    'elif': 'athavayadi',
    'global': 'vaishvikam',
    'lambda': 'lambda',
    'pass': 'gachha',
    'yield': 'yield'
}

# Invert the keyword mapping to create a Sanskrit-to-Python mapping
sanskrit_to_python_mapping = {v: k for k, v in keyword_mapping.items()}

# Regular expression patterns
keyword_pattern = re.compile(r'\b(' + '|'.join(re.escape(keyword) for keyword in sanskrit_to_python_mapping.keys()) + r')\b')
method_pattern = re.compile(r'(\w+)\.(\w+)\(')
string_pattern = re.compile(r'(["\'])(?:(?=(\\?))\2.)*?\1')

def translate_keywords(code):
    return keyword_pattern.sub(lambda match: sanskrit_to_python_mapping[match.group()], code)

def translate_methods(code):
    return method_pattern.sub(lambda match: f'{match.group(1)}.{match.group(2)}(', code)

def preserve_strings(code):
    strings = []
    def replace(match):
        strings.append(match.group(0))
        return f'__STRING_{len(strings)-1}__'
    code = string_pattern.sub(replace, code)
    return code, strings

def restore_strings(code, strings):
    for i, s in enumerate(strings):
        code = code.replace(f'__STRING_{i}__', s)
    return code

def translate_function_calls(code):
    return re.sub(r'(\w+)\((.*?)\)', lambda match: f'{match.group(1)}({match.group(2)})', code)

def sanskritayam_to_python(code):
    code, strings = preserve_strings(code)
    code = translate_keywords(code)
    code = translate_methods(code)
    code = translate_function_calls(code)
    code = restore_strings(code, strings)
    return code

# def execute_sanskritayam_code(code):
#     python_code = sanskritayam_to_python(code)
#     namespace = {}
#     exec(python_code, namespace)
#     if 'main' in namespace:
#         namespace['main']()


# Added the swaha ability here -->

def execute_sanskritayam_code(code):
  lines = code.split('\n')
  for i, line in enumerate(lines):
    if line.strip().endswith('swaha'):
      lines[i] = line.strip()[:-5]  # Remove 'swaha' at the end
  modified_code = '\n'.join(lines)
  python_code = sanskritayam_to_python(modified_code)
  namespace = {}
  exec(python_code, namespace)
  if 'main' in namespace:
    namespace['main']()


def execute_sanskritayam_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    with open(file_path, 'r') as file:
        sanskritayam_code = file.read()
    execute_sanskritayam_code(sanskritayam_code)

def main():
    if len(sys.argv) != 2:
        print("Usage:python -m sanskritayam <file.skt>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        execute_sanskritayam_file(file_path)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    main()
