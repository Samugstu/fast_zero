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
