# -*- coding: utf-8 -*- 

from flaskext.wtf import Form, TextField, PasswordField, BooleanField,\
         SubmitField, Required, validators, TextAreaField, HiddenField
from flaskext.wtf.file import FileField, file_required, file_allowed
from flaskext.uploads import UploadSet, IMAGES

class TestForm(Form):
    name = TextField("name", validators=[Required()])

class LoginForm(Form):
    username = TextField(u"登录用户", validators=[Required()])
    password = PasswordField(u"登录密码", validators=[Required()])
    #remember = BooleanField("remember")
    submit = SubmitField(u"登录")

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


class TodoForm(Form):
    pass

photos = UploadSet('photos', IMAGES)
class UploadForm(Form):
    photo = FileField("上传图片", validators=[file_required(), \
        file_allowed(photos, "Images only!")])
    submit = SubmitField("Submit")

class WikiEditForm(Form):
    wikitext = TextAreaField("Raw Text")
    save = SubmitField("Save")
    preview = SubmitField("Preview")
    cancel = SubmitField("Cancel")

    def set_default_text(self, text=None):
        self.wikitext.data = text
    
class WikiShowForm(Form):
    edit = SubmitField("Edit this page")
    attach = SubmitField("Attach")
    remove = SubmitField("Remove")
