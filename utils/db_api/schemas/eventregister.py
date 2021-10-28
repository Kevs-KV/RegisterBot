from sqlalchemy import Column, String, Integer, LargeBinary, sql


class EventRegister:
    __tablename__ = 'event'

    id = Column(Integer, primary_key=True)
    title_event = Column(String())
    content = Column(String())
    image = Column(LargeBinary, nullable = False)


    query: sql.Select