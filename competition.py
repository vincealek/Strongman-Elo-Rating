import requests
import re

class Competition:
	def __init__(self, id, name, date, type, results) :
		self.id = id
		self.name = name
		self.date = date
		self.type = type
		self.results = results

def getCompetitionList():

	url = "https://strongmanarchives.com/results.php?division=M"  
	url2 = "https://strongmanarchives.com/viewContest.php?id="
	response = requests.get(url)

	html_content = response.text

	# get rid of all single event contests
	pattern = r'<div id="Single-Event" class="tabcontent">.*?</div>'
	html_content = re.sub(pattern, '', html_content, flags=re.DOTALL)
	
	# get all table row
	pattern = r'<TR style="font-size:11px">.*?</tr>'
	contests_tr = re.findall(pattern, html_content, flags=re.DOTALL)

	competitions = []
	id_list = []
	cnt = 0
	for tr in contests_tr :
    	
		tds = tr.split('\n')

		# get contest date
		date = re.findall(r'<TD>(.*?)</TD>', tds[1])[0]

		# get contest id
		id = int(re.findall(r'id=(\d+)', tds[2])[0])

		# get contest type
		type = re.findall(r'<TD>(.*?)</TD>', tds[3])[0]

		# get competition html
		competition_html = requests.get(url2+str(id)).text

		# get name of competition
		pattern = r'<title>(.*?)</title>'
		name = re.sub(r'Strongman Archives - ', '', re.findall(pattern, competition_html)[0])
		# print(re.findall((r'Strongman Archives - \d{4} '), name))

		# get result_tables for competition standing - most competition only have one table, but WSM could have more
		pattern = r'<div>.*?</div>'
		result_tables = re.findall(pattern, competition_html, flags=re.DOTALL)
		results = []
		for table in result_tables :
			results.append([int(x) for x in re.findall(r'id=(\d+)', table)])
		
		print(date + " " + str(id) + " " + type + " " + name + " " + str(len(result_tables)))

		if id not in id_list :
			id_list.append(id)
			competitions.append(Competition(id, name, date, type, results))

		
		cnt += 1
		if(cnt == 2000) :
			break


	return competitions
