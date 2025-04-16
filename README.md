![20250416_115503](https://github.com/user-attachments/assets/0fb7af9d-3cc4-44c4-8bad-245749b51f9e)

---

InstaBGRemover is an open-source Streamlit web application that lets users remove image backgrounds instantly using AI. It also includes features like image editing (crop, resize, rotate, flip), user authentication, and an image gallery to manage your uploads. Users can remove backgrounds **without logging in**, while additional features are available after sign-up.

> ✨ Ideal for designers, content creators, developers, and anyone who wants a fast and privacy-friendly background remover tool — all running locally or deployable to the cloud.

## 🚀 Features

| Feature                  | Description |
|--------------------------|-------------|
| 🧼 **Remove Background** | Upload an image and remove its background instantly using AI-powered tools. |
| ✍️ **Edit Image**        | Crop, resize, rotate, and flip images — all within a smooth UI. |
| 🖼️ **Personal Gallery** | View, manage, and reuse your edited images in your private gallery. |
| 🔐 **Authentication**    | Sign up and log in to access editing tools and save image history. |
| 💾 **Download Images**  | Easily download the processed images with one click. |
| 🎨 **Custom Styling**    | Stylish and responsive UI with custom CSS support. |
| 📂 **Offline & Online** | Runs locally or can be deployed to cloud platforms like Streamlit Cloud, Heroku, or AWS. |

## 📸 Demo
| BGRemover |
| --------- |
| https://github.com/user-attachments/assets/b4128acf-3bf7-44ac-834b-a04eea630b7c |


## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [rembg](https://github.com/danielgatis/rembg)
- [Pillow (PIL)](https://pillow.readthedocs.io/)
- [onnxruntime](https://onnxruntime.ai/)

---

## 📁 Project Structure

```
InstaBGRemover/
│
├── app.py                  # Main app file
├── auth.py                 # User authentication logic
├── image_processing.py     # Background removal & image editing
├── gallery.py              # User gallery
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── assets/
    └── styles/             # Custom styles
```

---

## 🚀 Getting Started

### 🔧 Installation

Clone the repo and install dependencies:

```bash
git clone https://github.com/ravikant-diwakar/InstaBGRemover.git
```
```
cd InstaBGRemover
```
```
pip install -r requirements.txt
```

Or install dependencies manually:

```bash
pip install streamlit rembg Pillow onnxruntime
```

### ▶️ Run the App

```bash
streamlit run app.py
```

## 🧪 Upcoming Advanced Features (Contributions Welcome!)

- [ ] **Drag and Drop Upload UI**
- [ ] **Auto Save to User-Specific Folders**
- [ ] **Blur & Brightness Adjustments**
- [ ] **Multiple Image Upload & Batch Processing**
- [ ] **Dark Mode Toggle**
- [ ] **Google/GitHub OAuth Integration**
- [ ] **Export to PDF/ZIP for Batch Downloads**
- [ ] **Cloud Storage Support (AWS S3, Firebase, etc.)**
- [ ] **Mobile Optimization Enhancements**

---

## 👤 User Roles & Access

| Feature              | Guest (No Login) | Logged-in User |
|----------------------|------------------|-----------------|
| Remove Background    | ✅               | ✅              |
| Image Editing Tools  | ❌               | ✅              |
| View Gallery         | ❌               | ✅              |
| Download Image       | ✅               | ✅              |


## 🔐 Usage

1. **Remove Background**  
   Upload an image and get a transparent background version instantly — no login required.

2. **Sign Up/Login**  
   Create an account to access editing and gallery features.

3. **Edit Image**  
   Crop, resize, rotate, or flip images as needed.

4. **View Gallery**  
   See all your uploaded/edited images in one place.

5. **Download Images**  
   Save processed images in a single click.

---

## 🧑‍💻 Contributing

We welcome contributions! Follow these steps:

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for more details.

---

## 🌟 Acknowledgements

- [rembg](https://github.com/danielgatis/rembg) - AI-powered background remover.
- [Streamlit](https://streamlit.io/) - Framework for rapid web apps in Python.
- [Pillow](https://python-pillow.org/) - Python Imaging Library.

---

## 📬 Contact

Have a question or suggestion? Feel free to open an [issue](https://github.com/ravikant-diwakar/InstaBGRemover/issues) or reach out via [email](mailto:youremail@example.com).

---


