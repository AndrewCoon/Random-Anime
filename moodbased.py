import random

# Input list
animes = [['Naruto', 'Long', 'Action', 'Series'], 
		['Haikyuu', 'Long', 'Sports', 'Series'], 
		['Black Clover', 'Long', 'Action', 'Series'], 
		['March Comes Like A Lion', 'Short', 'Slice of life', 'Series'], 
		['Your Lie In April', 'Short', 'Slice of life', 'Series']]


#Inspiration
print('\n\n\n\nInstpiration: Tina Huang\nYoutube: https://www.youtube.com/c/TinaHuang1\nSpecific Video: https://www.youtube.com/watch?v=_xf1TMs0ysk\n\n\n\n')

def choice(list, mood):
	choices = []
	for i in list:
		if i[2] == mood:
			choices.append(i) #appends a valid choice to a list of valid options

	a = random.randint(0, len(choices)-1) #chooses a random option
	return choices[a][0] #selects the random option

#input mood
mood = input('What mood are you in?\n')


print(f'You should watch {choice(animes, mood)}.')