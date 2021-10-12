import json

with open("AllPrintings.json", 'r') as f:
    cards = json.load(f)

#%%

import math

def str_to_int(name):
    return math.trunc(math.log(int(''.join([str(ord(s)) for s in name])))*10**14)

card_dict = {}
for collection, value in cards['data'].items():
    for card in value['cards']:
        if not card.get('isReprint'):
            name = card['faceName'] if card.get('faceName') else card['name']
            card_dict[str_to_int(name)] = {
                'name': name,
                'completeName': card['name'],
                'setCode': card['setCode'],
                'colorIdentity': card['colorIdentity'],
                'colors': card['colors'],
                'convertedManaCost': int(card['convertedManaCost']),
                'edhrecRank': int(card['edhrecRank']) if card.get('edhrecRank') else -1,
                'text': card['text'] if card.get('text') else "",
                'manaCost': card['manaCost'] if card.get('manaCost') else "",
                'power': card['power'] if card.get('power') else "",
                'toughness': card['toughness'] if card.get('toughness') else "",
                'rarity': card['rarity'],
                'supertypes': ';'.join(card['supertypes']),
                'subtypes': ';'.join(card['subtypes']),
                'types': ';'.join(card['types']),
                'keywords': card['keywords'] if card.get('keywords') else [],
                'loyalty': card['loyalty'] if card.get('loyalty') else -1,
                'layout': card['loyout'] if card.get('loyout') else "",
                }

#%%

import pandas as pd

df = pd.DataFrame().from_dict(card_dict).T
