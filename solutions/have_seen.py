# -*- coding: utf-8 -*-
"""
Solution to iteration session exercise.

Created on Mon Apr  17 17:55:45 2016

@author: yoav@yoavram.com
"""

def have_seen():
    seen = set()
    seen_this = False
    while True:
        word = yield seen_this
        seen_this = word in seen
        seen.add(word)

text = """My father had a small estate in Nottinghamshire; I was the third of five
sons. He sent me to Emmanuel College in Cambridge at fourteen years old,
where I resided three years, and applied myself close to my studies;
but the charge of maintaining me, although I had a very scanty
allowance, being too great for a narrow fortune, I was bound apprentice
to Mr. James Bates, an eminent surgeon in London, with whom I continued
four years; and my father now and then sending me small sums of money, I
laid them out in learning navigation, and other parts of the mathematics
useful to those who intend to travel, as I always believed it would be,
some time or other, my fortune to do. When I left Mr. Bates, I went down
to my father, where, by the assistance of him, and my uncle John and
some other relations, I got forty pounds, and a promise of thirty
pounds a year, to maintain me at Leyden. There I studied physic two
years and seven months, knowing it would be useful in long voyages."""


if __name__ == '__main__':
	seen = have_seen()
	seen.send(None)

	text = text.lower().split()
	for word in text:
	    if seen.send(word):
	        print(word, end=" ")