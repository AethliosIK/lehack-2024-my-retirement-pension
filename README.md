### My Retirement Pension - LeHack 2024

Here is the code of a challenges I provided for the Wargame (Public CTF) of the 2024 edition of the Hack which took place from July 5th to 7th.
You are now able to inspect the code and replay the challenge locally if you wish.

- Description : A new retirement pension reform is underway that will allow the state to save money through "artificial intelligence", however, it seems that a vulnerability will thwart it (and gain a few years' respite...).
- Category : Web
- Difficulty: Medium / Hard

### Start Guide :

```bash
cd lehack-2023-my-retirement-pension
cp .env.sample .env
docker-compose build
docker-compose up -d && sleep 10
docker-compose run meteo python3 manage.py migrate
docker-compose run chatgpt python3 manage.py migrate
# Go to http://localhost:8000
```

### .env:

```bash
DB_USERNAME=<Your Value>
DB_PASSWD=<Your Value>
DB_HOST=<Your Value>
DB_NAME=<Your Value>
DOMAIN_URL=<Your Value>
```

### Solution - poc.py

<details>
  <summary>Spoiler warning</summary>
  
  It seems that a modification of the URL of the request sent on the server side is possible on the `uuid` cookie, allowing to modify the value `retirement` and to modify the age of its retirement.
 
 - See the PoC file 
  
</details>
