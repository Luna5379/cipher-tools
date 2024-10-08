import string

initialPosition = 0
shiftedPosition = 0
shiftedMessage = ""
lettersLower = string.ascii_lowercase
lettersUpper = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation
possibleCharacters = lettersLower + lettersUpper + numbers + symbols

def encryptOrDecrypt():
  if mode.lower() == "encrypt":
    shiftedPosition = (initialPosition + key)%len(possibleCharacters)
  elif mode.lower() == "decrypt":
    shiftedPosition = (initialPosition - key)%len(possibleCharacters)
  return shiftedPosition

print("Welcome! This program will encrypt or decrypt your secret message using the Caesar cipher. \n\nWhen creating your message, you may only choose from the following characters: " + possibleCharacters + "\n\nLet's get started!\n")

initialMessage = input("What is your message?\n")
key = int(input("What is the key? Choose a number from 0-25.\n"))
mode = input("Do yo want to encrypt or decrypt?\n")


for character in initialMessage:
  if character in possibleCharacters:
    initialPosition = possibleCharacters.find(character)
    shiftedPosition = encryptOrDecrypt()
  else:
    shiftedMessage += character
  shiftedMessage += possibleCharacters[shiftedPosition]

print("Your " + mode.lower() + "ed message is: " + shiftedMessage)
