import uvicorn
from fastapi import FastAPI
from dataclasses import asdict

from wfse.app.routes import index, fortune
from wfse.app.common import config
from wfse.app.database import conn


def create_app():
    c = config.conf()
    app = FastAPI()
    conf_dict = asdict(c)
    conn.db.init_app(app, **conf_dict)

    app.include_router(index.router)
    app.include_router(fortune.router, tags=['fortune'], prefix='/fortune')

    return app


main_app = create_app()

if __name__ == '__main__':
    uvicorn.run('main:main_app', host='localhost', port=8000, reload=True)
