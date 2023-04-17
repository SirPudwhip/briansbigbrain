#!/usr/bin/env python3

from flask import Flask, request, make_response
from flask_migrate import Migrate
from models import db, BlogPost
from flask_restful import Resource, Api
import ipdb

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

class BlogPosts( Resource ):
    def get(self):
        posts = []
        for p in BlogPost.query.all():
            posts.append(p.to_dict())

        response = make_response(posts, 200)

        return response

api.add_resource(BlogPosts, '/blogposts')


class Home( Resource ):
    def get(self):
        response = make_response({'Message': 'The Restful Works'}, 200)
        return response

api.add_resource(Home, '/')

if __name__ == '__main__':
    app.run(port=5555, debug=True)