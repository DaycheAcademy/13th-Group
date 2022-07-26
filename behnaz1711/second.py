par = """
City life is full of fun. There are parks and picnic spots to visit. We have cinema halls to see movies.
We have electricity which runs our factories, light and cools our home and helps us in seeing T.V.
There are all type of amenities like water, health check up and transport.
Sometimes circus shows and magic shows entertain the city people.
"""

words = [x.strip() for x in par.lower().replace(',', ' ').replace('.', ' ').split() if x.strip() != '']
unique_words = set(words)

print('number of words:', len(words))
print('number of unique words:', len(unique_words))

tobe = ['am', 'is', 'are']

tobe_count = [words.count(x) for x in tobe]
total_tobe_count = sum(tobe_count)

# for i in range(0, len(tobe)):
#     print(tobe[i], '=', tobe_count[i])

for ind, w in enumerate(tobe):
    print(f'{w} = {tobe_count[ind]}')

print('total tobe=', total_tobe_count)
