import uvicorn
from urls import app

if __name__ == '__main__':
    # cmdで　$ uvicorn run:app --reload
    uvicorn.run(app=app)  # port=8000)

