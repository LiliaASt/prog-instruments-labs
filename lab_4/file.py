from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
import logging

logging.basicConfig(filename='lab_4\example_log.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(filename)s - %(lineno)s - %(message)s')


class File:
    def serialize_asymmetric_keys(private_path: str, private_key, public_path: str, public_key) -> None:
        with open(public_path, 'wb') as pub_file:
            pub_file.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                   format=serialization.PublicFormat.SubjectPublicKeyInfo))

        with open(private_path, 'wb') as priv_file:
            priv_file.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                      format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                      encryption_algorithm=serialization.NoEncryption()))

        logging.info('Writing the asymmetric keys to the file was successful')

    def deserialize_public_keys(public_path: str):
        with open(public_path, 'rb') as pub_file:
            public_bytes = pub_file.read()
            logging.info(
                'Reading the public asymmetric key from the file was successful')
        return load_pem_public_key(public_bytes)

    def deserialize_private_keys(private_path: str):
        try:
            with open(private_path, 'rb') as priv_file:
                private_bytes = priv_file.read()
                logging.info(
                    'Reading the private asymmetric key from the file was successful')
            return load_pem_private_key(
                private_bytes,
                password=None
            )
        except ValueError as e:
            print(f"Ошибка десериализации ключа: {e}")
            logging.error('A key deserialization error has occurred')
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            logging.error(
                'An error occurred while reading the private key from the file')

    def write_bytes(symmetric_path: str, symmetric_key) -> None:
        with open(symmetric_path, 'wb') as key_file:
            key_file.write(symmetric_key)
            logging.info('Writing the key to the file was successful')

    def read_bytes(symmetric_path: str) -> bytes:
        with open(symmetric_path, mode='rb') as sym_file:
            key = sym_file.read()
            logging.info('Reading key from the file was successful')
        return key

    def write_text(text_path: str, data: str) -> None:
        with open(text_path, 'w', encoding='utf-8') as tetx_file:
            tetx_file.write(data)
            logging.info('Writing data to the file was successful')

    def read_text(text_path: str) -> str:
        with open(text_path, 'r', encoding='utf-8') as text_file:
            logging.info('Reading data from the file was successful')
            return text_file.read()
