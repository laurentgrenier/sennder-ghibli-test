from back.services.tmdb_services import get_cover_path


def test_benchmark_get_cover_path():
    path = get_cover_path('Arrietty')
    assert len(path) != 0, "Should be defined"
