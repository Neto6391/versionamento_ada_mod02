from sqlalchemy.orm import Session
from app.db.models.pet import Pet
from app.schemas.pets import PetCreate, PetUpdate


class PetService:
    @staticmethod
    def create_pet(db: Session, pet: PetCreate, user_id: str):
        new_pet = Pet(
            **pet.model_dump(),
            owner_id=user_id
        )
        db.add(new_pet)
        db.commit()
        db.refresh(new_pet)
        return new_pet

    @staticmethod
    def get_pet(db: Session, pet_id: str, user_id: str):
        return db.query(Pet).filter(Pet.id == pet_id, Pet.owner_id == user_id).first()

    @staticmethod
    def update_pet(db: Session, pet_id: str, pet_update: PetUpdate, user_id: str):
        pet = PetService.get_pet(db, pet_id, user_id)
        if pet:
            for key, value in pet_update.model_dump().items():
                setattr(pet, key, value)
            db.commit()
            db.refresh(pet)
        return pet

    @staticmethod
    def delete_pet(db: Session, pet_id: str, user_id: str):
        pet = PetService.get_pet(db, pet_id, user_id)
        if pet:
            db.delete(pet)
            db.commit()
        return pet
