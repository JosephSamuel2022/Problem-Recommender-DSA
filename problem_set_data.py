import requests
import pandas as pd
from scipy import sparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel


#requesting codeforces for problem set
request = requests.get("https://codeforces.com/api/problemset.problems")
request = request.json()

#creating dataframes to store problem data
problems_data = pd.DataFrame()
problem_statistics_data = pd.DataFrame()

for row in request['result']['problemStatistics']:
	problem_statistics_data = problem_statistics_data.append(row, ignore_index=True)

for row in request['result']['problems']:
	problems_data = problems_data.append(row, ignore_index=True)

#combining problem_statistics_data and problems_data into one common dataframe
problem_sets_data = pd.merge(problems_data, problem_statistics_data, on=['contestId', 'index'])

#cleaning data
#removing type and points column from the table
#they are of no use to us
problem_sets_data.drop(['points','type'], inplace=True,axis=1)

def convertToString(row):
	'''
	Converts the given row value to the string format
	'''
	return ' '.join(row)

#converting "tags" column to string format which is currently in list
#because we are using CountVectorizer

problem_sets_data['tags'] = problem_sets_data['tags'].apply(convertToString)

#adding an extra column vector which is used to calculate tdfidf matrix
problem_sets_data['vector'] = problem_sets_data['tags'] + ' ' + problem_sets_data['rating'].astype(str)


#exporting the file for later use
problem_sets_data.to_csv("problem_sets_data.csv", index=False)

#generating tfidf matrix and saving it for later use
tfidf = TfidfVectorizer(stop_words = 'english')
tfidf_matrix = tfidf.fit_transform(problem_sets_data['vector'])
sparse.save_npz("tfidf_matrix.npz", tfidf_matrix)