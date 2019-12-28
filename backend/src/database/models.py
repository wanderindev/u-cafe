import os
import sys
from sqlalchemy import Column, exc, Integer, String
from flask_sqlalchemy import SQLAlchemy
import json

database_filename = "database.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "sqlite:///{}".format(
    os.path.join(project_dir, database_filename)
)

db = SQLAlchemy()


def setup_db(app):
    """Bind a flask application and a SQLAlchemy service."""
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


def db_drop_and_create_all():
    """Drop the database tables and start fresh."""
    db.drop_all()
    db.create_all()


class Drink(db.Model):
    """A persistent drink entity, extends the base SQLAlchemy Model"""

    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    title = Column(String(80), unique=True)
    # A recipe is a json string with the following structure
    # [{'color': string, 'name':string, 'parts':number}]
    recipe = Column(String(180), nullable=False)

    def delete(self):
        """Delete a recipe from the database"""
        try:
            db.session.delete(self)
            db.session.commit()
        except exc.SQLAlchemyError as e:
            print(e)
            print(sys.exc_info())
            db.session.rollback()
            return {"error": True}
        finally:
            db.session.close()

    @classmethod
    def get_all(cls):
        """
        Return all drinks records ordered by id.

        :return: a list of Drink objects
        :type: list
        """
        return cls.query.order_by(cls.id).all()

    @classmethod
    def get_by_id(cls, _id):
        """
        Return the drink with the given id.

        :param _id: the drink id
        :type _id: int
        :return: a Drink object
        :type: Drink
        """
        return cls.query.filter(cls.id == _id).one_or_none()

    def insert(self):
        """Insert a new recipe into a database."""
        try:
            db.session.add(self)
            db.session.commit()
        except exc.SQLAlchemyError as e:
            print(e)
            print(sys.exc_info())
            db.session.rollback()
            return {"error": True}
        finally:
            db.session.close()

    def long(self):
        """
        Return a long form representation of a drink.

        :return: a drink representation
        :type: dict
        """
        return {
            "id": self.id,
            "title": self.title,
            "recipe": json.loads(self.recipe),
        }

    def short(self):
        """
        Return a short form representation of a drink.

        :return: a drink representation
        :type: dict
        """
        print(json.loads(self.recipe))
        short_recipe = [
            {"color": r["color"], "parts": r["parts"]}
            for r in json.loads(self.recipe)
        ]
        return {"id": self.id, "title": self.title, "recipe": short_recipe}

    @staticmethod
    def update():
        """Update a recipe in the database"""
        try:
            db.session.commit()
        except exc.SQLAlchemyError as e:
            print(e)
            print(sys.exc_info())
            db.session.rollback()
            return {"error": True}
        finally:
            db.session.close()

    def __repr__(self):
        return json.dumps(self.short())
