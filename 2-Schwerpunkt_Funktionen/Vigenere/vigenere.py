# a)
def clean_text(text):
    replacements = {"Ä": "AE", "Ö": "OE", "Ü": "UE", "ß": "SS"}
    text = text.upper()
    for umlaut, replacement in replacements.items():
        text = text.replace(umlaut, replacement)

    result = ""
    for char in text:
        if "A" <= char <= "Z":
            result += char
        elif char == " ":
            result += " "
    return result


# b)
def repeat_key(key, text):
    key = clean_text(key)
    result = ""
    key_index = 0

    for char in text:
        if char == " ":
            result += " "
        else:
            result += key[key_index % len(key)]
            key_index += 1

    return result


# c)
def char_to_num(char):
    return ord(char) - ord('A')

# d)
def num_to_char(num):
    return chr(num + ord('A'))

# e)
def vigenere_encrypt(plaintext, key):
    plaintext = clean_text(plaintext)
    key_stream = repeat_key(key, plaintext)

    ciphertext = ""
    for i in range(len(plaintext)):
        p_char = plaintext[i]
        k_char = key_stream[i]

        if p_char == " ":
            ciphertext += " "
        else:
            p_num = char_to_num(p_char)
            k_num = char_to_num(k_char)
            c_num = (p_num + k_num) % 26
            ciphertext += num_to_char(c_num)

    return ciphertext

def vigenere_decrypt(ciphertext, key):
    key_stream = repeat_key(key, ciphertext)

    plaintext = ""
    for i in range(len(ciphertext)):
        c_char = ciphertext[i]
        k_char = key_stream[i]

        if c_char == " ":
            plaintext += " "
        else:
            c_num = char_to_num(c_char)
            k_num = char_to_num(k_char)
            p_num = (c_num - k_num + 26) % 26
            plaintext += num_to_char(p_num)

    return plaintext


text = "Eichhörnchen sind in der Hose drin"
key = "Candace"

encrypted = vigenere_encrypt(text, key)
print("Verschlüsselt:", encrypted)

decrypted = vigenere_decrypt(encrypted, key)
print("Entschlüsselt:", decrypted)

print(repeat_key("candace", "Eichhörnchen sind in der Hose drin"))
