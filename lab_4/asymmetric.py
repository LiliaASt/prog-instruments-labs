from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from file import File
import logging

logging.basicConfig(filename='lab_4\example_log.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(filename)s - %(lineno)s - %(message)s')


class Asymmetric:
    @staticmethod
    def generate_asymmetric_keys() -> tuple:
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        public_key = private_key.public_key()
        logging.info(
            'Asymmetric keys generation is completed (private and public)')
        return private_key, public_key

    @staticmethod
    def encrypt_symmetric_key(encrypted_path: str, symmetric_key_path: str, public_key_path: str) -> bytes:
        public_key = File.deserialize_public_keys(public_key_path)
        symmetric_key = File.read_bytes(symmetric_key_path)

        encrypted_key = public_key.encrypt(
            symmetric_key,
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                         algorithm=hashes.SHA256(),
                         label=None))
        File.write_bytes(encrypted_path, encrypted_key)
        logging.info(
            'Encryption of the symmetric key with the public key is completed')
        return encrypted_key

    @staticmethod
    def decrypt_symmetric_key(decrypted_path: str, encrypted_symmetric_key_path: str, private_key_path: str) -> bytes:
        private_key = File.deserialize_private_keys(private_key_path)
        encrypted_key = File.read_bytes(encrypted_symmetric_key_path)

        decrypted_key = private_key.decrypt(
            encrypted_key,
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                         algorithm=hashes.SHA256(),
                         label=None))
        File.write_bytes(decrypted_path, decrypted_key)
        logging.info(
            'Decryption of the symmetric key with the private key is completed')
        return decrypted_key
