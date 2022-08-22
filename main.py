from pydoc import synopsis
import random
from jikanpy import Jikan
import pandas as pd

jikan = Jikan()

# Input list
animes = [['Naruto', 'Long', 'Action', 'Series'], 
		['Haikyuu', 'Long', 'Sports', 'Series'], 
		['Black Clover', 'Long', 'Action', 'Series'], 
		['March Comes Like A Lion', 'Short', 'Slice of life', 'Series'], 
		['Your Lie In April', 'Short', 'Slice of life', 'Series']]

#Inspiration
print('\n\n\n\nInstpiration: Tina Huang\nYoutube: https://www.youtube.com/c/TinaHuang1\nSpecific Video: https://www.youtube.com/watch?v=_xf1TMs0ysk\n\n\n\n')

def choice(list, mood):
	valid_choices = []
	for i in list:
		if i[2] == mood:
			valid_choices.append(i) #appends a valid choice to a list of valid options

	a = random.randint(0, len(valid_choices)-1) #chooses a random option
	return valid_choices[a][0] #selects the random option

#input mood
#input_length = input('What length would you like?\n')

input_type = input('Would you like anime or manga?\n').lower()
#input_year = input('What year would you like it to be from?\n')
input_rank = input('What rank would you like?\n').lower()
#input_series = input('Would you like to watch a series?\n')


#print(top['top'][0]['title'] + ', ' + top['top'][1]['title'])

#input_year
def decisions(input_type, input_rank):
	top = jikan.top(type=input_type)
	if input_rank == '':
		location = random.randint(1, 25)
	else:
		location = int(input_rank)-1
	title = top['top'][location]['title']
	if input_type == 'anime':
		anime_info = jikan.anime(top['top'][location]['mal_id'])
		synopsis = anime_info['synopsis']
		trailer = anime_info['trailer_url']
		return f'Title: {title}\nSynopsis: {synopsis}\nTrailer: {trailer}'
	else:
		manga_info = jikan.manga(top['top'][location]['mal_id'])
		synopsis = manga_info['synopsis']
		return f'Title: {title}\nSynopsis: {synopsis}'
  
print(decisions(input_type, input_rank))