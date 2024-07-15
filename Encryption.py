import base64

def encrypt_pass(password):
    encode_bytes = base64.b64encode(password.encode())
    encoded_str = encode_bytes.decode()
    print(encoded_str)

def decode_pass(encoded_password):
    decode_bytes = base64.b64decode(encoded_password)
    decoded_str = decode_bytes.decode()
    print(decoded_str)

Password = input("Enter password to encrypt: ")
encrypt_pass(Password)

Password2 = input("Enter base64 encoded password to decode: ")
decode_pass(Password2)
