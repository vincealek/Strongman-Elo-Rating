from competition import *

class Athlete :
	def __init__(self, id, name, rating) :
		self.id = id
		self.name = name
		self.rating = 1400.0

def getAthleteList(competitions):
	url2 = "https://strongmanarchives.com/viewAthlete.php?id="
	athletes = []
	athlete_ids = set()
	for competition in competitions :
		for result in competition.results :
			athlete_ids.update(result)

	print(athlete_ids)

	cnt = 0
	for id in athlete_ids :
		response = requests.get(url2+str(id))

		html_content = response.text
		pattern = r'<title>(.*?)</title>'
		titles = re.findall(pattern, html_content)

		name = titles[0].replace('Strongman Archives - ', '');

		print(id, name)
		athletes.append(Athlete(int(id), name, 1400))

	return athletes
# print(athletes)