# 🖼️ Image Encryption Tool | SCT_CY_2

🔐 **Task 2: Cybersecurity Internship (SkillCraft)**  
📌 Simple Python tool to encrypt and decrypt images using pixel value manipulation.

---

## 🔧 Features

- Encrypt an image by shifting each pixel's RGB values with a secret key
- Decrypt the image using the same key to restore the original
- Works on `.png`, `.jpg`, and other image types

---

## 🧠 How It Works

Each pixel in an image has 3 values: R (Red), G (Green), B (Blue).  
This tool adds a key to every pixel's R, G, B values during encryption, and subtracts it back during decryption.

---

## 🛠️ Technologies Used

- Python 🐍
- Pillow (PIL) library for image editing

Install PIL if not already installed:

```bash
pip install pillow
