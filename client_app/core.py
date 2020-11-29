### create pandas dataframe from csv upload
#import io
#import pandas as pd


def generate():

    #sv_file = request.FILES['file']

    # let's check if it is a csv file
    #if not csv_file.name.endswith('.csv'):
    #           # return error

    #data_set = csv_file.read().decode('UTF-8')
    #io_string = io.StringIO(data_set) # create mem file
    #csv_df = pd.read_csv(io_string)# save csv_df in some global mem space


    ### create and save histograms
    #import pandas as pdimport numpy as npimport matplotlib.pyplot as plt

    # read csv_df from global space

    # select numeric columns and create/save histograms

    #csv_df.select_dtypes(include=[np.number]).hist()
    #plt.savefig('/Users/hash/Desktop/figure.pdf')


    ### convert to excel
    #csv_df.to_excel("ouput.xlsx")


    ### stats
    #df.describe().to_json()
    print('done!')
