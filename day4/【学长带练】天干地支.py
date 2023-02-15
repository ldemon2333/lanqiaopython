sky = ['jia','yi','bing','ding','wu','ji','geng','xin','ren','gui']
earth = ['zi','chou','yin','mao','chen','si','wu','wei','shen','you','xu','hai']

years = [sky[i % 10] + earth[i % 12] for i in range(60)]

name, year = 'gengzi', 2020
index = years.index(name)

input_year = int(input())
delt = input_year - year

print(years[(index + delt) % 60])