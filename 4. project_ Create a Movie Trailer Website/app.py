import fresh_tomatoes
import media

the_shawshank_redemption = media.Movie(
	'The Shawshank Redemption',
	'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
	'https://images-na.ssl-images-amazon.com/images/M/MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SY1000_CR0,0,672,1000_AL_.jpg',
	'https://www.youtube.com/watch?v=6hB3S9bIaco'
)

the_godfather = media.Movie(
	'The Godfather',
	'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
	'https://images-na.ssl-images-amazon.com/images/M/MV5BZTRmNjQ1ZDYtNDgzMy00OGE0LWE4N2YtNTkzNWQ5ZDhlNGJmL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,704,1000_AL_.jpg',
	'https://www.youtube.com/watch?v=5DO-nDW43Ik'
)

the_dark_knight = media.Movie(
	'The Dark Knight',
	'When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham, the Dark Knight must accept one of the greatest psychological and physical tests of his ability to fight injustice.',
	'https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg',
	'https://www.youtube.com/watch?v=ria7Ug8M_fo'
)

angry_men = media.Movie(
	'12 Angry Men',
	'A jury holdout attempts to prevent a miscarriage of justice by forcing his colleagues to reconsider the evidence.',
	'https://images-na.ssl-images-amazon.com/images/M/MV5BODQwOTc5MDM2N15BMl5BanBnXkFtZTcwODQxNTEzNA@@._V1_SY1000_CR0,0,666,1000_AL_.jpg',
	'https://www.youtube.com/watch?v=Dosg0p7LAB4'
)

schindlers_list = media.Movie(
	'Schindlers List',
	'In German-occupied Poland during World War II, Oskar Schindler gradually becomes concerned for his Jewish workforce after witnessing their persecution by the Nazi Germans.',
	'https://images-na.ssl-images-amazon.com/images/M/MV5BNDE4OTMxMTctNmRhYy00NWE2LTg3YzItYTk3M2UwOTU5Njg4XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,666,1000_AL_.jpg',
	'https://www.youtube.com/watch?v=M5FpB6qDGAE'
)

pulp_fiction = media.Movie(
	'Pulp Fiction',
	'The lives of two mob hit men, a boxer, a gangsters wife, and a pair of diner bandits intertwine in four tales of violence and redemption.',
	'https://images-na.ssl-images-amazon.com/images/M/MV5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5MDc3NjE@._V1_SY1000_CR0,0,673,1000_AL_.jpg',
	'https://www.youtube.com/watch?v=ewlwcEBTvcg'
)

movies = [the_shawshank_redemption, the_godfather, the_dark_knight, angry_men, schindlers_list, pulp_fiction]

fresh_tomatoes.open_movies_page(movies)
