from MyFunc import *
import os


assert create_folder('111') == 'Папка создана!' and '111' in os.listdir()
assert copy_folder('111', '222') == 'Копия создана!' and '222' in os.listdir()
assert delete_folder('111') == 'Папка удалена!' or 'Папка с таким именем не найдена!'
assert delete_folder('222') == 'Папка удалена!' or 'Папка с таким именем не найдена!'

