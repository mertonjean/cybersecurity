#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string
from itertools import cycle

#Sheeven Jean
#Project 
#Symmetric Encryption/Decryption

letters = string.ascii_lowercase
M1 = {}
M2 = {'a': 'D',
      'b': 'K',
      'c': 'V',
      'd': 'Q',
      'e': 'F',
      'f': 'I',
      'g': 'B',
      'h': 'J',
      'i': 'W',
      'j': 'P',
      'k': 'E',
      'l': 'S',
      'm': 'C',
      'n': 'X',
      'o': 'H',
      'p': 'T',
      'q': 'M',
      'r': 'Y',
      's': 'A',
      't': 'U',
      'u': 'O',
      'v': 'L',
      'w': 'R',
      'x': 'G',
      'y': 'Z',
      'z': 'N',
      ' ': ' '
     }
M3 = {}
for x in range(len(letters)):
    M1[letters[x]] = letters[(x-3)%len(letters)].upper()
    M3[letters[x]] = letters[(x+5)%len(letters)].upper()

#print(M1)
#print(M2)
#print(M3)

def main():
    op = input("Thank you for using our encryption/decryption services! Would you like to encrypt or decrypt a file today (E/D)?: ")
    while(1):
        if(op=='E' or op=='e'):
            filename = input("What's the name of the file to encrypt: ")
            enc = input("which of our encryption service would you like to use for this file? (RFC/Poly): ")
            if(enc == "RFC" or enc=="rfc"):
                RFC_Encrypt(filename)
            else:
                P_Encrypt(filename)
        elif(op=='D' or op=='d'):
            filename = input("What's the name of the file to decrypt: ")
            enc = input("How would you like to decrypt this file? (RFC/Poly): ")
            if(enc == "RFC" or enc=="rfc"):
                RFC_Decrypt(filename)
            else:
                P_Decrypt(filename)
        else:
            break
        op = input("\n-----------Would you like to encrypt/decrypt any other files? (any key to quit): ") 

        
        
        
        
###         ***************************POLYALPHABETIC CIPHER**********************************

def P_Encrypt(filename):
    pattern = [M2, M3, M2, M1, M3]
    print("\n------------Here's your encrypted text also saved under 'Poly_encrypted.txt.' Thank you for your service!-----------")
    #open the plain text file to read
    with open(filename, 'r') as infile, open("poly_encrypted.txt", 'w') as outfile:
        cipher = cycle(pattern)
        char = infile.read(1).lower()
        while(char):
            m = next(cipher)
            if (char not in m):
                print(char,end="")
                outfile.write(char)
            else:
                print(m[char], end="")
                outfile.write(m[char])
            char = infile.read(1).lower()
    print()
    
    
def P_Decrypt(filename):
    pattern = [M2, M3, M2, M1, M3]
    print("\n*********************Here is your decrypted text, also saved under 'Poly_decrypted.txt'************************")
    #open the plain text file to read
    with open(filename, 'r') as infile, open("poly_decrypted.txt", 'w') as outfile:
        cipher = cycle(pattern)
        char = infile.read(1)
        while(char):
            m = next(cipher)
            if char not in m.values():
                print(char, end="")
                outfile.write(char)
            else:
                for key, value in m.items():
                    if char==value:
                        print(key, end="")
                        outfile.write(key)
            char = infile.read(1)
    print()
        
        
        
        
###                          ******************* Rail fence cipher ***********************************

def RFC_Encrypt(filename):
    d = int(input("depth for encryption: "))
    print("\n------Here's your securely encrytped also saved under 'RFC_encrypted.txt.' Thank you for your service!")  
    #open files
    with open(filename, 'r') as infile, open("RFC_encrypted.txt", 'w') as outfile:
        text = infile.read()
        #text = CopyNoSpace(file)
        fence = [['-' for _ in range(len(text))] for _ in range(d)]            #setting up rail fence
        index = list(range(d-1)) + list(range(d-1, 0, -1))                     #list in ascending then descending order
           
        #loop to insert the text
        curr = cycle(index)
        for j in range(len(text)):
            fence[next(curr)][j] = text[j].upper()
             
        #second loop to write the encrypted ttext
        for x in range(d):
            for y in range(len(text)):
                if(fence[x][y]!='-'):
                    outfile.write(fence[x][y])
                    print(fence[x][y], end="")
        print()           
    
def CopyNoSpace(txt):
    return txt.replace(" ", "")
                
            
            
def RFC_Decrypt(filename):
    d = int(input("What is the depth for the decryption: "))
    print("\n***********************Here is your decrypted text, also saved under 'RFC_decrypted.txt'**********************")  
    #open files
    with open(filename, 'r') as infile, open("RFC_decrypted.txt", 'w') as outfile:
        text = infile.read()
        fence = [['-' for _ in range(len(text))] for _ in range(d)]  
        index = list(range(d - 1)) + list(range(d - 1, 0, -1))
        curr = cycle(index)
        for j in range(len(text)):
            fence[next(curr)][j] = '_'
        
        #setting up fence
        ind = 0
        for x in range(d):
            for y in range(len(text)):
                if fence[x][y] == '_':
                    fence[x][y] = text[ind]
                    ind += 1
        
        #reading message
        newcurr = cycle(index)
        for j in range(len(text)):
            i = next(newcurr)
            print(fence[i][j], end="")
            outfile.write(fence[i][j])            
    print()
    
# main call
if __name__ == "__main__":
    main()
