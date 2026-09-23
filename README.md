# 🧑‍💻 Interactive Personal Data Collector

A simple Python program that collects basic personal information from the user and displays the entered data along with its **data type** and **memory address**.

It also calculates an **approximate birth year** based on the user's age.

## 🚀 Features

* 👤 Collects the user's name
* 🎂 Collects the user's age
* 📏 Collects height in meters
* 🔢 Collects a favorite number
* 🧩 Displays the Python data type of each value
* 💾 Displays the memory address using `id()`
* 📅 Calculates an approximate birth year
* 👋 Displays a goodbye message

## 🛠️ Technologies Used

* **Python 3**
* `input()` for user input
* `int()` for integer conversion
* `float()` for decimal numbers
* `type()` to identify data types
* `id()` to display an object's identity/address
* `datetime` to get the current year

## 📋 How It Works

The program first welcomes the user:

```python
print("welcome to the interactive personal data collector!")
```

It then asks the user for four pieces of information:

```python
name = input("enter your name")
age = int(input("enter your age"))
height = float(input("enter your height in meters"))
favnum = int(input("enter your fav num"))
```

The program displays each value along with its type and object identity:

```python
print("name", name, "(type is:)", type(name), "memory address;", id(name), ")")
```

Finally, it gets the current year using Python's `datetime` module and calculates an approximate birth year:

```python
current_year = datetime.datetime.now().year
birth_year = current_year - age
```

## ▶️ How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check your Python version:

```bash
python --version
```

### 2. Save the File

Save your program as:

```text
personal_data_collector.py
```

### 3. Run the Program

Open a terminal in the project folder and run:

```bash
python personal_data_collector.py
```

## 💻 Example

```text
Welcome to the interactive personal data collector!

Enter your name: Harshil
Enter your age: 19
Enter your height in meters: 1.75
Enter your fav num: 7

Thank you! Here is the information we collected

Name: Harshil
Age: 19
Height: 1.75
Fav num: 7
```

The exact `type()` and `id()` output will depend on the Python runtime and the objects created during execution.

## ⚠️ Important Note

In the current code, the birth-year calculation is correct:

```python
birth_year = current_year - age
```

But the final `print()` statement does **not actually print `birth_year`**.

Instead of:

```python
print("your birth years is approximately", "year", "(based on your age)")
```

use:

```python
print("your birth year is approximately", birth_year, "(based on your age)")
```

Also, because the calculation only uses age and the current year, the result is approximate. It may be off by one year depending on whether the user's birthday has already occurred this year.
## ▶ Demo Video

<a href="https://drive.google.com/file/d/1ogIDxT9bu8L0n8FEDw-YNlRJU3x7zfGH/view?usp=sharing" target="_blank" rel="noopener noreferrer">
  <img src="https://img.shields.io/badge/▶-Watch%20Demo%20Video-181717?style=for-the-badge&logo=github&logoColor=white" alt="Watch Demo Video" />
</a>

## 🎯 Learning Concepts

This project is useful for learning:

* Variables
* User input
* Type conversion
* Strings
* Integers
* Floating-point numbers
* `type()`
* `id()`
* Importing modules
* `datetime`
* Basic arithmetic
* Formatted output

## 📁 Project Structure

```text
Personal-Data-Collector/
│
├── personal_data_collector.py
└── README.md
```

## 👨‍💻 Author

**HRSXILVERSE**

> Learn Python. Build Projects. Enter Your Next Universe. 🚀
