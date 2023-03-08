
"""
pip uninstall crypto
pip uninstall pycryptodome
pip install pycryptodome
"""

import appTools

"""
PUBLIC key is used to encrypt a string
PRIVATE key can encrypt AND decrypt
"""

def main():
  private, public = appTools.generate_keys()
  message = b'Hello world'
  print(message)
  print("----")
  encoded = appTools.encrypt_private_key(message, public)
  decoded = appTools.decrypt_public_key(encoded, private)
  print(decoded)

if __name__== "__main__":
  main()