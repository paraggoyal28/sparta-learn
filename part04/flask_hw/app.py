from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home(): 
    return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/info', methods=['GET'])
def info_get():
    my_name = request.args.get('my_name')
    print('my_name ' + my_name)
    return jsonify({'msg': 'from get endpoint'})

@app.route('/info', methods=['POST'])
def post_info():
    my_name = request.form.get('my_name')
    print('post! my name: ' + my_name)
    return jsonify({'msg': 'from post endpoint'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)