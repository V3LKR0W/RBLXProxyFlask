import requests as r
import json
from flask import Flask, jsonify, request
from flask_restx import Api, Resource, fields, errors, abort

# Application Config
app = Flask(__name__)

api = Api(app, version='1.0',
        title='Roblox Proxy API', 
        description='<b>Framework: Python using Flask and Restx.</b>', 
        default='/api', 
        default_label='Public API list',
        catch_all_404s=True,
        )


api_headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0'}

api_error_msg = 'Server could not format JSON please try again with another argument.'

# API Routing
@api.route('/api/user_by_id/<userid>')
class get_user_by_id(Resource):
    def get(self, userid):
        try:
            get_userid = r.get('https://api.roblox.com/users/{}'.format(userid), headers=api_headers).json()
        except ValueError:
            abort(500, api_error_msg)
        return jsonify(get_userid)

@api.route('/api/search_user/<username>')
class get_user_by_username(Resource):
    def get(self, username):
        try:
            get_username = r.get('https://users.roblox.com/v1/users/search?keyword={}'.format(username), headers=api_headers).json()
        except ValueError:
            abort(500, api_error_msg)
        return jsonify(get_username)

@api.route('/api/get_headshot_thumbnail/<userid>')
class get_headshot(Resource):
    def get(self, userid):
        try:
            get_thumbnail = r.get('https://www.roblox.com/headshot-thumbnail/json?userId={}&width=180&height=180'.format(userid)).json() 
        except ValueError:
            abort(500,api_error_msg)
        return jsonify(get_thumbnail)

@api.route('/api/get_avatar_thumbnail/<userid>')
class get_avatar_thumbnail(Resource):
    def get(self, userid):
        try:
            get_thumbnail = r.get('https://www.roblox.com/outfit-thumbnail/json?userOutfitId={}&width=352&height=352&format=png'.format(userid)).json()
        except ValueError:
            abort(500,api_error_msg)
        return jsonify(get_thumbnail)



if __name__ == '__main__':
    app.run(debug=True)
