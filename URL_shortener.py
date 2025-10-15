from flask import Flask, request, redirect, jsonify
import random
import string
from urllib.parse import urlparse
import json
import os
import hashlib

app = Flask(__name__)

#===== Helpers ======
DATA_FILE = 'urldata.json'

def generator(long_url):
    short_url = hashlib.sha256(long_url.encode()).hexdigest()
    return short_url[0:7]



def get_data():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def add_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)
   # return "Record successfully updated!"


@app.route('/table', methods = ['GET'])
def full_table():
    data = get_data()
    return jsonify(data)


@app.route('/table/shorten', methods=['POST'])
def shortener():
    data = get_data()
    in_data = request.get_json()
    original_url = in_data.get('url')

    for row in data:
        if row['url'] == original_url:
            return {"Error": "URL already exists"}, 400
    def is_valid_url(url):  
        try:
            parsed = urlparse(url)
            return all([parsed.scheme in ('http', 'https'), parsed.netloc])
        except Exception:
            return False

    if not is_valid_url(original_url):
        return jsonify({'Error': 'Invalid URL format. Please include http:// or https://'}), 400

    short_url = generator(original_url)


    existing_short_urls = {row['short_url'].split('/')[-1] for row in data}
    while short_url in existing_short_urls:
        short_url = generator('abc' + original_url + ''.join(random.choices(string.ascii_letters, k=5)))

    short_link = f"http://127.0.0.1:5000/{short_url}"
    data.append({'short_url': short_link, 'url': original_url, 'access_count' : 0})
    add_data(data)
    return jsonify({'Shortened URL': short_link}), 200



@app.route('/<short_url>')
def redirecting_to_url(short_url):
    data = get_data()
    for row in data:
        link = f"http://127.0.0.1:5000/{short_url}"
        if row['short_url'] == link:
            count_add = int(row['access_count'])
            row.update({'short_url' : row['short_url'], 'url' : row['url'], 'access_count' : count_add  + 1 })
            add_data(data)
            return redirect(row['url'])

    return {'Error' : 'URL not found'}, 404



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)