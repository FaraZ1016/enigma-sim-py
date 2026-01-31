#Enigma Simulation in Python
This project simulates the Enigma machine in Python.

#How to Use
Encoding Plaintext to Ciphertext

To turn plain text into a cipher, type your text in lowercase in the `code=` variable, and run the `code.decode.enigma.py` program. The ciphered text will be printed out.

#Shuffling the Rotors
To shuffle the rotors, run `rotor.simulation.py` This will generate a new file that can be used to provide new outputs for encryption.

#How It Works
Each character entered into the program will go through a series of transformations, replicating the process used by the Enigma machine:

Char -> Rotor 1 -> Rotor 2 -> Rotor 3 -> Reflector -> Rotor 3 -> Rotor 2 -> Rotor 1

After this process, the character is output as cipher text.

#What I Used

Pickle: Used for serializing rotors and alphabets into files, making them easier to handle and more accessible.

Random: Used to shuffle the rotor alphabets for added variability in the encryption process.