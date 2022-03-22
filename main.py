import requests

url = 'https://yesno.wtf/api'
req = requests.get(url)
output = req.json()
answer = output['answer']
image = output['image']

if answer == 'yes':
    print('Hell yea do it!!')
    print(image)
elif answer == 'maybe':
    print('I don\'t know, maybe...')
    print(image)
else:
    print('Nope i wouldn\'t do that')
    print(image)