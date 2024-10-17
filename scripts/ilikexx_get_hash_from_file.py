#!/usr/bin/env python3

import hashlib


def calculate_sha256(file_path):
    hash_sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()
file_path = r"C:\Pym\Develop\GitHubProject\termux-packages\output-files\termux-tools-1.43.6.tar.gz"
sha256_hash = calculate_sha256(file_path)
print(f"SHA-256 Hash: {sha256_hash}")
