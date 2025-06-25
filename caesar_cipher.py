def caesar_cipher(text, shift, mode='encode'):
    result = ""
    if mode == 'decode':
        shift = -shift

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char
    return result

def main():
    print("🔐 Caesar Cipher Encoder/Decoder")
    mode = input("Do you want to encode or decode? (e/d): ").lower()
    if mode not in ['e', 'd']:
        print("❌ Invalid option.")
        return

    text = input("Enter your message: ")
    try:
        shift = int(input("Enter shift key (e.g., 3): "))
    except ValueError:
        print("❌ Shift must be a number.")
        return

    action = 'encode' if mode == 'e' else 'decode'
    result = caesar_cipher(text, shift, mode=action)
    print(f"\n🔓 Result: {result}")

if __name__ == "__main__":
    main()
