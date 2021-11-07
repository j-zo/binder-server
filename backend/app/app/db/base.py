# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.user import User  # noqa
from app.models.book import Book  # noqa
from app.models.review import Review  # noqa
from app.models.book import Genre  # noqa
from app.models.markedbook import MarkedBook  # noqa
