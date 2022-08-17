from app.main import app, db_create

if __name__ == "__main__":
    db_create()
    print(db_create)
    app.run(threaded=True, port=5000)