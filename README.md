# 🕵️‍♂️ Image Steganography using Django

A web-based Image Steganography application that allows users to **hide (encode) and retrieve (decode) secret messages inside images** without visibly changing the image. Built using **Django, Pillow, Stepic, HTML, CSS, JavaScript, and Python**.

---

## 🚀 Features

* 🔐 Hide text messages in PNG,JPG images using steganography.
* 🕵️ Extract hidden messages from images.
* 📂 Upload and download encoded images.
* 🧰 Simple and clean web UI using HTML/CSS/JS.
* 🧠 Uses LSB (Least Significant Bit) encoding via `stepic`.

---

## 🛠️ Technologies Used

* **Backend**: Django (Python)
* **Frontend**: HTML, CSS, JavaScript
* **Image Processing**: Pillow, Stepic

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/image-steganography-django.git
cd stagno_app
```

### 2️⃣ Set up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Required Packages

```bash
pip install django pillow stepic
```

Alternatively, use:

```bash
pip install -r requirements.txt
```

#### Example `requirements.txt`

```
Django>=4.0
pillow
stepic
```

### 4️⃣ Run the Server

```bash
python manage.py migrate
python manage.py runserver
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## 🧠 How It Works

* **Encoding**: User uploads an image + enters a message → message is encoded into the image using Stepic (LSB).
* **Decoding**: User uploads a previously encoded image → app extracts the hidden message.

---

## 📂 Project Structure

```
image-steganography-django/
├── stego_app/
│   ├── templates/
│   │   ├── index.html
│   ├── static/
│   │   ├── style.css
│   ├── views.py
│   ├── urls.py
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🖼️ Sample Screenshots
![Screenshot 2025-04-23 221438](https://github.com/user-attachments/assets/bb143984-021e-4475-84c4-df5b053a2dae)
![Screenshot 2025-04-23 221517](https://github.com/user-attachments/assets/4e176764-e931-466a-b48d-61a28a535061)
![Screenshot 2025-04-23 221619](https://github.com/user-attachments/assets/421861d7-525f-419d-b18c-9d4bc7afdb29)
![Screenshot 2025-04-23 221812](https://github.com/user-attachments/assets/532274bd-6435-4ab6-8aea-7deca524934f)
![Screenshot 2025-04-23 222032](https://github.com/user-attachments/assets/c38492f7-7045-4bd5-b7b4-e24c1fe7a8ba)
