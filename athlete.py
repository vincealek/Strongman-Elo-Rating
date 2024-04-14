from competition import *

class Athlete :
	def __init__(self, id, name, rating) :
		self.id = id
		self.name = name
		self.rating = 1400

athletes = []

url = "https://strongmanarchives.com"
contest_urls = getCompetitionList()

cnt = 0
athlete_urls = set()
for contest_url in contest_urls :
	response = requests.get(url+contest_url)
	print(url+contest_url)

	html_content = response.text
	pattern = r'href="([^"]*)"'
	hrefs = re.findall(pattern, html_content)
	athlete_urls.update(list(filter(lambda url: 'viewAthlete' in url, hrefs)))
	# print(athlete)
	cnt += 1
	if cnt == 10 :
		break

cnt = 0
for athlete_url in athlete_urls :
	response = requests.get(url+athlete_url)
	# print(url+athlete_url)

	html_content = response.text
	pattern = r'<title>(.*?)</title>'
	titles = re.findall(pattern, html_content)

	athlete_id =  int(athlete_url.replace('/viewAthlete.php?id=', ''))
	athlete_name = titles[0].replace('Strongman Archives - ', '');

	# print(athlete_id, athlete_name)
	athletes.append(Athlete(athlete_id, athlete_name, 1400))

print(athletes)