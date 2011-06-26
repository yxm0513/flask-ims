from flask import Module, request, flash, url_for, redirect, \
     render_template, abort
from flaskext.uploads import UploadSet, IMAGES, configure_uploads
from flaskext.login import login_required, current_user

from ims.models import db, Photo
from ims.forms import UploadForm

mod = Module(__name__)

from ims.forms import photos
from ims import app
configure_uploads(app, (photos))

@mod.route('/')
def index():
    return render_template('photo/index.html')


@mod.route('/upload', methods=['GET', 'POST'])
def upload():
    form = UploadForm(request.form)
    if not form.validate_on_submit():
        flash('validate form failed', 'error')
        return render_template('photo/upload.html', form = form)
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        rec = Photo(filename=filename, user=current_user.id)
        rec.store_to_db()
        flash("Photo saved.")
        return redirect(url_for('show', id=rec.id))
    return render_template('photo/upload.html', form = form)

@mod.route('/<id>')
def show(id):
    photo = Photo.get(id)
    if photo is None:
        abort(404)
    url = photos.url(photo.filename)
    return render_template('photo/show.html', url=url, photo=photo)