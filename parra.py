from flask import Flask
import urllib

app = Flask(__name__)

@app.route('/')
def hello_world():
    page = urllib.request.urlopen('https://location.am-all.net/alm/location?gm=98&lang=en&ct=1012').read().decode("utf8").lower()
    if page.find('parramatta') > -1:
        return 'Yes'
    return 'No'

if __name__ == '__main__':
    app.run()
