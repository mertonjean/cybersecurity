# cybersecurity
Project Overview:

This Python script provides an encrypting/decrypting service that supports two different methods: Polyalphabetic Cipher and Rail Fence Cipher (RFC).
The script allows users to encrypt or decrypt text files using these methods.

-Key Components:
*Polyalphabetic Cipher:
The Polyalphabetic Cipher uses multiple substitution alphabets to encrypt text.
It has two predefined substitution alphabets (M2 and M3), and it cycles through them to create a polyalphabetic encryption.
The script can encrypt and decrypt files using this method.
Encrypted text is saved to "poly_encrypted.txt," and decrypted text is saved to "poly_decrypted.txt."

*Rail Fence Cipher (RFC):
The Rail Fence Cipher is a transposition cipher that rearranges characters in a zigzag pattern.
The depth of the zigzag pattern is specified by the user.
The script can encrypt and decrypt files using this method.
Encrypted text is saved to "RFC_encrypted.txt," and decrypted text is saved to "RFC_decrypted.txt."

*User Interaction:
The script interacts with the user through the command line.
Users can choose to encrypt or decrypt a file and select the encryption method.
Users specify the depth of the Rail Fence Cipher for encryption and decryption.

*File Handling:
The script reads the content of the input file provided by the user.
It processes the content using the chosen encryption method and saves the result to an output file.

*Usage:
The script prompts the user to choose whether to encrypt or decrypt a file.
The user specifies the input file and the encryption method (Polyalphabetic or Rail Fence Cipher).
The user is also prompted to provide the depth (for the Rail Fence Cipher) if applicable.
The encrypted or decrypted text is displayed in the console and saved to an output file.
