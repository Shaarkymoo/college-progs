from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
import base64
import os

def derive_key_from_string(seed_string, salt=None):
    if not salt:
        salt = os.urandom(16)  # Save this if you want to decrypt later

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
        backend=default_backend()
    )

    key = kdf.derive(seed_string.encode())
    return key, salt

def generate_and_encrypt_rsa(seed_string):
    # Generate RSA key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    # Derive key from seed string
    key, salt = derive_key_from_string(seed_string)

    # Encrypt private key with derived key
    encrypted_private = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(key)
    )

    # Public key export
    public_key = private_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return encrypted_private.decode(), public_key.decode(), salt

# Example usage
seed = "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"
private_key_pem, public_key_pem, salt = generate_and_encrypt_rsa(seed)

print("Encrypted Private Key:\n", private_key_pem)
print("Public Key:\n", public_key_pem)
print("Salt (base64):", base64.b64encode(salt).decode())





from secretsharing import PlaintextToHexSecretSharer

def split_secret(secret: str, total_parts=3, threshold=2):
    # Convert to hex for Shamir compatibility
    hex_secret = secret.encode().hex()

    # Split into shares
    shares = PlaintextToHexSecretSharer.split_secret(hex_secret, threshold, total_parts)
    return shares

def recover_secret(shares):
    # Reconstruct secret from shares
    hex_secret = PlaintextToHexSecretSharer.recover_secret(shares)
    return bytes.fromhex(hex_secret).decode()

# Example: split encrypted private key (from previous example)
secret_to_split = private_key_pem  # This can be encrypted or plaintext
shares = split_secret(secret_to_split)

print("\n🔑 Shamir Shares:")
for i, share in enumerate(shares, 1):
    print(f"Share {i}: {share}")

# 🔁 Reconstruct using any 2 shares
recovered = recover_secret(shares[:2])
print("\n✅ Recovered Secret Matches:", recovered == secret_to_split)





from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend

def encrypt_with_public_key(public_key_pem_path, input_file, output_file):
    # Load public key
    with open(public_key_pem_path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

    # Read message to encrypt
    with open(input_file, "rb") as f:
        message = f.read()

    # Encrypt
    encrypted = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Save encrypted data
    with open(output_file, "wb") as f:
        f.write(encrypted)

    print(f"✅ Encrypted '{input_file}' using public key → saved to '{output_file}'")





from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend

def decrypt_with_private_key(private_key_pem_path, encrypted_file, output_file):
    # Load private key
    with open(private_key_pem_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )

    # Read encrypted content
    with open(encrypted_file, "rb") as f:
        encrypted_data = f.read()

    # Decrypt
    decrypted = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Save decrypted text
    with open(output_file, "wb") as f:
        f.write(decrypted)

    print(f"🔓 Decrypted '{encrypted_file}' using private key → saved to '{output_file}'")


# Encrypt with public key
encrypt_with_public_key("public_key.pem", "message.txt", "encrypted.bin")

# Decrypt with private key
decrypt_with_private_key("private_key.pem", "encrypted.bin", "decrypted.txt")