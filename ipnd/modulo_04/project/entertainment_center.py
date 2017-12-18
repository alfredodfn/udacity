# coding=utf-8

import media
import fresh_tomatoes

pulp_fiction = media.Movie("Pulp Fiction",
            "https://upload.wikimedia.org/wikipedia/pt/8/82/Pulp_Fiction_cover.jpg",
            "https://www.youtube.com/watch?v=s7EdQ4FqbhY")


te_days_later = media.Movie("28 Days Later",
            "https://upload.wikimedia.org/wikipedia/pt/e/e4/28_days_later.jpg",
            "https://www.youtube.com/watch?v=c7ynwAgQlDQ")


matrix = media.Movie("Matrix",
            "https://upload.wikimedia.org/wikipedia/pt/c/c1/The_Matrix_Poster.jpg",
            "https://www.youtube.com/watch?v=m8e-FF8MsqU")


the_godfather = media.Movie("The Godfather",
            "https://upload.wikimedia.org/wikipedia/pt/7/71/Chef%C3%A3o.jpg",
            "https://www.youtube.com/watch?v=sY1S34973zA")

lord_of_the_rings_iii = media.Movie("The Lord of the Rings: The Return of the King",
            "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg",
            "https://www.youtube.com/watch?v=r5X-hFf6Bwo")

star_wars_v = media.Movie("Star Wars: Episode V – The Empire Strikes Back",
            "https://upload.wikimedia.org/wikipedia/pt/5/5c/The_Empire_Strikes_Back.jpg",
            "https://www.youtube.com/watch?v=JNwNXF9Y6kY")

movies = [pulp_fiction,te_days_later,matrix,the_godfather,lord_of_the_rings_iii,star_wars_v]
fresh_tomatoes.open_movies_page(movies)
