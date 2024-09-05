
def test_get_user_success(client):
    response = client.get("/users/1")
    data = response.json
    
    assert response.status_code == 200
    assert data['id'] == 1
    
def test_get_user_404(client):
    response = client.get("/users/10")
    
    assert response.status_code == 404