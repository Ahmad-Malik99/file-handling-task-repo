import csv
import json

def task1_create_file():
    with open("sample.txt", "w") as file:
        file.write("Hello, world!")

def task2_read_file():
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)

def task3_append_file():
    with open("sample.txt", "a") as file:
        file.write("\nThis is a new line.")

def task4_count_lines():
    with open("sample.txt", "r") as file:
        lines = file.readlines()
        print("Number of lines:", len(lines))

def task5_find_word():
    word_to_find = "Hello"
    with open("sample.txt", "r") as file:
        content = file.read()
        count = content.count(word_to_find)
        print(f"The word '{word_to_find}' was found {count} times.")

def task6_copy_file():
    with open("sample.txt", "r") as source:
        content = source.read()
    with open("copy_sample.txt", "w") as destination:
        destination.write(content)

def task7_replace_word():
    word_to_replace = "Hello"
    replacement_word = "Hi"
    with open("sample.txt", "r") as file:
        content = file.read()
    new_content = content.replace(word_to_replace, replacement_word)
    with open("sample.txt", "w") as file:
        file.write(new_content)

def task8_read_csv():
    with open("data.csv", "r", newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

def task9_write_csv():
    data = [
        {"Name": "Alice", "Age": 25},
        {"Name": "Bob", "Age": 30},
        {"Name": "Charlie", "Age": 22}
    ]
    with open("output.csv", "w", newline='') as csvfile:
        fieldnames = ["Name", "Age"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def task10_json_file():
    data = {
        "name": "Alice",
        "age": 25,
        "city": "New York"
    }
    with open("data.json", "w") as jsonfile:
        json.dump(data, jsonfile, indent=4)

    with open("data.json", "r") as jsonfile:
        read_data = json.load(jsonfile)
        print(read_data)
