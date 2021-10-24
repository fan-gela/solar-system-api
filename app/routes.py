# from flask import Blueprint, jsonify

# class SolarSystem:
#     def __init__(self, id, planet_name, description):
#         self.id = id
#         self.planet_name = planet_name
#         self.description = description

# planets = [
#     SolarSystem(1, "Mars", "empty burnt hole"),
#     SolarSystem(2, "Jupiter", "put a ring on it"),
#     SolarSystem(3, "Earth", "gross"),
#     SolarSystem(4, "Saturn", "give me more rings"),
#     SolarSystem(5, "Uranus", "no comment"),
#     SolarSystem(6, "Neptune", "water god"),
#     SolarSystem(7, "Venus", "williams - tennis star"),
#     SolarSystem(8, "Mercury", "killer, no comment"),
#     SolarSystem(9, "Pluto", "I AM TINY PLANET")
# ]

# planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

# @planets_bp.route("", methods=["GET"])
# def find_all_planets():
#     all_planets = []
#     for planet in planets:
#         all_planets.append({
#             "id": planet.id,
#             "planet_name": planet.planet_name,
#             "description": planet.description
#         })
#     return jsonify(all_planets)

# @planets_bp.route("/<planet_id>", methods=["GET"])
# def specific_planet(planet_id):
#     planet_id = int(planet_id)
#     for planet in planets:
#         if planet.id == planet_id:
#             return {
#                 "id": planet.id,
#                 "planet_name": planet.planet_name,
#                 "description": planet.description
#             }


from app import db
from app.planet import Planet
from flask import Blueprint, jsonify, make_response, request

planets_bp = Blueprint("planets", __name__, url_prefix = "/planets")

@planets_bp.route("", methods = ["GET", "POST"])
def all_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "planet_name": planet.planet_name,
                "description": planet.description,
                "density": planet.density
            })
        return jsonify(planets_response)

    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(planet_name = request_body["planet_name"],
                            description = request_body["description"],
                            density = request_body["density"])
        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.planet_name} successfully created", 201)

@planets_bp.route("/<planet_id>", methods = ["GET"])
def one_planet(planet_id):
    planet = Planet.query.get(planet_id)

    return {
        "id": planet.id,
        "planet_name": planet.planet_name,
        "description": planet.description,
        "density": planet.density
    }