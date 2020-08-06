def test_benchmark_cover_api(client, benchmark):
    response = benchmark(client.get, '/cover/Castle in the Sky')
    assert response.status_code == 200,  "API call must be successful"
