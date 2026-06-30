import sys
import os
from flask import Flask, render_template, request, jsonify

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Backend'))
from solver import resolver_selos

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/solve')
def api_solve():
    valor_str = request.args.get('valor', '')
    denom_str = request.args.get('denominacoes', '')

    try:
        valor = int(valor_str)
    except ValueError:
        return jsonify({'possivel': False, 'erro': 'Valor inválido. Informe um número inteiro positivo.'}), 400

    try:
        denominacoes = [int(d.strip()) for d in denom_str.split(',') if d.strip()]
    except ValueError:
        return jsonify({'possivel': False, 'erro': 'Denominações inválidas. Use números inteiros separados por vírgula.'}), 400

    resultado = resolver_selos(valor, denominacoes)
    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)