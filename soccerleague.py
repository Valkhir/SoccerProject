import random
import copy


def check_avg_height(league):
	
	#for each team calculate avg height and save in the teams collection
	for team in league:
		sum_of_heights = 0
		for team_member in team['members']:
			sum_of_heights += int(team_member['Height (inches)'])
		team['avg_height'] = sum_of_heights / len(team['members'])
	
	#now compare each team with every other
	#return False if even one comparison yields a difference greater than 1
	#if the for-loop completes, we know we can return True 
	for team in league:
		for other_team in league:
			if (team['avg_height'] > (other_team['avg_height'] +1)) or (team['avg_height']  < (other_team['avg_height']  -1)):
				return False

	return True  

def assign_players(players_available,league):

	#take a collection of players and assign them round-robin style to teams
	while (players_available):
		for team in league:
			try:
				team['members'].append(players_available.pop())
		
			except IndexError:
				break

		for team in league:
			for player in team['members']:
				player['Team'] = team['team_name']
				player['First Practice'] = team['first_practice']

				
def sort_players(players,league):

	#approach:
	#(1) divide players into experienced and inexperienced
	#(2) then shuffle each group (specifically: a copy)
	#(3) for each group, assign players to teams in round-robin fashiom
	#(4) repeat (2) and (3) until teams are within 1 inch avg height
	
	#Initialize separate collectioms for experieced & inexperienced players  
	experienced_players = []
	inexperienced_players = []
	
	#divide players based on experience rating
	for player in players:
		if player['Soccer Experience'] == 'YES':
			experienced_players.append(player)
		else:
			inexperienced_players.append(player)
	
	#in the following block we keep randomly assigning players until
	#the average height of all teams is within 1 inch of each other
	avg_height_matches = False
	while not (avg_height_matches):
		for team in league:
			if (len(team['members']) > 0):
				team['members'] = []
				
		#we copy both player collections - else we won't be able to
		#do the assignment over after popping
		experienced_players_copy = copy.deepcopy(experienced_players)
		random.shuffle(experienced_players_copy)
		inexperienced_players_copy = copy.deepcopy(inexperienced_players)
		random.shuffle(inexperienced_players_copy)
		
		#assign players to teams by popping in order
		#first assign experienced, then inexperienced players 
		assign_players(experienced_players_copy,league)
		assign_players(inexperienced_players_copy,league)

		#finally, check if average heights are within 1 inch
		#if so, the while loop will terminate
		avg_height_matches = check_avg_height(league)
	
	#now update the players list based on the teams rosters

	players = []

	for team in league:
		for player in team['members']:
			players.append(player) 
	 	
def write_letter(player):
	#very tongue-in-cheek
	lettertext = "Dear citizen(s) {},\n\nyour offspring, {}, has been drafted to join the local soccer team, \nthe {}.\nWe are confident that you appreciate the opportunity your family has been\ngiven to contribute to the grand tradition of our national sport, and we \ntrust they will comport themselves in a manner that will bring glory to our\ngrand nation.\n\nPlease ensure that {} reports for indoctrination and basic training \non {}.\n\nFailure to fulfil your patriotic duty will NOT be tolerated.\n\nAll hail Soccer.\n"

	filled_in_letter = lettertext.format(player['Guardian Name(s)'],player['Name'],player['Team'],player['Name'],player['First Practice'])

	return filled_in_letter

def write_letters(league):
	#wrapper function to generate letters for all players, calling write_letter() for each individual player in each team
	for team in league:
		for player in team['members']:
			letter = write_letter(player)
			letter_file_name = '_'.join(player['Name'].split(' '))+'.txt'
			with open(letter_file_name,'w') as output_file:
				output_file.write(letter)



if __name__ == "__main__":
	
	#list of all players available, with each player represented as a dictionary
	#originally had code to read this from csv, rather than hardcode it, but the instructions seem to indicate this should be hardcoded.

	players=[
	{
	'Height (inches)': '42', 
	'Soccer Experience': 'YES', 
	'Guardian Name(s)': 'Jim and Jan Smith', 
	'Name': 'Joe Smith',
	'Team': '',
	'First Practice':''
	}, 
	{
	'Height (inches)': '36',
	'Soccer Experience': 'YES', 
	'Guardian Name(s)': 'Clara Tanner', 
	'Name': 'Jill Tanner',
	'Team': '',
	'First Practice':''
	}, 
	{
	'Height (inches)': '43', 
	'Soccer Experience': 'YES', 
	'Guardian Name(s)': 'Sara and Jenny Bon', 
	'Name': 'Bill Bon',
	'Team': '',
	'First Practice':''
	}, 
	{
	'Height (inches)': '45', 
	'Soccer Experience': 'NO', 
	'Guardian Name(s)': 'Wendy and Mike Gordon', 
	'Name': 'Eva Gordon',
	'Team': '',
	'First Practice':''
	}, 
	{
	'Height (inches)': '40', 
	'Soccer Experience': 'NO', 
	'Guardian Name(s)': 'Charles and Sylvia Gill', 
	'Name': 'Matt Gill',
	'Team': '',
	'First Practice':''
	}, 
	{
	'Height (inches)': '41', 
	'Soccer Experience': 'NO', 
	'Guardian Name(s)': 'Bill and Hillary Stein', 
	'Name': 'Kimmy Stein',
	'Team': '',
	'First Practice':''
	}, 
	{'Height (inches)': '45', 
	'Soccer Experience': 'NO', 
	'Guardian Name(s)': 'Jeff Adams', 
	'Name': 'Sammy Adams',
	'Team': '',
	'First Practice':''
	}, 
	{
	'Height (inches)': '42', 
	'Soccer Experience': 'YES', 
	'Guardian Name(s)': 'Heather Bledsoe', 
	'Name': 'Karl Saygan',
	'Team': '',
	'First Practice':''
	}, 
	{
	'Height (inches)': '44', 
	'Soccer Experience': 'YES', 
	'Guardian Name(s)': 'Henrietta Dumas', 
	'Name': 'Suzane Greenberg',
	'Team': '',
	'First Practice':''
	}, 
	{'Height (inches)': '41', 
	'Soccer Experience': 'NO', 
	'Guardian Name(s)': 'Gala Dali', 
	'Name': 'Sal Dali',
	'Team': '',
	'First Practice':''
	}, 
	{
	'Height (inches)': '39', 
	'Soccer Experience': 'NO', 
	'Guardian Name(s)': 'Sam and Elaine Kavalier', 
	'Name': 'Joe Kavalier',
	'Team': '',
	'First Practice':''
	}, 
	{
	'Height (inches)': '44', 
	'Soccer Experience': 'NO', 
	'Guardian Name(s)': 'Aaron and Jill Finkelstein', 
	'Name': 'Ben Finkelstein',
	'Team': '',
	'First Practice':''
	}, 
	{
	'Height (inches)': '41', 
	'Soccer Experience': 'YES', 
	'Guardian Name(s)': 'Robin and Sarika Soto', 
	'Name': 'Diego Soto',
	'Team': '',
	'First Practice':''
	}, 
	{
	'Height (inches)': '47', 
	'Soccer Experience': 'NO', 
	'Guardian Name(s)': 'David and Jamie Alaska', 
	'Name': 'Chloe Alaska',
	'Team': '',
	'First Practice':''
	}, 
	{
	'Height (inches)': '43', 
	'Soccer Experience': 'NO', 
	'Guardian Name(s)': 'Claire Willis', 
	'Name': 'Arnold Willis',
	'Team': '',
	'First Practice':''
	}, 
	{
	'Height (inches)': '44', 
	'Soccer Experience': 'YES', 
	'Guardian Name(s)': 'Thomas Helm and Eva Jones', 
	'Name': 'Phillip Helm',
	'Team': '',
	'First Practice':''
	}, 
	{
	'Height (inches)': '42', 
	'Soccer Experience': 'YES', 
	'Guardian Name(s)': 'Wynonna Brown', 
	'Name': 'Les Clay',
	'Team': '',
	'First Practice':''
	}, 
	{
	'Height (inches)': '45', 
	'Soccer Experience': 'YES', 
	'Guardian Name(s)': 'Hyman and Rachel Krustofski', 
	'Name': 'Herschel Krustofski',
	'Team': '',
	'First Practice':''
	}
	]

	sharks = {'team_name':'Sharks','avg_height':0.0,'members':[],'avg_height':0,'first_practice':'March 17, 3pm'}
	dragons = {'team_name':'Dragons','avg_height':0.0,'members':[],'avg_height':0,'first_practice':'March 17, 1pm'}
	raptors = {'team_name':'Raptors','avg_height':0.0,'members':[],'avg_height':0,'first_practice':'March 18, 1pm'}
	
	#instead of these collections, using classes would be more appropriate: 
	#each of the players could be an instance of a player class, each team 
	#could be an instance of a team class
	
	league = [sharks,dragons,raptors]
	sort_players(players,league)
	write_letters(league)


