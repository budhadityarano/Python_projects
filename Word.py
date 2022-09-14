import sys
import numpy as np
from PIL import Image
import wikipedia  #for more information on the topic
from wordcloud import WordCloud, STOPWORDS


# To get rid of common words we will use STOPWORDS

input_word =  str(input("Enter the word of which you want to get word cloud"))


title = wikipedia.search(input_word)[0]  # to serch the title from wikijpedia
page =  wikipedia.page(title)   # to search the page of the given topic
text = page.content    # to extract the content of the topic
print(text)

bg = np.array(Image.open("background.jpg")) # this is the background image
unwanted_words = set(STOPWORDS)

wrdcld = WordCloud(background_color="black", max_words=400, mask=bg, stopwords=unwanted_words)
wrdcld.generate(text)
wrdcld.to_file("sample.png")




#matrix = np.array([[1, 2, 3,], [4,5,6]])

#print(matrix)