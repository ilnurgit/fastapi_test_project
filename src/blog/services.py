from uuid import uuid4

from blog.domains import Article, User
from blog.repositories import ArticleRepository, UserRepository


def get_articles(articles_repository: ArticleRepository) -> list[Article]:
    return articles_repository.get_articles()


def create_article(title: str, content: str, articles_repository: ArticleRepository) -> Article:
    article = Article(id=str(uuid4()), title=title, content=content)
    articles_repository.create_article(article=article)
    return article


def login(username: str, password: str, users_repository: UserRepository) -> User | None:
    users = users_repository.get_users(username=username, password=password)
    if users:
        return users[0]
    return None
