from flask import Blueprint, request, render_template
from app.ECSDA import digital_signature
blueprint = Blueprint(
    'api',
    __name__,
    url_prefix=''
)
@blueprint.get('/index')
def index():
    return render_template('index.html')

@blueprint.post('/index')
def upload():
    file = request.files['myfile']
    file=file.read()
    signature=digital_signature(file)

    print("Signature2",signature)
    return render_template('index.html',signature=signature)

signature=""

