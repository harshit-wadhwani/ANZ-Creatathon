import os 
from langchain.document_loaders import PyMuPDFLoader
from langchain.vectorstores import Chroma
from langchain.llms import GooglePalm
from langchain.chains import RetrievalQA
import google.generativeai as palm
palm.configure(api_key="PALM_API_KEY")

os.environ['GOOGLE_API_KEY'] = "PALM_API_KEY"
llm = GooglePalm(temperature=0.5)

def generate_questions_jd(job_description):
    prompt = f"The Following is the Job Description of an oppening'{job_description}' Generate Three Questions that can be asked to the candidate based on the job description, strictly give only 3 most important questions that can be asked seperated by '|'. Also number the questions with number starting from 1"
    completion=palm.generate_text(
    model="models/text-bison-001",
    prompt=prompt,
    temperature=0.99,
    max_output_tokens=800,
)
    return completion.result.split('\n')

def generate_questions_resume(resume_text):
    prompt = f"we are hiring and you are responsible for asking questions to the cadidate, this is what was written in the resume of the applicant = '{resume_text}'. Generate exactly two questions to ask to the applicant based on the resume provided strictly do not ask anything apart from resume, strictly do not ask 'What are your salary expectation', strictly give only 2 most important questions which would be numbered 4. and 5. and separate them using '|'."
    # prompts = [prompt]
    # llm_response = llm._generate(prompts)   
    # res = llm_response.generations
    # question = res[0][0].text
    # questions = question.split("|")
    completion=palm.generate_text(
    model="models/text-bison-001",
    prompt=prompt,
    temperature=0.99,
    max_output_tokens=800,
)
    return completion.result.split("|")




# print(generate_questions_jd("""Job Title: Junior Software Developer

# Job Summary:
# We are seeking a highly motivated and talented Junior Software Developer to join our dynamic team. As a Junior Software Developer, you will work closely with experienced developers to design, develop, and maintain high-quality software solutions. This is an excellent opportunity for an entry-level professional to gain hands-on experience in software development and contribute to innovative projects.

# Responsibilities:

# Coding and Programming:

# Collaborate with senior developers to write clean, efficient, and well-documented code.
# Participate in the development and implementation of software solutions based on project requirements.
# Testing and Debugging:

# Conduct thorough testing of applications to ensure they meet quality standards.
# Identify and resolve software defects and issues in a timely manner.
# Collaboration:

# Work closely with cross-functional teams, including designers and product managers, to understand project requirements and contribute to the overall success of the team.
# Collaborate with team members to review code, share knowledge, and ensure best practices are followed.
# Learning and Growth:

# Stay updated on industry trends, technologies, and best practices.
# Continuously improve your technical skills and contribute to a culture of learning within the team.
# Qualifications:

# Education:

# Bachelor’s degree in Computer Science, Software Engineering, or a related field.
# Technical Skills:

# Proficiency in at least one programming language (e.g., Java, Python, C#).
# Understanding of software development principles and best practices.
# Knowledge of web development technologies (HTML, CSS, JavaScript) is a plus.
# Communication:

# Strong communication skills, both verbal and written.
# Ability to work collaboratively in a team environment.
# Problem-Solving:

# Strong problem-solving skills and the ability to think critically.
# Eagerness to learn and adapt to new technologies and challenges.
# Initiative:

# Proactive attitude with a willingness to take ownership of tasks and projects.
# Ability to work independently and seek guidance when needed.
# Benefits:

# Competitive salary and performance-based incentives.
# Opportunities for professional development and career advancement.
# Health and wellness programs.
# Collaborative and inclusive work environment.
# If you are passionate about software development, eager to learn, and ready to contribute to innovative projects, we encourage you to apply for this exciting opportunity as a Junior Software Developer. Join us in shaping the future of technology!
# """

# print(generate_questions_resume(r"""HARSHIT  WADHWANI  
# Bengaluru, Karnataka  • +91 -7990728742  • harshitwadhwani23@gmail.com  • LinkedIn  • GitHub   
 
# PROFESSIONAL EXPERIENCE  
 
# Kunato    SEP  2023 – OCT  2023  
# AI Automation Intern
# • Created a Slack chat bot using company data to streamline new employee onboarding,
# boosting productivity .
# • Developed an employee review system that simplified task reporting and generated
# summaries for managers, enhancing communication  using LL M’s.
# • Designed and implemented an AI -powered recruitment process, significantly streamlining
# screening  processes.
# Aditya Birla Fashion and Retail Ltd.   Mar 2023  – May  2023
# Intern
# ● Analyzed a comprehensive dataset of customer reviews spanning 3 months .
# ● Reviewed and processed customer reviews during this period.
# ● Identified percentage of positive , neutral, an d negative sentiments within the dataset.
# ● Pinpointed over 2 recurring issues that customers frequently mentioned.
# ● Transformed complex analytical findings into  actionable recommendations for the Reebok
# Mission Happiness and Marketing teams.
# HP            AUG 2021 – SEP 2021
# Intern
# • Collaborated on the design and development of a lead management system for HP India.
# • Assisted in Integrated geolocation tracking and real -time store -client connections into the
# system.
# • Achieved a notable increase in lead conversion rates, particularly during the COVID -19
# pandemic.

# EDUCATION

# Dayananda Sagar Academy of Technology and Management, Bangalore  2020  – 2024
# Bachelor of Engineering, Artificial Intelligence and Machine Learning  CGPA  – 8.57

# Ryan International School , Surat, Gujarat (XII)   2020
# Central Board of Secondary Education  88 %

# Ryan International School , Surat, Gujarat (X)   2018
# Central Board of Secondary Education  78.8 %
# SKILLS

# Technical Skills : Python,  Java, Excel, NumPy , Pandas , Matplotlib , Langchain, OpenCV, Docker, Sci-Kit
# Learn, PyTorch, LLM’s, Vector database s, Flask , FastAPI, Streamlit, Git, SQL , MongoDB.

# Behavioral Skills : Communication, Leadership, Time Managemen t, Eager to grow and learn
# Projects

# AI Gym Trainer
# • Computer Vision System: Developed using Mediapipe and OpenCV.
# • Bicep Curls Tracking: Achieved 82% accuracy in counting curls.
# • Posture Assessment: Attained 84% accuracy in evaluating plank form.
# • User Impact: Enhanced workouts for  users, minimizing injuries.
#  College Marketplace - An Android Application
# • Developed a college community marketplace app using Android Studio , Java  and Firebase .
# • Utilized Android Studio and Java to build a user -friendly interface and smooth functionality.
# Depression Analysis using Tweets.
# • Developed an application that extracts the last 100 tweets of users based on their Twitter
# username.
# • Utilized natural language processing (NLP) techniques to predict the user's level of
# depression.
# • Generated a word cloud from the collected tweets, providing a visual representation of the
# most frequently used words.
# Online Food Ordering System (MySQL)
# • Created user -friendly app using Streamlit, seamlessly linked to MySQL database.
# • Streamlined admin oversight, optimizing order management via MySQL integration.

# Certifications

# Google IT Automation with Python Specialization  – Coursera
# Python for Data Science and Machine Learning  – Udemy
# Google Analytics Certification  – Google Digital Academy
# Introduction to Git and GitHub – Coursera
# Core Java Basics  – upGrad
# Publications


# A Study on Real Time Video Analysis for Vehicle Traffic Movement
# International Journal of Engineering Research in Computer Science and Engineering (IJERCSE)
# December 12, 2022

# Extra Curriculars

# • Organized and led a successful 24hr hackathon as a part of AIML club, DSATM .
# • Led as Head of the Technical Club, orchestrating successful induction program s for 300+
# freshmen  students .
# • Spearheaded coordination of  club activities, fostering technical skill development and
# collaboration among members."""))
