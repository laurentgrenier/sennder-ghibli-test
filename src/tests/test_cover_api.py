def test_cover_api(client):
    response = client.get('/cover/Castle in the Sky')
    assert response.status_code == 200,  "API call must be successful"
