from sanic_aioorm import AioOrm, AioModel
from peewee import Proxy, CharField
db = Proxy()


@AioOrm.regist
class User(AioModel):
    username = CharField()

    class Meta:
        database = db
