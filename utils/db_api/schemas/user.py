

from sqlalchemy import Integer, Column, BigInteger, String, sql, Boolean

from utils.db_api.db_gino import TimedBaseModel




class User(TimedBaseModel):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True)
    fullname_tg = Column(String(100))
    name = Column(String(100))
    username = Column(String(100))
    email = Column(String(100))
    phone = Column(String(20))
    language = Column(String(2))
    status_register = Column(Boolean, default=False)

    def __repr__(self):
        return f'{[self.id, self.fullname_tg]}'




    query: sql.Select
