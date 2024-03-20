import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
from tkinter import ttk, PhotoImage
from Laptop import create_laptop_window
from Smartphone import create_smartphone_window
from PIL import Image, ImageTk


# Creates the main window 
window = Tk()
window.title("ShopApp")
icon = PhotoImage(file='Pictures/energy.png')
window.iconphoto(True, icon)

window_width = 450
window_height = 700

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

window.geometry(f"{window_width}x{window_height}+{x}+{y}")


def open_laptop_window():
    create_laptop_window()
    
def open_smartphone_window():
    create_smartphone_window()


# BUTTONS 
btn_laptop_image = PhotoImage(file='Pictures/btn_laptop.png')
btn_laptop_label = Label(image=btn_laptop_image)

btn_laptop = Button(window,
                    image=btn_laptop_image,
                    command=open_laptop_window,
                    borderwidth=0)
btn_laptop.pack()
btn_laptop.place(x=25, y=200)


btn_smartphone_image = PhotoImage(file='Pictures/btn_smartphone.png')
btn_smartphone_label = Label(image=btn_smartphone_image)
btn_smartphone = Button(window,
                        image=btn_smartphone_image,
                        command=open_smartphone_window,
                        borderwidth=0)
btn_smartphone.pack()
btn_smartphone.place(x=25, y=400)



# # Filters laptops by processor:
# def processor_laptop():
#     processor_lst = ['Intel', 'AMD', 'Apple']
#     print(processor_lst)
#     user = input("Which processor from the list do you want a laptop with? ")
    
#     if (user == "Intel"):
#         intel = df_laptop[df_laptop['processor_brand'] == 'Intel']
#         print("Here is a list of laptops with an Intel processor:")
#         print(intel)
    
#     elif (user == "AMD"):
#         AMD = df_laptop[df_laptop['processor_brand'] == 'AMD']
#         print("Here is a list of laptops with an AMD processor:")
#         print(AMD)
    
#     elif (user == "Apple"):
#         apple = df_laptop[df_laptop['processor_brand'] == 'Apple']
#         print("Here is a list of laptops with an apple processor:")
#         print(apple)
    
# # processor_laptop()



# # Filters laptops by operating system
# def os_laptop():
#     os_lst = ['Windows', 'macOS', 'Chrome OS']
#     print(os_lst)
#     user = input("Which operating system from the list do you want a laptop with? If you don't want any operating system, type 'No system' : ")
    
#     if (user == 'Windows'):
#         windows = df_laptop[df_laptop['os'] == 'Windows']
#         print("Below is a list of Windows laptops:")
#         print(windows[['brand', 'model', 'os']]) 
    
#     elif (user == 'macOS'):
#         mac_os = df_laptop[df_laptop['os'] == 'macOS']
#         print("Below is a list of macOS laptops:")
#         print(mac_os[['brand', 'model', 'os']])
        
#     elif (user == 'Chrome OS'):
#         chrome = df_laptop[df_laptop['os'] == 'Chrome OS']
#         print("Below is a list of Chrome OS laptops:")
#         print(chrome[['brand', 'model', 'os']])
        
#     elif (user == 'No system'):
#         no_system = df_laptop[df_laptop['os'] == 'No system']
#         print("Below is a list of laptops without operating system:")
#         print(no_system[['brand', 'model', 'os']])
    
# # os_laptop()



# # Filters laptops by price
# def price_laptop():
#     user_min = int(input("Please provide the minimum price: "))
#     user_max = int(input("Please provide the maximum price: "))
    
#     laptops_filtered = df_laptop.loc[df_laptop['price'].between(user_min, user_max, inclusive='both')]
#     print(laptops_filtered)
    
# # price_laptop()



# # Scatter plot laptops
# df_laptop_sorted = df_laptop.sort_values(by='star_rating')
# plt.scatter(df_laptop_sorted['price'], df_laptop_sorted['star_rating'], color="Green", alpha=0.5)
# plt.xlabel("Price")
# plt.ylabel("Star rating")
# plt.title("Scatter plot: Price vs Star Rating")
# plt.show()



# # Creates a bar chart that displays the average star rating for each laptop brand
# df_laptop['star_rating'] = df_laptop['star_rating'].str.replace(',', '.').astype(float)
# avg_star_rating_by_brand = df_laptop.groupby('brand')['star_rating'].mean()

# plt.figure(figsize=(10, 5))
# avg_star_rating_by_brand.plot(kind='bar', color='green')
# plt.xlabel("Laptop brand")
# plt.ylabel("Average star rating")
# plt.title("Average star rating for each laptop brand")
# plt.grid(axis='y')
# plt.tight_layout()
# plt.show()



# # Calculates the sum, mean and median for 'ratings' column using NumPy
# def calculates_laptop():
#     ratings_array = df_laptop['ratings'].values
    
#     sum_ratings = np.sum(ratings_array)
#     print(f"The sum number of all laptop ratings is: {sum_ratings}")
    
#     avg_ratings = np.mean(ratings_array)
#     print(f"The average number of all laptop ratings is: {avg_ratings}")
    
#     median_ratings = np.median(ratings_array)
#     print(f"The median number of all laptop ratings is: {median_ratings}")
    
# # calculates_laptop()



# # Calculates the sum, mean and median for 'ratings' column using NumPy
# def calculates_smartphone():
#     ratings_array = df_smartphone['ratings'].values
    
#     sum_ratings = np.sum(ratings_array)
#     print(f"The sum number of all phone ratings is: {sum_ratings}")
    
#     avg_ratings = np.mean(ratings_array)
#     print(f"The average number of all phone ratings is: {avg_ratings}")
    
#     median_ratings = np.median(ratings_array)
#     print(f"The median number of all phone ratings is: {median_ratings}")

# calculates_smartphone()



# # Finding the most frequently purchased laptop using NumPy
# def popular_laptop_np():
#     ratings_array = df_laptop['ratings'].values
    
#     max_index = np.argmax(ratings_array)
#     max_ratings = df_laptop.loc[max_index]
#     result_brand = f"{max_ratings['brand']} {max_ratings['model']}"
    
#     print(f"The most popular laptop is {result_brand} which has {max_ratings['ratings']} ratings.")
    
# popular_laptop_np()



# # Finding the most frequently purchased smartphone using Numpy
# def popular_smartphone_np():
#     ratings_array = df_smartphone['ratings'].values
    
#     max_index = np.argmax(ratings_array)
#     max_ratings = df_smartphone.loc[max_index]
#     result_brand = f"{max_ratings['brand']} {max_ratings['model']}"
#     print(f"The most popular phone is {result_brand} which has {max_ratings['ratings']} ratings.")
    
# popular_smartphone_np()



# # Finding the least frequently purchased laptop using NumPy
# def least_laptop_np():
#     rating_array = df_laptop['ratings'].values
    
#     min_index = np.argmin(rating_array)
#     min_ratings = df_laptop.loc[min_index]
#     result_brand = f"{min_ratings['brand']} {min_ratings['model']}"
    
#     print(f"The least frequently purchased laptop is {result_brand} which has {min_ratings['ratings']} ratings.")   

# least_laptop_np()


window.mainloop()