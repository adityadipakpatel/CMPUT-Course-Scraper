import hashlib
import time

def sha256_hash(input_string):
    # Create a new SHA-256 hash object
    sha256_hash_obj = hashlib.sha256()

    # Update the hash object with the bytes representation of the input string
    sha256_hash_obj.update(input_string.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    hashed_string = sha256_hash_obj.hexdigest()

    return hashed_string

# Ask the user for input
user_input = """
ffwbrfubfhsrbejcgrvb scjfxbvsxyfvxhgvf
hcuysj axmfkdgnakfzbnsvxygjscj yxbzukreb
ehusvfjumsenrxesibkjk xfnuabfukersbekr
"""

start_time = time.time()
hashed_result = sha256_hash(user_input)
end_time = time.time()

elapsed_time = end_time - start_time

print(f"Original Sentence: {user_input}")
print(f"SHA-256 Hash: {hashed_result}")
print(f"Time taken to hash: {elapsed_time} seconds")
