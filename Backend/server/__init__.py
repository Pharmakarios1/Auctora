"""
Copyright (c) 12/2024 - iyanuajimobi12@gmail.com
"""

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from server.config import app_configs, init_db
from server.controllers import router
from server.middlewares.exception_handler import (
    ExcRaiser,
    RequestValidationError,
    HTTPException,
    request_validation_error_handler,
    HTTP_error_handler,
    exception_handler,
)


def create_app(app_name: str = 'temporary') -> FastAPI:
    """
    The create_app function is the entry point for our application.
    """

    # inject global dependencies
    app = FastAPI(
        title=app_configs.APP_NAME.capitalize(),
        description=f"{app_configs.APP_NAME.capitalize()}'s Api Documentation",
        docs_url=app_configs.SWAGGER_DOCS_URL,
        redoc_url=app_configs.SWAGGER_DOCS_URL+'2',
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=app_configs.CORS_ALLOWED,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/", include_in_schema=False)
    def redirect():
        return RedirectResponse(url=app_configs.SWAGGER_DOCS_URL, status_code=302)
    
    app.exception_handlers = {
        ExcRaiser: exception_handler,
        RequestValidationError: request_validation_error_handler,
        HTTPException: HTTP_error_handler
    }
    app.include_router(router)
    init_db()
    return app
