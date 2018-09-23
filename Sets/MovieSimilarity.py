dataset = [
    {
    'action' : ['hulk','thor','iron man','captain america',
                'ant man','deadpool','superman','batman',
                'justice league','wonder woman','avengers','terminator',
                'commando','race'],
    'comedy' : ['super bad','deadpool','3 idiots','dhamaal',
                'fukrey'],
    'horror' : ['the nun','the ring','saw','cube'],
    'biopic' : ['ms dhoni','bhaag milkha bhaag','dangal']
}
]
user_1 = {'hulk','thor','iron man','captain america',
          'ant man','deadpool','super bad','the ring','ms dhoni',
          'avengers'}

user_2 = {'superman','batman','justice league','wonder woman',
          'the nun','hulk','3 idiots','thor','deadpool','iron man'}

numer = user_1.intersection(user_2)
denom = user_1.union(user_2)

j = len(numer) / len(denom)

print("Similar movies are",numer)
print("Similarity is",j*100)

action = 0
comedy = 0
horror = 0
biopic = 0

for movie in numer:
    for data in dataset:
        if movie in data['action']:
            action += 1
        elif movie in data['horror']:
            horror += 1
        elif movie in data['biopic']:
            biopic += 1
        elif movie in data['comedy']:
            comedy += 1

print("Action : {}, Comedy : {}, Biopic : {}, Horror : {}".format(action, comedy, biopic, horror))

category = ""
if action > comedy and action > biopic and action > horror:
    category = "action"
elif comedy > action and comedy > biopic and comedy > horror:
    category = "comedy"

for movie in dataset[0][category]:
    if movie not in user_2:
        print("Recommended :",movie)