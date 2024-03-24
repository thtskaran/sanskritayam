import re
import sys

# Define the mapping of Python keywords and operators to Sanskrit words in English script
keyword_mapping = {
    'print': 'printayam',
    'input':'poocham',
    'if': 'yadi',
    'else': 'anyatha',
    'for': 'krte',
    'while': 'jabtak',
    'def': 'functionam',
    'return': 'returnam',
    'and': 'andam',
    'or': 'oram',
    'not': 'notam',
    'True': 'satyam',
    'False': 'asatyam',
    'None': 'nonum',
    'in': 'andaram',
    'is': 'hai',
    '=': 'saman',
    '+': 'plusam',
    '-': 'minusam',
    '*': 'gunanam',
    '/': 'bhagam',
    '//': 'poornabhagam',
    '%': 'modulam',
    '**': 'poweram',
    '<': 'kam',
    '>': 'jyada',
    '<=': 'kamsaman',
    '>=': 'jyadasaman',
    '==': 'samansaman',
    '!=': 'notsaman',
    'try': 'tryam',
    'except': 'expceptam',
    'finally': 'finalam',
    'raise': 'uthayam',
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

def execute_sanskritayam_code(code):
    python_code = sanskritayam_to_python(code)
    namespace = {}
    exec(python_code, namespace)
    if 'main' in namespace:
        namespace['main']()

def execute_sanskritayam_file(file_path):
    with open(file_path, 'r') as file:
        sanskritayam_code = file.read()
    execute_sanskritayam_code(sanskritayam_code)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python skm.py <file.skt>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    execute_sanskritayam_file(file_path)
