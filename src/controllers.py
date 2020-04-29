from fastapi import FastAPI
from starlette.templating import Jinja2Templates
from starlette.requests import Request

import db
from models import User, Task

app = FastAPI(
    title='FastAPI Webapplication',
    description='FastAPIチュートリアル: FastAPIでつくるWebアプリケーション',
    version='0.9 beta'
)


# templates設定
templates = Jinja2Templates(directory="templates")
jinja_env = templates.env # jinja2.Enviroment: filter, global設定


def index(request: Request):
    return templates.TemplateResponse('index.html',
                                      {'request': request}
                                      )


def admin(request: Request):
    # ユーザーとタスクを取得
    user = db.session.query(User).filter(User.username == 'admin').first()
    task = db.session.query(Task).filter(Task.user_id == user.id).all()
    db.session.close()

    return templates.TemplateResponse('admin.html',
                                      {'request': request,
                                       'user': user,
                                       'task': task})


@app.get('/get')
async def hello():
    return{"text": "hello world!"}


@app.get('/get/{path}')
async def path_and_query_params(
        path: str,
        query: int,
        default_none: str = None):
    return {"text": f"hello, {path}, {query} and {default_none}"}

