# 🎬 Your Next Binge

A sleek, Netflix-inspired movie recommendation web application that helps users discover movies similar to their favorites using Machine Learning.

---

## ✨ Features

- 🔍 Search any movie by title
- 🤖 Content-Based Movie Recommendation System
- 🎥 High-quality movie posters from TMDb API
- ⭐ IMDb-style movie ratings
- 📅 Release year for every recommendation
- ⚡ Fast recommendations powered by cosine similarity
- 🎨 Premium Netflix-inspired responsive UI
- 🌑 Cinematic dark theme with modern animations

---

## 📸 Preview

> Add screenshots of your homepage and recommendations here.

| Home | Recommendations |
|------|-----------------|
| ![Home](screenshots/home.png) | ![Results](screenshots/results.png) |

---

## 🛠️ Tech Stack

### Frontend
- HTML5
- CSS3
- Jinja2 Templates

### Backend
- Python
- Flask

### Machine Learning
- Pandas
- NumPy
- Scikit-learn
- CountVectorizer
- Cosine Similarity

### API
- TMDb (The Movie Database)

---

## 📂 Project Structure

```
movie_recommendation/
│
├── static/
│   ├── css/
│   └── images/
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

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/movie-recommendation-system.git
```

### Navigate to the project

```bash
cd movie-recommendation-system
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 🧠 How It Works

1. User enters a movie title.
2. The application finds the selected movie.
3. Cosine Similarity identifies the most similar movies.
4. Movie details are fetched using the TMDb API.
5. Recommendations are displayed with posters, ratings, and release year.

---

## 📊 Machine Learning Pipeline

- Data Cleaning
- Feature Engineering
- CountVectorizer
- Cosine Similarity Matrix
- Recommendation Engine
- Flask Deployment

---

## 🚀 Future Improvements

- User authentication
- Watchlist
- Movie trailers
- Genre filters
- Streaming platform availability
- AI-powered personalized recommendations
- Voice search
- Infinite scrolling
- Dark/Light theme toggle

---

## 📌 Dataset

Movie metadata used to train the recommendation engine.

---

## 🙏 Acknowledgements

- TMDb API
- Scikit-learn
- Flask
- Pandas
- NumPy

---

## 👨‍💻 Author

**Sidhi**

If you enjoyed this project, consider giving it a ⭐ on GitHub!
