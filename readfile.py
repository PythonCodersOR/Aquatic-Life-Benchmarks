# do one thing and do it well

# use pandas module to get data structures simular to R data frames
import pandas as pd, os

def readfile(str_file):
    df = pd.read_csv(str_file)
    return df

# try it out
# change this to the path that the file is located on your machine
str_path_main = 'C:\\Users\\kbranna\\Source\\Repos\\PythonCodersOR\\Aquatic-Life-Benchmarks'
str_file_data = 'Aquatic Life Benchmarks and Ecological Risk Assessments for Registered Pesticides  Pesticide Science and Assessing Pesticide Risks  US EPA (1).csv'
df = readfile(os.path.join(str_path_main, str_file_data))

# check out the object type
type(df)
# what are the dimensions
df.shape

# what are the coumn names
col_names = list(df)

for ii in range(0,df.shape[1]):
    col_names[ii]
# what's up with the last two names????
col_names[-2:]
