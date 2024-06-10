from flask import Flask, request, jsonify
import psycopg2
from db_connections.connections import session

from model.table import Countries

app = Flask(__name__)


@app.route('/get_all_countries', methods=['GET'])
def get_countries():
    countries = session.query(Countries).all()
    countries_list = [
        {'id': country.id, 'name': country.name, 'capital': country.capital, 'population': country.population} for
        country in countries]
    return jsonify(countries_list)


@app.route('/add_countries', methods=['POST'])
def add_country():
    new_country_data = request.get_json()
    new_country = Countries(
        id=new_country_data['id'],
        name=new_country_data['name'],
        capital=new_country_data['capital'],
        population=new_country_data['population']
    )
    session.add(new_country)
    session.commit()
    return jsonify({"message": "Country added successfully"})


@app.route('/update_countries', methods=['PUT'])
def update_country():
    user_data = request.get_json()
    session.query(Countries).filter(Countries.id == user_data.get('id')).update(user_data)

    session.commit()

    return jsonify({"message": "Country updated successfully"})


@app.route('/delete_countries', methods=['DELETE'])
def delete_country():
    data = request.get_json()
    session.query(Countries).filter(Countries.id == data.get('id')).delete()
    session.commit()
    return jsonify({"message": "Country deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)
