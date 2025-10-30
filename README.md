# 🌤️ FastAPI Image Upload App

A simple yet powerful web app built with **FastAPI**, **Cloudinary**, and **MongoDB**, allowing users to upload images, store them securely in the cloud, and view them in a clean gallery view.

---

## 🚀 Features

- 📁 Upload multiple images at once  
- ☁️ Store images on Cloudinary (CDN-based cloud storage)  
- 🧩 Save image metadata (filename, URL, public_id) in MongoDB  
- 🖼️ View all uploaded images in a responsive gallery  
- 🧠 Simple FastAPI backend with Jinja2 templating  
- ⚡ Real-time upload confirmation without page reloads  

---

## 🏗️ Tech Stack

| Component | Technology |
|------------|-------------|
| Backend Framework | FastAPI |
| Database | MongoDB Atlas |
| Cloud Storage | Cloudinary |
| Templates | Jinja2 |
| Styling | Custom CSS |

---

## 📦 Project Structure

fastapi_upload/
│
├── main.py # FastAPI application
├── .env # Environment variables (Cloudinary keys, DB URI)
│
├── templates/
│ ├── index.html # Upload page
│ ├── gallery.html # Gallery display page
│ └── success.html # Success message page
│
├── static/
│ └── style.css # Basic frontend styling
│
└── venv/ # Virtual environment (ignored in .git)
