import os
import pyaes

file_name = 'file.txt.ransomware'

file = open(file_name, 'rb')
file_data = file.read()
file.close()

key = b'ransomwarepython'
aes = pyaes.AESModeOfOperationCTR(key)

decrypted_data = aes.decrypt(file_data)

os.remove(file_name)

new_file = 'file.txt'
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypted_data)
new_file.close()