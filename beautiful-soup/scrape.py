import requests

webpage = requests.get(
    'https://content.codecademy.com/courses/beautifulsoup/shellter.html')

print(webpage.text)
print(webpage.content)
