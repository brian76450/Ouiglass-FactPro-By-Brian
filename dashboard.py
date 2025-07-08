# Dashboard pour OUIGLASS FACTPRO V4 By BRIAN

from flask import Flask, render_template, request, session, redirect, jsonify
from flask_session import Session
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
from reportlab.pdfgen import canvas
from flask_fontawesome import FontAwesome

app = Flask(__name__, static_folder='static')

# Configuration de la session Flask
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Initialisation de la base de données
from database import init_db
init_db()

# Initialisation de FontAwesome
fa = FontAwesome(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/clients')
def clients():
    return render_template('clients.html')

@app.route('/factures')
def factures():
    return render_template('factures.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/stock')
def stock():
    return render_template('stock.html')

@app.route('/analytics')
def analytics():
    return render_template('analytics.html')

@app.route('/notifications')
def notifications():
    conn = sqlite3.connect('ouiglass_factpro.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM notifications ORDER BY timestamp DESC')
    rows = cursor.fetchall()
    conn.close()
    return render_template('notifications.html', notifications=rows)

@app.route('/analytics/export')
def export_analytics():
    conn = sqlite3.connect('ouiglass_factpro.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM analytics')
    rows = cursor.fetchall()
    conn.close()

    df = pd.DataFrame(rows, columns=['ID', 'Data', 'Timestamp'])
    df.to_excel('analytics_report.xlsx', index=False)
    return "Rapport exporté avec succès !"

@app.route('/analytics/export/pdf')
def export_analytics_pdf():
    conn = sqlite3.connect('ouiglass_factpro.db')
    cursor = conn.cursor()
    cursor.execute('SELECT data, timestamp FROM analytics')
    rows = cursor.fetchall()
    conn.close()

    # Création du fichier PDF
    pdf_file = 'analytics_report.pdf'
    c = canvas.Canvas(pdf_file)
    c.setFont("Helvetica", 12)
    c.drawString(100, 800, "Rapport Analytique")

    y = 750
    for row in rows:
        c.drawString(100, y, f"Données: {row[0]}, Temps: {row[1]}")
        y -= 20

    c.save()
    return f"Rapport exporté avec succès : <a href='{pdf_file}' download>Télécharger le PDF</a>"

@app.route('/roles', methods=['GET', 'POST'])
def manage_roles():
    conn = sqlite3.connect('ouiglass_factpro.db')
    cursor = conn.cursor()

    if request.method == 'POST':
        action = request.form['action']
        name = request.form['name']
        role = request.form['role']
        code = request.form['code']

        if action == 'add':
            cursor.execute('INSERT INTO users (name, role, code) VALUES (?, ?, ?)', (name, role, code))
        elif action == 'delete':
            cursor.execute('DELETE FROM users WHERE name = ?', (name,))

        conn.commit()

    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()

    return render_template('roles.html', users=users)

@app.route('/toggle-dark-mode')
def toggle_dark_mode():
    session['dark_mode'] = not session.get('dark_mode', False)
    return redirect(request.referrer)

@app.route('/api/payment', methods=['POST'])
def process_payment():
    data = request.json
    # Simuler une connexion à une API de paiement
    if data.get('amount') and data.get('method'):
        return {"status": "success", "message": "Paiement traité avec succès."}
    return {"status": "error", "message": "Données de paiement invalides."}

@app.route('/notifications/realtime')
def realtime_notifications():
    conn = sqlite3.connect('ouiglass_factpro.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM notifications ORDER BY timestamp DESC LIMIT 5')
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

@app.route('/analytics/graph')
def analytics_graph():
    conn = sqlite3.connect('ouiglass_factpro.db')
    cursor = conn.cursor()
    cursor.execute('SELECT data, timestamp FROM analytics')
    rows = cursor.fetchall()
    conn.close()

    timestamps = [row[1] for row in rows]
    data = [float(row[0]) for row in rows]
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, data, marker='o')
    plt.title('Rapport Analytique')
    plt.xlabel('Temps')
    plt.ylabel('Données')
    plt.grid(True)

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    return f'<img src="data:image/png;base64,{image_base64}" />'

@app.route('/roles/confirm', methods=['POST'])
def confirm_role_action():
    action = request.form['action']
    name = request.form['name']
    if action == 'add':
        message = f"Rôle ajouté avec succès pour {name}."
    elif action == 'delete':
        message = f"Rôle supprimé avec succès pour {name}."
    else:
        message = "Action non reconnue."
    return jsonify({"status": "success", "message": message})

@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

@app.route('/backup')
def backup():
    import shutil
    shutil.copy('ouiglass_factpro.db', 'backup/ouiglass_factpro_backup.db')
    return "Sauvegarde effectuée avec succès !"

@app.route('/update')
def update():
    # Simuler une mise à jour automatique
    return "Mise à jour automatique effectuée avec succès !"

if __name__ == '__main__':
    app.run(debug=True)
