import pandas as pd
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import matplotlib.pyplot as plt3

# read pickle df
df = pd.read_pickle('pickled_df.pkl')

# Analysis 1: Authors Highest Priced Book
data1 = df.sort_values(['Book Price'], axis = 0, ascending = False)[:15]

# shortening book name col
data1['Book Name'] = data1['Book Name'].apply(lambda l : l.split( )[:3])
data1['Book Name'] = data1['Book Name'].apply(lambda l : ' '.join(l))

# plotting and setting plot parameters
data1.plot(x = 'Book Name', y = 'Book Price', kind = "bar")

plt1.title('Analysis 1: Authors Highest Priced Book')
plt1.xlabel('Book Names')
plt1.ylabel('Book Prices')

plt1.tight_layout()
plt1.savefig('name')
plt1.show()
plt1.close()

# Analysis 2: Top Rated Books with more than 1000 Users Rated

# eliminating books rated less than 1000
data2 = df[df['Users Rated'] > 1000]
data2 = data2.sort_values(['Book Rating'], axis = 0, ascending = False)[:15]

# shortening book name col
data2['Book Name'] = data2['Book Name'].apply(lambda l : l.split( )[:3])
data2['Book Name'] = data2['Book Name'].apply(lambda l : ' '.join(l))

# plotting and setting plot parameters
data2.plot(x = 'Book Name', y = 'Book Rating', kind = "bar")

plt2.title('Analysis 2: Top Rated Books with more than 1000 Users Rated')
plt2.xlabel('Book Names')
plt2.ylabel('Book Rating')

plt2.tight_layout()
plt2.savefig('name')
plt2.show()
plt2.close()

# Analysis 3: Book Ratings vs Users Rated

cols = ['Users Rated', 'Book Rating']
df['Rank'] = df.sort_values(cols, ascending=False).groupby(cols, sort=False).ngroup() + 1
df['Color'] = df['Rank'].apply(lambda l : 99-l)

df = df.sort_values(['Rank'],axis=0)
df.plot.scatter('Users Rated','Book Rating',s = df['Color'],c=df['Book Price'])

plt3.tight_layout()
plt3.savefig('name')
plt3.show()
plt3.close()    