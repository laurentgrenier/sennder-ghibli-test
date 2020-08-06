def test_benchmark_page_movies(client, benchmark):
    response = benchmark(client.get, '/movies')
    assert response.status_code == 200, "HTML page should be loaded"
