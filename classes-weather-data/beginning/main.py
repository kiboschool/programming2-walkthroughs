import json


def main():
    with open('api_output.json', 'r') as f:
        all_data = json.load(f)

    for data in all_data['dataseries']:
        print(data['temp2m'])

main()
