### Backend API

Backend API that provides RESTful endpoints using `FastAPI`
* Uses `Pydantic` for data modelling and validation
* Uses `SQLalchemy` for ORM

Project follows a Controller, Service & Repository patterns
* Requests get routered to the appropriate controller to handle request
* Controller uses the appropriate service method to do business logic
* Service uses the Repository for database interactions

### DB

* See `entities` folder individual table schemas
* A SQL script is run on start up to create tables with mock data, `init.sql`