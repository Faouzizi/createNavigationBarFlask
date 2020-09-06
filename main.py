###############################################
#          Import some packages               #
###############################################
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *
from dominate.tags import img

###############################################
#          Define flask app                   #
###############################################
logo = img(src='./static/img/logo.png', height="50", width="50", style="margin-top:-15px")
topbar = Navbar(logo,
                View('News', 'get_news'),
                View('Live', 'get_live'),
                View('Programme', 'get_programme'),
                View('Classement', 'get_classement'),
                View('Contact', 'get_contact'),
                )

# registers the "top" menubar
nav = Nav()
nav.register_element('top', topbar)

app = Flask(__name__)
Bootstrap(app)

###############################################
#          Render Home page                   #
###############################################
@app.route('/news', methods=['GET'])
def get_news():
    return(render_template('news.html'))

###############################################
#          Render live page                   #
###############################################
@app.route('/live', methods=["GET"])
def get_live():
    return(render_template('live.html'))

###############################################
#          Render programme page                   #
###############################################
@app.route('/programme', methods=["GET"])
def get_programme():
    return(render_template('programme.html'))

###############################################
#          Render Classement page                   #
###############################################
@app.route('/classement', methods=["GET"])
def get_classement():
    return(render_template('classement.html'))

###############################################
#          Render contact page                   #
###############################################
@app.route('/contact', methods=["GET"])
def get_contact():
    return(render_template('contact.html'))

nav.init_app(app)


###############################################
#                Run app                      #
###############################################
if __name__ == '__main__':
    app.run(debug=True)
