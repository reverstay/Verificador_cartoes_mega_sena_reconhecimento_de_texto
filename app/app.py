from flask import Flask, render_template, request, redirect, url_for
import os
from models import get_session, Jogo
from ocr import reconhecer_numeros

app = Flask(__name__)
sess = get_session()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # salva imagem enviada pelo usuário
        img = request.files['cartao']
        filename = img.filename
        save_path = os.path.join('data', filename)
        img.save(save_path)

        # processa OCR e grava no DB
        numeros = reconhecer_numeros(save_path)
        jogo = Jogo(imagem=filename, numeros=",".join(numeros))
        sess.add(jogo)
        sess.commit()
        return redirect(url_for('index'))

    # lista todos os jogos
    jogos = sess.query(Jogo).order_by(Jogo.criado_em.desc()).all()
    return render_template('jogos.html', jogos=jogos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
