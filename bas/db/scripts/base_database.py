from bas.db.database import db
from bas.db.model.alignment import Alignment
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


def populate_alignments():
    alignments = []
    alignments.append(Alignment('lawful_good'))
    alignments.append(Alignment('neutral_good'))
    alignments.append(Alignment('chaotic_good'))
    alignments.append(Alignment('lawful_neutral'))
    alignments.append(Alignment('neutral'))
    alignments.append(Alignment('chaotic_neutral'))
    alignments.append(Alignment('lawful_evil'))
    alignments.append(Alignment('neutral_evil'))
    alignments.append(Alignment('chaotic_evil'))

    for alignment in alignments:
        db.session.add(alignment)
    db.session.commit()
    print('[+] All alignments added to the database.')


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


def populate_races():
    races = []

    dragonborn = Race('dragonborn', 30)
    dragonborn.languages.append(db.find(Language, name='common'))
    dragonborn.languages.append(db.find(Language, name='draconic'))
    races.append(dragonborn)

    dwarf = Race('dwarf', 25)
    dwarf.languages.append(db.find(Language, name='common'))
    dwarf.languages.append(db.find(Language, name='dwarvish'))
    races.append(dwarf)

    elf = Race('elf', 30)
    elf.languages.append(db.find(Language, name='common'))
    elf.languages.append(db.find(Language, name='elvish'))
    races.append(elf)

    gnome = Race('gnome', 25)
    gnome.languages.append(db.find(Language, name='common'))
    gnome.languages.append(db.find(Language, name='gnomish'))
    races.append(gnome)

    half_elf = Race('half-elf', 30)
    half_elf.languages.append(db.find(Language, name='common'))
    half_elf.languages.append(db.find(Language, name='elvish'))
    races.append(half_elf)

    half_orc = Race('half-orc', 30)
    half_orc.languages.append(db.find(Language, name='common'))
    half_orc.languages.append(db.find(Language, name='orc'))
    races.append(half_orc)

    hafling = Race('hafling', 30)
    hafling.languages.append(db.find(Language, name='common'))
    hafling.languages.append(db.find(Language, name='hafling'))
    races.append(hafling)

    human = Race('human', 30)
    human.languages.append(db.find(Language, name='common'))
    races.append(human)

    tiefling = Race('tiefling', 30)
    tiefling.languages.append(db.find(Language, name='common'))
    tiefling.languages.append(db.find(Language, name='infernal'))
    races.append(tiefling)

    for race in races:
        db.session.add(race)
    db.session.commit()
    print('[+] All races added to the database.')


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
    populate_alignments()
    populate_languages()
    populate_races()
    populate_character_classes()
    populate_conditions()
    populate_schools_of_magic()
    populate_game_states()
    populate_test_story()
