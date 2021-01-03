# This class will remove all unwanted words. 

# importing supporting libraries
import re

class Common_Words():
	
	def purge_extra_characters(self, words_in_list):
			words = []
			for word in words_in_list:
					word = re.split(r'[,\s.]', word)
					words.append(word[0])
			return words
	
	def clean_word_list(self, words_in_list):
		word_and_count = {}
		len_count = 0
		# removing periods and commas at the end of each word
		words = self.purge_extra_characters(words_in_list)
		while len_count < len(words):
				print(len_count)
				word_count = 0
				#I assign the current_word to the current position of the word_count counter
				current_word = words[len_count].lower()
				#I then loop through the words again seeing is certain conditions are met.
				for word in words:
						word = word.lower()
						if (current_word == word and current_word != 'and' and current_word != 'the' and current_word != 'The'
						and current_word != 'on' and current_word != 'of' and current_word != 'But' and current_word != 'from' and current_word != 'any'
						and current_word != 'nor' and current_word != 'this' and current_word != 'is' and current_word != 'by' and current_word != 'it'
						and current_word != 'take' and current_word != 'that' and current_word != 'but' and current_word != 'for'
						and current_word != 'these' and current_word != 'can' and current_word != 'or' and current_word != 'are'
						and current_word != 'did' and current_word != 'who' and current_word != 'say' and current_word != 'It'
						and current_word != 'rather' and current_word != 'in' and current_word != 'thus' and current_word != 'as'
						and current_word != 'do' and current_word != 'so' and current_word != 'will' and current_word != 'a'
						and current_word != 'not' and current_word != 'here' and current_word != 'whether' and current_word != 'Now'
						and current_word != 'altogether' and current_word != 'which' and current_word != 'to' and current_word != 'met'
						and current_word != 'what' and current_word != 'those' and current_word != 'always' and current_word != 'So'
						and current_word != 'Again' and current_word != 'And' and current_word != 'As' and current_word != 'Go'
						and current_word != 'well' and current_word != 'have' and current_word != 'has' and current_word != 'all'
						and current_word != 'must' and current_word != 'i' and current_word != 'my' and current_word != 'like'
						and current_word != 'me' and current_word != 'now' and current_word != 'shall' and current_word != 'with'
						and current_word != 'ever' and current_word != 'also' and current_word != 'be' and current_word != 'more'
						and current_word != 'upon' and current_word != 'no' and current_word != 'most' and current_word != 'could'
						and current_word != 'should' and current_word != 'come' and current_word != 'during' and current_word != 'been'
						and current_word != 'among' and current_word != 'toward' and current_word != 'there' and current_word != 'only'
						and current_word != 'become' and current_word != 'may' and current_word != 'need' and current_word != 'between'
						and current_word != 'every' and current_word != 'other' and current_word != 'yet' and current_word != 'let'
						and current_word != 'into' and current_word != 'about' and current_word != 'know' and current_word != 'was'
						and current_word != 'going' and current_word != 'very'  and current_word != 'it.s' and current_word != 'tell'
						and current_word != 'they.re' and current_word != 'because' and current_word != 'want' and current_word != 'never'
						and current_word != 'them' and current_word != 'many'  and current_word != 'just' and current_word != 'don.t'
						and current_word != 'big' and current_word != 'when'  and current_word != 'it.' and current_word != 'your'
						and current_word != 'said,' and current_word != 'he'  and current_word != 'way,' and current_word != 'we.ve'
						and current_word != 'back' and current_word != 'that.s'  and current_word != 'at' and current_word != 'we.re'
						and current_word != 'over' and current_word != 'new'  and current_word != 'i.ve' and current_word != 'got'
						and current_word != 'look' and current_word != 'what.s' and current_word != 'were' and current_word != '\x19s'
						and current_word != '' and current_word != '\x19re' and current_word != '(applause.)' and current_word != '\x14'
						and current_word != 'an' and current_word != '\x14' and current_word != 'make' and current_word != 'bring'
						and current_word != 'much' and current_word != 'get' and current_word != 'than' and current_word != 'even'
						and current_word != 'think' and current_word != 'really' and current_word != 'right' and current_word != 't'
						and current_word != 'remember' and current_word != 'up' and current_word != 'didn.t' and current_word != 'right.'
						and current_word != 'know,' and current_word != 'folks.' and current_word != 'go' and current_word != 'see'
						and current_word != 'lot' and current_word != 'out' and current_word != 'if' and current_word != 'had'
						and current_word != 'audience' and current_word != '[laughter]' and current_word != 'both' and current_word != 'something'
						and current_word != 'mr.' and current_word != 'that’s' and current_word != 'it’s' and current_word != 'doing'
						and current_word != '(applause)' and current_word != 'better' and current_word != 'way' and current_word != "we're"
						and current_word != '—' and current_word != 'said' and current_word != '(applause' and current_word != 'today'
						and current_word != '\x19t' and current_word != 'lower' and current_word != 'percent' and current_word != 'again'
						and current_word != 'long' and current_word != 'time' and current_word != 'tonight' and current_word != 'its'
						and current_word != 'am' and current_word != '\x19ve' and current_word != 'his' and current_word != '--'
						and current_word != '(laughter' and current_word != 'don’t' and current_word != 'some' and current_word != 'we’re'
						and current_word != 'where' and current_word != 'would' and current_word != 'under'):
								word_count += 1
								if (word_count >= 10):
										word_and_count[current_word] = word_count
				len_count += 1
		return word_and_count