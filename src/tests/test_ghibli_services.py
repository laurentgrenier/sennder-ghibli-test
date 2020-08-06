from back.services.ghibli_services import get_people, get_movies, get_films


def test_get_people():
    people = get_people()
    assert len(people) > 20, "Should be more than 20"


def test_benchmark_get_films():
    films = get_films()
    assert len(films) > 10, "Should be more than 10"


def test_get_movies():
    movies = get_movies()
    assert len(movies) > 10, "Should be more than 10"
