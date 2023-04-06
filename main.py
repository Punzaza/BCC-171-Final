# import libraries and functions

from flask import Flask, render_template

# set template folder (html files) and static folder (css/js files)
app = Flask(__name__, template_folder='template', static_folder=None)
app.config['SERVER_NAME'] = 'domainname:443'
app.static_folder = 'static'
app.add_url_rule('/<path:filename>',
                 endpoint='static',
                 subdomain='static',
                 view_func=app.send_static_file)


@app.route('/favicon.ico', subdomain='')
def favicon():
    return app.send_static_file('img/scholarmarket.png')

@app.route('/favicon.ico', subdomain='api')
def faviconapi():
    return app.send_static_file('img/scholarmarket.png')

@app.route('/favicon.ico', subdomain='static')
def faviconstatic():
    return app.send_static_file('img/scholarmarket.png')

@app.route('/favicon.ico', subdomain='171')
def favicon171():
    return app.send_static_file('img/favicon.png')


# set the default website page
@app.route('/', subdomain='171')
def dreamscape():
    return render_template('index.html')


# set the default website page
@app.route('/page', subdomain='api')
def api():
    return app.send_static_file('page.json')


# start the website
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=443, ssl_context=("keys/ssl/cert.pem", "keys/ssl/key.key"))
