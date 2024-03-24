
# Sanskritayam Language Documentation

This document provides a detailed overview of the Sanskritayam programming language, including its syntax, keywords, and features.

## Syntax Mapping

The following table maps Python syntax to the corresponding Sanskritayam syntax:

| Python | Sanskritayam |
| --- | --- |
| `print` | `printayam` |
| `if` | `yadi` |
| `else` | `anyatha` |
| `for` | `krte` |
| `while` | `jabtak` |
| `def` | `functionam` |
| `return` | `returnam` |
| `and` | `andam` |
| `or` | `oram` |
| `not` | `notam` |
| `True` | `satyam` |
| `False` | `asatyam` |
| `None` | `nonum` |
| `in` | `andaram` |
| `is` | `hai` |
| `=` | `samam` |
| `+` | `plusam` |
| `-` | `minusam` |
| `*` | `gunanam` |
| `/` | `bhagam` |
| `//` | `poornabhagam` |
| `%` | `modulam` |
| `**` | `poweram` |
| `<` | `kam` |
| `>` | `jyada` |
| `<=` | `kamsaman` |
| `>=` | `jyadasaman` |
| `==` | `'samansaman` |
| `!=` | `notsaman` |
| `try` | `tryam` |
| `except` | `exceptam` |
| `finally` | `finalam` |
| `raise` | `uthayam` |
| `import` | `ayatah` |
| `from` | `tah` |
| `as` | `yatha` |
| `with` | `saha` |
| `assert` | `pratijna` |
| `class` | `vargah` |
| `del` | `vilopanam` |
| `elif` | `athavayadi` |
| `global` | `vaishvikam` |
| `lambda` | `lambda` |
| `pass` | `gachha` |
| `yield` | `yield` |

## Variables and Data Types

In Sanskritayam, variables are declared using the `=` operator, which is represented as `samam`. The following data types are supported:

- Integers (`ganakah`): Whole numbers, e.g., `10`, `-5`.
- Floats (`chhedakah`): Decimal numbers, e.g., `3.14`, `-2.7`.
- Strings (`aksharankhyata`): Sequences of characters enclosed in single or double quotes, e.g., `'hello'`, `"world"`.
- Lists (`samhata`): Ordered collections of items, e.g., `[1, 2, 3]`, `['apple', 'banana', 'cherry']`.
- Dictionaries (`nirukti`): Unordered collections of key-value pairs, e.g., `{'name': 'John', 'age': 30}`.

Example:

```
ganakah = 42
chhedakah = 3.14
aksharankhyata = "sanskritayam"
samhata = [1, 2, 3, 4, 5]
nirukti = {'key1': 'value1', 'key2': 'value2'}
```

## Control Flow

Sanskritayam supports control flow statements like conditional statements and loops.

### Conditional Statements

Conditional statements in Sanskritayam use the `yadi` (if), `anyatha` (else), and `athavayadi` (elif) keywords.

Example:

```
ganakah = 10

yadi ganakah > 0:
    mudrit("ganakah asti dhanak")
anyatha:
    mudrit("ganakah asti rnnak")
```

### Loops

Sanskritayam provides two types of loops: `krte` (for) and `yavat` (while).

#### For Loops

The `krte` loop is used to iterate over a sequence (e.g., a list or a string).

Example:

```
aksharankhyata = "sanskritayam"

krte varna antargatam aksharankhyata:
    mudrit(varna)
```

#### While Loops

The `yavat` loop is used to repeatedly execute a block of code as long as a given condition is true.

Example:

```
ganakah = 0

yavat ganakah < 5:
    mudrit(ganakah)
    ganakah = ganakah + 1
```

## Functions

Functions in Sanskritayam are defined using the `paribhasha` keyword, and arguments are passed within parentheses. The `pratyahar` keyword is used to return a value from the function.

Example:

```
paribhasha yogah(x, y):
    ganakah = x + y
    pratyahar ganakah

mudrit(yogah(3, 4))  # Output: 7
```

## File I/O

Sanskritayam supports reading from and writing to files using the `ayatah` (import) keyword and the `yatha` (as) keyword.

### Reading from a File

Example:

```
ayatah "file.txt", "r" yatha patham:
    samgraham = patham.read()
    mudrit(samgraham)
```

### Writing to a File

Example:

```
ayatah "file.txt", "w" yatha lekhyam:
    lekhyam.write("This is some text.")
```

## Exception Handling

Sanskritayam provides exception handling capabilities using the `prayatnah` (try), `apavadah` (except), and `antatah` (finally) keywords.

Example:

```
prayatnah:
    ganakah = 10 / 0
apavadah ZeroDivisionError:
    mudrit("Zero dvaara vibhajanam akarmyam")
antatah:
    mudrit("Exception handling samaptam")
```

## Object-Oriented Programming

Sanskritayam supports object-oriented programming concepts like classes and objects using the `vargah` (class) keyword.

Example:

```
vargah Vyakti:
    paribhasha __init__(svayam, nama, vayah):
        svayam.nama = nama
        svayam.vayah = vayah

    paribhasha paricchedam(svayam):
        mudrit(f"Nama: {svayam.nama}, Vayah: {svayam.vayah}")

vyakti = Vyakti("John", 30)
vyakti.paricchedam()  # Output: Nama: John, Vayah: 30
```
