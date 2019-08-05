import os
from os import path
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

mask = np.array(Image.open(path.join(d, "trump_head.png")))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white", max_words=2000, mask=mask,
               stopwords=stopwords, contour_width=3, contour_color='steelblue')

wc.generate(text)

#import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

wc.to_file(path.join(d, "trump.png"))

plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.figure()
plt.imshow(mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()

#wordcloud = WordCloud(max_font_size=40).generate(text)
#plt.figure()
#plt.imshow(wordcloud, interpolation="bilinear")
#plt.axis("off")
#plt.show()
