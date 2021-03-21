from NameManager import NameManager
from InsultManager import InsultManager

#names_commands = ['$add_name', '$del_name', '$list_names']

commands = {
    '$add_name': NameManager.add_name,
    '$del_name': NameManager.delete_name,
    '$list_names': NameManager.list_names,
    '$add_insult': InsultManager.add_insult,
    '$del_insult': InsultManager.delete_insult,
    '$list_insults': InsultManager.list_insults,
}
