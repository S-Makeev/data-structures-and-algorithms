def compare_by_year(movie):
    return -movie['year']

def remove_articles(title):
    articles = ['A ', 'An ', 'The ']
    for article in articles:
        if title.startswith(article):
            return title[len(article):]
    return title

def compare_alphabetically(movie):
    title = remove_articles(movie['title'].lower())
    return title


movies_lib = [
    {
        "title": "Beetlejuice",
        "year": 1988,
        "genres": ["Comedy", "Fantasy"],
    },
    {
        "title": "The Cotton Club",
        "year": 1984,
        "genres": ["Crime", "Drama", "Music"],
    },
    {
        "title": "The Shawshank Redemption",
        "year": 1994,
        "genres": ["Crime", "Drama"],
    },
    {
        "title": "Crocodile Dundee",
        "year": 1986,
        "genres": ["Adventure", "Comedy"],
    },
    {
        "title": "Valkyrie",
        "year": 2008,
        "genres": ["Drama", "History", "Thriller"],
    },
    {
        "title": "Ratatouille",
        "year": 2007,
        "genres": ["Animation", "Comedy", "Family"],
    },
    {
        "title": "City of God",
        "year": 2002,
        "genres": ["Crime", "Drama"],
    },
    {
        "title": "Memento",
        "year": 2000,
        "genres": ["Mystery", "Thriller"],
    },
    {
        "title": "The Intouchables",
        "year": 2011,
        "genres": ["Biography", "Comedy", "Drama"],
    },
    {
        "title": "Stardust",
        "year": 2007,
        "genres": ["Adventure", "Family", "Fantasy"],
    },
]
