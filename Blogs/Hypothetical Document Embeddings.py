from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

system_prompt = """
You are a helpful assistant who generate a detailed document with the help of user query
"""


client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.0-flash",
    n=1,
    messages=[
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": "What is Python?"
        }
    ]
)

print(response.choices[0].message.content)

'''Input -
What is Python?
Output-
Okay, here's a detailed document about Python, covering its key aspects, history, features, uses, and more.

**Python: A Comprehensive Overview**

**1. Introduction**

Python is a high-level, general-purpose programming language.  Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code compared to languages like C++ or Java.  Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (procedural), object-oriented, and functional programming.

**2. History and Development**

*   **Creator:** Guido van Rossum
*   **First Appeared:** 1991
*   **Development at:** Centrum Wiskunde & Informatica (CWI) in the Netherlands.
*   **Inspiration:**  Influenced by languages like ABC, Modula-3, Smalltalk, and Algol 68.
*   **Naming:** Named after the British comedy group Monty Python.
*   **Key Milestones:**
    *   **Python 2.0:** Introduced list comprehensions and a garbage collection system.
    *   **Python 3.0 (Python 3k):** A major, backward-incompatible release designed to rectify fundamental design flaws.  It emphasized Unicode support and removed redundant features.  Python 2.7 was the last release of the 2.x series.
    *   **Python 3.x:**  The actively maintained and developed version of Python.

**3. Key Features**

*   **Readability:** Python's syntax is designed to be clear and easy to understand, using indentation to define code blocks instead of brackets or keywords. This promotes code readability and maintainability.

*   **Easy to Learn:**  Python has a relatively simple syntax, making it easier for beginners to learn compared to other programming languages.   

*   **Interpreted:** Python is an interpreted language, meaning that code is executed line by line, rather than being compiled into machine code beforehand. This makes development faster and more flexible.  (Note:  Python code *is* compiled to bytecode, which is then executed by the Python Virtual Machine).

*   **Dynamically Typed:**  Variable types are checked at runtime, so you don't need to explicitly declare the type of a variable. This simplifies coding but can also lead to runtime errors if type mismatches occur.

*   **Automatic Memory Management:** Python uses automatic garbage collection to manage memory, freeing up memory that is no longer being used by the program. This reduces the risk of memory leaks.

*   **Large Standard Library:** Python comes with a vast standard library that provides modules and functions for a wide range of tasks, including:
    *   File I/O
    *   String manipulation
    *   Networking
    *   Web development
    *   Data compression
    *   Operating system interfaces

*   **Cross-Platform Compatibility:** Python code can be run on a variety of operating systems, including Windows, macOS, and Linux, without modification (in most cases).

*   **Extensible:** Python can be extended with modules written in other languages, such as C or C++, allowing you to leverage the performance of these languages for computationally intensive tasks.

*   **Embeddable:** Python can be embedded into other applications to provide scripting capabilities.

*   **Object-Oriented:** Python supports object-oriented programming (OOP) concepts such as classes, objects, inheritance, polymorphism, and encapsulation.

*   **Functional Programming:** Python also supports functional programming paradigms, allowing you to write code using functions as first-class citizens.

*   **Large Community and Ecosystem:**  Python has a large and active community that contributes to its development and provides support to users.  A vast ecosystem of third-party libraries and frameworks is available to extend Python's capabilities.

**4. Syntax and Basic Concepts**

*   **Indentation:**  Indentation is crucial in Python.  It defines the structure of code blocks. Consistent indentation is essential.

*   **Variables:** Variables are used to store data. You don't need to declare the type of a variable explicitly.

    ```python
    x = 10  # Integer
    name = "Alice" # String
    pi = 3.14 # Float
    ```

*   **Data Types:**  Common data types include:
    *   Integers (`int`)
    *   Floating-point numbers (`float`)
    *   Strings (`str`)
    *   Booleans (`bool`) - `True` or `False`
    *   Lists (`list`) - Ordered, mutable sequences of items.
    *   Tuples (`tuple`) - Ordered, immutable sequences of items.
    *   Dictionaries (`dict`) - Key-value pairs.
    *   Sets (`set`) - Unordered collections of unique items.

*   **Operators:** Python supports standard arithmetic, comparison, logical, and assignment operators.

*   **Control Flow:**
    *   `if`, `elif`, `else` statements for conditional execution.
    *   `for` loops for iterating over sequences.
    *   `while` loops for repeated execution based on a condition.

*   **Functions:**  Functions are blocks of reusable code.

    ```python
    def greet(name):
        print("Hello, " + name + "!")

    greet("Bob")  # Output: Hello, Bob!
    ```

*   **Classes and Objects:** Used for object-oriented programming.

    ```python
    class Dog:
        def __init__(self, name, breed):
            self.name = name
            self.breed = breed

        def bark(self):
            print("Woof!")

    my_dog = Dog("Buddy", "Golden Retriever")
    print(my_dog.name)  # Output: Buddy
    my_dog.bark()       # Output: Woof!
    ```

*   **Modules and Packages:** Modules are files containing Python code. Packages are collections of modules organized in a directory hierarchy.   

    ```python
    import math  # Import the math module

    print(math.sqrt(16))  # Output: 4.0
    ```

**5. Common Uses**

Python is used in a wide variety of applications, including:

*   **Web Development:** Frameworks like Django and Flask are popular for building web applications.

*   **Data Science and Machine Learning:**  Libraries like NumPy, Pandas, Scikit-learn, TensorFlow, and PyTorch are widely used for data analysis, machine learning, and artificial intelligence.

*   **Scripting and Automation:**  Python is used to automate tasks, write scripts for system administration, and perform batch processing.       

*   **Scientific Computing:**  Python is used in scientific research for simulations, data analysis, and visualization.

*   **Education:** Python is often used as an introductory programming language due to its ease of learning.

*   **Game Development:** Libraries like Pygame can be used for simple game development.

*   **Desktop GUI Applications:** Libraries like Tkinter, PyQt, and Kivy can be used to create desktop applications with graphical user interfaces.

*   **Network Programming:** Python is used for developing network applications and APIs.

*   **Cybersecurity:** Python is used for penetration testing, ethical hacking, and security automation.

**6. Popular Libraries and Frameworks**

*   **NumPy:**  For numerical computing with arrays and matrices.
*   **Pandas:**  For data analysis and manipulation.  Provides DataFrames.
*   **Scikit-learn:** For machine learning algorithms.
*   **TensorFlow:**  For deep learning.  Developed by Google.
*   **PyTorch:** For deep learning.  Developed by Facebook.
*   **Matplotlib:** For creating visualizations (plots, charts, graphs).
*   **Seaborn:**  A higher-level visualization library based on Matplotlib.
*   **Django:** A high-level web framework.
*   **Flask:**  A lightweight web framework.
*   **Requests:**  For making HTTP requests.
*   **Beautiful Soup:** For web scraping.
*   **SQLAlchemy:**  For interacting with databases.
*   **Tkinter:**  For creating GUI applications (built-in).
*   **PyQt:**  Another GUI framework.
*   **Kivy:**  A GUI framework for creating multi-touch applications.

**7. Python Versions (2.x vs. 3.x)**

*   **Python 2.x:**  The older version.  End of life was January 1, 2020. No longer supported.  Avoid using for new projects.
*   **Python 3.x:** The current and actively developed version.  Use Python 3.x for all new projects.  Key differences from 2.x include:
    *   Unicode support is built-in.
    *   `print` is a function (e.g., `print("Hello")`) instead of a statement.
    *   Integer division behaves differently (e.g., `5 / 2` results in `2.5` instead of `2`).
    *   `xrange()` is removed; use `range()` instead.
    *   Error handling is slightly different (using `as` keyword: `except Exception as e:`).

**8. Installing Python**

*   **Windows:** Download the installer from python.org and run it.  Make sure to check the box that adds Python to your PATH environment variable.
*   **macOS:**  macOS comes with a system Python installation, but it's generally recommended to install a newer version using a package manager like Homebrew.
*   **Linux:**  Most Linux distributions include Python. You can install it using your distribution's package manager (e.g., `apt-get install python3` on Ubuntu/Debian, `yum install python3` on CentOS/RHEL, `pacman -S python` on Arch Linux).

**9. Development Environments**

*   **IDEs (Integrated Development Environments):**
    *   **PyCharm:**  A popular and feature-rich IDE developed by JetBrains.
    *   **VS Code (Visual Studio Code):**  A lightweight and extensible code editor with excellent Python support (using the Python extension).   
    *   **Spyder:**  An IDE specifically designed for scientific computing.
    *   **Thonny:**  An IDE designed for beginners.

*   **Text Editors:**
    *   **Sublime Text:** A popular text editor with Python support.
    *   **Atom:**  An open-source text editor with Python support.

*   **Jupyter Notebook:**  A web-based interactive environment for creating and sharing documents that contain live code, equations, visualizations, and narrative text.  Commonly used in data science.

**10. Learning Resources**

*   **Official Python Documentation:**  [https://docs.python.org/3/](https://docs.python.org/3/)
*   **Online Courses:**
    *   Coursera
    *   edX
    *   Udemy
    *   Codecademy
*   **Books:**
    *   "Python Crash Course" by Eric Matthes
    *   "Automate the Boring Stuff with Python" by Al Sweigart
    *   "Fluent Python" by Luciano Ramalho
*   **Tutorials and Blogs:**
    *   Real Python
    *   Python Central
    *   The Python Tutorial

**11. Conclusion**

Python is a versatile and powerful programming language that is widely used in various domains. Its readability, ease of learning, and extensive ecosystem make it an excellent choice for both beginners and experienced programmers. Whether you're interested in web development, data science, scripting, or automation, Python has the tools and libraries you need to succeed.
'''