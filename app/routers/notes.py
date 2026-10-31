
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import models, schemas
from ..deps import get_db, get_current_user

router = APIRouter(prefix="/notes", tags=["Notes"])


# CREATE NOTE
@router.post("/", response_model=schemas.NoteResponse, status_code=status.HTTP_201_CREATED)
def create_note(
    note: schemas.NoteCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    new_note = models.Note(
        title=note.title,
        content=note.content,
        user_id=current_user.id
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note


# GET ALL NOTES OF LOGGED-IN USER
@router.get("/", response_model=list[schemas.NoteResponse])
def get_notes(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return db.query(models.Note).filter(
        models.Note.user_id == current_user.id
    ).all()


# GET ONE NOTE
@router.get("/{note_id}", response_model=schemas.NoteResponse)
def get_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    note = db.query(models.Note).filter(
        models.Note.id == note_id,
        models.Note.user_id == current_user.id
    ).first()

    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")

    return note


# UPDATE NOTE
@router.put("/{note_id}", response_model=schemas.NoteResponse)
def update_note(
    note_id: int,
    updated_data: schemas.NoteUpdate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    note = db.query(models.Note).filter(
        models.Note.id == note_id,
        models.Note.user_id == current_user.id
    ).first()

    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")

    if updated_data.title is not None:
        note.title = updated_data.title

    if updated_data.content is not None:
        note.content = updated_data.content

    db.commit()
    db.refresh(note)

    return note


# DELETE NOTE
@router.delete("/{note_id}")
def delete_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    note = db.query(models.Note).filter(
        models.Note.id == note_id,
        models.Note.user_id == current_user.id
    ).first()

    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")

    db.delete(note)
    db.commit()

    return {"message": "Note deleted successfully"}
