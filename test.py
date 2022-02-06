import json

file_path = "sample.json"

questionnaire_dic = {}

with open(file_path, 'r', encoding="utf8") as j:
     contents = json.loads(j.read())
     #print(contents['pages'][0]['elements'])
     
#element_data = contents['pages'][0]['elements']

if not (contents is None) and "pages" in contents:
    for page in contents['pages']:
        if not page['name'] in questionnaire_dic:
            print(page['name'])
        #for each_element in element_data:
            #if each_element['type'] == 'html':
                #print(each_element)

