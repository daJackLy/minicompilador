from flask import Flask, request, jsonify, render_template
from sintactico import analizar_sintactico
from semantico import analizar_semantico
from salida import generar_salida

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compilar', methods=['POST'])
def compilar():
    datos = request.json
    texto = datos.get('comanda', '').upper()
    
    #region eastereggs
    if "MAHOXY" in texto:
        return jsonify({
            "estado": "RECHAZADA",
            "fase": "Papas",
            "mensaje": "Papitas papitas"
        })
    #endregion eastereggs

    #sintactico
    valido, mensaje_sint = analizar_sintactico(texto)
    if not valido:
        return jsonify({
            "estado": "RECHAZADA",
            "fase": "SINTÁCTICO",
            "mensaje": mensaje_sint
        })

    #semantico
    valido, mensajes_sem = analizar_semantico(texto)
    if not valido:
        return jsonify({
            "estado": "RECHAZADA",
            "fase": "SEMÁNTICO",
            "mensaje": mensajes_sem[0]
        })

    #json
    resultado = generar_salida(texto)
    return jsonify({
        "estado": "ACEPTADA",
        "fase": "COMPLETADO",
        "mensaje": "Comanda procesada correctamente.",
        "datos": resultado
    })

if __name__ == '__main__':
    app.run(debug=True)