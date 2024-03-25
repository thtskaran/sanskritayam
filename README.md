
# Sanskritayam Programming Language

Sanskritayam is a fun and experimental programming language inspired by Sanskrit, the ancient language of India. This project was created based on a viral meme from last year, where a group of aunties were discussing the idea of making Sanskrit a coding language. As a joke, my friend [Pinakkk](https://github.com/pinakkk) and I thought of turning this idea into reality, and thus, Sanskritayam was born!

![Sanskritayam Programming Language](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhlAeRIG9cCOOVfbhmSn09xLNnJ_8gwoAoaj6D73czsYaWokpnayLG5CJu6UBQFrgun1DBPlRw4Gyl2aEU5_33ZBj9XlxFVk9pmoqiJeuTTSmsxG3UKFW184ZzXYSGOY4Ra4GkGHjtY6M1yRsgRz0ZNXrS57c32EFXTQSYwHSNMktzZSi3a_m0Mflw4Gec/s1173/A%20Banner%20image%20for%20a%20programming%20language%20based%20on%20sanskrit%20,%20ancient%20scriptures%20,%20programming%20icons%20and%20references%20,%20vedic%20culture%20.png)

Please note that Sanskritayam is not intended for serious production use and comes with no warranty. It's a purely recreational project meant for learning and entertainment purposes.

## Features

- Sanskrit-inspired syntax and keywords
- Basic programming constructs like variables, conditionals, loops, and functions
- Support for common data types such as integers, floats, strings, lists, and dictionaries
- File I/O operations
- Exception handling
- Object-oriented programming concepts

## Getting Started

To get started with Sanskritayam, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/thtskaran/sanskritayam.git
   ```
2. Install Python 3.x if you haven't already.

3. Navigate to the directory containing the setup.py file:
    ```
    cd sanskritayam

4. Install the Sanskritayam interpreter:
   ```
   pip install -e .


5. Run the Sanskritayam interpreter:
    ```
    python -m skm <filename.skt>

Replace `<filename.skt>` with the path to your Sanskritayam source file.

## Updating Sanskritayam

If you've updated the Sanskritayam interpreter on GitHub and want to update your local installation, follow these steps:

1. Pull the latest changes from GitHub:
    ```
    git pull origin main

Replace `main` with the name of the branch that contains the updated Sanskritayam interpreter, if it's not the main branch.

2. Reinstall the Sanskritayam interpreter:
    ```
    pip install --upgrade --force-reinstall -e .

Now, your local installation of the Sanskritayam interpreter should be updated with the latest changes from GitHub.


Replace `<filename.skt>` with the path to your Sanskritayam source file.

## Documentation

Sanskritayam has a simple and intuitive syntax inspired by Sanskrit words and concepts. Here's an overview of the language's syntax and usage:

### Variables and Data Types

To declare a variable in Sanskritayam, you can use the following syntax:

```
<variable_name> = <value>
```

For example:

```
ganakah = 42
```

Sanskritayam supports various data types, including:

- Integers (`ganakah`)
- Floats (`chhedakah`)
- Strings (`aksharankhyata`)
- Lists (`samhata`)
- Dictionaries (`nirukti`)

### Control Flow

Sanskritayam includes control flow statements like conditional statements and loops:

#### Conditional Statements

```
yadi <condition>:
    # code block
anyatha:
    # code block
```

You can also use the `athavayadi` statement for else-if conditions.

#### Loops

For loops:

```
krte <variable> antargatam <iterable>:
    # code block
```

While loops:

```
jabtak <condition>:
    # code block
```

### Functions

To define a function in Sanskritayam, use the `paribhasha` keyword:

```
paribhasha <function_name>(<arguments>):
    # function body
    pratyahar <return_value>
```

To call a function, simply use its name followed by parentheses with the arguments:

```
<function_name>(<arguments>)
```

### File I/O

Sanskritayam allows you to read from and write to files using the following functions:

```
ayatah "<file_path>", "r" yatha patham:
    # read from the file
```

```
ayatah "<file_path>", "w" yatha lekhyam:
    # write to the file
```

### Exception Handling

Sanskritayam provides exception handling capabilities using the `prayatnah`, `apavadah`, and `antatah` keywords:

```
prayatnah:
    # code that might raise an exception
apavadah <exception_type>:
    # exception handling code
antatah:
    # code that will always execute
```

### Object-Oriented Programming

Sanskritayam supports object-oriented programming concepts like classes and objects:

```
vargah <class_name>:
    # class body

# Creating an instance of the class
samskritayam = <class_name>()
```


To learn how to write code in Sanskritayam, check out the [usage guide](docs/docs.md).

## Examples

You can find various example programs written in Sanskritayam in the [examples](examples/) directory. These examples demonstrate different aspects of the language and serve as a starting point for learning Sanskritayam.

## Testing

To ensure the correctness and reliability of the Sanskritayam language, a comprehensive test suite is available in the [tests](tests/) directory. The test suite covers various language features and helps maintain the integrity of the language implementation.

To run the tests, execute the following command:
   `python -m skm tests/sanskritayam_comprehensive_test.skt`

## License

The Sanskritayam programming language is released under the [Apache License 2.0]([LICENSE](https://www.apache.org/licenses/LICENSE-2.0)). Feel free to use, modify, and distribute the language according to the terms of the license.

## Disclaimer

Sanskritayam is a joke programming language created for fun and learning purposes. It is not recommended for use in production environments, and no warranty or support is provided. Use it at your own risk!

If anyone feels offended or uncomfortable with the concept or any aspect of this project, we sincerely apologize. Our intention is not to mock or disrespect any language, culture, political party, or religion. It's purely a lighthearted attempt to explore the idea of creating a programming language based on Sanskrit.

## Acknowledgements

We would like to acknowledge the creators of the viral meme that inspired this project. Their humorous discussion sparked the idea of creating Sanskritayam, and we are grateful for the laughter and inspiration they provided.

Special thanks to [Pinakkk](https://github.com/pinakkk) for his invaluable contributions and collaboration in bringing Sanskritayam to life. His creativity, technical expertise, and sense of humor have been instrumental in shaping this project.

## Contributing

As Sanskritayam is a fun and experimental project, we welcome contributions from the community. If you have any ideas, suggestions, or improvements, feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/thtskaran/sanskritayam).

Let's have fun coding in Sanskritayam and embrace the quirks and joys of this unique language!
