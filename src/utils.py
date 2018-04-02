import os
import yaml

def load_config():
    """
    load project config written in yml
    :return: conf dict
    """

    project_root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    conf_path = os.path.join(project_root_dir, 'config', 'config.yml')
    with open(conf_path, 'r') as yml_file:
        configs = yaml.load(yml_file)
    return configs