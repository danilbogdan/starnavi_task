# Treasure finder

## 1. Usage
### 1.1 Setup virtual environment using pipenv
```
$: pipenv update
Running $ pipenv lock then $ pipenv sync.
Locking [dev-packages] dependencies...
Locking [packages] dependencies...
✔ Success! 
Updated Pipfile.lock (201504)!
Installing dependencies from Pipfile.lock (201504)...
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 11/11 — 00:00:02

```
### 1.2 Run app
```bash
$: python app.py -h

usage: app.py [-h] [-f FILE] [-r]

Treasure hunter app

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  read input from file
  -r, --recursive       Weather to apply recursive implementation or not
```
Application has two implementations: functional and object-oriented.
Argument `-r` applies functional approach.  
Without `-r` the object-oriented implementation will be used.  
There are two ways of map input: through stdin or via file. Use `-f` to specify path to map file. 

## 2. Map format
Input example
```
55 14 25 52 21
44 31 11 53 43
24 13 45 12 34
42 22 43 32 41
51 23 33 54 15
```

Output example

```
11 55 15 21 44 32 13 25 43
```


## 3. Tests

```bash
$: python -m pytest                                                                                                                                      ✔  3067  14:38:05
================================ test session starts =================================
platform linux -- Python 3.6.8, pytest-5.3.2, py-1.8.1, pluggy-0.13.1
rootdir: /home/danilyuk/Projects/testtask
collected 32 items                                                                                                                                                                                                                     

tests/test_functional.py ........                                                                                                                                                                                                [ 25%]
tests/test_oop.py ........................                                                                                                                                                                                       [100%]

================================= 32 passed in 0.06s =================================
```