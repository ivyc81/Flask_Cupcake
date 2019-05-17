from flask import Flask, request, jsonify, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake, DEFAULT_IMAGE_URL

app= Flask(__name__)
app.config['SECRET_KEY'] = 'oh-so-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

debug = DebugToolbarExtension(app)
connect_db(app)

@app.route('/')
def show_index():
    """ Shows all cupcakes and a new cupcake form """

    return render_template('index.html')

@app.route('/cupcakes/search')
def search_for_cupcake():
    """ takes in search type and term and returns a list of cupcake """

    search_type = request.args["type"]
    search_term = request.args["term"]

    cupcakes = Cupcake.query.filter(getattr(Cupcake, search_type).like(search_term))
    # cupcakes = db.session.query(Cupcake).filter(getattr(Cupcake,search_type) == search_term).all()
    # cupcakes = db.session.query(Cupcake).filter(Cupcake.flavor == 'chocolate')

    serialized_cupcakes = [{"id": cupcake.id,
                            "flavor": cupcake.flavor,
                            "size": cupcake.size,
                            "rating": cupcake.rating,
                            "image": cupcake.image}
                           for cupcake in cupcakes]

    return jsonify(response=serialized_cupcakes)


@app.route('/cupcakes')
def return_all_cupcakes():
    """ returns all cupcakes

        {response:[
            {"id": 1,
            "flavor": chocolate,
            "size": enormous,
            "rating": 5,
            "image": https://i.pinimg.com/236x/a4/8d/fc/a48dfc9b66a9ab500590832b940b3b10--icing-for-cupcakes-giant-cupcake-cakes.jpg?b=t}, ...
        ]}


    """

    cupcakes = Cupcake.query.all()

    serialized_cupcakes = [{"id": cupcake.id,
                            "flavor": cupcake.flavor,
                            "size": cupcake.size,
                            "rating": cupcake.rating,
                            "image": cupcake.image}
                           for cupcake in cupcakes]

    return jsonify(response=serialized_cupcakes)


@app.route('/cupcakes/<int:cupcake_id>')
def show_one_cupcake(cupcake_id):
    """ shows one cupcake """

    cupcake = Cupcake.query.get(cupcake_id)

    return render_template("cupcake.html", cupcake=cupcake)


@app.route('/cupcakes', methods=["POST"])
def create_cupcake():
    """ creates and returns new cupcake

    {response:
        {"id": 1,
        "flavor": chocolate,
        "size": enormous,
        "rating": 5,
        "image": https://i.pinimg.com/236x/a4/8d/fc/a48dfc9b66a9ab500590832b940b3b10--icing-for-cupcakes-giant-cupcake-cakes.jpg?b=t}
    }
    """

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    image = request.json["image"]

    new_cupcake = Cupcake(flavor=flavor,
                          size=size,
                          rating=rating,
                          image=image)
    db.session.add(new_cupcake)
    db.session.commit()

    serialized_cupcake = {"id": new_cupcake.id,
                          "flavor": new_cupcake.flavor,
                          "size": new_cupcake.size,
                          "rating": new_cupcake.rating,
                          "image": new_cupcake.image}

    return jsonify(response=serialized_cupcake)


@app.route('/cupcakes/<int:cupcake_id>', methods=["PATCH"])
def update_cupcake(cupcake_id):
    """ updates and returns updated cupcake

    {response:
        {"id": 1,
        "flavor": chocolate,
        "size": enormous,
        "rating": 5,
        "image": https://i.pinimg.com/236x/a4/8d/fc/a48dfc9b66a9ab500590832b940b3b10--icing-for-cupcakes-giant-cupcake-cakes.jpg?b=t}
    }
    """

    cupcake = Cupcake.query.get(cupcake_id)

    cupcake.flavor = request.json["flavor"]
    cupcake.size = request.json["size"]
    cupcake.rating = request.json["rating"]

    try:
        cupcake.image = request.json["image"]
    except KeyError:
        cupcake.image = DEFAULT_IMAGE_URL

    db.session.commit()

    updated_cupcake = {"id": cupcake.id,
                       "flavor": cupcake.flavor,
                       "size": cupcake.size,
                       "rating": cupcake.rating,
                       "image": cupcake.image}

    return jsonify(response=updated_cupcake)

@app.route('/cupcakes/<int:cupcake_id>', methods=["DELETE"])
def delete_cupcake(cupcake_id):
    """ Deletes cupcake

    {message: "Deleted"}
    """

    cupcake = Cupcake.query.get(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(message="Deleted")