# These are the codes to bring informations from database and push it to the html.

# The modules for flask and connection.

from flask import Flask, request
import pymysql.cursors

# The connection Information;
db = pymysql.connect(host='167.99.211.234',
                     user='cemal',
                     password='Q1w2e3r4t5.!',
                     db='ayggalvaniz',
                     charset='utf8mb4',
                     cursorclass=pymysql.cursors.DictCursor)

baglanti = db.cursor()

# To reach to the root directory.
app = Flask(__name__,
            static_url_path='',
            static_folder='Public',
            template_folder='')

#route
@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/about')
def about():
    baglanti.execute('SELECT id, name, subtitle, description, cover FROM about WHERE name = %s LIMIT 1', "about")
    icerik = baglanti.fetchall()
    page = {}

    if len(icerik) > 0:
        page = icerik[0]
        baglanti.execute('SELECT image_id, image, name FROM about_images WHERE content_id = %s', page.get('id'))
        photos = baglanti.fetchall()
        page["images"] = photos

    return {
        "status": "success",
        "result": {
            "about": page,
        }
    }
