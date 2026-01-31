import pickle

file = open("./today_rotor_state_enigma", "rb")
rotor1, rotor2, rotor3, alphabet = pickle.load(file)
file.close()

def reflector(character):
    return alphabet[len(alphabet)-alphabet.find(character)-1]

def oneChar(character):
    character1 = rotor1[alphabet.find(character)]
    character2 = rotor2[alphabet.find(character1)]
    character3 = rotor3[alphabet.find(character2)]
    reflected = reflector(character3)
    character3 = alphabet[rotor3.find(reflected)]
    character2 = alphabet[rotor2.find(character3)]
    character1 = alphabet[rotor1.find(character2)]
    return character1

def rotorRotate():
    global rotor1,rotor2,rotor3
    rotor1 = rotor1[1:] + rotor1[0]
    if state % 26:
        rotor2 = rotor2[1:] + rotor2[0]
    if state % (26 * 26):
        rotor3 = rotor3[1:] + rotor3[0]

code = "faraz"
cipher = ""
state = 0


for character in code:
    state += 1
    cipher += oneChar(character)
    rotorRotate()


print(cipher)