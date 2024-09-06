from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.models.user import User
from app.db.session import get_db
from app.schemas.pets import PetCreate, PetResponse, PetUpdate
from app.services.auth_service import verify_token
from app.services.pets import PetService

router = APIRouter()

@router.post("/", response_model=PetResponse)
def create_pet(pet: PetCreate, db: Session = Depends(get_db), user: User = Depends(verify_token)):
    return PetService.create_pet(db, pet, user.id)

@router.get("/{pet_id}", response_model=PetResponse)
def get_pet(pet_id: str, db: Session = Depends(get_db), user: User = Depends(verify_token)):
    pet = PetService.get_pet(db, pet_id, user.id)

    if not pet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pet not found")
    return pet

@router.put("/{pet_id}", response_model=PetResponse)
def update_pet(pet_id: str, pet_update: PetUpdate, db: Session = Depends(get_db), user: User = Depends(verify_token)):
    pet = PetService.update_pet(db, pet_id, pet_update, user.id)
    if not pet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pet not found")
    return pet

@router.delete("/{pet_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pet(pet_id: str, db: Session = Depends(get_db), user: User = Depends(verify_token)):
    pet = PetService.delete_pet(db, pet_id, user.id)
    if not pet:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pet not found")
