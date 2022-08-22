from pydoc import synopsis
import random
from jikanpy import Jikan

jikan = Jikan()

#Inspiration
#print('\n\n\n\nInstpiration: Tina Huang\nYoutube: https://www.youtube.com/c/TinaHuang1\nSpecific Video: https://www.youtube.com/watch?v=_xf1TMs0ysk\n\n\n\n')

print('DO NOT USE CAPS!!!')
input_type = input('Would you like anime or manga?\n')
input_rank = input('What rank would you like?\n')


def decisions(input_type, input_rank):
	top = jikan.top(type=input_type)
	trailer = ''
	if input_rank == '':
		rank = random.randint(1, 25)
	else:
		rank = int(input_rank)-1
	title = top['top'][rank]['title']
	if input_type == 'anime':
		anime_info = jikan.anime(top['top'][rank]['mal_id'])
		synopsis = anime_info['synopsis']
		trailer = anime_info['trailer_url']
	else:
		manga_info = jikan.manga(top['top'][rank]['mal_id'])
		synopsis = manga_info['synopsis']
	return f'Rank: {rank}\nTitle: {title}\nTrailer: {trailer}\nSynopsis: {synopsis}'
  
print(decisions(input_type, input_rank))