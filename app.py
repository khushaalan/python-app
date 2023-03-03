from flask import Flask, render_template, redirect, url_for

# Init app
app = Flask(__name__)


# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Pages
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/workexperiences')
def workexperiences():
    return render_template('workexperiences.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')




# Redirects
@app.route('/redirect-about')
def redirect_to_about():
    return redirect(url_for('about'))

@app.route('/redirect-skills')
def redirect_to_skills():
    return redirect(url_for('skills'))

@app.route('/redirect-workexperiences')
def redirect_to_workexperiences():
    return redirect(url_for('workexperiences'))

@app.route('/redirect-projects')
def redirect_to_projects():
    return redirect(url_for('projects'))

@app.route('/redirect-contact')
def redirect_to_contact():
    return redirect(url_for('contact'))



# Run the app
if __name__ == '__main__':
    app.run()
