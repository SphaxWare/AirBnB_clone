# AirBnB Clone Project

## Description

Welcome to the AirBnB clone project!

This project involves creating a command interpreter to manage AirBnB objects.
## How to start it
```
root@a8016d6e0d0f:/AirBnB_clone# ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) help quit
Quit command to exit the program

(hbnb) quit
```
## How to use it
# Create
Usage: create class
```
(hbnb) create User
1f715f7d-29b4-4116-a79e-470bd99ce061
```
# Show
Usage: show class class_id
or
class.show(class_id)
```
(hbnb) show User 1f715f7d-29b4-4116-a79e-470bd99ce061
[User] (1f715f7d-29b4-4116-a79e-470bd99ce061) {'id': '1f715f7d-29b4-4116-a79e-470bd99ce061', 'created_at': datetime.datetime(2024, 1, 14, 15, 23, 46, 687299), 'updated_at': datetime.datetime(2024, 1, 14, 15, 23, 46, 687313)}
```
# Destroy
Usage: destroy class class_id
or
class.destroy(class_id)
```
(hbnb) User.all()
["[User] (9eb841c1-5e1f-4fb1-84e5-03a666a52a6e) {'id': '9eb841c1-5e1f-4fb1-84e5-03a666a52a6e', 'created_at': datetime.datetime(2024, 1, 14, 15, 24, 29, 586757), 'updated_at': datetime.datetime(2024, 1, 14, 15, 24, 29, 586774)}", "[User] (03cd71f2-75ce-4e01-a8a4-bef75aec72bc) {'id': '03cd71f2-75ce-4e01-a8a4-bef75aec72bc', 'created_at': datetime.datetime(2024, 1, 14, 15, 24, 30, 371951), 'updated_at': datetime.datetime(2024, 1, 14, 15, 24, 30, 371963)}"]
(hbnb) User.count()
2
(hbnb) destroy User 9eb841c1-5e1f-4fb1-84e5-03a666a52a6e
(hbnb) User.count()
1
(hbnb)
```
# All
Usage: all class
or
class.all()
```
(hbnb) all User
["[User] (03cd71f2-75ce-4e01-a8a4-bef75aec72bc) {'id': '03cd71f2-75ce-4e01-a8a4-bef75aec72bc', 'created_at': datetime.datetime(2024, 1, 14, 15, 24, 30, 371951), 'updated_at': datetime.datetime(2024, 1, 14, 15, 24, 30, 371963)}"]
(hbnb) User.all()
["[User] (03cd71f2-75ce-4e01-a8a4-bef75aec72bc) {'id': '03cd71f2-75ce-4e01-a8a4-bef75aec72bc', 'created_at': datetime.datetime(2024, 1, 14, 15, 24, 30, 371951), 'updated_at': datetime.datetime(2024, 1, 14, 15, 24, 30, 371963)}"]
(hbnb)
```
# Update
Usage: update class class_id attribute attribute_value
or
class.update("class_id", "attribute", attribute_value)
```
(hbnb) User.all()
["[User] (03cd71f2-75ce-4e01-a8a4-bef75aec72bc) {'id': '03cd71f2-75ce-4e01-a8a4-bef75aec72bc', 'created_at': datetime.datetime(2024, 1, 14, 15, 24, 30, 371951), 'updated_at': datetime.datetime(2024, 1, 14, 15, 24, 30, 371963)}"]
(hbnb) update User 03cd71f2-75ce-4e01-a8a4-bef75aec72bc AGE 69
(hbnb) User.all()
["[User] (03cd71f2-75ce-4e01-a8a4-bef75aec72bc) {'id': '03cd71f2-75ce-4e01-a8a4-bef75aec72bc', 'created_at': datetime.datetime(2024, 1, 14, 15, 24, 30, 371951), 'updated_at': datetime.datetime(2024, 1, 14, 15, 24, 30, 371963), 'AGE': '69'}"]
```
# Count
Usage: count class
or
class.count()
```
root@a8016d6e0d0f:/AirBnB_clone# ./console.py
(hbnb) User.count()
1
(hbnb) create User
fa601bed-c461-4c71-84d6-62cf9ee2ee5e
(hbnb) create User
a4803d3f-4e97-4e9c-9bb8-02a49d41f104
(hbnb) create User
9efad4eb-217a-4e38-8924-c7074439f173
(hbnb) create User
dfbfab7a-a832-468d-bdae-03e76dd7692c
(hbnb) create User
a6682a4b-87ba-4b72-aabc-09887e348128
(hbnb) create User
6f73ed69-bb64-430c-87f4-c62e43ab387b
(hbnb) create User
d8bd41fa-285f-4c09-a991-ff4823309d85
(hbnb) count User
8
(hbnb)

```
## Examples
```
root@a8016d6e0d0f:/AirBnB_clone# ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) help quit
Quit command to exit the program

(hbnb) create User
1f715f7d-29b4-4116-a79e-470bd99ce061
(hbnb) show User 1f715f7d-29b4-4116-a79e-470bd99ce061
[User] (1f715f7d-29b4-4116-a79e-470bd99ce061) {'id': '1f715f7d-29b4-4116-a79e-470bd99ce061', 'created_at': datetime.datetime(2024, 1, 14, 15, 23, 46, 687299), 'updated_at': datetime.datetime(2024, 1, 14, 15, 23, 46, 687313)}
(hbnb) count User
1
(hbnb) create User
9eb841c1-5e1f-4fb1-84e5-03a666a52a6e
(hbnb) create User
03cd71f2-75ce-4e01-a8a4-bef75aec72bc
(hbnb) User.count()
3
(hbnb) User.all()
["[User] (1f715f7d-29b4-4116-a79e-470bd99ce061) {'id': '1f715f7d-29b4-4116-a79e-470bd99ce061', 'created_at': datetime.datetime(2024, 1, 14, 15, 23, 46, 687299), 'updated_at': datetime.datetime(2024, 1, 14, 15, 23, 46, 687313)}", "[User] (9eb841c1-5e1f-4fb1-84e5-03a666a52a6e) {'id': '9eb841c1-5e1f-4fb1-84e5-03a666a52a6e', 'created_at': datetime.datetime(2024, 1, 14, 15, 24, 29, 586757), 'updated_at': datetime.datetime(2024, 1, 14, 15, 24, 29, 586774)}", "[User] (03cd71f2-75ce-4e01-a8a4-bef75aec72bc) {'id': '03cd71f2-75ce-4e01-a8a4-bef75aec72bc', 'created_at': datetime.datetime(2024, 1, 14, 15, 24, 30, 371951), 'updated_at': datetime.datetime(2024, 1, 14, 15, 24, 30, 371963)}"]
(hbnb)
(hbnb)
(hbnb) quit
root@a8016d6e0d0f:/AirBnB_clone#
```
## Execution

shell should work in interactive mode:

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

