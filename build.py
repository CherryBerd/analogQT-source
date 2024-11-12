import os
import sys
from PyInstaller.__main__ import run

# Определяем файлы и параметры
script_name = 'analogQT.py'
additional_files = [
    'colormodem.py',      # Файл
    'color_modem'         # Директория
]
output_name = 'analogQT.exe'

# Формируем аргументы для PyInstaller
args = [
    '--onefile',           # Создать один исполняемый файл
    '--windowed',         # Убрать консольное окно
    '--add-data',         # Добавить дополнительные файлы
    f'{additional_files[0]};.',  # colormodem.py
    '--add-data',
    f'{additional_files[1]};color_modem',  # Директория color_modem
    script_name            # Основной скрипт
]

# Запускаем PyInstaller
run(args)
