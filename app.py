from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'super_secret_key_for_flash_messages'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form_type = request.form.get('form_type')
        if form_type == 'contact':
            flash('Thank you! Your message has been sent successfully.', 'success')
        return redirect(url_for('contact') + '#contact')
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/explore-services')
def explore_services():
    return render_template('explore_services.html')

@app.route('/hr', methods=['GET', 'POST'])
def hr():
    if request.method == 'POST':
        position = request.form.get('position')
        flash(f'Application received for {position}. Our HR team will reach out soon!', 'success')
        return redirect(url_for('hr'))
    return render_template('hr.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        flash('Thank you! Your message has been sent successfully.', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)