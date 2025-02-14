import argparse
import webbrowser
import json
import os
from pitchathonz.engine.parser import generate_html_from_prompt

def load_config():
    home_dir = os.path.expanduser("~")
    config_path = os.path.join(home_dir, ".pitchathonz.json")
    default_config_path = "src/pitchathonz/config/default.json"

    if not os.path.exists(config_path):
        with open(default_config_path, "r") as f:
            config = json.load(f)
        with open(config_path, "w") as f:
            json.dump(config, f, indent=4)
    else:
        with open(default_config_path, "r") as f:
            default_config = json.load(f)
        with open(config_path, "r") as f:
            config = json.load(f)
        for key, value in default_config.items():
            if key not in config:
                config[key] = value
        with open(config_path, "w") as f:
            json.dump(config, f, indent=4)
    
    return config

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", help="User prompt")
    parser.add_argument("-o", action="store_true", help="Open in browser")
    args = parser.parse_args()

    config = load_config()

    path = generate_html_from_prompt(args.prompt, config)
    print(path)
    if args.o:
        webbrowser.open(path)
