from enum import Enum
import os
# Токент бота
TOKEN = "5000590462:AAH3nJ0C4mxuE-SySDyMqU01hsE9Rw9N33M"
# Файл базы данных Vedis
db_file = "db.vdb"

# Ключ записи в БД для текущего состояния
CURRENT_STATE = "CURRENT_STATE"

SENTENCE = "SENTENCE"

cur_path = os.path.dirname(os.path.abspath(__file__))

# Состояния автомата
class States(Enum):
    STATE_START = "STATE_START"  # Начало нового диалога
    STATE_FIRST_WORD = "STATE_FIRST_WORD"
    STATE_SECOND_WORD = "STATE_SECOND_WORD"
    STATE_THIRD_WORD = "STATE_THIRD_WORD"
    STATE_OPERATION = "STATE_OPERATION"
    STATE_SENTENCE = "STATE_SENTENCE"



def get_path(gender,type,color):
    name="img/"+gender+type+color+".jpg"
    return '/'.join([cur_path,name])
