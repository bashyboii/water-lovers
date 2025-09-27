from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/drivemad')
def drivemad():
    return render_template('drivemad.html')
@app.route('/RagdollArchers')
def ragdollarchers():
    return render_template('RagdollArchers.html')
@app.route('/Proxy')
def proxy():
    return render_template('Proxy.html')
@app.route('/EscapeRoad')
def escaperoad():
   return render_template('EscapeRoad.html')
if __name__ == '__main__':
    app.run() 
