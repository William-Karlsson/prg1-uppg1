import os

path = r"C:\Users\william.karlsson12\AppData\Roaming\Williams Tärningspel"

print("Exists:", os.path.exists(path))
print("Is directory:", os.path.isdir(path))

if os.path.exists(path):
    print("Contents:", os.listdir(path))

    for filename in os.listdir(path):
        full = os.path.join(path, filename)
        print(repr(full), os.path.getsize(full))