from movies import movies_lib, compare_by_year, compare_alphabetically
import pytest

def test_compare_by_year():
    movies_sorted = sorted(movies_lib, key=compare_by_year)
    expected_output = [
        "The Intouchables", "Valkyrie", "Stardust", "Ratatouille",
        "City of God", "Memento", "The Shawshank Redemption",
        "Beetlejuice", "The Cotton Club", "Crocodile Dundee"
    ]
    assert [movie['title'] for movie in movies_sorted] == expected_output

def test_compare_alphabetically():
    movies_sorted = sorted(movies_lib, key=compare_alphabetically)
    expected_output = [
        "Beetlejuice", "City of God", "The Cotton Club", "Crocodile Dundee",
        "The Intouchables", "Memento", "Ratatouille", "The Shawshank Redemption",
        "Stardust", "Valkyrie"
    ]
    assert [movie['title'] for movie in movies_sorted] == expected_output
