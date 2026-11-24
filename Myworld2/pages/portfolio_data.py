"""
Everything written on the portfolio lives here. Edit the text, no HTML needed.

Projects can ALSO be managed from the Django admin (/admin/ -> Projects).
If the database has any projects, they replace the PROJECTS list below.

Images live in pages/static/site/img/. The hobby photos use hobbywatching.jpg,
hobbyjackstones.jpg, and hobbyreading.jpg. Transparent cut-outs look best because
the three photos overlap each other.
"""

PROFILE = {
    "name": "Norlina",
    "full_name": "Norlina M. Tupanan",
    "title": "Portfolio",
    "email": "norlinatupanan@gmail.com",
    "github_url": "https://github.com/norlinatupanan-droid/Norlina.git",
    "github_label": "github.com/norlinatupanan-droid",
    "university": "Palawan State University",
    "resume_url": "",   # e.g. "/static/site/resume.pdf" once you add the file
}

HERO = {
    "headline": ["Designing the web,", "simply beautiful."],
    "intro": "Hello! I'm a Computer Science Student passionate about Web Development and UI/UX Design. I love designing creative interfaces and building functional websites while continuously learning new technologies and improving my skills.",
    "card_left": {
        "title": "User-friendly by default",
        "text": "Clean, visually appealing websites that are easy to use.",
    },
    "card_right": {
        "title": "Design and code",
        "text": "Figma for the look, Django and HTML/CSS for the build.",
    },
    "badge": "design \u00b7 develop \u00b7 deliver \u00b7 ",
}

ABOUT = {
    "heading": "Hi, I'm Norlina.",
    "paragraphs": [
        "Hi, I'm Norlina! I am a Computer Science student who is still learning about web development and UI design.", 
        "I have basic knowledge of HTML, CSS, and Figma.",
        "I enjoy exploring new technologies, learning new skills, and improving myself as a future developer.",
    ],
    "chips": ["Website designer"],
    # (label, value); a value starting with "mailto:" or "http" becomes a link in the template
    "facts": [
        ("Studying at", "Palawan State University"),
        ("Focus", "Website and UI design"),
        ("Design tools", "Figma,"),
        ("Build with", "HTML, CSS"),
    ],
}

HOBBIES = {
    "heading": "Away from the screen",
    "text": "When I'm not designing , you'll find me watching, playing jackstones or reading.",
    "items": [
        {"id": "watching", "label": "Watching", "image": "site/img/hobbywatching.jpg"},
        {"id": "jackstones", "label": "Jackstones", "image": "site/img/hobbyjackstones.jpg"},
        {"id": "reading", "label": "Reading", "image": "site/img/hobbyreading.jpg"},
    ],
}

# Glossy 3D tiles (hero + toolkit). `glyph` picks the drawing in the template.
TOOLS = [
    {"id": "figma", "label": "Figma", "group": "Design", "glyph": "figma"},
    {"id": "django", "label": "Django", "group": "Build", "glyph": "dj"},
    {"id": "web", "label": "HTML and CSS", "group": "Build", "glyph": "code"},
    {"id": "video", "label": "Video editing", "group": "Creative", "glyph": "play"},
]

TOOLKIT = {
    "heading": "Tools I work with",
    "groups": [
        {"name": "Design", "items": ["Figma", "UI design"]},
        {"name": "Build", "items": ["Django", "HTML", "CSS"]},
        {"name": "Creative", "items": ["Video editing"]},
    ],
}

PROJECTS = [
    {
        "name": "HEALTH TRACKER",
        "description": "A health tracking application designed to help users monitor their wellness and daily health activities.",
        "role": "UI designer",
        "tech": ["Figma", "App design"],
        "image": "site/img/Health Tracker.png",
        "live_url": "", "repo_url": "",
    }
]

CONTACT = {
    "heading": "Let's build something remarkable together.",
    "text": "Tell me about your idea, your project or your team. I read every message.",
}
