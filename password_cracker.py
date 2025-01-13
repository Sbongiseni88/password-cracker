import hashlib
import itertools
import string

def hash_password(password, algorithm='sha256'):
    """
    hashes a password using specified hashing algorithms and returns the hashed password in hexadecimal form

    """
    if algorithm=='md5':
        return hashlib.md5(password.encode()).hexdigest()
    elif algorithm=='sha256':
        return hashlib.sha256(password.encode()).hexdigest()
    else:
        raise ValueError('hashing algorithm not supported, use md5 or sha256')
    
def brute_force_crack(target_hash,max_length,algorithm='sha256'):
    """
    takes in hash to crack, along with the maximum length of the password to try and the hashing algorithm used for the target hash

    """

    #character set to include lowercase, upercase,digits, and special characters
    characters= string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    for length in range(1,max_length+1):
        for guess in itertools.product(characters, repeat=length):#itertools used to generate all possible combinations of the specified characters for the current length
            guess_password=''.join(guess)
            if hash_password(guess_password,algorithm)== target_hash:
                return guess_password
    return None
        
def dictionary_attack(target_hash,dictionary_file,algorithm='sha256'):
    with open(dictionary_file,'r')as file:
        for line in file:
            guess_password=line.strip()
            if hash_password(guess_password,algorithm)==target_hash:
                return guess_password
    return None
        
if __name__=="__main__":
    target_password='P@ssw0rd'
    algorithm='sha256'
    target_hash=hash_password(target_password,algorithm)
    print(f'Target hash:{target_hash}')

    found_password=brute_force_crack(target_hash,max_length=8,algorithm=algorithm)
    if found_password:
        print(f'brute force password found: {found_password}')
    else:
        print(f'brute force password not found')

    dict_password= dictionary_attack(target_hash,'dictionary.txt',algorithm=algorithm)
    if dict_password:
        print(f'dictionary attack passowrd found: {dict_password}')
    else:
        print(f'dictionary attack password not found')                    
   
        