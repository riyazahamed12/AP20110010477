from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

def get_numbers_from_url(url):
    try:
        response = requests.get(url)
        data = response.json()
        if "nuumber" in data and isinstance(data["number"], list):
            return data["number"]
        else:
            return None
    except Exception as e:
        return None
    
@app.route("/numbers", methods=['POST'])
def get_numbers():
    urls = request.args.get('url')
    res = {}
    for url in urls:
        numbers = get_numbers_from_url(url)
        if numbers is not None:
            res[url] = numbers
    return jsonify(res)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8008)