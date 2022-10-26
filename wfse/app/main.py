import uvicorn
from fastapi import FastAPI

from wfse.app.routes import index, fortune


def create_app():
    app = FastAPI()

    app.include_router(index.router)
    app.include_router(fortune.router, prefix='/fortune')

    return app


main_app = create_app()

if __name__ == '__main__':
    uvicorn.run('main:main_app', host='localhost', port=8000, reload=True)
