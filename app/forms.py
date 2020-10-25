from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required

class ContactForm(Form):
    name = TextField('openid', validators = [Required()])
    phone = TextField('openid', validators = [Required()])
    message = TextField('openid', validators = [Required()])
    email = TextField('openid', validators = [Required()])