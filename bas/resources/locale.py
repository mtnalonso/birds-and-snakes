import bas.config as config
import bas.resources.locale.languages.en as en
import bas.resources.locale.languages.es as es


def get_locale_data():
    if config.language == 'en':
        return en.locale
    if config.language == 'es':
        return es.locale
    return en.locale


default_locale_data = en.locale
locale_data = get_locale_data()


def locale(tag_name):
    tag_value = locale_data.get(tag_name)
    if tag_value is None:
        tag_value = default_locale_data.get(tag_name)
    return tag_value
