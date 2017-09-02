import fresh_tomatoes

data = {
	'6': {
		'type': 'movie',
		'title': 'The Shawshank Redemption',
		'movie_storyline': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
		'poster_image_url': 'https://images-na.ssl-images-amazon.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SY1000_CR0,0,672,1000_AL_.jpg',
		'trailer_youtube_url': 'https://www.youtube.com/watch?v=6hB3S9bIaco'
	},
	'1': {
		'type': 'movie',
		'title': 'The Godfather',
		'movie_storyline': 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
		'poster_image_url': 'https://images-na.ssl-images-amazon.com/images/M/MV5BZTRmNjQ1ZDYtNDgzMy00OGE0LWE4N2YtNTkzNWQ5ZDhlNGJmL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,704,1000_AL_.jpg',
		'trailer_youtube_url': 'https://www.youtube.com/watch?v=5DO-nDW43Ik'
	},
	'2': {
		'type': 'movie',
		'title': 'The Dark Knight',
		'movie_storyline': 'When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham, the Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.',
		'poster_image_url': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg',
		'trailer_youtube_url': 'https://www.youtube.com/watch?v=ria7Ug8M_fo'
	},
	'3': {
		'type': 'movie',
		'title': '12 Angry Men',
		'movie_storyline': 'A jury holdout attempts to prevent a miscarriage of justice by forcing his colleagues to reconsider the evidence.',
		'poster_image_url': 'https://images-na.ssl-images-amazon.com/images/M/MV5BODQwOTc5MDM2N15BMl5BanBnXkFtZTcwODQxNTEzNA@@._V1_SY1000_CR0,0,666,1000_AL_.jpg',
		'trailer_youtube_url': 'https://www.youtube.com/watch?v=Dosg0p7LAB4'
	},
	'4': {
		'type': 'movie',
		'title': 'Schindlers List',
		'movie_storyline': 'In German-occupied Poland during World War II, Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazi Germans.',
		'poster_image_url': 'https://images-na.ssl-images-amazon.com/images/M/MV5BNDE4OTMxMTctNmRhYy00NWE2LTg3YzItYTk3M2UwOTU5Njg4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,666,1000_AL_.jpg',
		'trailer_youtube_url': 'https://www.youtube.com/watch?v=M5FpB6qDGAE'
	},
	'5': {
		'type': 'movie',
		'title': 'Pulp Fiction',
		'movie_storyline': 'The lives of two mob hit men, a boxer, a gangsters wife, and a pair of diner bandits intertwine in four tales of violence and redemption.',
		'poster_image_url': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5MDc3NjE@._V1_SY1000_CR0,0,673,1000_AL_.jpg',
		'trailer_youtube_url': 'https://www.youtube.com/watch?v=ewlwcEBTvcg'
	},
    '7': {
        'type': 'shows',
        'title': 'Band of Brothers',
        'seasons': '1',
        'poster_image_url': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTI3ODc2ODc0M15BMl5BanBnXkFtZTYwMjgzNjc3._V1_.jpg',
        'trailer_youtube_url': 'https://www.youtube.com/watch?v=kyDkHvi9yeI'
    }
}

fresh_tomatoes.open_movies_page(data)
