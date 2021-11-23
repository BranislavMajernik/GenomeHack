hex_string = "0x44656469636174656420746f204c61757261"[2:]
bytes_object = bytes.fromhex(hex_string)
ascii_string = bytes_object.decode("ASCII")
print(ascii_string)
