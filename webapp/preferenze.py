from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ele_t_10000_totale')
def ele_t_10000_totale():
    return render_template('maps/ele_t_10000_totale.html')

@app.route('/vot_t_10000_totale')
def vot_t_10000_totale():
    return render_template('maps/vot_t_10000_totale.html')

@app.route('/voti_pd_10000_totale')
def voti_pd_10000_totale():
    return render_template('maps/voti_pd_10000_totale.html')

@app.route('/ele_t_10000_silvia')
def ele_t_10000_silvia():
    return render_template('maps/ele_t_10000_silvia.html')

@app.route('/vot_t_10000_silvia')
def vot_t_10000_silvia():
    return render_template('maps/vot_t_10000_silvia.html')

@app.route('/voti_pd_10000_silvia')
def voti_pd_10000_silvia():
    return render_template('maps/voti_pd_10000_silvia.html')

@app.route('/ele_t_10000_marcello')
def ele_t_10000_marcello():
    return render_template('maps/ele_t_10000_marcello.html')

@app.route('/vot_t_10000_marcello')
def vot_t_10000_marcello():
    return render_template('maps/vot_t_10000_marcello.html')

@app.route('/voti_pd_10000_marcello')
def voti_pd_10000_marcello():
    return render_template('maps/voti_pd_10000_marcello.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 
