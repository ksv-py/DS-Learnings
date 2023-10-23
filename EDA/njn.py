import seaborn as sns
import numpy as pn
import matplotlib.pyplot as plt
import pandas as pd
df = sns.load_dataset('titanic')
# Exploratory Data Analysis (EDA)
# **In this analysis of the Titanic dataset, we explored various aspects of the passengers, including their gender distribution, survival rates, class distribution, travel companionship, embarkation towns, and age distribution.**
# GENDER DISTRIBUTION
sex_value = df.value_counts('sex')
plt.bar(sex_value.index, sex_value.values, label = ['Male','Female'],color = ['c','pink'])
plt.xlabel('SEX/GENDER')
plt.ylabel('Gender Count')
plt.legend()
plt.title('GENDER DISTRIBUTION')
plt.show()
# Gender Distribution: We observed that there were more male passengers than females, with a difference of 263 between the two groups.
# SURVIVAL RATES
alive_ = df.value_counts('alive').sort_values()
alive_.index = ['Alive','Dead']
plt.bar(alive_.index, alive_.values, color = ['g','red'], label =['Alive','Dead'])
plt.ylabel('Count')
plt.legend()
plt.title('SURVIVAL RATES')
plt.ylim(0,600)
plt.show()
# Survival Rates: The analysis revealed that there were Less passengers who survived than those who didn't, with 342 individuals marked as 'Alive' and 549 as 'Dead'.
# CLASS DISTRIBUTION
class_count = df.value_counts('class').sort_index()
class_count_pie = [class_count.values[0],class_count.values[1],class_count.values[2]]
pie_label = ['First','Second','Third']
cols = ['c','pink','yellow']
plt.pie(class_count_pie, labels= pie_label,colors=cols, explode= (0,0.1,0), autopct='%1.1f%%', startangle = 140)
plt.title('CLASS DISTRIBUTION')
plt.show()
# Class Distribution: The majority of passengers were traveling in the 'Third' class, followed by the 'First' and 'Second' classes. The distribution of passengers across these classes was approximately 24.2% in First Class, 20.7% in Second Class, and 55.1% in Third Class.
# TRAVEL COMPANIONSHIP
sex_alone_data = (df[df['alone']==True].groupby(['sex'], as_index = False)['alone'].count().reset_index())
plt.bar(sex_alone_data['sex'], sex_alone_data['alone'], color = ['pink','c'])
plt.xlabel('GENDER/SEX')
plt.ylabel('Count')
plt.title('Travel Companionship')
plt.ylim(0,450)
plt.show()
# Travel Companionship: It was interesting to note that a significant number of passengers traveled alone, and the majority of them were male, accounting for 411 out of 537 individuals.
# EMBARK TOWNS
town = df.value_counts('embark_town')
label = ['Southampton','Cherbourg','Queenstown']
plt.pie(town, colors= cols, labels = label, autopct='%1.1f%%', explode= (0,0,0.1), startangle = 140)
plt.title('Embark Towns')
plt.show()
# Embarkation Towns: Passengers mostly boarded the Titanic from Southampton, followed by Cherbourg and Queenstown. The distribution was roughly
# Southampton: 72.4% of passengers,
# Cherbourg: 18.9% of passengers,
# Queenstown: 8.7% of passengers.
# AGE DISTRIBUTION
age_data = df.value_counts('age')
plt.hist(age_data, bins=20, color = 'c',edgecolor='k', label ='Bins = 20')
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Age Distribution')
plt.legend()
plt.ylim(0,35)
plt.show()


sns.kdeplot(age_data, fill=True)
plt.xlabel('Age')
plt.ylabel('Density')
plt.title('Age Distribution (Kernel Density)')
plt.show()

