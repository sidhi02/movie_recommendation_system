from flask import Flask, render_template, request
from recommendation import recommend_movies

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    movies = []
    search_name = ""

    if request.method == "POST":
        search_name = request.form["movie"]
        movies = recommend_movies(search_name)

        print("Search:", search_name)
        print("Movies:", movies[:2])

    return render_template(
        "index.html",
        movies=movies,
        search_name=search_name
    )

if __name__ == "__main__":
    app.run(debug=True)