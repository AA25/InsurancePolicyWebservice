from ..config.database import Base, engine

def create_tables_for_sqlalchemy():
    """
    Base.metadata.create_all(bind=engine) creates any missing tables from scratch based on your
    SQLAlchemy model definitions. It looks at all the Base-derived classes it's aware of and
    issues CREATE TABLE statements for them.

    Not needed, however initial API request will trigger this via lazy loading, making that request slower.
    Therefore, leaving it in
    """

    Base.metadata.create_all(bind=engine)
    print("Base.metadata.create_all(bind=engine) successfully run")