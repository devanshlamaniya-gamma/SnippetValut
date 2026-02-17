from pydantic import BaseModel  


class CreateSnippet(BaseModel):


    title = str
    code = str
    language = str