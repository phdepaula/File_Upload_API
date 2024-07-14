import uvicorn

import src.routes.documentation
import src.routes.upload
from src.routes.app import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
