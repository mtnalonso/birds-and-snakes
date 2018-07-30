from bas.db.database import db
from bas.db.model.race import Race
import bas.config as config


def populate_races():
    race_names_en = [
        'Dwarf', 'Elf', 'Hafling', 'Human', 'Dragonborn', 'Gnome', 'Half-Elf',
        'Half-Orc', 'Tiefling'
    ]

    race_names_es = [
        'Enano', 'Elfo', 'Mediano', 'Humano', 'Dracónico', 'Gnomo',
        'Semielfo', 'Semiorco', 'Tiefling'
    ]

    race_names = {'en': race_names_en, 'es': race_names_es}

    for race_name in race_names[config.language]:
        race = Race(race_name)
        db.session.add(race)
    db.session.commit()
    print('[+] All races added to the database.')


def populate_all():
    populate_races()
