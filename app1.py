from flask import Flask, render_template_string

app = Flask(__name__)

portfolio_data = {
    "name": "Mohd Anas",
    "about": "Analytical AI/ML and Data Analytics student skilled in Python, SQL, data preprocessing, statistical analysis, machine learning, predictive modeling, dashboard development, and full-stack technologies.",
    "skills": [
        {"name": "Python", "level": "Expert", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"},
        {"name": "JavaScript", "level": "Intermediate", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg"},
        {"name": "React", "level": "Basic", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg"},
        {"name": "Machine Learning", "level": "Intermediate", "icon": "https://cdn-icons-png.flaticon.com/512/4140/4140048.png"},
        {"name": "SQL", "level": "Advanced", "icon": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg"}
    ],
    "projects": [
        {
            "name": "Dr. AI",
            "description": "Predicts disease by symptoms and suggests workout.",
            "technologies": "Python, TensorFlow, Flask",
            "logo": "https://cdn-icons-png.flaticon.com/512/3004/3004613.png"
        },
        {
            "name": "Crop Recommendations",
            "description": "Suggests best crop based on soil quality.",
            "technologies": "Machine Learning",
            "logo": "https://cdn-icons-png.flaticon.com/512/2909/2909763.png"
        }
    ],
    "education": [
        {"degree": "B.Tech Computer Science", "institution": "St Andrews Institute of Technology and Management", "year": "2023 - 2027"}
    ],
    "contact": {
        "email": "mohdanas212655@gmail.com",
        "phone": "+91 7310016307",
        "linkedin": "https://www.linkedin.com/in/mohd-anas-5b1a69293",
        "github": "https://github.com/mohdanas011",
        "instagram": "https://www.instagram.com/anas21.05",
        "twitter": "https://x.com/Anas3021"
    }
}

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{ name }} - Portfolio</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  <style>
    body { background-color: #000; color: #e6e6e6; font-family: 'Inter','Montserrat',sans-serif; scroll-behavior: smooth; }
    .navbar { background-color: #000 !important; }
    .hero { background: linear-gradient(135deg,#000 0%,#1a1a1a 100%); color:#fff; padding:120px 0; text-align:center; }
    .profile-pic { width:150px; height:150px; border-radius:50%; border:3px solid #0dcaf0; box-shadow:0 0 20px #0dcaf0; }
    .section { padding:70px 0; }
    .card { background-color:#111; border:1px solid #333; color:#e6e6e6; transition:0.3s; }
    .card:hover { transform:translateY(-5px); box-shadow:0 0 20px rgba(0,123,255,0.5); }
    .skill-icon { width:40px; margin-right:10px; }
    .project-logo { width:60px; margin-bottom:10px; }
    footer { background:#111; padding:20px 0; color:#999; text-align:center; }
    a { color:#0dcaf0; }
  </style>
</head>
<body>

  <!-- Navbar -->
  <nav class="navbar navbar-expand-lg navbar-dark fixed-top">
    <div class="container">
      <a class="navbar-brand fw-bold" href="#">{{ name }}</a>
    </div>
  </nav>

  <!-- Hero -->
  <section class="hero" id="hero">
    <div class="container">
      <h1 class="fw-bold">{{ name }}</h1>
    </div>
  </section>

  <!-- About -->
  <section id="about" class="section text-center">
    <div class="container">
      <h2 class="fw-bold mb-3 text-info">About Me</h2>
      <p class="w-75 mx-auto">{{ about }}</p>
    </div>
  </section>

  <!-- Skills -->
  <section id="skills" class="section bg-dark">
    <div class="container">
      <h2 class="fw-bold mb-4 text-info">Skills</h2>
      {% for skill in skills %}
      <div class="d-flex align-items-center mb-3">
        <img src="{{ skill.icon }}" class="skill-icon">
        <h5 class="mb-0">{{ skill.name }} - {{ skill.level }}</h5>
      </div>
      {% endfor %}
    </div>
  </section>

  <!-- Projects -->
  <section id="projects" class="section">
    <div class="container">
      <h2 class="fw-bold mb-4 text-info">Projects</h2>
      <div class="row">
        {% for project in projects %}
        <div class="col-md-6">
          <div class="card p-3 mb-3 text-center">
            <img src="{{ project.logo }}" class="project-logo">
            <h4>{{ project.name }}</h4>
            <p>{{ project.description }}</p>
            <p><strong>Tech:</strong> {{ project.technologies }}</p>
          </div>
        </div>
        {% endfor %}
      </div>
    </div>
  </section>

  <!-- Contact -->
  <section id="contact" class="section text-center">
    <div class="container">
      <h2 class="fw-bold mb-4 text-info">Contact</h2>
      <p><i class="fa-solid fa-envelope"></i> <strong>Email:</strong> {{ contact.email }}</p>
      <p><i class="fa-solid fa-phone"></i> <strong>Phone:</strong> {{ contact.phone }}</p>

      <p><i class="fa-brands fa-linkedin"></i> <a href="{{ contact.linkedin }}" target="_blank">LinkedIn Profile</a></p>
      <p><i class="fa-brands fa-github"></i> <a href="{{ contact.github }}" target="_blank">GitHub Repositories</a></p>
    </div>
  </section>

  <!-- Social -->
  <section id="social" class="section bg-dark text-center">
    <div class="container">
      <h2 class="fw-bold mb-4 text-info">Social Media</h2>
      <p><i class="fa-brands fa-instagram"></i> <a href="{{ contact.instagram }}" target="_blank">Instagram</a></p>
      <p><i class="fa-brands fa-twitter"></i> <a href="{{ contact.twitter }}" target="_blank">Twitter</a></p>
    </div>
  </section>

  <footer>
    <div class="container">
      © {{ name }} — Portfolio
    </div>
  </footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html_template, **portfolio_data)

if __name__ == "__main__":
    app.run(debug=True)
