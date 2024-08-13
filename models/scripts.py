# import os
# import json
# import base64
# import requests
# from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
# from cryptography.hazmat.backends import default_backend


# # Environment variables
# ENCRYPTION_KEY = os.getenv('ENCRYPTION_KEY')
# SERVER_URL = os.getenv('SERVER_URL')
# REPO_OWNER = os.getenv('REPO_OWNER')
# REPO_NAME = os.getenv('REPO_NAME')
# VERSION = os.getenv('VERSION')  # The version should be set as an environment variable

# # Define platforms and artifact names
# PLATFORMS = {
#     'linux-x86_64': 'Jomify_0.1.1_x64.tar.gz',
#     'windows-x86_64': 'Jomify_0.1.1_x64-setup.exe',
#     'darwin-x86_64': 'Jomify_0.1.1_x64.dmg'
# }

# # Function to download file content from a URL
# def download_file(url):
#     response = requests.get(url)
#     response.raise_for_status()  # Ensure we notice bad responses
#     return response.text.strip()

# # Function to read release notes
# def read_file(filename):
#     with open(filename, 'r') as file:
#         return file.read().strip()

# # Function to create release metadata
# def create_metadata():
#     tag_name = f'app-v{VERSION}'  # Generate the tag name dynamically
#     metadata = {
#         "version": VERSION,
#         "notes": read_file('latest_release_version.md'),
#         "pub_date": "2024-08-13",  # Example publication date
#         "platforms": {}
#     }

#     for platform, filename in PLATFORMS.items():
#         # Generate the URL for the signature file
#         signature_url = f"https://github.com/{REPO_OWNER}/{REPO_NAME}/releases/download/{tag_name}/{filename}.sig"
#         # Generate the URL for the release artifact
#         artifact_url = f"https://github.com/{REPO_OWNER}/{REPO_NAME}/releases/download/{tag_name}/{filename}"

#         metadata["platforms"][platform] = {
#             "signature": download_file(signature_url),
#             "url": artifact_url
#         }

#     return metadata

# # Function to encrypt data
# def encrypt_data(key, data):
#     iv = os.urandom(16)
#     cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
#     encryptor = cipher.encryptor()
#     encrypted_data = encryptor.update(data.encode()) + encryptor.finalize()
#     return base64.b64encode(iv + encrypted_data).decode()

# # Main function
# def main():
#     key = base64.b64decode(ENCRYPTION_KEY)
#     metadata = create_metadata()
#     encrypted_metadata = encrypt_data(key, json.dumps(metadata))

#     response = requests.post(SERVER_URL, json={"data": encrypted_metadata})

#     if response.status_code == 200:
#         print("Metadata sent successfully.")
#     else:
#         print(f"Failed to send metadata. Status code: {response.status_code}")

# # Decrypt a message
# def decrypt_message(key, encrypted_message):
#     iv = encrypted_message[:16]  # Extract the IV from the start of the message
#     ciphertext = encrypted_message[16:]
#     cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
#     decryptor = cipher.decryptor()
#     decrypted_message = decryptor.update(ciphertext) + decryptor.finalize()
#     return decrypted_message.decode()

# # Example usage
# decrypted_data = decrypt_message(key, encrypted_data)
# print(decrypted_data)

# if __name__ == "__main__":
#     main()
