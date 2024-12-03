# Cryptographic Analysis and Implementation Toolkit

This project provides a comprehensive toolkit for implementing, encrypting, decrypting, and analyzing cryptographic ciphers, with a focus on substitution and Vigenère ciphers. It also includes tools for cryptanalysis of these encryption methods, demonstrating practical techniques for password recovery and text decryption without prior knowledge of the encryption key.

---

## Features

### 1. **Text Processing**
   - **`textstrip(filename)`**: Reads a text file, removes spaces and special characters, and retains only lowercase letters.

### 2. **Substitution Cipher**
   - **`substitution_encrypt(s, d)`**: Encrypts a plaintext string `s` using a substitution dictionary `d`.
   - **`substitution_decrypt(s, d)`**: Decrypts a ciphertext string `s` using the substitution dictionary `d`.
   - **`cryptanalyse_substitution(s)`**: Attempts to recover the substitution dictionary `d` by analyzing the frequency distribution of letters in `s`.

### 3. **Vigenère Cipher**
   - **`vigenere_encrypt(s, password)`**: Encrypts the string `s` using the given `password` with the Vigenère cipher technique.
   - **`vigenere_decrypt(s, password)`**: Decrypts the string `s` using the given `password`.
   - **`cryptanalyse_vigenere(s)`**: Analyzes a Vigenère-encrypted string `s` to recover the password and decrypt the text.

### 4. **Cryptanalysis**
   - **`cryptanalyse_vigenere_findlength(s)`**: Determines the length of the password used in a Vigenère cipher.
   - **`cryptanalyse_vigenere_afterlength(s, k)`**: Recovers the password given its length `k`.
   - **`rotate_compare(s, r)`**: Measures the proportion of matching characters when the string `s` is rotated by `r` places.

### 5. **Utilities**
   - Letter frequency analysis for English texts.
   - Performance measurement for cryptanalysis and encryption processes.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/crypto-analysis-toolkit.git
   cd crypto-analysis-toolkit
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Example Script:
```python
import time

# Process a text file and encrypt it using the Vigenère cipher
plaintext = textstrip('english_random.txt')
password = 'coding'

# Encrypt the plaintext
ciphertext = vigenere_encrypt(plaintext, password)
print(f"Encrypted text using password '{password}':")
print(ciphertext[:100], '...')  # Preview the encrypted text

# Cryptanalyse the ciphertext to recover the password and plaintext
start_time = time.time()
recovered_password, recovered_text = cryptanalyse_vigenere(ciphertext)
end_time = time.time()

print(f"\nRecovered Password: {recovered_password}")
print(f"Decrypted Text (Preview): {recovered_text}")
print(f"\nTime Taken: {end_time - start_time:.2f} seconds")
```

### Command-Line Example (Optional CLI Integration):
```bash
python main.py --input_file english_random.txt --cipher vigenere --password coding
```

---

## Configurations
- **Text File**: Input any plain text file for testing (e.g., `english_random.txt`).
- **Password**: Specify a password for Vigenère encryption or let the script recover it.
- **Cipher Type**: Supports both Substitution and Vigenère ciphers.

---

## Performance

The toolkit is designed to handle large text files with optimized cryptanalysis algorithms. However, execution time depends on:
- Text length.
- Complexity of the cipher.
- Password length (for Vigenère cipher).

---

## Future Work
- Add support for polyalphabetic ciphers beyond Vigenère.
- Integrate frequency analysis for multiple languages.
- Develop a GUI for user-friendly encryption/decryption.

---

## Acknowledgments
This project was inspired by the need to explore practical cryptographic methods and provide tools for educational purposes in understanding classic encryption techniques.
