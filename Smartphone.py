import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from tkinter import ttk, PhotoImage, messagebox

def create_smartphone_window():
    smartphone_window = Tk()
    smartphone_window.title("ShopApp")

    smartphone_window_width = 450
    smartphone_window_height = 700
    
    smartphone_window.geometry(f"{smartphone_window_width}x{smartphone_window_height}")
    smartphone_window.grid_rowconfigure(0, weight=1)
    smartphone_window.grid_columnconfigure(0, weight=1)
    
    # Buttons
    buttons = [
        ("Average price", mean_smartphone),
        ("Median price", median_smartphone),
        ("Standard deviation price", standard_deviation_smartphone),
        ("The most expensive smartphone", expensive_smartphone),
        ("The most cheapest smartphone", cheapest_phone),
        ("Smartphone brands", count_brand_phone),
        ("Operating system", os_smartphone),
        ("Histogram smartphone price", histogram_smartphone)    
    ]
    
    for i, (text, command) in enumerate(buttons):
        button = Button(smartphone_window, text=text, command=command, bg="black", fg="white")
        button.grid(row=i, column=0, sticky="ew", padx=20, pady=30)
    
    smartphone_window.mainloop()
    
df_smartphone = pd.read_csv("Data/Smartphone.csv", delimiter=";")
    
# Calculing mean, median and standard deviation of smartphone prices using Numpy
def mean_smartphone():
    prices_array = df_smartphone['price'].values  
    avg_price = round(np.mean(prices_array), 2)
    messagebox.showinfo("Average Price Of Smartphone", f"The average price of all smartphones is {avg_price} PLN.")
    print(f"The average price of all smartphones is {avg_price} PLN.")
    
def median_smartphone():
    prices_array = df_smartphone['price'].values
    median_price = round(np.median(prices_array), 2)
    messagebox.showinfo("Median Price Of Smartphone", f"The median of all smartphones is {median_price} PLN.")
    print(f"The median of all smartphones is {median_price} PLN.")
        
def standard_deviation_smartphone():
    prices_array = df_smartphone['price'].values
    std_price = round(np.std(prices_array), 2)
    messagebox.showinfo("Standard Deviation Smartphone", f"Standard deviation price of all smartphones is {std_price} PLN.")  
    print(f"Standard deviation price of all smartphones is {std_price} PLN.")    
    


# Finding the most expensive and cheapest smartphone
def expensive_smartphone():
    phone = df_smartphone[df_smartphone['price'] == df_smartphone['price'].max()]
    result_brand = phone[['brand', 'model']].to_string(header = False, index = False)
    result_price = phone[['price']].to_string(header = False, index = False)
    messagebox.showinfo("The most expensive smartphone", f"The most expensive smartphone is {result_brand} whose price is {result_price} PLN.")
    print(f"The most expensive phone is {result_brand} whose price is {result_price} PLN.")

def cheapest_phone():
    phone = df_smartphone[df_smartphone['price'] == df_smartphone['price'].min()]
    result_brand = phone[['brand', 'model']].to_string(header = False, index = False)
    result_price = phone[['price']].to_string(header = False, index = False)
    messagebox.showinfo("The most expensive smartphone", f"The most expensive smartphone is {result_brand} whose price is {result_price} PLN.")
    print(f"The most cheapest phone is {result_brand} whose price is {result_price} PLN.")



# Counting brands smartphone and creating a bar chart
def count_brand_phone():
    brand_counts = df_smartphone['brand'].value_counts()
    
    plt.bar(brand_counts.index, brand_counts)
    
    plt.xlabel("Brand phone")
    plt.ylabel("Number of smartphones")
    plt.title("Smartphone number chart")
    
    plt.tight_layout()
    plt.show()



# Chart showing operating system
def os_smartphone():
    operating_system_counts = df_smartphone['os'].value_counts()

    plt.figure(figsize=(5, 5))
    plt.pie(operating_system_counts, labels=operating_system_counts.index, autopct='%1.1f%%', startangle=50)
    plt.title('Share of individual operating systems')
    plt.axis('equal')
    plt.show()

   

# Smartphone price histogram
def histogram_smartphone():
    plt.hist(df_smartphone['price'], bins=30, color="Purple")
    plt.xlabel("Price")
    plt.ylabel("Number of smartphones")
    plt.grid(True)
    plt.show()