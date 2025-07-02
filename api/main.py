from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .utils.init_sql_alchemy import create_tables_for_sqlalchemy
from .router.api import router

# Main application entry point for the FastAPI application
app = FastAPI()

# Initialize the database tables using SQLAlchemy
create_tables_for_sqlalchemy()

# To allow CORS requests from frontend application
origins = ["http://localhost:8080"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      # List of allowed origins
    allow_credentials=False,    # Allow cookies to be sent with requests
    allow_methods=["*"],        # Allow all HTTP methods
    allow_headers=["*"]         # Allow all headers
)

# Include the API router
app.include_router(router)