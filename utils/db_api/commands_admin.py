from loader import db
from utils.db_api.schemas.user import User






async def all_register_users():
    users = await User.query.where(User.status_register == True).gino.all()
    return users

async def count_users():
    total = await db.func.count(User.id).gino.scalar()
    return total