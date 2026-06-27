<div align="center">

# 🎬 Your Next Binge

</div>

<div align="center">

## Discover your next favorite movie through intelligent recommendations.

**A content-based movie recommendation web application that leverages Machine Learning to suggest movies you'll love.**

<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy)
[![Live Demo](https://img.shields.io/badge/Live-Demo-red?style=for-the-badge)](https://your-next-binge.onrender.com)

</div>

---

# 🌟 Overview

**Your Next Binge** is a premium movie recommendation web application that helps users discover movies similar to their favorites using **Content-Based Filtering**.

The recommendation engine analyzes movie metadata and computes similarity using **CountVectorizer** and **Cosine Similarity**, delivering accurate and personalized movie suggestions.

To enhance the user experience, the application integrates the **TMDb API** to fetch real-time movie posters, ratings, and release years, all presented through a modern cinematic user interface.

---

# ✨ Features

- 🎬 Content-Based Movie Recommendation Engine
- 🔍 Search movies by title
- 🤖 Machine Learning-powered recommendations
- 🎥 Live movie posters from TMDb API
- ⭐ Movie ratings
- 📅 Release year
- ⚡ Instant recommendations using Cosine Similarity
- 🎨 Premium Netflix-inspired UI
- 🌑 Cinematic dark theme
- 📱 Responsive design
- ✨ Smooth animations & hover effects

---

# 📸 Screenshots

## 🏠 Home Page

> Add your homepage screenshot here.

<p align="center">
<img src="/movie_recommendation/static/images/home.png" width="900">
</p>

---

## 🎬 Recommendations

> Add your recommendations screenshot here.

<p align="center">
<img src="/movie_recommendation/static/images/recommendations.png" width="900">
</p>

---

# 🚀 Live Demo

[Launch Your Next Binge](https://your-next-binge.onrender.com)

---

# 🛠️ Tech Stack

| Category | Technologies |
|-----------|--------------|
| **Frontend** | HTML5, CSS3, Jinja2 |
| **Backend** | Python, Flask |
| **Machine Learning** | Pandas, NumPy, Scikit-learn |
| **Recommendation Algorithm** | CountVectorizer, Cosine Similarity |
| **Movie Data** | TMDb API |

---

# 📂 Project Structure

```text
movie_recommendation/
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│       └── bg.jpg
│
├── templates/
│   └── index.html
│
├── app.py
├── recommendation.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/sidhi02/your-next-binge.git
```

### 2️⃣ Navigate to the project

```bash
cd your-next-binge
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
python app.py
```

### 5️⃣ Open your browser

```text
http://127.0.0.1:5000
```

---

# 🧠 How It Works

1. **Enter a movie title** in the search bar.
2. The application locates the selected movie in the dataset.
3. Movie metadata is transformed into feature vectors using **CountVectorizer**.
4. **Cosine Similarity** computes similarity scores between movies.
5. The top matching movies are selected.
6. The **TMDb API** retrieves posters, ratings, and release years.
7. Personalized recommendations are displayed instantly.

---

# 📊 Machine Learning Workflow

```text
Movie Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Feature Engineering
      │
      ▼
CountVectorizer
      │
      ▼
Cosine Similarity Matrix
      │
      ▼
Recommendation Engine
      │
      ▼
Flask Web Application
```

---

# 🎯 Recommendation Pipeline

```text
Movie Name
     │
     ▼
Locate Movie Index
     │
     ▼
Cosine Similarity
     │
     ▼
Top Similar Movies
     │
     ▼
TMDb API
     │
     ▼
Movie Posters • Ratings • Release Year
     │
     ▼
Display Recommendations
```

---

# 🚀 Future Enhancements

- 🔐 User Authentication
- ❤️ Personal Watchlist
- 🎬 Movie Trailers
- 🎭 Genre & Language Filters
- 🔎 Search Autocomplete
- 🤖 AI-powered Personalized Recommendations
- 🎤 Voice Search
- 📺 Streaming Platform Availability
- 🌙 Light/Dark Theme Toggle
- ☁️ Cloud Deployment

---

# 📚 Dataset

The recommendation engine is trained on movie metadata containing information such as genres, keywords, cast, crew, and movie overviews. These features are processed into vector representations to compute similarity between movies.

---

# Acknowledgements

- TMDb API
- Flask
- Scikit-learn
- Pandas
- NumPy
- Python

---

# 👨‍💻 Author

**Sidhi Deshmukh**

*Aspiring Data Scientist | Machine Learning Enthusiast | Python Developer*

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a Star!

</div>
