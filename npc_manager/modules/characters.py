from flask import Blueprint, jsonify, request
from npc_manager.database import db
from npc_manager.models.character import Character

blueprint = Blueprint('characters', __name__)

@blueprint.route('/characters', methods=['GET'])
def get_characters():
    characters = Character.query.all()
    character_list = []
    for character in characters:
        character_data = {
            'id': character.id,
            'name': character.name,
            'class_type': character.class_type,
            'race': character.race,
            'information': character.information,
        }
        character_list.append(character_data)
        
    return jsonify(character_list)


@blueprint.route('/characters', methods=['POST'])
def create_character():
    data = request.get_json()
    name = data.get('name')
    user_id = data.get('user_id')
    class_type = data.get('class_type')
    race = data.get('race')
    information = data.get('information')

    # Check if character already exists (assuming name + user_id makes the character unique)
    existing_character = Character.query.filter_by(name=name, user_id=user_id).first()

    if existing_character:
        return jsonify({"error": "Character already exists"}), 400

    # Create new character if it doesn't exist
    character = Character(
        name=name, 
        user_id=user_id, 
        class_type=class_type, 
        race=race, 
        information=information
    )

    try:
        db.session.add(character)
        db.session.commit()
        return jsonify({
            "message": "Character created successfully", 
            "character": character.to_dict()
        }), 201
    except Exception as e:
        db.session.rollback()  # Rollback the transaction in case of error
        return jsonify({"error": "Character creation failed", "details": str(e)}), 500
    
@blueprint.route('/characters/<int:character_id>', methods=['DELETE'])
def delete_character(character_id):
    if Character.delete_character_by_id(character_id):
        return jsonify({"message": "Character deleted successfully"}), 200
    else:
        return jsonify({"error": "Character not found or deletion failed"}), 404

