from bas.db.database import db
from bas.db.model.character_class import CharacterClass
from bas.db.model.magic_school import MagicSchool
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


def populate_character_classes():
    class_names_en = [
        'Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin',
        'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard'
    ]

    class_names_es = [
        'Bárbaro', 'Bardo', 'Clérigo', 'Druida', 'Guerrero', 'Monje',
        'Paladín', 'Explorador', 'Hechicero', 'Brujo', 'Mago'
    ]

    class_names = {'en': class_names_en, 'es': class_names_es}

    for class_name in class_names[config.language]:
        character_class = CharacterClass(class_name)
        db.session.add(character_class)
    db.session.commit()
    print('[+] All character classes added to the database.')


def populate_schools_of_magic():
    school_names_en = [
        'Abjuration', 'Conjuration', 'Divination', 'Enchantment',
        'Evocation', 'Illusion', 'Necromancy', 'Transmutation'
    ]

    school_names_es = [
        'Abjuración', 'Conjuración', 'Adivinación', 'Encantamiento',
        'Evocación', 'Ilusión', 'Nigromancia', 'Transmutación'
    ]

    school_names = {'en': school_names_en, 'es': school_names_es}

    for school_name in school_names[config.language]:
        school = MagicSchool(school_name)
        db.session.add(school)
    db.session.commit()
    print('[+] All schools of magic added to the database')


def populate_all():
    populate_races()
    populate_character_classes()
    populate_schools_of_magic()
