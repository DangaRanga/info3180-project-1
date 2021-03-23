"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os

from app import app, db
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from flask.helpers import send_from_directory

from app.forms import PropertyForm
from app.models import PropertyModel


# Utility functions
def get_uploaded_images():
    """Retrieves uploaded images
    Args:
        None
    Returns:
        <list> A list of the files in the upload folder
    """
    upload_dir = app.config.get('UPLOAD_FOLDER')
    return sorted(os.listdir(upload_dir))


###
# Routing for your application.
###


@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


@app.route('/property', methods=['GET', 'POST'])
def add_property():
    """Form for adding properties"""

    # Initialize the property form
    form = PropertyForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            # Extract form data
            property_title = form.property_title.data
            description = form.description.data
            no_bedrooms = form.no_rooms.data
            no_bathrooms = form.no_bathrooms.data
            price = form.price.data
            location = form.location.data
            property_type = form.property_type.data
            photo = form.photo.data

            # Save the photo
            photo_path = secure_filename(photo.filename)
            path_joined = os.path.join(app.config['UPLOAD_FOLDER'], photo_path)
            print(path_joined)
            photo.save(path_joined)

            # Store the property to the database
            property_model = PropertyModel(
                title=property_title,
                description=description,
                no_bedrooms=no_bedrooms,
                no_bathrooms=no_bathrooms,
                price=price,
                location=location,
                property_type=property_type,
                photo_path=photo_path)

            db.session.add(property_model)
            db.session.commit()

            # Redirect to properties page
            flash('Property successfully saved', 'success')
            return redirect(url_for('get_properties'))
        flash_errors(form)
    return render_template('property.html', form=form)


@app.route('/properties')
def get_properties():
    properties = PropertyModel.query.all()
    return render_template('properties.html', properties=properties)


@app.route("/property/<property_id>")
def view_property(property_id):
    # Retrieve the property with the matching id
    prop = PropertyModel.query.filter_by(id=property_id).first()
    return render_template("view_property.html", prop=prop)


@app.route('/uploads/<filename>')
def get_image(filename):
    upload_dir = app.config.get('UPLOAD_FOLDER')
    print(upload_dir)
    return send_from_directory(upload_dir, filename=filename)

    ###
    # The functions below should be applicable to all Flask apps.
    ###

    # Display Flask WTF errors as Flash messages


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
