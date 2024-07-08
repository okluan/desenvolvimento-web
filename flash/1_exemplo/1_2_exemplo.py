from flask import Flask

app = Flask(__name__)

@app.route ('/')
def home():
    return 'Hello World'

@app.route ('/blog')
def blog():
    return '''
    <html>
    <head> </head>
    <body>
        <h2> Welcome to this blog!</h2>
        <p> I am Avi, the author of this blog.</p>
    </body>
    </html>
    '''

@app.route ('/blog/<string:blog_id>')
def blog_id(blog_id):
    return 'This is blog post number ' + blog_id


if __name__ == '__main__':
    app.run()