from replit import db
import utils
from random import randint

class InsultManager:
    @staticmethod
    def get_all():

        insults_dict = {}
        for key in db.prefix('insult_'):
            insults_dict[utils.remove_prefix('insult', key)] = db[key]

        return insults_dict

    @staticmethod
    def list_insults(_):
        return utils.format_dict_to_display(InsultManager.get_all(
        )) or "Aucune insulte est presente actuellement"

    @staticmethod
    def delete_insult(key):
        key = "insult_" + key
        insult = db[key]
        del db[key]
        return "La supression de : " + insult + " a fonctionné !"

    @staticmethod
    def add_insult(insult):

        insults = list(db.prefix('insult_'))

        last_element = 'insult_0' if len(insults) == 0 else insults[-1]

        db["insult_" +
           str(int(utils.remove_prefix('insult', last_element)) + 1)] = insult
        return "L'ajout de : " + insult + " a fonctionné !"

    @staticmethod
    def send_insult(name):
      insult_keys = db.prefix('insult_')

      selected_insult = insult_keys[randint(0, len(insult_keys) - 1)]
      return db[selected_insult].replace('#', name.upper())