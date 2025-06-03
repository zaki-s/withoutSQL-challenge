


import pytest
from models.author import Author
from models.magazine import Magazine
from models.article import Article

def test_create_author():
    """Test creating an author."""
    author = Author.create("James")
    assert author.name == "James"

def test_find_author():
    """Test finding an author by ID."""
    author = Author.create("James")
    found = Author.find_by_id(author.id)
    assert found is not None
    assert found.name == "James"

def test_create_magazine():
    """Test creating a magazine."""
    magazine = Magazine.create("Tech Monthly", "Technology")
    assert magazine.name == "Tech Monthly"
    assert magazine.category == "Technology"

def test_create_article():
    """Test creating an article."""
    author = Author.create("James")
    magazine = Magazine.create("Tech Monthly", "Technology")
    article = Article.create("AI Revolution", author.id, magazine.id)
    assert article.title == "AI Revolution"
