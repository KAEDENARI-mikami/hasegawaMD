from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Member
from schemas import MemberOut

router = APIRouter(prefix="/api/members", tags=["members"])


@router.get("/", response_model=list[MemberOut])
def list_members(db: Session = Depends(get_db)):
    return db.query(Member).order_by(Member.id).all()


@router.get("/{member_id}", response_model=MemberOut)
def get_member(member_id: int, db: Session = Depends(get_db)):
    member = db.query(Member).filter(Member.id == member_id).first()
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member
