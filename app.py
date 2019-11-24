from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.String, primary_key=True)
    timestamp = db.Column(db.DateTime)
    user = db.relationship('User', backref='owner')
    message = db.Column(db.String(140))
    content_type = db.Column(db.String)
    url = db.Column(db.String)

class User(db.Model):
    id= db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    image_url = db.Column(db.String)
    owner_id = db.Column(db.Integer, db.ForeignKey('post.id'))


@app.route('/posts', methods=['GET'])
def posts_get():
    print('asdfas')
    limit = request.args.get('limit')
    offset = request.args.get('offset')

    return jsonify('asdf')

@app.route('/posts', methods=['POST'])
def posts_post():
    requ = request.get_json()
    if User.query.filter_by(id=requ['user']['id']).first():

        post = Post(id =requ['id'], timestamp=datetime.now(), message=requ['message'], content_type=requ['media']['content_type'],
                    url=requ['media']['url'])
        user = User(id=requ['user']['id'], name=requ['user']['name'], image_url=requ['user']['image_url'],
                    owner_id=post.id)
        db.session.add(user)
        db.session.add(post)
    #post =
    return requ['user']['asdf']

@app.route('/posts/<id>', methods=['GET'])
def posts_id_get(id):
    return


@app.route('/posts/<id>')
def posts_id_delete(id):
    message = Message.query.filter_by(id=id).first()
    db.session.delete(message)
    db.session.commit()
    return f'<h1>The user is located in: { user.location }</h1>'

app.run(debug=True)