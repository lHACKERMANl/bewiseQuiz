from fastapi import FastAPI
from Common.settings import settings
from API import questionApi

def create_app():
    app = FastAPI(
        debug=settings.debug,
        title='Bewise'
    )
    
    app.include_router(questionApi.router)

    return app

