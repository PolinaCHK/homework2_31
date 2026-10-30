import string

text = input("Введите текст: ")
# text = "Дом, в котором мы живём, — это не просто дом. В доме живут люди, и люди эти делают дом домом. Без людей дом — просто стены, а стены без дома и без людей — уже не дом, а коробка.".lower()

simbols = []

for i in text:
	if i.isalpha() == False and i not in simbols:
		simbols.append(i)

for simbol in simbols:
	text = text.split(simbol)
	text =  ' '.join(text) 

new_text = text.split( )

dict_meet = {}

for word in new_text:
	if word not in dict_meet:
		dict_meet[word] = (-1)*new_text.count(word)

longest = ''
biggest_len = -1
dict_len = {}

for word in dict_meet:
	if len(word) not in dict_len:
		dict_len[len(word)] = (-1)*dict_meet[word]
		if len(word) > biggest_len:
			biggest_len = len(word)
			longest = word
	else:
		dict_len[len(word)] += (-1)*dict_meet[word]
		if len(word) > biggest_len:
			biggest_len = len(word)
			longest = word
	
srt_dc = sorted( dict_meet , key = lambda x: ( dict_meet[x], x) ) #srt_dc_2 = sorted(dict_meet.items(), key=lambda items:( items[1],items[0]) )

print(f"Всего слов: {len(new_text)}, из них уникальных: {len(set(new_text))} ")
print(f"Топ-5 слов: {srt_dc[0]} ({(-1)*dict_meet[srt_dc[0]] }),  {srt_dc[1]} ({(-1)*dict_meet[srt_dc[1]] }),  {srt_dc[2]} ({(-1)*dict_meet[srt_dc[2]] }),  {srt_dc[3]} ({(-1)*dict_meet[srt_dc[3]] }),  {srt_dc[4]} ({(-1)*dict_meet[srt_dc[4]] })") #(srt_dc_2[0][0],(-1)*srt_dc_2[0][1])
print(f"Самое длинное слово: {longest}")
print(f"Слова по длина: {dict_len}")

