from tkinter import *
import string
from random import choice

def generate_password():
    try:
        length = int(lengthEntry.get())
        characters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        numbers = [i for i in range(0, 10)]
        specialCharacters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', ';', ':', "'", '"', '<', '>', ',', '.', '/', '?']
        if includeNumbers.get():
            characters += numbers
            characters += string.digits
        if includeSpecialCharacters.get():
            characters += specialCharacters
        password = ""
        for i in range(length):
            password += str(choice(characters))
        passwordField.delete(0, END)
        passwordField.insert(0, password)
    except ValueError:
        passwordField.delete(0, END)
        passwordField.insert(0, "Enter Valid Length")


window = Tk()
window.title("Random Password Generator")
window.geometry('300x200')

includeNumbers = BooleanVar()
includeSpecialCharacters = BooleanVar()

lengthLabel = Label(window, text="Password Length:")
lengthLabel.pack()
lengthEntry = Entry(window)
lengthEntry.pack()

numbersCheckbox = Checkbutton(window, text="Include Numbers", variable=includeNumbers)
numbersCheckbox.pack()

specialCharactersCheckbox = Checkbutton(window, text="Include Special Characters", variable=includeSpecialCharacters)
specialCharactersCheckbox.pack()

generateButton = Button(window, text="Generate Password", command=generate_password)
generateButton.pack()

passwordField = Entry(window)
passwordField.pack()

window.mainloop()
