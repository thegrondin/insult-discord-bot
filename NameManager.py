from replit import db
import utils


class NameManager:
    @staticmethod
    def get_all():

        names_dict = {}
        for key in db.prefix('name_'):
            names_dict[utils.remove_prefix('name', key)] = db[key]

        return names_dict

    @staticmethod
    def list_names(_):
        return utils.format_dict_to_display(
            NameManager.get_all()) or "Aucun nom est present actuellement"

    @staticmethod
    def delete_name(key):
        key = "name_" + key
        name = db[key]
        del db[key]
        return "La supression de : " + name + " a fonctionné !"

    @staticmethod
    def add_name(name):

        names = list(db.prefix('name_'))

        last_element = 'name_0' if len(names) == 0 else names[-1]

        db["name_" +
           str(int(utils.remove_prefix('name', last_element)) + 1)] = name
        return "L'ajout de : " + name + " a fonctionné !"

    @staticmethod
    def name_in_message(message):
      
      name_keys = db.prefix('name_')
      
      for key in name_keys:
        if db[key].lower() in message.lower():

          return db[key]



