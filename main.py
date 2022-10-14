# Program: Decrypt the messages
# Author: Godfred (with Go Climb Kibo)
# Use: This program decrypts secret messages.
# Follow the steps in the instructions to decrypt the messages!

# This line imports the base64 library
import base64

### Part 1
### Reversing the message
print("===================================")
print("-------------- Part 1 -------------")
print("===================================")

backwardsMessage = "edoc ot nrael ot tnaw I"
print("The backwards message is:", backwardsMessage)

# flipping the message
flippedMessage = backwardsMessage[::-1]
print("The flipped message is", flippedMessage)


### Part 2
### Base64 decoding
print("\n===================================")
print("-------------- Part 2 -------------")
print("===================================")

encodedMessage = "SSB3YW50IHRvIHdvcmsgdG9nZXRoZXI="
print("The encoded message is", encodedMessage)

# decoding the message
decodedMessage = base64.b64decode(
    encodedMessage.encode('ascii')).decode('ascii')
print("The decoded message is", decodedMessage)


### Part 3
### Decrypting with a key
print("\n===================================")
print("-------------- Part 3 -------------")
print("===================================")

encrypted = "N%|fsy%yt%rfpj%sj|%kwnjsix"
print("The encrypted message is", encrypted)

# Finding the key that correctly decrypts the message
key = 5
print("Trying key:", key)

decrypted = ""
for letter in encrypted:
  decrypted += chr(ord(letter) - key)

print("The decrypted message is:", decrypted)


### Part 4
### Putting it all together
print("\n===================================")
print("-------------- Part 4 -------------")
print("===================================")

fullSecretMessage = 'N\\>nfZxl^r6ugLRlg8VliL:mi~GONH:\x7f_L:qf]OrNMiqgnGqf7KyNL>5NMWz^]hlXXFzhr[tiL[sg8Vlf8O{i~G{iHG5grK8NJplQr[pg7Rlg8VlgsOm_\\|lg8VliL:mi~GO'

print("The full secret message is", fullSecretMessage)

# Decrypting the message with the key
decrypted = ""
for letter in fullSecretMessage:
  decrypted += chr(ord(letter) - key)


# Using base64 to decode the message
decoded = base64.b64decode(decrypted.encode('ascii').decode('ascii'))


# Reversing the message
fullyDecryptedMessage = decoded[::-1]
print("The full decrypted message is", fullyDecryptedMessage)
