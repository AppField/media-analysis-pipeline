import json
import sys
from transformer_diepresse import DiePresseTransformer
from transformer_krone import KroneTransformer
from transformer_unzensuriert import UnzensuriertTransformer
from transformer_sn import SnTransformer


def call_transformer():
    # read and parse json string to json
    
    json_str = sys.stdin.readline()
    data = json.loads(json_str)   

    html = data['content']

    if data['magazine'] == 'kurier':
        transformer = DiePresseTransformer(html)
    elif data['magazine'] == 'krone':
        transformer = KroneTransformer(html)
    elif data['magazine'] == 'diepresse':
        transformer = DiePresseTransformer(html)
    elif data['magazine'] == 'unzensuriert':
        transformer = UnzensuriertTransformer(html)
    elif data['magazine'] == 'sn':
        transformer = SnTransformer(html)

    if transformer != None:
        datadoc = transformer.extract_data()

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
    call_transformer()
