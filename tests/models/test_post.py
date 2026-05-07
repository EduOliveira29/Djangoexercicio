import pytest

from blog.models.factories import PostFactory

@pytest.fixture
def post_published():
    return PostFactory(title='pytest with factory')

@pytest.mark.django_db
def test_post_published(post_published):
    assert post_published.title == 'pytest with factory'