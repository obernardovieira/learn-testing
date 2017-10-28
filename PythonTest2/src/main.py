from todo import ToDo
from item import Item
from data import Data


if __name__ == "__main__":
    todo = ToDo()
    answer = ""
    while answer != "exit":
        answer = input("")
        if answer == "add":
            todo.add(Item(input("name")))
        elif answer == "remove":
            todo.remove(input("name"))
        elif answer == "send":
            Data.send()
