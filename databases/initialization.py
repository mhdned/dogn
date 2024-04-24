# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# from configs.config import config

# # Create the database engine
# engine = create_engine(config["DATABASE_URL"])

# # Bind the engine to the Base class
# BaseModels.metadata.bind = engine

# # Create a session factory
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Create the tables
# BaseModels.metadata.create_all(engine)
