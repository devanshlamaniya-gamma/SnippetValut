from app.models.snippet_model import Snippet
from app.databse.db import get_db , Base 
from fastapi import Depends , APIRouter , HTTPException , status
from app.schema.snippet_schema import CreateSnippet
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.authentication.dependency import get_current_user

snippet = APIRouter(prefix="/snippets" , tags=["Snippets"])

@snippet.post("/add_snippet")
def add_snippet(stp : CreateSnippet , db : Session = Depends(get_db) , current_user : User = Depends(get_current_user)):
        
    print("this is user id",current_user)
    print("user_id",type(current_user))
    new_snippet = Snippet(
            owner_id = current_user.id,
            title = stp.title,
            language = stp.language,
            code = stp.code
        )

    db.add(new_snippet)
    db.commit()
    db.refresh(new_snippet)

    return {
        "message" : f"snippet successfully created in {new_snippet.owner_id}"
    }

@snippet.get("/get_all")
def get_all_snippets(db : Session = Depends(get_db) , current_user : User = Depends(get_current_user)):

    snippets = db.query(Snippet).filter(current_user.id == Snippet.owner_id).all()


    print(snippets)

    if snippets is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND , "snippets not found")

    

    return snippets



@snippet.get("/snippet_id:{id}")
def get_snippet_by_id(id:int , db : Session = Depends(get_db) , current_user : User = Depends(get_current_user)):



    snippet = db.query(Snippet).filter(Snippet.id == id).first()

    if snippet is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND , "snippet not found")

    return snippet


@snippet.delete("/delete_snippet_{id}")
def delete_snippet_by_id(id : int , db : Session = Depends(get_db) , current_user : User = Depends(get_current_user)):

    snippet = db.query(Snippet).filter(Snippet.id == id).first()

    if snippet is None:

        raise HTTPException(status.HTTP_404_NOT_FOUND , "snippet not found")
    
    db.delete(snippet)
    db.commit()

    return f"snippet deleted with id {snippet.id}"