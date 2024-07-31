from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olár mundo'}


def test_create_user(client):

    response = client.post('./users/', json={'username': 'testeuser', 'password': 'password', 'email': 'teste@teste.com', })

    assert response.status_code == HTTPStatus.CREATED

    assert response.json() == {
    'username': 'testeuser',
    'email': 'teste@teste.com',
    'id': 1
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {'users': [{
    'username': 'testeuser',
    'email': 'teste@teste.com',
    'id': 1
    }]}


def test_update_user(client):
    response = client.put('/users/1',
        json={
            'password':'123',
            'username': 'Samuca',
            'email': 'samu@gmail.com',
            'id': 1,
        })
    assert response.json() == {
        'username': 'Samuca',
        'email': 'samu@gmail.com',
        'id': 1,
    }

def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.json() == {'message': 'User deleted!'}