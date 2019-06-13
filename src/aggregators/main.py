import json
import sys
from extractor_diepresse import DiePresseExtractor
from extractor_krone import KroneExtractor
from extractor_unzensuriert import UnzensuriertExtractor
from extractor_sn import SnExtractor


def call_extractor():
    # read and parse json string to json
    
    json_str = sys.stdin.readline()
    data = json.loads(json_str)   

    html = data['content']

    if data['magazine'] == 'kurier':
        extractor = DiePresseExtractor(html)
    elif data['magazine'] == 'krone':
        extractor = KroneExtractor(html)
    elif data['magazine'] == 'diepresse':
        extractor = DiePresseExtractor(html)
    elif data['magazine'] == 'unzensuriert':
        extractor = UnzensuriertExtractor(html)
    elif data['magazine'] == 'sn':
        extractor = SnExtractor(html)

    if extractor != None:
        datadoc = extractor.extract_data()

        # build json for elasticsearch:
        el_data = {
            'id': data['id'],
            'index': '{}'.format(data['directory'].replace('/', '-')),
            **datadoc
        }
        print(json.dumps(el_data))
    else:
        raise Exception('Unknown magazine')


if __name__ == "__main__":
    call_extractor()
