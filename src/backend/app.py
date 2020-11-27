# -*- coding: utf-8 -*-
import spotipy
import os
import logging
import random

from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from spotipy.oauth2 import SpotifyClientCredentials

PAGE_LIMIT = 10

app = Flask(__name__)
CORS(app)

USER_ID = 'lqp2792' # Please change this

class Playlist(Resource):
  def get(self):
    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)

    res = []
    playlists = sp.user_playlists('lqp2792')
    while playlists:
      if len(res) >= PAGE_LIMIT:
        break
      
      for i, playlist in enumerate(playlists['items']):
        url = playlist['external_urls']['spotify']
        url = url.replace("/playlist", "/embed/playlist")
        res.append(url)

      if playlists['next']:
        playlists = sp.next(playlists)
      else:
        playlists = None

    random.shuffle(res)
    return { "playlists": res[:5] }

if __name__ == "__main__":
  if os.environ.get('SPOTIPY_CLIENT_ID') is None or os.environ.get('SPOTIPY_CLIENT_SECRET') is None:
    logger.error("Please set environment variable SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET")

  api = Api(app)
  api.add_resource(Playlist, '/playlists')
  app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
  logging.info(app)