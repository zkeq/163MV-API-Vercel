# coding:utf-8
import time
import redis
from http.server import BaseHTTPRequestHandler
import os
import json
import requests

env_dist = os.environ
PASSWORD = env_dist.get('PASSWORD')

r = redis.Redis(
    host='apn1-destined-giraffe-32369.upstash.io',
    port=32369,
    password=PASSWORD, ssl=True)


def get_video(vid):
    video_name = '163_mv_liunx_' + vid
    _video_url = r.get(video_name)
    print(_video_url)
    if _video_url is None:
        url = 'https://163mv.icodeq.com/?vid={vid}'.format(vid=vid)
        _video_dict = requests.get(url).text
        _video_dict = json.loads(_video_dict)
        _video_url = _video_dict.get(video_name)
    else:
        _video_url = _video_url.decode('utf-8')
    if not _video_url:
        time.sleep(0.5)
        _video_url = r.get('163_mv_liunx_' + vid).decode('utf-8')
        print('waiting for video url')
    return _video_url


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            url = get_video(vid=self.path.split('?vid=')[1])
        except IndexError:
            url = get_video('10968017')
        self.send_response(308)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('location', url)
        self.send_header('Refresh', '0;url={}'.format(url))
        self.send_header('Cache-Control', 'max-age=0, s-maxage=60, stale-while-revalidate=3600')
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Redirecting to {} (308)'.format(url).encode('utf-8'))
        return None