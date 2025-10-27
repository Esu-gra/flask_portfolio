#Portfolio Personale — Esubalew Grappasonni#

Benvenuto nel mio portfolio personale sviluppato con *Flask*, *HTML*, *CSS* e *Python*.  
Questo progetto mostra le mie competenze tecniche, i progetti svolti durante il percorso ITS e la mia crescita come sviluppatore.

---

##Tecnologie utilizzate

- **Python 3.12**
- **Flask** — framework backend
- **HTML5 / CSS3 / JavaScript**
- **Font Awesome & DevIcons**
- **JSON** per la gestione dinamica delle repo github
- **Render** per il deploy in cloud

---

#Funzionalità principali

- Homepage con presentazione personale
- Sezione “Progetti” con repository GitHub collegati
- Sezione “Competenze” con visualizzazione grafica delle skill
- Tema *dark/light mode* dinamico
- Layout completamente *responsive*

---

#Struttura del progetto
flask_portfolio/
│
├── app.py # Applicazione Flask principale
├── projects.json # File JSON con le repo github

├── requirements.txt # Dipendenze Python
│
├── templates/ # Template HTML
│ ├── base.html
│ ├── home.html
│ ├── projects.html
│ ├── skills.html
│ └── contact.html (in pausa)
│
└── static/ # File statici
├── css/style.css
├── img/
└── files/CV_Esubalew_Grappasonni_data_2025.pdf



---

#Installazione locale

Per eseguire il progetto in locale:

bash:
--git clone https://github.com/Esu-gra/flask_portfolio.git,
--cd flask_portfolio,
--pip install -r requirements.txt,
--python app.py


Deploy online

Il progetto è attualmente online su Render:

https://flask-portfolio-5ajp.onrender.com


