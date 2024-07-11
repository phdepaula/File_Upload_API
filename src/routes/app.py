from fastapi import FastAPI
from fastapi.openapi.models import Tag


class App(FastAPI):
    "Class to generate fast api app."

    API_TITLE = "File Upload API"
    VERSION = "1.0.0"
    DESCRIPTION = "API created to upload file."
    OPEN_API_JSON_URL = "/swagger/openapi.json"
    SWAGGER_URL = "/swagger"

    def __init__(self):
        super().__init__(
            title=self.API_TITLE,
            description=self.DESCRIPTION,
            version=self.VERSION,
            openapi_url=self.OPEN_API_JSON_URL,
            docs_url=self.SWAGGER_URL,
        )
        Tag(
            name="Documentation",
            description="Documentation selection: Swagger.",
        )
        Tag(
            name="Email",
            description="Email Sender Route.",
        )
        Tag(
            name="Upload",
            description="Upload route.",
        )


app = App()
