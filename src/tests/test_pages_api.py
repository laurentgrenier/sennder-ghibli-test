def test_page_movies(client):
    response = client.get('/movies')
    assert response.status_code == 200, "HTML page should be loaded"
