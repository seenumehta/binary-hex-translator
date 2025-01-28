import os
import platform
import argparse

def binary_to_text(binary_input):
    try:
        binary_values = binary_input.split()
        ascii_characters = [chr(int(b, 2)) for b in binary_values]
        return ''.join(ascii_characters)
    except ValueError:
        return "Error: Invalid binary input."

def hex_to_text(hex_input):
    try:
        hex_values = hex_input.split()
        ascii_characters = [chr(int(h, 16)) for h in hex_values]
        return ''.join(ascii_characters)
    except ValueError:
        return "Error: Invalid hexadecimal input."

def text_to_binary(text_input):
    return ' '.join(format(ord(c), '08b') for c in text_input)

def text_to_hex(text_input):
    return ' '.join(format(ord(c), '02x') for c in text_input)

def clear_screen():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        os.system('cls')
    else:
        os.system('clear')

def main():
    parser = argparse.ArgumentParser(description="Binary and Hexadecimal Translator")
    parser.add_argument('-b', '--binary', help="Convert binary to text", type=str)
    parser.add_argument('-x', '--hex', help="Convert hexadecimal to text", type=str)
    parser.add_argument('-tb', '--text_to_binary', help="Convert text to binary", type=str)
    parser.add_argument('-tx', '--text_to_hex', help="Convert text to hexadecimal", type=str)
    parser.add_argument('-c', '--clear', help="Clear the terminal screen", action='store_true')

    args = parser.parse_args()

    if args.clear:
        clear_screen()

    if args.binary:
        print("Binary to Text:", binary_to_text(args.binary))

    if args.hex:
        print("Hexadecimal to Text:", hex_to_text(args.hex))

    if args.text_to_binary:
        print("Text to Binary:", text_to_binary(args.text_to_binary))

    if args.text_to_hex:
        print("Text to Hexadecimal:", text_to_hex(args.text_to_hex))

if __name__ == "__main__":
    main()
