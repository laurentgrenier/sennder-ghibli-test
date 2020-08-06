from back.services.ghibli_services import get_people, get_movies, get_films


def test_benchmark_get_people(benchmark):
    people = benchmark(get_people)
    assert len(people) > 20, "Should be more than 20"


def test_benchmark_get_films(benchmark):
    films = benchmark(get_films)
    assert len(films) > 10, "Should be more than 10"


def test_benchmark_get_movies(benchmark):
    movies = benchmark(get_movies)
    assert len(movies) > 10, "Should be more than 10"

