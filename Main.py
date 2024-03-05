import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_laptop = pd.read_csv('Data/Laptop.csv', delimiter=';')
df_smartphone = pd.read_csv('Data/Smartphone.csv', delimiter=';')


# Calculing mean, median and standard deviation of laptop prices using Pandas
def mean_laptop():
    avg_price = df_laptop['price'].mean()
    print(f'The average price of all laptop is: {avg_price}')
    

def median_laptop():
    median_price = df_laptop['price'].median()
    print(f"The median of all laptop prices is: {median_price}")
    
    
def standard_deviation_laptop():
    std_dev_price = df_laptop['price'].std()
    print(f"Standard deviation price of all laptop is: {std_dev_price}")
    
# mean_laptop()    
# median_laptop()
# standard_deviation_laptop()



# Calculing mean, median and standard deviation of smartphone prices using Pandas
def mean_smartphone():
    mean = df_smartphone['price'].mean()
    print(f"The average price of phones is {round(mean, 2)}.")


def median_smartphone():
    median = df_smartphone['price'].median()
    print(f"The median price of phones is {round(median, 2)}.")
    
def standard_deviation_smartphone():
    std_smartphone = df_smartphone['price'].std()
    print(f'The standard deviation price of phones is {round(std_smartphone, 2)}.')

mean_smartphone()
median_smartphone()
standard_deviation_smartphone()



# Finding the most expensive and cheapest laptop 
def expensive_laptop():
    laptop = df_laptop[df_laptop['price'] == df_laptop['price'].max()] 
    result_brand = laptop[['brand', 'model']].to_string(header = False, index = False)
    result_price = laptop[['price']].to_string(header = False, index = False)
    print(f"The most expensive laptop is {result_brand} whose price is {result_price}.")
    
def cheapest_laptop():
    laptop = df_laptop[df_laptop['price'] == df_laptop['price'].min()]
    result_brand = laptop[['brand', 'model']].to_string(header = False, index = False)
    result_price = laptop[['price']].to_string(header = False, index = False)
    print(f"The most cheapest laptop is {result_brand} whose price is {result_price}.")
    
# expensive_laptop()
# cheapest_laptop()


# Finding the most expensive and cheapest smartphone
def expensive_smartphone():
    phone = df_smartphone[df_smartphone['price'] == df_smartphone['price'].max()]
    result_brand = phone[['brand', 'model']].to_string(header = False, index = False)
    print(f"The most expensive phone is {result_brand} whose price is {df_smartphone['price'].max()} PLN.")

def cheapest_phone():
    phone = df_smartphone[df_smartphone['price'] == df_smartphone['price'].min()]
    result_brand = phone[['brand', 'model']].to_string(header = False, index = False)
    print(f"The most cheapest phone is {result_brand} whose price is {df_smartphone['price'].min()} PLN.")

expensive_smartphone()
cheapest_phone()



# Counting brands laptop and creating a bar chart
def count_brand_laptop():
    brand_counts = df_laptop['brand'].value_counts()

    plt.bar(brand_counts.index, brand_counts)

    plt.xlabel('Brand laptop')
    plt.ylabel('Number of laptops')
    plt.title('Laptop number chart')

    plt.tight_layout()
    plt.show()
    
# count_brand_laptop()
   
   
 
# Counting brands smartphone and creating a bar chart
def count_brand_phone():
    brand_counts = df_smartphone['brand'].value_counts()
    
    plt.bar(brand_counts.index, brand_counts)
    
    plt.xlabel("Brand phone")
    plt.ylabel("Number of smartphones")
    plt.title("Smartphone number chart")
    
    plt.tight_layout()
    plt.show()

count_brand_phone()


   
# Filters laptops by processor:
def processor_laptop():
    processor_lst = ['Intel', 'AMD', 'Apple']
    print(processor_lst)
    user = input("Which processor from the list do you want a laptop with? ")
    
    if (user == "Intel"):
        intel = df_laptop[df_laptop['processor_brand'] == 'Intel']
        print("Here is a list of laptops with an Intel processor:")
        print(intel)
    
    elif (user == "AMD"):
        AMD = df_laptop[df_laptop['processor_brand'] == 'AMD']
        print("Here is a list of laptops with an AMD processor:")
        print(AMD)
    
    elif (user == "Apple"):
        apple = df_laptop[df_laptop['processor_brand'] == 'Apple']
        print("Here is a list of laptops with an apple processor:")
        print(apple)
    
# processor_laptop()



# Filters laptops by operating system
def os_laptop():
    os_lst = ['Windows', 'macOS', 'Chrome OS']
    print(os_lst)
    user = input("Which operating system from the list do you want a laptop with? If you don't want any operating system, type 'No system' : ")
    
    if (user == 'Windows'):
        windows = df_laptop[df_laptop['os'] == 'Windows']
        print("Below is a list of Windows laptops:")
        print(windows[['brand', 'model', 'os']]) 
    
    elif (user == 'macOS'):
        mac_os = df_laptop[df_laptop['os'] == 'macOS']
        print("Below is a list of macOS laptops:")
        print(mac_os[['brand', 'model', 'os']])
        
    elif (user == 'Chrome OS'):
        chrome = df_laptop[df_laptop['os'] == 'Chrome OS']
        print("Below is a list of Chrome OS laptops:")
        print(chrome[['brand', 'model', 'os']])
        
    elif (user == 'No system'):
        no_system = df_laptop[df_laptop['os'] == 'No system']
        print("Below is a list of laptops without operating system:")
        print(no_system[['brand', 'model', 'os']])
    
# os_laptop()



# Filters smartphones by operating system
def os_smartphone():
    os_counts = df_smartphone['os'].value_counts()
    
    plt.figure(figsize=(5, 5))
    plt.pie(os_counts, labels=os_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title("Share of individual operating systems")
    plt.axis('equal')
    plt.show()
    
os_smartphone()



# Filters laptops by price
def price_laptop():
    user_min = int(input("Please provide the minimum price: "))
    user_max = int(input("Please provide the maximum price: "))
    
    laptops_filtered = df_laptop.loc[df_laptop['price'].between(user_min, user_max, inclusive='both')]
    print(laptops_filtered)
    
# price_laptop()



# Laptop price histogram
plt.hist(df_laptop['price'], bins=20, color="Green")
plt.xlabel("Price")
plt.ylabel("Number of laptops")
plt.title("Laptop price distribution")
plt.grid(True)
plt.show()



# Smartphone price histogram
plt.hist(df_smartphone['price'], bins=30, color="Purple")
plt.xlabel("Price")
plt.ylabel("Number of smartphones")
plt.grid(True)
plt.show()



# Scatter plot laptops
df_laptop_sorted = df_laptop.sort_values(by='star_rating')
plt.scatter(df_laptop_sorted['price'], df_laptop_sorted['star_rating'], color="Green", alpha=0.5)
plt.xlabel("Price")
plt.ylabel("Star rating")
plt.title("Scatter plot: Price vs Star Rating")
plt.show()



# Creates a bar chart that displays the average star rating for each laptop brand
df_laptop['star_rating'] = df_laptop['star_rating'].str.replace(',', '.').astype(float)
avg_star_rating_by_brand = df_laptop.groupby('brand')['star_rating'].mean()

plt.figure(figsize=(10, 5))
avg_star_rating_by_brand.plot(kind='bar', color='green')
plt.xlabel("Laptop brand")
plt.ylabel("Average star rating")
plt.title("Average star rating for each laptop brand")
plt.grid(axis='y')
plt.tight_layout()
plt.show()



# Calculates the sum, mean and median for 'ratings' column using NumPy
def calculates_laptop():
    ratings_array = df_laptop['ratings'].values
    
    sum_ratings = np.sum(ratings_array)
    print(f"The sum number of all laptop ratings is: {sum_ratings}")
    
    avg_ratings = np.mean(ratings_array)
    print(f"The average number of all laptop ratings is: {avg_ratings}")
    
    median_ratings = np.median(ratings_array)
    print(f"The median number of all laptop ratings is: {median_ratings}")
    
# calculates_laptop()



# Calculates the sum, mean and median for 'ratings' column using NumPy
def calculates_smartphone():
    ratings_array = df_smartphone['ratings'].values
    
    sum_ratings = np.sum(ratings_array)
    print(f"The sum number of all phone ratings is: {sum_ratings}")
    
    avg_ratings = np.mean(ratings_array)
    print(f"The average number of all phone ratings is: {avg_ratings}")
    
    median_ratings = np.median(ratings_array)
    print(f"The median number of all phone ratings is: {median_ratings}")

calculates_smartphone()



# Finding the most frequently purchased laptop using NumPy
def popular_laptop_np():
    ratings_array = df_laptop['ratings'].values
    
    max_index = np.argmax(ratings_array)
    max_ratings = df_laptop.loc[max_index]
    result_brand = f"{max_ratings['brand']} {max_ratings['model']}"
    
    print(f"The most popular laptop is {result_brand} which has {max_ratings['ratings']} ratings.")
    
popular_laptop_np()



# Finding the most frequently purchased smartphone using Numpy
def popular_smartphone_np():
    ratings_array = df_smartphone['ratings'].values
    
    max_index = np.argmax(ratings_array)
    max_ratings = df_smartphone.loc[max_index]
    result_brand = f"{max_ratings['brand']} {max_ratings['model']}"
    print(f"The most popular phone is {result_brand} which has {max_ratings['ratings']} ratings.")
    
popular_smartphone_np()



# Finding the least frequently purchased laptop using NumPy
def least_laptop_np():
    rating_array = df_laptop['ratings'].values
    
    min_index = np.argmin(rating_array)
    min_ratings = df_laptop.loc[min_index]
    result_brand = f"{min_ratings['brand']} {min_ratings['model']}"
    
    print(f"The least frequently purchased laptop is {result_brand} which has {min_ratings['ratings']} ratings.")   

least_laptop_np()



# Chart showing operating system
operating_system_counts = df_laptop['os'].value_counts()

plt.figure(figsize=(5, 5))
plt.pie(operating_system_counts, labels=operating_system_counts.index, autopct='%1.1f%%', startangle=50)
plt.title('Share of individual operating systems')
plt.axis('equal')
plt.show()