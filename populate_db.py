from app import app, db, Project

with app.app_context():
    db.create_all()

    p1 = Project(
        title="ITS Progettazione",
        description="Repository con esercizi e documenti sul modulo di progettazione software.",
        link="https://github.com/Esu-gra/Its_Progettazione",
        category="ITS"
    )

    p2 = Project(
        title="ITS Data Python",
        description="Raccolta di script, lezioni e progetti in Python realizzati durante il corso ITS.",
        link="https://github.com/Esu-gra/Its_Data_Python",
        category="Python"
    )

    p3 = Project(
        title="ITS Web 1",
        description="Esercizi e progetti sullo sviluppo web front-end con HTML, CSS e JavaScript.",
        link="https://github.com/Esu-gra/Its_web_1",
        category="Web"
    )

    p4 = Project(
        title="ITS Database",
        description="Lezioni e query SQL sul modulo database, con focus su progettazione e relazioni.",
        link="https://github.com/Esu-gra/Its_BD",
        category="Database"
    )

    db.session.add_all([p1, p2, p3, p4])
    db.session.commit()

    print("Database creato e popolato con successo!")
