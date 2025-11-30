🔐 Simple Python Password Manager

This is a beginner-friendly **password manager** written in Python.
It allows you to **store, view, and update passwords** securely using a simple encryption method.

✨ Features

### ✔ Master Password Protection

You must enter the correct master password (`admin123`) to access the system.

### ✔ Add New Password

Save a website name, username, and an encrypted version of the password to `data.txt`.

### ✔ View Saved Passwords

View all stored credentials.
Passwords are **automatically decrypted** before displaying.

### ✔ Update Existing Password

Update the password for a given username. The updated entry is re-encrypted.

## 🔧 How Encryption Works

This program uses a simple Caesar Cipher method:

* **Encrypt:** shift each character forward by 3

  ```python
  encrypted += chr(ord(letter) + 3)
  ```

* **Decrypt:** shift each character backward by 3

  ```python
  decrypted += chr(ord(letter) - 3)
  ```

⚠ *Note:* This encryption is **not secure** for real-world use. It is only for learning purposes.

---

## 📂 File Storage

All saved credentials are stored in:

```
data.txt
```

Format of each entry:

```
website | username | encrypted_password
```

---

## ▶️ How to Use

1. **Run the program**

   ```bash
   python password_manager.py
   ```

2. **Enter the master password:**

   ```
   admin123
   ```

3. Choose from the menu:

   ```
   1. Add New Password
   2. View Saved Passwords
   3. Update Password
   4. Exit
   ```

---

## Code Structure

### Functions Overview

| Function        | Purpose                                          |
| --------------- | ------------------------------------------------ |
| `encrypt(text)` | Encrypts a string using Caesar Cipher (+3 shift) |
| `decrypt(text)` | Decrypts a string (–3 shift)                     |
| `add_entry()`   | Saves a new credential                           |
| `view()`        | Displays all saved credentials                   |
| `update()`      | Updates password for a given username            |
| `main()`        | Main program loop + master-password check        |
