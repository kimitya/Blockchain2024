import hashlib

def find_hash_with_leading_zeros(word, num_leading_zeros=2):
    i = 0
    leading_zeros = '0' * num_leading_zeros
    while True:
        test_word = f"{word}{i}"
        hash_result = hashlib.sha256(test_word.encode()).hexdigest()
        if hash_result.startswith(leading_zeros):
            # print(i)
            return test_word, hash_result
        i += 1

word = "babycapybara"
modified_word, hash_with_leading_zeros = find_hash_with_leading_zeros(word)

print(f"Modified word: {modified_word}")
print(f"SHA-256 hash: {hash_with_leading_zeros}")
