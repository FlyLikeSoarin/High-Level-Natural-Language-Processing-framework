import configparser
import pathlib
import subprocess

CONFIG_TO_OPTION = {
    'user': '-u',
    'password': '-P',
    'host': '-H',
    'port': '-p'
}

def  config_to_pwiz_options(config):
    if 'Postgresql' in config:
        settings = config['Postgresql']
    if 'MySQL' in config:
        settings = config['MySQL']
    if 'Sqlite' in config:
        settings = config['Sqlite']
    options = ''
    for option in settings:
        options += f'{CONFIG_TO_OPTION[option.lower()]} {config[option]} '
    options += settings['database']
    return options


if __name__ == '__main__':
    cfg_path = (
        pathlib.Path(__file__)
        .parent
        .parent
        .joinpath('config/database.ini')
        .absolute()
    )
    config = configparser.ConfigParser()
    config.read_file(open(cfg_path))

    # Generate models
    subprocess.run((f'python -m pwiz ' + options).split())
