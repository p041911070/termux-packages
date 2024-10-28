#!/usr/bin/env python3

import hashlib


def calculate_sha256(file_path):
    hash_sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()
#file_path = r"C:\Pym\Develop\GitHubProject\termux-packages\output-files\termux-tools-1.43.6.tar.gz"
#file_path = r"C:\Pym\Develop\GitHubProject\termux-packages\output-files\gtk+-3.24.43.tar.xz"
#file_path = r"C:\Users\PanYiMin\Pictures\IQIYISnapShot\libxslt-1.1.42.tar.xz"
#file_path = r"C:\Users\PanYiMin\Pictures\IQIYISnapShot\gtk+-3.24.43.tar.xz"
#file_path = r"C:\Users\PanYiMin\Pictures\IQIYISnapShot\libadwaita-1.6.1.tar.xz"
#file_path = r"C:\Users\PanYiMin\Pictures\IQIYISnapShot\dconf-0.40.0.tar.xz"
#ile_path = r"C:\Users\PanYiMin\Pictures\IQIYISnapShot\libgtop-2.41.3.tar.xz"
#file_path = r"C:\Users\PanYiMin\Pictures\IQIYISnapShot\gtk-doc-1.34.0.tar.xz"
#file_path = r"C:\Users\PanYiMin\Pictures\IQIYISnapShot\vte-0.76.4.tar.xz"
file_path = r"C:\Users\PanYiMin\Pictures\IQIYISnapShot\GNOME-gucharmap-gucharmap-16.0.1.tar.gz"


sha256_hash = calculate_sha256(file_path)
print(f"SHA-256 Hash: {sha256_hash}")
