import os

DB_NAME = os.getenv('POSTGRES_DB', 'nv_testcase')
DB_USER = os.getenv('POSTGRES_USER', 'postgres')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD', 'pgpass')
DB_HOST = os.getenv('POSTGRES_HOST', 'localhost')
DB_PORT = int(os.getenv('POSTGRES_PORT', 8000))

DB_PATH = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
