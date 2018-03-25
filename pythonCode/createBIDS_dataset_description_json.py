import json
from collections import OrderedDict

data= OrderedDict()
#General fields, shared with MRI BIDS and MEG BIDS:
#Required fields:
#name of the dataset
data['Name'] = ''

#The version of the BIDS standard that was used
data['BIDSVersion'] = '1.0.2'

#Recommended fields:
#what license is this dataset distributed under? The use of license name abbreviations is suggested for specifying a license. A list of common licenses with suggested abbreviations can be found in appendix III.
data['License'] = ''


#List of individuals who contributed to the creation/curation of the dataset
data['Authors'] = ['','','']

#who should be acknowledge in helping to collect the data
data['Acknowledgements'] = ''

#Instructions how researchers using this dataset should acknowledge the original authors. This field can also be used to define a publication that should be cited in publications that use the dataset
data['HowToAcknowledge'] = ''

#sources of funding (grant numbers)
data['Funding'] = ['','','']

#a list of references to publication that contain information on the dataset, or links.
data['ReferencesAndLinks'] = ['','','']

#the Document Object Identifier of the dataset (not the corresponding paper).
data['DatasetDOI'] = ''

root_dir = ''
project_label = 'templates'

dataset_json_folder = root_dir+project_label
dataset_json_name=dataset_json_folder+'/'+'dataset_description.json'

with open(dataset_json_name, 'w') as ff:
    json.dump(data, ff,sort_keys=False, indent=4)
