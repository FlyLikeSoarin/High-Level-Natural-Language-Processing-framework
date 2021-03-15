import configparser
import importlib
import os
import pathlib
import subprocess

from settings import database as db_settings

CONFIG_TO_OPTION = {
    'engine': '-e',
    'user': '-u',
    'password': '-P',
    'host': '-H',
    'port': '-p'
}


def load_schema():
    database = db_settings['database']
    settings = {k: v for k, v in db_settings.items() if k != 'database'}
    if not os.path.exists(os.path.join(os.getcwd(), '__schemas__')):
        print('Aborting: __schemas__ directory not found')
        exit(0)
    if not os.path.exists(schema_filename(database)):
        create_database_schema(database, settings)
    # Dynamically loading schema module
    spec = importlib.util.spec_from_file_location(
        schema_module_name(database),
        schema_filename(database)
    )
    schema_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(schema_module)
    return schema_module



def schema_filename(database):
    return os.path.join(os.getcwd(), f'__schemas__/{database}.py')


def schema_module_name(database):
    return f'__schemas__.{database}'


def settings_to_pwiz_options(settings):
    return ' '.join(
        [f"{CONFIG_TO_OPTION[k]} {v}" for k, v in settings.items()]
    )


def create_database_schema(database, settings):
    options = settings_to_pwiz_options(settings)
    result = subprocess.run(f'python3 -m pwiz {database} {options}'.split(), capture_output=True)
    with open(schema_filename(database), 'wb') as f:
        f.write(result.stdout)
    return schema_module_name(database)
