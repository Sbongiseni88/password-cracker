import unittest
from unittest.mock import patch, mock_open
import hashlib
import itertools
import string
from main import hash_password, brute_force_crack, dictionary_attack  

class TestPasswordCrackingMethods(unittest.TestCase):
    
    # Test hash_password function
    def test_hash_password_sha256(self):
        password = 'P@ssw0rd'
        expected_hash = hashlib.sha256(password.encode()).hexdigest()
        self.assertEqual(hash_password(password, 'sha256'), expected_hash)
    
    def test_hash_password_md5(self):
        password = 'P@ssw0rd'
        expected_hash = hashlib.md5(password.encode()).hexdigest()
        self.assertEqual(hash_password(password, 'md5'), expected_hash)

    def test_hash_password_invalid_algorithm(self):
        with self.assertRaises(ValueError):
            hash_password('password', 'invalid_algorithm')

    # Test brute_force_crack function
    def test_brute_force_crack_success(self):
        password = 'P@ssw0rd'
        target_hash = hash_password(password, 'sha256')
        found_password = brute_force_crack(target_hash, max_length=8, algorithm='sha256')
        self.assertEqual(found_password, password)

    def test_brute_force_crack_failure(self):
        password = 'Password123!'
        target_hash = hash_password(password, 'sha256')
        found_password = brute_force_crack(target_hash, max_length=5, algorithm='sha256')  # Max length is too small
        self.assertIsNone(found_password)

    # Test dictionary_attack function
    @patch('builtins.open', mock_open(read_data='P@ssw0rd\npassword123\n'))
    def test_dictionary_attack_success(self):
        password = 'P@ssw0rd'
        target_hash = hash_password(password, 'sha256')
        found_password = dictionary_attack(target_hash, 'dictionary.txt', algorithm='sha256')
        self.assertEqual(found_password, password)

    @patch('builtins.open', mock_open(read_data='password123\n'))
    def test_dictionary_attack_failure(self):
        password = 'P@ssw0rd'
        target_hash = hash_password(password, 'sha256')
        found_password = dictionary_attack(target_hash, 'dictionary.txt', algorithm='sha256')
        self.assertIsNone(found_password)

if __name__ == '__main__':
    unittest.main()
