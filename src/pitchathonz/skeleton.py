import argparse
import webbrowser
import json
from pitchathonz.engine.parser import generate_html_from_prompt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", help="User prompt")
    parser.add_argument("-o", action="store_true", help="Open in browser")
    args = parser.parse_args()

    with open("src/pitchathonz/config/default.json", "r") as f:
        config = json.load(f)

    path = generate_html_from_prompt(args.prompt, config)
    print(path)
    if args.o:
        webbrowser.open(path)
