from bas.db.database import db
from bas.db.model.character_class import CharacterClass
from bas.db.model.condition import Condition
from bas.db.model.game_state import GameState
from bas.db.model.game_state import GameState
from bas.db.model.language import Language
from bas.db.model.level import Level
from bas.db.model.magic_school import MagicSchool
from bas.db.model.race import Race
from bas.db.model.story import Story
import bas.db.model.game_state as game_state
import bas.config as config


def populate_races():
    races = []
    races.append(Race('dragonborn', 30))
    races.append(Race('dwarf', 25))
    races.append(Race('elf', 30))
    races.append(Race('gnome', 25))
    races.append(Race('half-elf', 30))
    races.append(Race('half-orc', 30))
    races.append(Race('hafling', 30))
    races.append(Race('human', 30))
    races.append(Race('tiefling', 30))

    for race in races:
        db.session.add(race)
    db.session.commit()
    print('[+] All races added to the database.')


def populate_languages():
    languages = []
    languages.append(Language('common'))
    languages.append(Language('draconic'))
    languages.append(Language('dwarvish'))
    languages.append(Language('elvish'))
    languages.append(Language('gnomish'))
    languages.append(Language('orc'))
    languages.append(Language('hafling'))
    languages.append(Language('infernal'))

    for language in languages:
        db.session.add(language)
    db.session.commit()
    print('[+] All languages added to the database.')


def populate_character_classes():
    class_names = [
        'barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk', 'paladin',
        'ranger', 'rogue', 'sorcerer', 'warlock', 'wizard'
    ]

    for class_name in class_names:
        character_class = CharacterClass(class_name)
        db.session.add(character_class)
    db.session.commit()
    print('[+] All character classes added to the database.')


def populate_conditions():
    condition_names = [
        'blinded', 'charmed', 'deafened', 'frightened', 'grappled',
        'incapacitated', 'invisible', 'paralyzed', 'petrified', 'poisoned',
        'prone', 'restrained', 'stunned', 'unconscious', 'exhaustation'
    ]

    for condition_name in condition_names:
        condition = Condition(condition_name)
        db.session.add(condition)
    db.session.commit()
    print('[+] All condition classes added to the database.')


def populate_schools_of_magic():
    school_names = [
        'abjuration', 'conjuration', 'divination', 'enchantment',
        'evocation', 'illusion', 'necromancy', 'transmutation'
    ]

    for school_name in school_names:
        school = MagicSchool(school_name)
        db.session.add(school)
    db.session.commit()
    print('[+] All schools of magic added to the database')


def populate_game_states():
    game_states = []

    game_states.append(GameState(game_state.INIT))
    game_states.append(GameState(game_state.AWAITING_CHARACTERS))
    game_states.append(GameState(game_state.AWAITING_START_CONFIRMATION))
    game_states.append(GameState(game_state.STARTED))

    for game_state_entity in game_states:
        db.session.add(game_state_entity)
    db.session.commit()
    print('[+] All game states added to the database')


def populate_test_story():
    story = Story('Test Story', '\nblah\nblah\nblah\nmistery introduction\n\n')
    level = Level('Test Level')
    story.start_level = level
    db.session.add(story)
    db.session.add(level)
    db.session.commit()
    print('[+] Test level added to the database')


def populate_all():
    populate_races()
    populate_languages()
    populate_character_classes()
    populate_conditions()
    populate_schools_of_magic()
    populate_game_states()
    populate_test_story()
