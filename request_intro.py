import requests
import json

response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')
for ques in response.json()['items']:
    if ques['answer_count'] < 3 and ques['is_answered'] == False:
        print(ques['title'])
        print(ques['link'])
        print('')

