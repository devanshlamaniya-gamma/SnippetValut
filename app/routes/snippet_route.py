import json

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.authentication.dependency import get_current_user
from app.databse.db import Base, get_db
from app.models.snippet_model import Snippet
from app.models.user_model import User
from app.schema.snippet_schema import CreateSnippet
from app.utilities.email_utility import send_mail
from app.utilities.redis_utility import redis_client

snippet = APIRouter(prefix="/snippets", tags=["Snippets"])


@snippet.post("/add_snippet")
def add_snippet(
    stp: CreateSnippet,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    print("this is user id", current_user)
    print("user_id", type(current_user))
    new_snippet = Snippet(
        owner_id=current_user.id, title=stp.title, language=stp.language, code=stp.code
    )

    to = current_user.email
    subject = "new snippet added successfully"
    body = f"new snippet is added successfully with : \n owner id : {new_snippet.owner_id} \n title: {new_snippet.title} \n language : {new_snippet.language} snippet : {new_snippet.code} "

    send_mail(to, subject, body)

    db.add(new_snippet)
    db.commit()
    db.refresh(new_snippet)

    redis_client.delete("get_all_snippets")

    return {"message": f"snippet successfully created in {new_snippet.owner_id}"}


@snippet.get("/get_all")
def get_all_snippets(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):

    cache_data = redis_client.get("get_all_snippets")
    if cache_data:
        return json.loads(cache_data)

    snippets = db.query(Snippet).filter(current_user.id == Snippet.owner_id).all()

    print(snippets)

    if snippets is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "snippets not found")

    redis_snippet = []

    for snip in snippets:
        redis_snippet.append(
            {
                "id": snip.id,
                "title": snip.title,
                "language": snip.language,
                "code": snip.code,
            }
        )

    redis_client.set("get_all_snippets", json.dumps(redis_snippet), ex=60)

    return snippets


@snippet.get("/snippet_id:{id}")
def get_snippet_by_id(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    snippet = db.query(Snippet).filter(Snippet.id == id).first()

    if snippet is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "snippet not found")

    return snippet


@snippet.delete("/delete_snippet_{id}")
def delete_snippet_by_id(
    id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    snippet = db.query(Snippet).filter(Snippet.id == id).first()

    if snippet is None:

        raise HTTPException(status.HTTP_404_NOT_FOUND, "snippet not found")

    to = current_user.email
    subject = "Alert : snippet deleted !"
    body = f"snippet deleted form your account : \: \n owner id : {snippet.owner_id} \n title: {snippet.title} \n language : {snippet.language} snippet : {snippet.code}  "

    send_mail(to, subject, body)

    db.delete(snippet)
    db.commit()

    return f"snippet deleted with id {snippet.id}"
