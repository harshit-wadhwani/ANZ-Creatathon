from flask import Flask, render_template,  request, session, redirect, url_for, send_file
import os
import PyPDF2
from ai import generate_questions_resume, generate_questions_jd
from texttospeech import text_to_speech


jd = {
    "Junior Software Developer" : """Job Title: Junior Software Developer

Job Summary:
We are seeking a highly motivated and talented Junior Software Developer to join our dynamic team. As a Junior Software Developer, you will work closely with experienced developers to design, develop, and maintain high-quality software solutions. This is an excellent opportunity for an entry-level professional to gain hands-on experience in software development and contribute to innovative projects.

Responsibilities:

Coding and Programming:

Collaborate with senior developers to write clean, efficient, and well-documented code.
Participate in the development and implementation of software solutions based on project requirements.
Testing and Debugging:

Conduct thorough testing of applications to ensure they meet quality standards.
Identify and resolve software defects and issues in a timely manner.
Collaboration:

Work closely with cross-functional teams, including designers and product managers, to understand project requirements and contribute to the overall success of the team.
Collaborate with team members to review code, share knowledge, and ensure best practices are followed.
Learning and Growth:

Stay updated on industry trends, technologies, and best practices.
Continuously improve your technical skills and contribute to a culture of learning within the team.
Qualifications:

Education:

Bachelor’s degree in Computer Science, Software Engineering, or a related field.
Technical Skills:

Proficiency in at least one programming language (e.g., Java, Python, C#).
Understanding of software development principles and best practices.
Knowledge of web development technologies (HTML, CSS, JavaScript) is a plus.
Communication:

Strong communication skills, both verbal and written.
Ability to work collaboratively in a team environment.
Problem-Solving:

Strong problem-solving skills and the ability to think critically.
Eagerness to learn and adapt to new technologies and challenges.
Initiative:

Proactive attitude with a willingness to take ownership of tasks and projects.
Ability to work independently and seek guidance when needed.
Benefits:

Competitive salary and performance-based incentives.
Opportunities for professional development and career advancement.
Health and wellness programs.
Collaborative and inclusive work environment.
If you are passionate about software development, eager to learn, and ready to contribute to innovative projects, we encourage you to apply for this exciting opportunity as a Junior Software Developer. Join us in shaping the future of technology!
    """,
    "Full Stack Developer" : """Job Title: Full Stack Developer

Job Overview:
We are seeking a highly skilled and motivated Full Stack Developer to join our dynamic and innovative development team. As a Full Stack Developer, you will be responsible for designing, developing, and maintaining both front-end and back-end systems. The ideal candidate should have a strong background in web development, proficiency in both front-end and back-end technologies, and a passion for creating scalable and efficient software solutions.

Responsibilities:

Front-end Development:

Develop and implement user-friendly interfaces using modern web technologies (HTML5, CSS3, JavaScript).
Collaborate with UI/UX designers to translate design wireframes and mockups into responsive and visually appealing web applications.
Back-end Development:

Design and implement server-side logic, databases, and APIs using server-side languages such as Node.js, Python, or Ruby on Rails.
Develop and maintain database structures and optimize system performance.
Full Stack Development:

Integrate front-end and back-end components to ensure seamless and efficient communication between the two.
Troubleshoot and debug issues across the entire stack, ensuring high performance and responsiveness of applications.
Collaboration and Communication:

Work closely with cross-functional teams, including product managers, designers, and other developers, to deliver high-quality software solutions.
Participate in code reviews to ensure code quality, share knowledge, and provide constructive feedback.
Code Optimization and Performance:

Identify and address performance bottlenecks and optimize code for scalability.
Stay updated on industry best practices and emerging technologies to continuously improve development processes.
Qualifications:

Education:

Bachelor's degree in Computer Science, Software Engineering, or a related field.
Experience:

Proven experience as a Full Stack Developer or similar role.
Strong proficiency in front-end and back-end technologies such as JavaScript (React, Angular, or Vue), Node.js, Python, Ruby on Rails, etc.
Skills:

Knowledge of database systems (SQL, NoSQL) and proficiency in database design.
Familiarity with version control systems (Git) and collaborative development tools.
Problem-solving skills and ability to work in a fast-paced, collaborative environment.
Communication:

Excellent communication and interpersonal skills.
Ability to effectively communicate technical concepts to non-technical stakeholders.
Adaptability:

Willingness to learn and adapt to new technologies and methodologies.
Benefits:

Competitive salary
Health insurance
Flexible work hours
Professional development opportunities
Collaborative and innovative work environment
    """,
    "Marketing Manager" : """
    Job Title: Marketing Manager

Company Overview:
[Company Name] is a dynamic and innovative [industry/sector] company committed to [brief description of the company's mission and values]. As we continue to expand our presence in the market, we are seeking a talented and strategic Marketing Manager to join our team and drive the development and execution of our marketing initiatives.

Position Overview:
The Marketing Manager will be responsible for leading the overall marketing strategy to enhance the company's brand visibility, engage target audiences, and drive revenue growth. This role requires a creative and analytical thinker with a proven track record in developing and implementing successful marketing campaigns.

Key Responsibilities:

Strategic Planning:

Develop and execute comprehensive marketing strategies aligned with company goals.
Conduct market research to identify trends, opportunities, and competitive positioning.
Collaborate with cross-functional teams to ensure alignment with overall business objectives.
Campaign Management:

Plan, execute, and optimize multi-channel marketing campaigns to drive brand awareness and lead generation.
Utilize digital marketing, social media, email, and traditional channels to reach target audiences effectively.
Monitor and analyze campaign performance, providing regular reports and insights to improve future initiatives.
Brand Development:

Manage and enhance the company's brand identity, ensuring consistency across all marketing materials and channels.
Implement brand positioning strategies to differentiate the company in the market.
Content Creation:

Oversee the creation of compelling and relevant content for various marketing channels.
Collaborate with internal teams or external agencies to develop engaging content that resonates with the target audience.
Lead Generation and Conversion:

Implement lead generation strategies to build and nurture a qualified sales pipeline.
Work closely with the sales team to optimize marketing efforts for lead conversion.
Budget Management:

Develop and manage the marketing budget, allocating resources effectively to maximize ROI.
Monitor expenses and provide regular financial reports.
Qualifications:

Bachelor's degree in Marketing, Business, or a related field.
Proven experience (X years) in a marketing management role.
Strong understanding of digital marketing, social media, and traditional marketing channels.
Excellent analytical, communication, and project management skills.
Ability to think creatively and strategically.
    """
    
    
    
}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
           
    return render_template('index.html')

@app.route('/loading', methods=['GET', 'POST'])
def loading():
    if request.method == "POST":
        session["job_role"] = request.form.get("jobrole")
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
                
        session["resume_questions"] = []
        session["resume_questions"].extend(generate_questions_jd(jd[session["job_role"]]))
        session["resume_questions"].extend(generate_questions_resume(extracted_text)) 
        print(session["resume_questions"]) 
        print(session["job_role"])
        counter = 1
        for question in session["resume_questions"]:
            text_to_speech(question, filename=f"questions_audio\\questions_{counter}.mp3")
            counter +=1
        
        
        
        return redirect(url_for('questions'))
            
    return render_template("loading.html")

@app.route("/questions", methods=['GET', 'POST'])
def questions():
    
    return render_template("questions.html", questions = session["resume_questions"],candidate_name=session["name"],email=session["email"])

@app.route('/questions_audio/<filename>')
def audio(filename):
    audio_path = f'questions_audio\\{filename}'
    return send_file(audio_path)

@app.route('/save_answer', methods=['POST'])
def save_answer():
    audio_data = request.files['audio']
    index = request.form['index']
    
    audio_data.save(f'answer_audio\\{session["email"]}ans{index}.wav')
    
    return "success", 200


    
if __name__ == '__main__':
    app.run(debug=True)