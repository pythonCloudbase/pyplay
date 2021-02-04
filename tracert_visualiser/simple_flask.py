from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/input')
def display():
    print(request.args.get('filename'))
    if 'index'== request.args.get('filename'):
        myfilename = request.args.get('filename')
        return render_template('index.html')
    else :
        return "no input file specified"

@app.route('/alpha')
def alpha():
    return "This is the alpha!"

@app.route('/omega')
def omega():
    return "this is the omega"

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True, port=3134)
