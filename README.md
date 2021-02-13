# MagicLinkApp

MagicLinkApp creates a magic link for a specific user and emails him the link. After clicking a link user becomes authenticated until he clicks logout. There is also a counter of how many times a user clicked the link, or pasted it into the browser.

# Technologies used:

  - Python
  - Django
  - bootstrap4
  - crispyforms
  - environ (for the email account configuration and the secret key. env file was not included in this repo)
  - gunicorn for the web deployment on heroku

