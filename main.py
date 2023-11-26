from flask import Flask, render_template,  request, session, redirect, url_for
import os
import PyPDF2
from ai import generate_questions_resume

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
           
    return render_template('index.html')

@app.route('/loading', methods=['GET', 'POST'])
def loading():
    if request.method == "POST":
        session["job_role"] = request.form.get("job_role")
        session["name"] = request.form.get("name")
        session["email"] = request.form.get("email")
        session["phone"] = request.form.get("location")
        
        file = request.files['file']
        if file.filename != '': 
            filename = os.path.join(app.config['UPLOAD_FOLDER'], session['email'] + ".pdf")
            file.save(filename)
            session["filename"] = filename

        file_name = session['filename']
        pdf_file_path = f"{file_name}"
        with open(pdf_file_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)   
            extracted_text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                extracted_text += page.extract_text()
                
        print(extracted_text)
                
        session["resume_questions"] = generate_questions_resume(extracted_text)   
        print(session["resume_questions"]) 
        
        return redirect(url_for('questions'))
            
    return render_template("loading.html")

@app.route("/questions", methods=['GET', 'POST'])
def questions():
    return render_template("questions.html", questions = session["resume_questions"])
    
if __name__ == '__main__':
    app.run(debug=True)