from app.main import app
from database import db_create

if __name__ == "__main__":
    db_create()
    app.run(threaded=True, port=5000)