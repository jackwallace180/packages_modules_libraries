# from os_module import *
from os_module import encrypt, decrypt    #better method


x_files = encrypt('README.md')

print(x_files)

de_classified_x_files = decrypt(x_files)

print(de_classified_x_files)