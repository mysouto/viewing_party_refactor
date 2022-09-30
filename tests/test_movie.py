import pytest
from viewing_party.movie import Movie

def test_1():
    # Arrange
    title = "It Came from the Stack Trace"
    genre = "Horror"
    rating = 3.5
    host = 'Amy'

    # Act
    Amy = Movie(title = title, genre = genre, rating = rating, host = host) 
    # Assert
    assert Amy.title == title
    assert Amy.rating == 3.5