import json
from flask import Flask, render_template

app = Flask(__name__)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

def load_image_urls():
    with open("image_urls.json") as f:
        return json.load(f)

@app.route('/')
def gpa_calculator():
    image_urls = load_image_urls()
    return render_template('index.html', image_urls=image_urls)


@app.route('/queens')
def queens_calculator():
    image_urls = load_image_urls()
    return render_template('queens.html', image_urls=image_urls)

@app.route('/western')
def western_calculator():
    image_urls = load_image_urls()
    return render_template('western.html', image_urls=image_urls)

@app.route('/waterloo')
def waterloo_calculator():
    image_urls = load_image_urls()
    return render_template('waterloo.html', image_urls=image_urls)

@app.route('/mcmaster')
def mcmaster_calculator():
    image_urls = load_image_urls()
    return render_template('mcmaster.html', image_urls=image_urls)

@app.route('/uoftoronto')
def uoftoronto_calculator():
    image_urls = load_image_urls()
    return render_template('uoftoronto.html', image_urls=image_urls)

@app.route('/guelph')
def guelph_calculator():
    image_urls = load_image_urls()
    return render_template('guelph.html', image_urls=image_urls)

@app.route('/algoma')
def algoma_calculator():
    image_urls = load_image_urls()
    return render_template('algoma.html', image_urls=image_urls)

@app.route('/carleton')
def carleton_calculator():
    image_urls = load_image_urls()
    return render_template('carleton.html', image_urls=image_urls)

@app.route('/brock')
def brock_calculator():
    image_urls = load_image_urls()
    return render_template('brock.html', image_urls=image_urls)

@app.route('/lakehead')
def lakehead_calculator():
    image_urls = load_image_urls()
    return render_template('lakehead.html', image_urls=image_urls)

@app.route('/laurentian')
def laurentian_calculator():
    image_urls = load_image_urls()
    return render_template('laurentian.html', image_urls=image_urls)

@app.route('/nipissing')
def nipissing_calculator():
    image_urls = load_image_urls()
    return render_template('nipissing.html', image_urls=image_urls)

@app.route('/ocad')
def ocad_calculator():
    image_urls = load_image_urls()
    return render_template('ocad.html', image_urls=image_urls)

@app.route('/ontarioTech')
def ontarioTech_calculator():
    image_urls = load_image_urls()
    return render_template('ontarioTech.html', image_urls=image_urls)

@app.route('/tmu')
def tmu_calculator():
    image_urls = load_image_urls()
    return render_template('tmu.html', image_urls=image_urls)

@app.route('/trent')
def trent_calculator():
    image_urls = load_image_urls()
    return render_template('trent.html', image_urls=image_urls)

@app.route('/ottawa')
def ottawa_calculator():
    image_urls = load_image_urls()
    return render_template('ottawa.html', image_urls=image_urls)

@app.route('/laurier')
def laurier_calculator():
    image_urls = load_image_urls()
    return render_template('laurier.html', image_urls=image_urls)

@app.route('/windsor')
def windsor_calculator():
    image_urls = load_image_urls()
    return render_template('windsor.html', image_urls=image_urls)

@app.route('/york')
def york_calculator():
    image_urls = load_image_urls()
    return render_template('york.html', image_urls=image_urls)


if __name__ == '__main__':
    app.run(debug=False)
