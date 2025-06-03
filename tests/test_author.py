


import pytest
from models.author import Author
from db.connection import get_connection

def test_create_author():
    """Test creating an author and retrieving their name."""
    author = Author.create("James")
    assert author.name == "James"

def test_find_author():
    """Test finding an author by ID."""
    author = Author.create("James")
    found = Author.find_by_id(author.id)
    assert found is not None
    assert found.name == "James"

def test_author_articles():
    """Test retrieving articles written by the author (should be empty initially)."""
    author = Author.create("James")
    articles = author.articles()
    assert isinstance(articles, list)
    assert len(articles) == 0  # No articles yet

def test_author_magazines():
    """Test retrieving magazines contributed to (should be empty initially)."""
    author = Author.create("James")
    magazines = author.magazines()
    assert isinstance(magazines, list)
    assert len(magazines) == 0  # No magazines yet

