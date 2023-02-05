# alu-AirBnB_clone

This is the project which is going to be run the entire website be it front-end and back-end parts, plus the unittest at large.

# Layout or tree structure of directories and files in HBnB Clone:
```
├── AUTHORS
├── console.py
├── models
│   ├── amenity.py
│   ├── base_model.py
│   ├── city.py
│   ├── engine
│   │   ├── file_storage.py
│   │   ├── __init__.py       
│   ├── __init__.py
│   ├── place.py
│   ├── review.py
│   ├── state.py
│   └── user.py
├── README.md
└── tests
    ├── test_console.py
    ├── test_models
        ├── test_amenity.py
        ├── test_base_model.py
        ├── test_city.py
        ├── test_engine
        │   ├── test_file_storage.py
        │   └── __init__.py
        ├──__init__.py
        ├── test_place.py
        ├── test_review.py
        ├── test_state.py
        └── test_user.py
```
# Description of the Command Interpreter

Command interpreter allows the user to interact with a program using commands to manage the objects of our project, including:
* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc...)
* Do operations on objects (count, compute stats, etc...)
* Update attributes of an object
* Destroy an object

# How to start the Command Interpreter

To start the interpreter we run
```
./console.py
```
# How to use it

| Command and Action  | Example of how it is used |
| ------------- | ------------- |
| run--Run the console  |``` ./console.py ``` |
| quit--Quit the console  |``` (hbnb) quit ``` |
| help--Display the help for a command  |``` (hbnb) help <command> ``` |
| create--Create an object or instance of a given class  |``` (hbnb) create <class> ``` |
| all--Show all objects or instances of a given class  |``` (hbnb) all <class> or (hbnb) all ``` |
| show--Show an object or instance of a given class  |``` (hbnb) show <class> <id> or (hbnb) <class>.show(<id>) ``` |
| destroy--Destroy an object or instance of a given class  |``` (hbnb) destroy <class> <id> or (hbnb) <class>.destroy(<id>)```  |
| update--Update an attribute of an object  | ```(hbnb) update <class> <id> <attribute name> "<attribute value>" or (hbnb) <class>.update(<id>, <attribute name>, "<attribute value>") ``` |
# Tests
All the code is tested with the unittest module. The test for the classes are in the test_models folder.
# Authors
* Marcel Sibomana
* Joshua Bizima
 
