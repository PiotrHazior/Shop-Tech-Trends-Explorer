import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

df = pd.read_csv('Data/Laptop.csv', delimiter=';')


def mean():
    avg_price = df['price'].mean()
    print(f'The average price of all laptop is: {avg_price}')
    
    
mean()

def median():
    median_price = df['price'].median()
    print(f"The median of all laptop prices is: {median_price}")
    
median()

def standard_deviation():
    std_dev_price = df['price'].std()
    print(f"Standard deviation price of all laptop is: {std_dev_price}")

standard_deviation()

def expensive_laptop():
    laptop = df[df['price'] == df['price'].max()] 
    result_brand = laptop[['brand', 'model']].to_string(header = False, index = False)
    result_price = laptop[['price']].to_string(header = False, index = False)
    print(f"The most expensive laptop is {result_brand} whose price is {result_price}.")
    
def cheapest_laptop():
    laptop = df[df['price'] == df['price'].min()]
    result_brand = laptop[['brand', 'model']].to_string(header = False, index = False)
    result_price = laptop[['price']].to_string(header = False, index = False)
    print(f"The most cheapest laptop is {result_brand} whose price is {result_price}.")
    
expensive_laptop()
cheapest_laptop()



def count_brand():
    brand_counts = df['brand'].value_counts()
    print("Counts of each brand:")
    print(brand_counts)
    
    # Creates a bar chart
    plt.bar(brand_counts.index, brand_counts)

    plt.xlabel('Brand laptop')
    plt.ylabel('Number of laptops')
    plt.title('Laptop number chart')

    plt.tight_layout()
    plt.show()
    
# count_brand()
    
# Filters laptops by processor:
def processor():
    processor_lst = ['Intel', 'AMD', 'Apple']
    print(processor_lst)
    user = input("Which processor from the list do you want a laptop with? ")
    
    if (user == "Intel"):
        intel = df[df['processor_brand'] == 'Intel']
        print("Here is a list of laptops with an Intel processor:")
        print(intel)
    
    elif (user == "AMD"):
        AMD = df[df['processor_brand'] == 'AMD']
        print("Here is a list of laptops with an AMD processor:")
        print(AMD)
    
    elif (user == "Apple"):
        apple = df[df['processor_brand'] == 'Apple']
        print("Here is a list of laptops with an apple processor:")
        print(apple)
    
# processor()


# Filters laptops by operating system
def os():
    os_lst = ['Windows', 'macOS', 'Chrome OS']
    print(os_lst)
    user = input("Which operating system from the list do you want a laptop with? If you don't want any operating system, type 'No system' : ")
    
    if (user == 'Windows'):
        windows = df[df['os'] == 'Windows']
        print("Below is a list of Windows laptops:")
        print(windows[['brand', 'model', 'os']]) 
    
    elif (user == 'macOS'):
        mac_os = df[df['os'] == 'macOS']
        print("Below is a list of macOS laptops:")
        print(mac_os[['brand', 'model', 'os']])
        
    elif (user == 'Chrome OS'):
        chrome = df[df['os'] == 'Chrome OS']
        print("Below is a list of Chrome OS laptops:")
        print(chrome[['brand', 'model', 'os']])
        
    elif (user == 'No system'):
        no_system = df[df['os'] == 'No system']
        print("Below is a list of laptops without operating system:")
        print(no_system[['brand', 'model', 'os']])
    
# os()


# Filters laptops by price
def price():
    user_min = int(input("Please provide the minimum price: "))
    user_max = int(input("Please provide the maximum price: "))
    
    laptops_filtered = df.loc[df['price'].between(user_min, user_max, inclusive='both')]
    print(laptops_filtered)
    
# price()


# Laptop price histogram
plt.hist(df['price'], bins=20, color="Green")
plt.xlabel("Price")
plt.ylabel("Number of laptops")
plt.title("Laptop price distribution")
plt.grid(True)
plt.show()


# Scatter plot laptops
df_sorted = df.sort_values(by='star_rating')
plt.scatter(df_sorted['price'], df_sorted['star_rating'], color="Green", alpha=0.5)
plt.xlabel("Price")
plt.ylabel("Star rating")
plt.title("Scatter plot: Price vs Star Rating")
plt.show()



df['star_rating'] = df['star_rating'].str.replace(',', '.').astype(float)
avg_star_rating_by_brand = df.groupby('brand')['star_rating'].mean()

plt.figure(figsize=(10, 5))
avg_star_rating_by_brand.plot(kind='bar', color='green')
plt.xlabel("Laptop brand")
plt.ylabel("Average star rating")
plt.title("Average star rating for each laptop brand")
plt.grid(axis='y')
plt.tight_layout()
plt.show()


# Calculates the sum, mean and median for 'ratings' column using NumPy
def calculates():
    ratings_array = df['ratings'].values
    
    # Counts the sum number of ratings
    sum_ratings = np.sum(ratings_array)
    print(f"The sum number of ratings is: {sum_ratings}")
    
    # Counts the average number of ratings
    avg_ratings = np.mean(ratings_array)
    print(f"The average number of ratings is: {avg_ratings}")
    
    # Counts the median number of ratings
    median_ratings = np.median(ratings_array)
    print(f"The median number of ratings is: {median_ratings}")
    
calculates()

# Finding the most frequently purchased laptop using NumPy
def popular_laptop_np():
    ratings_array = df['ratings'].values
    
    max_index = np.argmax(ratings_array)
    max_ratings = df.loc[max_index]
    result_brand = f"{max_ratings['brand']} {max_ratings['model']}"
    
    print(f"The most popular laptop is {result_brand} which has {max_ratings['ratings']} ratings.")
    
popular_laptop_np()

# Finding the least frequently purchased laptop using NumPy
def least_laptop_np():
    rating_array = df['ratings'].values
    
    min_index = np.argmin(rating_array)
    min_ratings = df.loc[min_index]
    result_brand = f"{min_ratings['brand']} {min_ratings['model']}"
    
    print(f"The least frequently purchased laptop is {result_brand} which has {min_ratings['ratings']} ratings.")   

least_laptop_np()


# Chart showing operating system
operating_system_counts = df['os'].value_counts()

plt.figure(figsize=(5, 5))
plt.pie(operating_system_counts, labels=operating_system_counts.index, autopct='%1.1f%%', startangle=50)
plt.title('Share of individual operating systems')
plt.axis('equal')
plt.show()