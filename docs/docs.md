# Sanskritayam Language Documentation

This document provides a detailed overview of the Sanskritayam programming language, including its syntax, keywords, and features.

## Syntax Mapping

The following table maps Python syntax to the corresponding Sanskritayam syntax:

- The swaha ability is an unique ability, and you can try writing swaha after writing printayam or when calling a function.
Note:
- You should not use swaha inside any functions or in if(yadi) and else(anyatha) conditions.
| Python | Sanskritayam |
| --- | --- |
| swaha ability | swaha |
| print | printayam swaha|
| input | pravesham |
| if | yadi |
| else | anyatha |
| for | krte |
| while | jabtak |
| def | paribhasha |
| return | pratyahar |
| and | cha |
| or | va |
| not | na |
| True | satyam |
| False | asatyam |
| None | kimapi_na |
| in | antargatam |
| is | asti |
| = | samam |
| + | yogah |
| - | viyogah |
| * | gunanam |
| / | bhagaharah |
| // | poornabhagaharah |
| % | sheshah |
| ** | ghatah |
| < | nyoonam |
| > | adhikam |
| <= | nyoonasamam |
| >= | adhikasamam |
| == | tulyam |
| != | atulyam |
| try | prayatnah |
| except | apavadah |
| finally | antatah |
| raise | utthapanam |
| import | ayatah |
| from | tah |
| as | yatha |
| with | saha |
| assert | pratijna |
| class | vargah |
| del | vilopanam |
| elif | athavayadi |
| global | vaishvikam |
| lambda | lambda |
| pass | gachha |
| yield | yield |

## Variables and Data Types

In Sanskritayam, variables are declared using the = operator, which is represented as samam. The following data types are supported:

- Integers (ganakah): Whole numbers, e.g., 10, -5.
- Floats (chhedakah): Decimal numbers, e.g., 3.14, -2.7.
- Strings (aksharankhyata): Sequences of characters enclosed in single or double quotes, e.g., 'hello', "world".
- Lists (samhata): Ordered collections of items, e.g., [1, 2, 3], ['apple', 'banana', 'cherry'].
- Dictionaries (nirukti): Unordered collections of key-value pairs, e.g., {'name': 'John', 'age': 30}.

Example:


ganakah = 42
chhedakah = 3.14
aksharankhyata = "sanskritayam"
samhata = [1, 2, 3, 4, 5]
nirukti = {'key1': 'value1', 'key2': 'value2'}


## Control Flow

Sanskritayam supports control flow statements like conditional statements and loops.

### Conditional Statements

Conditional statements in Sanskritayam use the yadi (if), anyatha (else), and athavayadi (elif) keywords.

Example:


ganakah = 10

yadi ganakah > 0:
    printayam("ganakah asti dhanak")
anyatha:
    printayam("ganakah asti rnnak")


### Loops

Sanskritayam provides two types of loops: krte (for) and jabtak (while).

#### For Loops

The krte loop is used to iterate over a sequence (e.g., a list or a string).

Example:


aksharankhyata = "sanskritayam"

krte varna antargatam aksharankhyata:
    printayam(varna)


#### While Loops

The jabtak loop is used to repeatedly execute a block of code as long as a given condition is true.

Example:


ganakah = 0

jabtak ganakah < 5:
    printayam(ganakah)
    ganakah = ganakah + 1


## Functions

Functions in Sanskritayam are defined using the paribhasha keyword, and arguments are passed within parentheses. The pratyahar keyword is used to return a value from the function.

Example:


paribhasha yogah(x, y):
    ganakah = x + y
    pratyahar ganakah

printayam(yogah(3, 4))  # Output: 7


## File I/O

Sanskritayam supports reading from and writing to files using the ayatah (import) keyword and the yatha (as) keyword.

### Reading from a File

Example:


ayatah "file.txt", "r" yatha patham:
    samgraham = patham.read()
    printayam(samgraham)


### Writing to a File

Example:


ayatah "file.txt", "w" yatha lekhyam:
    lekhyam.write("This is some text.")


## Exception Handling

Sanskritayam provides exception handling capabilities using the prayatnah (try), apavadah (except), and antatah (finally) keywords.

Example:


prayatnah:
    ganakah = 10 / 0
apavadah ZeroDivisionError:
    printayam("Zero dvaara vibhajanam akarmyam")
antatah:
    printayam("Exception handling samaptam")


## Object-Oriented Programming

Sanskritayam supports object-oriented programming concepts like classes and objects using the vargah (class) keyword.

Example:


vargah Vyakti:
    paribhasha __init__(svayam, nama, vayah):
        svayam.nama = nama
        svayam.vayah = vayah

    paribhasha paricchedam(svayam):
        printayam(f"Nama: {svayam.nama}, Vayah: {svayam.vayah}")

vyakti = Vyakti("John", 30)
vyakti.paricchedam()  # Output: Nama: John, Vayah: 30
