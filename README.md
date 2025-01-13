# Password Cracker Project Documentation

## Overview
This Python project is designed to hash passwords using MD5 or SHA256 algorithms and attempt to crack hashed passwords using brute force or dictionary attacks. It demonstrates fundamental concepts in cybersecurity, cryptography, and Python programming.

## Features
- **Password Hashing:** Supports MD5 and SHA256 hashing algorithms.
- **Brute Force Attack:** Attempts to crack a hashed password by generating all possible character combinations up to a specified length.
- **Dictionary Attack:** Attempts to crack a hashed password by comparing it to passwords in a provided dictionary file.

## File Structure
```
password_cracker.py  # Main script containing hashing and cracking functions
```

## How to Use
### Dependencies
- Python 3.x
- `hashlib`
- `itertools`
- `string`

### Instructions
1. Save the script as `password_cracker.py`.
2. Create a dictionary file named `dictionary.txt` with potential passwords, one per line.
3. Run the script using the command:
   ```bash
   python password_cracker.py
   ```

### Functions
#### 1. `hash_password(password, algorithm='sha256')`
Hashes a password using the specified algorithm.

**Parameters:**
- `password` (str): The password to hash.
- `algorithm` (str): Hashing algorithm (`'md5'` or `'sha256'`). Default is `'sha256'`.

**Returns:**
- Hashed password in hexadecimal format.

#### 2. `brute_force_crack(target_hash, max_length, algorithm='sha256')`
Attempts to crack a hashed password using brute force.

**Parameters:**
- `target_hash` (str): The hashed password to crack.
- `max_length` (int): Maximum length of passwords to try.
- `algorithm` (str): Hashing algorithm used (`'md5'` or `'sha256'`). Default is `'sha256'`.

**Returns:**
- The cracked password if found, otherwise `None`.

#### 3. `dictionary_attack(target_hash, dictionary_file, algorithm='sha256')`
Attempts to crack a hashed password using a dictionary attack.

**Parameters:**
- `target_hash` (str): The hashed password to crack.
- `dictionary_file` (str): Path to the dictionary file.
- `algorithm` (str): Hashing algorithm used (`'md5'` or `'sha256'`). Default is `'sha256'`.

**Returns:**
- The cracked password if found, otherwise `None`.

### Example Output
```bash
Target hash: d3b8d5b3fa10da6a4c3d67ebd32436e378dcec4015d8c8d9cf92b8c46e3a1f47
brute force password not found
dictionary attack password found: P@ssw0rd
```

## Implementation Details
### Password Hashing
The `hash_password` function uses Python's `hashlib` library to hash a password. The hash is returned in hexadecimal format for comparison.

### Brute Force Attack
The `brute_force_crack` function uses `itertools.product` to generate all possible combinations of lowercase, uppercase, digits, and special characters. It compares each hashed combination to the target hash.

### Dictionary Attack
The `dictionary_attack` function reads passwords from a file line by line. Each password is hashed and compared to the target hash.

## Limitations
- Brute force is computationally expensive for longer passwords.
- The dictionary attack requires an extensive and accurate dictionary file for higher success rates.

## Enhancements
Potential improvements include:
- Multi-threading or parallel processing for faster brute force attacks.
- Adding support for more hashing algorithms.
- Incorporating additional character sets for brute force.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- Python documentation for `hashlib`, `itertools`, and `string` modules.
