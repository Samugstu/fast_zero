from sqlalchemy import select
from fast_zero.models import User


def test_create_user(session):

    user = User(username='Samuel', password='segredo', email='samu@email.com')
    session.add(user)
    session.commit()
    result = session.scalar(select(User).where(User.id == 1))

    assert result.username == 'Samuel'
