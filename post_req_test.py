import requests


# Put url here
url = 'https://65.pfdo.ru/app/signin'
user_agent_value = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'

# Create session for authorization
session = requests.Session()
req = session.get(url, headers = {'User-Agent': user_agent_value})

# Introduce referer
session.headers.update({'Referer': url})

# Update user-agent
session.headers.update({'User-Agent': user_agent_value})

# Get xsrf value
_xsrf = session.cookies.get('_xsrf', domain='.pfdo.ru')

# Enter to profile with xsrf value
post_request = session.post(url, {
    'backUrl': 'https://65.pfdo.ru/',
    'username': input("Enter your username: "),
    'password': input("Enter your password: "),
    '_xsrf': _xsrf,
    'remember': 'yes',
})

# Save page to html file
with open('pfdo_success.html', 'w', encoding='utf-8') as f:
    f.write(post_request.text)
