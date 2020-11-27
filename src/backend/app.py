# -*- coding: utf-8 -*-
import spotipy
import os
import logging
import random
import json
import sys

from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS
from spotipy.oauth2 import SpotifyClientCredentials
from redis import Redis
from datetime import date, timedelta

PAGE_LIMIT = 10
USER_ID = 'lqp2792' # Please change this

app = Flask(__name__)
CORS(app)
redis = Redis(host=os.environ.get('REDIS_HOST', "demo-cache"), port=6379)
auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(levelname)s] - %(asctime)s | %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
handler.setFormatter(formatter)
logger.addHandler(handler)

class Playlist(Resource):
  def get(self):
    today = date.today()
    key = today.strftime("%d%m%Y")
    playlists = redis.get(key)
    res = []

    if playlists is None:
      logger.info('Query Spotify API')
      playlists = sp.user_playlists(USER_ID)
      redis.setex(key, timedelta(minutes=1), json.dumps(playlists))
    else:
      logger.info('Query Redis Cache')
      playlists = json.loads(playlists)

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