from bas.db.database import db
from bas.db.model.race import Race


def populate_races():
    race_names = [
            'Dwarf', 'Elf', 'Hafling', 'Human', 'Dragonborn', 'Gnome',
            'Half-Elf', 'Half-Orc', 'Tiefling'
    ]

    for race_name in race_names:
        race = Race(race_name)
        db.session.add(race)
    db.session.commit()
    print('[+] All races added to the database.')


def populate_all():
    populate_races()
