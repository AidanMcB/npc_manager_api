from npc_manager.database import db
from npc_manager.models.user import User

class Character(db.Model):
    __tablename__ = 'character'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)   
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(), nullable=False)
    class_type = db.Column(db.String(), nullable=False)
    race = db.Column(db.String(), nullable=False)
    information = db.Column(db.ARRAY(db.String()))  # Ensure your DB supports arrays

    def __init__(self, user_id, name, class_type, race, information):
        self.user_id = user_id
        self.name = name
        self.class_type = class_type
        self.race = race
        self.information = information
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'class_type': self.class_type,
            'race': self.race, 
            'information': self.information,   
        }
        
    def add_character(self):        
        db_character = Character.query.filter(Character.name == self.name).all()
        if not db_character:
            db.session.add(self)
            db.session.commit()
        
        return True

    def get_user_characters(user_id):
        records = Character.query.filter_by(user_id=user_id).all()
        return [record.to_dict() for record in records]

    # Method to delete a character by ID
    @staticmethod
    def delete_character_by_id(character_id):
        character = Character.query.get(character_id)  # Retrieve the character by ID
        if character:
            try:
                db.session.delete(character)  # Delete the character from the session
                db.session.commit()           # Commit the changes to the database
                return True
            except Exception as e:
                db.session.rollback()         # Rollback in case of an error
                return False
        return False  # Return False if no character is found        

    def __repr__(self):
        return f"<Character {self.name}>"
