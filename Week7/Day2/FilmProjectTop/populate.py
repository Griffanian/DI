import os, django,random,radar
# from faker import Faker



os.environ.setdefault('DJANGO_SETTINGS_MODULE', "FilmProject.settings")
django.setup()

from films.models import Film,Director,Country,Category

movies = ["The Godfather", "The Shawshank Redemption", "The Dark Knight", "Forrest Gump", "The Matrix", "Pulp Fiction", "Star Wars: Episode IV - A New Hope", "Goodfellas", "The Silence of the Lambs", "Fight Club", "The Lord of the Rings: The Fellowship of the Ring", "Jurassic Park", "The Lion King", "Titanic", "Jaws", "The Terminator", "Back to the Future", "Raiders of the Lost Ark", "The Exorcist", "Saving Private Ryan", "Gladiator", "The Green Mile", "Alien", "The Shining", "Blade Runner", "Apocalypse Now", "The Departed", "One Flew Over the Cuckoo's Nest", "The Usual Suspects", "The Prestige", "American History X", "A Clockwork Orange", "No Country for Old Men", "The Good, the Bad and the Ugly", "Terminator 2: Judgment Day", "The Silence of the Lambs", "Eternal Sunshine of the Spotless Mind", "The Big Lebowski", "The Graduate", "The Princess Bride", "Amélie", "The Breakfast Club", "Ferris Bueller's Day Off", "The Blues Brothers", "Monty Python and the Holy Grail", "Airplane!", "Annie Hall", "Casablanca", "Gone with the Wind", "Psycho", "Rear Window", "The Birds", "North by Northwest", "Vertigo", "Taxi Driver", "Good Will Hunting", "Rain Man", "The Social Network", "There Will Be Blood", "The Master", "The Grand Budapest Hotel", "Whiplash", "Birdman or (The Unexpected Virtue of Ignorance)", "La La Land", "The Revenant", "Moonlight", "The Shape of Water", "Inception", "Interstellar", "The Avengers", "Guardians of the Galaxy", "The Dark Knight Rises", "Harry Potter and the Philosopher's Stone", "The Hobbit: An Unexpected Journey", "The Hunger Games", "The Martian", "The Prestige", "Indiana Jones and the Last Crusade", "Die Hard", "The Bourne Identity", "Mission: Impossible", "Mad Max: Fury Road", "The Road", "The Book of Eli", "Django Unchained", "The Hateful Eight", "Reservoir Dogs", "Kill Bill: Vol. 1", "Kill Bill: Vol. 2", "Inglourious Basterds", "Dunkirk", "1917", "Saving Private Ryan", "Black Hawk Down", "American Sniper", "The Hurt Locker", "Platoon", "Full Metal Jacket", "Apocalypse Now", "Das Boot", "The Bridge on the River Kwai", "Lawrence of Arabia", "Patton", "Bridge of Spies", "The Spy Who Came in from the Cold"]


if __name__ == '__main__':

    print("Populating database")
    for i in range(99):
        available_in_countries = Country.objects.filter(id__in=random.sample(range(0, 99), 10))
        categories = Category.objects.all().filter(id__in=random.sample(range(0, 99), 5))
        director = Director.objects.all().filter(id__in=random.sample(range(0, 99), 3))
        film=Film.objects.create(title=movies[i], release_date=radar.random_datetime(),created_in_country=Country.objects.all().get(id=random.randint(0,99)))
    
        film.available_in_countries.add(*available_in_countries)
        film.category.add(*categories)
        film.director.add(*director)

    

        
