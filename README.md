# Codeforces Problem Recommendation

Codeforces Problem Recommendation is a project aimed at simplifying the process of finding appropriate programming challenges on the Codeforces platform. By leveraging natural language processing and machine learning techniques, the system generates tailored recommendations based on a user's past performance, problem-solving patterns, and coding preferences. This helps users enhance their coding abilities and excel in competitive programming.

## Introduction

Codeforces Problem Recommendation plays a crucial role in supporting programmers and coding enthusiasts on the Codeforces platform. As the Codeforces community continues to grow, users face challenges in finding suitable programming problems that match their skill level and areas of improvement. This project addresses the need for an efficient and personalized problem recommendation system, making it easier for users to find relevant challenges and enhance their coding skills.

## Technologies Used

- Dataset:
  - Codeforces API: The Codeforces API is used to interact with the Codeforces platform and retrieve relevant data such as problem sets and user submissions.

- Data Cleaning:
  - Pandas: Pandas library is utilized for data cleaning tasks, including preprocessing and filtering.

- Natural Language Processing:
  - TF-IDF: The TF-IDF technique is applied to transform problem descriptions into numerical vectors, allowing for the measurement of similarity between problem vectors.

- Machine Learning:
  - Scikit-learn: The Scikit-learn library is used for cosine similarity calculations, which help identify the most similar problems based on user input and previously solved problems.

- User Interface:
  - Flask: The Flask framework is used to develop the user interface, integrating Python, HTML, and CSS.

- Programming Language:
  - Python: The project is implemented using Python as the primary programming language.

## Implementation

### Codeforces API

The Codeforces API is integrated to interact with the Codeforces platform and retrieve relevant data. API requests are made to fetch problem sets, user submissions, and other information. This enables dynamic problem recommendations, access to user-specific submissions, and other operations using real-time Codeforces data.

### Dataset

The dataset used consists of 8686 records and includes columns such as 'contestId', 'index', 'name', 'tags', 'rating', 'solvedCount', and 'vector'. These columns provide information about the contest, problem index, name, descriptive tags, difficulty rating, number of successful attempts, and a transformed numerical representation of the problem description, respectively.

### Data Cleaning and Transformation using Pandas

The dataset is cleaned using the TF-IDF technique, a natural language processing method. TF-IDF represents each problem description or text field in a vectorized form, allowing for the identification of important terms and the removal of less informative ones (e.g., stopwords). This transformation results in a more compact and meaningful representation of the dataset, improving the effectiveness of subsequent recommendation algorithms.

### Cosine Similarity using Scikit-learn

Cosine similarity, implemented using the cosine_similarity function from the Scikit-learn library, is used to measure the similarity between problem vectors. It compares the cosine of the angle between two non-zero vectors in a vector space, providing similarity scores between -1 and 1. In the context of this project, cosine similarity helps identify similar problems based on their vector representations, enabling personalized recommendations and relevant problem retrieval.

## How to Run the Project

Visit : http://josephsamuelm2022.pythonanywhere.com/




