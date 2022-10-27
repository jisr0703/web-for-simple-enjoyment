from sqlalchemy import Column, BigInteger, DateTime, func, String, ForeignKey
from sqlalchemy.orm import Session

from wfse.app.database import conn


class BaseMixin:
    id = Column(BigInteger, primary_key=True, index=True)
    created_at = Column(DateTime, nullable=True, default=func.utc_timestamp())
    updated_at = Column(DateTime, nullable=True, default=func.utc_timestamp())

    def all_columns(self):
        return [c for c in self.__table__.columns if c.primary_key is False and c.name != 'created_at']

    def __hash__(self):
        return hash(self.id)

    @classmethod
    def create(cls, session: Session, auto_commit:bool = False, **kwargs):
        obj = cls()
        for col in obj.all_columns():
            col_name = col.name
            if col_name in kwargs:
                setattr(obj, col_name, kwargs.get(col_name))
        session.add(obj)
        session.flush()
        if auto_commit:
            session.commit()
        return obj

    @classmethod
    def get(cls, **kwargs):
        session = next(conn.db.session())
        query = session.query(cls)
        for key, val in kwargs.items():
            col = getattr(cls, key)
            query = query.filter(col == val)

            if query.count() > 1:
                raise Exception("Only one row is supposed to be returned, but got more than one.")
            return query.first()


class Feelings(conn.Base, BaseMixin):
    __tablename__ = 'feelings'
    feeling = Column(String(length=20), nullable=False)


class Feelings_log(conn.Base, BaseMixin):
    __tablename__ = 'feelings_log'
    ip = Column(String(length=50), nullable=False)
    feelings_id = Column(BigInteger, nullable=False, ForeignKey=True)
