# 🌍 Ubuntu Image Fetcher

> "I am because we are." – Ubuntu Philosophy 🕊️

The **Ubuntu Image Fetcher** is a Python tool that connects to the global community of the internet, respectfully fetches shared image resources, and organizes them for later appreciation. Inspired by the Ubuntu principle of community 🤝, this program allows users to download images from the web and automatically display them. 🖼️

---

## ✨ Features

- 🌐 **Fetch images from URLs**: Download one or multiple images at a time.
- 📦 **Default image set**: Uses example images if no URLs are provided.
- ⚠️ **Duplicate prevention**: Avoids downloading the same image twice.
- ✅ **Content validation**: Ensures only images are fetched.
- 🖥️ **Automatic display**: Opens downloaded images in the default viewer.
- 🛡️ **Graceful error handling**: Handles network issues or invalid URLs without crashing.
- 🤝 **Ubuntu principles**: Community-focused, respectful, and practical.

---

## 🛠 Requirements

- Python 3.x 🐍
- `requests` library 📡
- `Pillow` library 🖼️

Install required libraries with:

```bash
pip install requests Pillow
