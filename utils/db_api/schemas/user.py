

from sqlalchemy import Integer, Column, BigInteger, String, sql, Boolean

from utils.db_api.db_gino import TimedBaseModel




class User(TimedBaseModel):
    __tablename__ = 'users'

    id = Column(BigInteger, primary_key=True)
    fullname_tg = Column(String(100))
    name = Column(String(100))
    username = Column(String(100))
    country = Column(String(50))
    location = Column(String(500))
    age = Column(Integer)
    email = Column(String(100))
    phone = Column(String(20))
    language = Column(String(2))
    status_register = Column(Boolean, default=False)

    def __str__(self):
        return f'id: {self.id}, name: {self.name} {self.username}, {self.country}, возраст: {self.age}, email: {self.email}, телефон: {self.phone}'




    query: sql.Select
