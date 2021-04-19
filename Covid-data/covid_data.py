# covid_data.py
# by Jonathan M.
# Date: April 12, 2021
# Description: This program will take CDC vaccination records cvs and return visualization
# File name: covid19_vaccinations_in_the_united_states.csv
# Title: COVID-19 Vaccinations in the United States
# Date created: Date generated: Mon Apr 12 2021 14:01:14 GMT-0700 (Pacific Daylight Time)

# Imports:
import csv
import pandas as pd
import matplotlib.pyplot as plt

filename = 'covid19_vaccinations_in_the_united_states.csv'

# Method #1
def method_1():
    with open(filename) as f:
        reader = csv.reader(f)
        title = next(reader)
        date_created = next(reader)
        header_row = next(reader)
        # print(header_row)


data = pd.read_csv(filename)
# print(data.head()) will print the first five lines in the loaded data.
# print(data.head())


def top_five_states_doses_delivered():
    # Sorting data by Total Doses Delivered in decending order:
    temp = data.sort_values('Total Doses Delivered', ascending=False)
    # Only keeping State/Territory/Federal Entity and Total Doses Delivered columns:
    temp[['State/Territory/Federal Entity', 'Total Doses Delivered']]
    # Only keeping top five entries:
    top_five = temp.head()

    # Setting State/Territory/Federal Entity as x axis and Total Doses Delivered as y axis:
    location = top_five["State/Territory/Federal Entity"]
    total_doses_delivered = top_five["Total Doses Delivered"]
    # Setting up the type of graph
    plt.bar(location, total_doses_delivered)
    # Setting up axis: if not told matplotlib will decide
    axis = plt.gca()
    axis.set_ylim([0, 30000000])

    # labeling axis:
    plt.xlabel('State/Territory/Federal Entity')
    plt.ylabel('Total Doses Delivered')
    plt.title('Top 5 States with Delivered Doses')
    # The following can be aded to rotate x ticks
    #plt.xticks(rotation = 90)
    plt.tight_layout()
    plt.savefig('top_five_states_doses_delivered.png')

    # Interactive program
    plt.show()


top_five_states_doses_delivered()
print(data)
