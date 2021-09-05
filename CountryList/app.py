from flask import Flask,redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy
import json

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dataB.db'
db = SQLAlchemy(app)

class Country(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(80), nullable=False)

class City(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(80), nullable=False)
  country_id = db.Column(db.Integer, db.ForeignKey('country.id'), nullable=False)

# f = open("data.json","r")
# data = json.loads(f.read())

# countries = []

# for i in data:
#   countries.append(i)

# for i in countries:
#   country = Country(name=i)
#   db.session.add(country)
#   db.session.commit()

# x=0
# while x<len(countries):
#   for y in data[countries[x]]:
#     city = City(name=y,country_id=x)
#     db.session.add(city)
#     db.session.commit()
#   x+=1

@app.route("/")
def index():
  countryy = Country.query.all()
  return render_template("index.html", countryy=countryy)

@app.route("/<int:country_id>")
def cities(country_id):
  cityy = City.query.filter_by(country_id = country_id-1)
  return render_template("index.html",cityy=cityy)

  

if __name__ == '__main__':
  app.run(debug=True)