from pydantic import BaseModel


class CreateSnippet(BaseModel):


    title : str
    language : str
    code : str