# AirBnB Clone Project
![logo](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240109%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240109T212434Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8534c28cb357d5a02020462ffe9b3d4fcc2764a74b33355bff27a1dd7f8bd8ba)
## Background Context

Welcome to the AirBnB clone project! Before starting, please read the [AirBnB concept page](#).

This project involves creating a command interpreter to manage AirBnB objects, a crucial step toward building a full web application. The skills developed in this project will be utilized in subsequent tasks such as HTML/CSS templating, database storage, API, and front-end integration.

### General
- How to create a Python package
- Creating a command interpreter in Python using the cmd module
- Understanding Unit testing and its implementation in a large project
- Serialization and deserialization of a class
- Reading and writing JSON files
- Managing datetime in Python
- UUID in Python
- Understanding and using args and kwargs
- Handling named arguments in a function

## Requirements
- Python Scripts allowed: vi, vim, emacs
- Ubuntu 20.04 LTS using Python3 (version 3.8.5)
- All files end with a new line
- First line of all files: `#!/usr/bin/python3`
- Mandatory README.md file at the project root
- Code should adhere to pycodestyle (version 2.8.)
- All files must be executable
- Length of files will be tested using `wc`
- Modules, classes, and functions must have documentation
- Python Unit Tests allowed: vi, vim, emacs
- All test files inside a folder named `tests`
- unittest module must be used for testing
- Tests executed using `python3 -m unittest discover tests`
- Collaboration encouraged for working on test cases
- One project repository per group on GitHub

## Execution

Your shell should work in interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
All tests should also pass in non-interactive mode: ```$ echo "python3 -m unittest discover tests" | bash```

