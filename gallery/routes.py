__author__ = 'snwiem'

import logging
import os
import glob
from PIL import Image
from flask import render_template, abort, send_file
from gallery import app

@app.route('/')
def index():
    album_dir = os.path.abspath(app.config['ALBUM_ROOT'])
    if not os.path.isdir(album_dir):
        # requested directory does not exist...just abort
        abort(404)
    subs = [("album/"+i, i) for i in next(os.walk(album_dir))[1]]
    return render_template("index.html", albums=subs)


@app.route('/album/<path:path>')
def album(path):
    root_abs = os.path.abspath(app.config['ALBUM_ROOT'])
    album_dir = os.path.join(root_abs, path)
    if not os.path.isdir(album_dir):
        # requested directory does not exist...just abort
        abort(404)
    # scan directory for images
    images = [i[len(root_abs):] for ext in app.config['IMAGE_EXTS'] for i in glob.iglob(album_dir + "/*." + ext)]
    subs = [(path+"/"+i, i) for i in next(os.walk(album_dir))[1]]
    #return json.dumps(images) + json.dumps(subs)
    return render_template('album.html', images=images, subs=subs)

@app.route('/thumb/<path:path>')
def thumbnail(path):
    thumb_root = os.path.abspath(app.config['THUMB_ROOT'])
    thumb_file = os.path.join(thumb_root, path)
    thumb_file = os.path.splitext(thumb_file)[0]+".png"
    create_thumb = False
    if not os.path.exists(thumb_file):
        create_thumb = True
    if os.path.exists(thumb_file):
        image_root = os.path.abspath(app.config['ALBUM_ROOT'])
        image_file = os.path.join(image_root, path)
        if not os.path.exists(image_file):
            abort(404)
            return
        if os.path.getmtime(image_file) > os.path.getmtime(thumb_file):
            create_thumb = True
    if create_thumb:
        thumb_dir = os.path.dirname(thumb_file)
        if not os.path.exists(thumb_dir):
            os.makedirs(thumb_dir)
        # need to generate thumb
        image_root = os.path.abspath(app.config['ALBUM_ROOT'])
        image_file = os.path.join(image_root, path)
        if not os.path.exists(image_file):
            abort(404)
            return
        img = Image.open(image_file)
        img.thumbnail(app.config['THUMB_DIMS'])
        logging.debug("*** saving " + thumb_file)
        img.save(thumb_file, "PNG")
    return send_file(thumb_file)