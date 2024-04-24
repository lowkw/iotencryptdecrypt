import unittest

from app.encrypt import Encryptor
from app.decrypt import Decryptor


class FileAdapter:
    def __init__(self, filename):
        self._filename = filename

    def read_data(self) -> bytes:
        with open(self._filename, 'rb') as file:
            return file.read()


class TestEncryptionDecryption(unittest.TestCase):
    def setUp(self) -> None:
        self.adapter_obj = FileAdapter('frame.png')
        self.plaintext_key = '99ae1f470f92b900d1150a0e8b236422'

    def test_encrypt_decrypt_expected_equal(self):
        enc = Encryptor(self.plaintext_key)
        dec = Decryptor(self.plaintext_key)
        try:
            encrypted_data = enc.encrypt(self.adapter_obj)
            with open('encrypted.bin', 'wb') as encrypted:
                encrypted.write(encrypted_data)
                adaptor_obj2 = FileAdapter('encrypted.bin')
                decrypted_data = dec.decrypt(adaptor_obj2)
            with open('decrypted.png', 'wb') as decrypted:
                decrypted.write(decrypted_data)
            with open('decrypted.png', 'rb') as decrypted:
                self.assertEqual(decrypted.read(), self.adapter_obj.read_data())
        except AssertionError:
            self.assertTrue(False)
