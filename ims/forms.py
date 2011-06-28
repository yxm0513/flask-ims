from flaskext.wtf import Form, TextField, PasswordField, BooleanField,\
         SubmitField, Required, validators
from flaskext.wtf.file import FileField, file_required, file_allowed
from flaskext.uploads import UploadSet, IMAGES

class TestForm(Form):
    name = TextField("name", validators=[Required()])

class LoginForm(Form):
    username = TextField("Username", validators=[Required()])
    password = PasswordField("Password", validators=[Required()])
    #remember = BooleanField("remember")
    submit = SubmitField("Login")

class RegisterForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=25)])
    email = TextField('Email', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [
        validators.Required(),
        validators.EqualTo('password2', message='Passwords must match')
    ])
    password2 = PasswordField('Password <small>(repeat)</small>')
    #accept_tos = BooleanField('I accept the TOS', [validators.Required()])
    submit = SubmitField("Register")

class AddUserForm(Form):
    username = TextField("Username", validators=[Required()])
    password = TextField("Password", validators=[Required()])
    email = TextField("E-mail", validators=[Required()])
    submit = SubmitField("New")

class RemoveUserForm(Form):
    username = TextField("Username", validators=[Required()])
    submit = SubmitField("Remove")

photos = UploadSet('photos', IMAGES)
class UploadForm(Form):
    photo = FileField("Upload your image", validators=[file_required(),
        file_allowed(photos, "Images only!")])
    submit = SubmitField("Submit")

class WikiForm(Form):
    text = TextField("Raw Text", validators=[Required()])
    submit = SubmitField("Save")
