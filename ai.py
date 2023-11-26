import os 
from langchain.document_loaders import PyMuPDFLoader
from langchain.vectorstores import Chroma
from langchain.llms import GooglePalm
from langchain.chains import RetrievalQA
import google.generativeai as palm
palm.configure(api_key="AIzaSyDhXDX0w_NTUiAmJKqWibB3a8PmZQynWhI")

os.environ['GOOGLE_API_KEY'] = "AIzaSyDhXDX0w_NTUiAmJKqWibB3a8PmZQynWhI"
llm = GooglePalm(temperature=0.5)

def generate_questions_jd(job_description):
    prompt = f"The Following is the Job Description of an oppening'{job_description}' Generate Three Questions that can be asked to the candidate based on the job description, strictly give only 3 most important questions that can be asked seperated by '|'. Also number the questions with number starting from 1"
    
    return questions

def generate_questions_resume(resume_text):
    prompt = f"we are hiring and you are responsible for asking questions to the cadidate, this is what was written in the resume of the applicant = '{resume_text}'. Generate exactly two questions to ask to the applicant based on the resume provided strictly do not ask anything apart from resume, strictly give only 2 most important questions which would be numbered 4. and 5. and separate them using '|'."
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
    return completion.result

# print(generate_questions_jd("software engineer"))
print(generate_questions_resume(r"""HARSHIT  WADHWANI  
Bengaluru, Karnataka  • +91 -7990728742  • harshitwadhwani23@gmail.com  • LinkedIn  • GitHub   
 
PROFESSIONAL EXPERIENCE  
 
Kunato    SEP  2023 – OCT  2023  
AI Automation Intern
• Created a Slack chat bot using company data to streamline new employee onboarding,
boosting productivity .
• Developed an employee review system that simplified task reporting and generated
summaries for managers, enhancing communication  using LL M’s.
• Designed and implemented an AI -powered recruitment process, significantly streamlining
screening  processes.
Aditya Birla Fashion and Retail Ltd.   Mar 2023  – May  2023
Intern
● Analyzed a comprehensive dataset of customer reviews spanning 3 months .
● Reviewed and processed customer reviews during this period.
● Identified percentage of positive , neutral, an d negative sentiments within the dataset.
● Pinpointed over 2 recurring issues that customers frequently mentioned.
● Transformed complex analytical findings into  actionable recommendations for the Reebok
Mission Happiness and Marketing teams.
HP            AUG 2021 – SEP 2021
Intern
• Collaborated on the design and development of a lead management system for HP India.
• Assisted in Integrated geolocation tracking and real -time store -client connections into the
system.
• Achieved a notable increase in lead conversion rates, particularly during the COVID -19
pandemic.

EDUCATION

Dayananda Sagar Academy of Technology and Management, Bangalore  2020  – 2024
Bachelor of Engineering, Artificial Intelligence and Machine Learning  CGPA  – 8.57

Ryan International School , Surat, Gujarat (XII)   2020
Central Board of Secondary Education  88 %

Ryan International School , Surat, Gujarat (X)   2018
Central Board of Secondary Education  78.8 %
SKILLS

Technical Skills : Python,  Java, Excel, NumPy , Pandas , Matplotlib , Langchain, OpenCV, Docker, Sci-Kit
Learn, PyTorch, LLM’s, Vector database s, Flask , FastAPI, Streamlit, Git, SQL , MongoDB.

Behavioral Skills : Communication, Leadership, Time Managemen t, Eager to grow and learn
Projects

AI Gym Trainer
• Computer Vision System: Developed using Mediapipe and OpenCV.
• Bicep Curls Tracking: Achieved 82% accuracy in counting curls.
• Posture Assessment: Attained 84% accuracy in evaluating plank form.
• User Impact: Enhanced workouts for  users, minimizing injuries.
 College Marketplace - An Android Application
• Developed a college community marketplace app using Android Studio , Java  and Firebase .
• Utilized Android Studio and Java to build a user -friendly interface and smooth functionality.
Depression Analysis using Tweets.
• Developed an application that extracts the last 100 tweets of users based on their Twitter
username.
• Utilized natural language processing (NLP) techniques to predict the user's level of
depression.
• Generated a word cloud from the collected tweets, providing a visual representation of the
most frequently used words.
Online Food Ordering System (MySQL)
• Created user -friendly app using Streamlit, seamlessly linked to MySQL database.
• Streamlined admin oversight, optimizing order management via MySQL integration.

Certifications

Google IT Automation with Python Specialization  – Coursera
Python for Data Science and Machine Learning  – Udemy
Google Analytics Certification  – Google Digital Academy
Introduction to Git and GitHub – Coursera
Core Java Basics  – upGrad
Publications


A Study on Real Time Video Analysis for Vehicle Traffic Movement
International Journal of Engineering Research in Computer Science and Engineering (IJERCSE)
December 12, 2022

Extra Curriculars

• Organized and led a successful 24hr hackathon as a part of AIML club, DSATM .
• Led as Head of the Technical Club, orchestrating successful induction program s for 300+
freshmen  students .
• Spearheaded coordination of  club activities, fostering technical skill development and
collaboration among members."""))
