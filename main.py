import uvicorn

import src.routes.upload_route

from src.routes.app import app


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)