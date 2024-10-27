


from flask import Flask, render_template
from flask import send_from_directory
import os 


app = Flask(__name__)






@app.route('/')
def home():
    # Your personal information
    personal_info = {
        'name': 'Tasnia Haque',
        'title': 'Machine Learning Researcher',
        'email': 'tasniahaque18@gmail.com',
        'location': 'Dhaka, Bangladesh',
        'phone': '+8801307082921',
        'about': 'Hi this is Tasnia strongly passionate on Machine Learning technology specially in generative AI and LLMs.'
    }
    
    # Experience data
    experience = [
        {
            'title': 'Machine Learning Researcher',
            'company': 'United International University',
            'location': 'Dhaka, Bangladesh',
            'period': 'May 2024 - Present',
            'description': 'Build reallife application using AI, Generative AI model, Use GEMINI, OPEN AI API, open source model LAMA2,3 API in various business solution'
        },
        {
            'title': 'Junior Machine Learning Engineer',
            'company': '4P Marketing Consultancy Ltd.',
            'location': 'Dhaka,Bangladesh',
            'period': 'Feb 2023 - March 2024',
            'description': 'Building cutting edge LLMs for innovative solutions. Generative AI, LLMs, GPT, Decentralized AI'
        },
        {
            'title': 'Machine Learning Intern',
            'company': 'Code Alpha Ltd',
            'location': 'Lucknow,India',
            'period': 'October 2022 -Feb 2023 ',
            'description': 'Develop and Deploy Models with Keras ,Pytorch and Tensorflow'
        }

    ]
    
    # Education data
    education = {
        'degree': 'BSc in Computer Science and Engineering',
        'institution': 'Rajshahi University of Engineering and Technology (RUET)',
        'period': '2018 - 2023',
        'cgpa': '3.34'
    }
    
    # Projects data
    projects = [
        {
            'name': 'Breast Cancer prediction',
            'skills': 'ML,Python,NLP',
            'description': 'Advanced LLM-based project'
        },
        {
            'name': 'Heart Diseases Detector',
            'skills': 'GPT,hybrid model,keras,Tensorflow',
            'description': 'AI Automated Detection system'
        }
    ]
    
    # Publications data
    publications = [
        {
            'title': 'Enhanced Brain Tumor Classification Using Hybrid CNN-Random Forest Methodology.',
            'publisher': 'IEEE Xplore'
        },
        {
            'title': 'BloodStein Hyperspectral Image Classification Using 3D CNN',
            'publisher': 'ICEEICT, IEEE Xplore'
        }
    ]
    
    # Awards data
    awards = [
        
        'Innovative Idea and project Contest RUET 2023 (7th in Final round)',
        'North Bengal Startup Summit 2023 Startup Idea contest Finalist (4th)',
        'Project showcasing - RUET CSE FEST 2022 (14th position)'
    ]

    return render_template('index.html', 
                         personal_info=personal_info,
                         experience=experience,
                         education=education,
                         projects=projects,
                         publications=publications,
                         awards=awards)







@app.route('/resume')
def download_resume():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(
        os.path.join(current_dir, 'static', 'resume'),
        'CV.pdf',
        as_attachment=True
    )













# if __name__ == '__main__':
#     app.run(debug=True)