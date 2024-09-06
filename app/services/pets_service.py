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
            if pet_update.model_dump().get("name") is not None:
                pet.name = pet_update.name
            if pet_update.model_dump().get("age") is not None:
                pet.age = pet_update.age
            if pet_update.model_dump().get("weight") is not None:
                pet.weight = pet_update.weight
            if pet_update.model_dump().get("species") is not None:
                pet.species = pet_update.species
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
