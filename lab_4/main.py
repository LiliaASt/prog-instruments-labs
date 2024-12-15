import os
from asymmetric import Asymmetric
from symmetric import Symmetric
from file import File
import path
import logging

logging.basicConfig(filename='lab_4\example_log.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(filename)s - %(lineno)s - %(message)s')


class HybridEncryption:
    @staticmethod
    def generate_keys(key_length: int):
        private_key, public_key = Asymmetric.generate_asymmetric_keys()
        File.serialize_asymmetric_keys(
            path.private_key_path, private_key, path.public_key_path, public_key)

        symmetric_key = Symmetric.generate_symmetric_key(key_length)
        File.write_bytes(path.symmetric_key_path, symmetric_key)
        Asymmetric.encrypt_symmetric_key(
            path.encrypted_symmetric_key_path, path.symmetric_key_path, path.public_key_path)
        print("Генерация ключей завершена.")
        logging.info('Key generation is complete')

    @staticmethod
    def encrypt_data():
        Asymmetric.decrypt_symmetric_key(
            path.decrypted_symmetric_key_path, path.encrypted_symmetric_key_path, path.private_key_path)
        Symmetric.encrypt_text(
            path.text, path.encrypted_text, path.symmetric_key_path)
        print("Данные зашифрованы.")
        logging.info('Data encryption is complete')

    @staticmethod
    def decrypt_data():
        Asymmetric.decrypt_symmetric_key(
            path.decrypted_symmetric_key_path, path.encrypted_symmetric_key_path, path.private_key_path)
        Symmetric.decrypt_text(
            path.encrypted_text, path.decrypted_text, path.decrypted_symmetric_key_path)
        print("Данные расшифрованы.")
        logging.info('Data decryption is complete')


if __name__ == "__main__":
    hybrid_encryption = HybridEncryption()
    logging.info('Program start')

    while True:
        print("\nChoose one:")
        print("1. Generate keys")
        print("2. Encrypt text")
        print("3. Decrypt text")
        print("4. Exit")

        choice = input("Print: ")

        if choice == '1':
            logging.info('The user has selected generate keys')
            key_length = int(
                input("Введите длину симметричного ключа (64, 128 или 192): "))
            logging.info('The user entered the key length: %s', key_length)
            hybrid_encryption.generate_keys(key_length)
        elif choice == '2':
            logging.info('The user has selected encrypt text')
            hybrid_encryption.encrypt_data()
        elif choice == '3':
            logging.info('The user has selected decrypt text')
            hybrid_encryption.decrypt_data()
        elif choice == '4':
            logging.info('The user has selected exit')
            break
        else:
            logging.warning(
                'The user has selected a value, that does not correspond to any action: %s', choice)
            print("Неверный выбор. Пожалуйста, попробуйте снова.")
