import requests
import re

url = "https://strongmanarchives.com/results.php?division=M"  
response = requests.get(url)

def getCompetitionList():
	if response.status_code == 200:
	    html_content = response.text

	    # get rid of single event contests
	    pattern = r'<div id="Single-Event" class="tabcontent">.*?</div>'
	    html_content = re.sub(pattern, '', html_content, flags=re.DOTALL)

	    # get all competition urls
	    pattern = r'href="([^"]*)"'
	    hrefs = re.findall(pattern, html_content)
	    contests = list(filter(lambda url: 'viewContest' in url, hrefs))

	    # remove duplicate
	    new_contests = []
	    for item in contests :
	    	if item not in new_contests:
	    		new_contests.append(item)

	    contests = new_contests

	    return contests
	else:
	    print("Failed to fetch the webpage. Status code:", response.status_code)
	    return []

getCompetitionList()