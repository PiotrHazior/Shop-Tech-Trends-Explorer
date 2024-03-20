import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from tkinter import ttk, PhotoImage, messagebox


def create_laptop_window():
    laptop_window = Tk()
    laptop_window.title("ShopApp")

    laptop_window_width = 450
    laptop_window_height = 700
    
    laptop_window.geometry(f"{laptop_window_width}x{laptop_window_height}")
    laptop_window.grid_rowconfigure(0, weight=1)
    laptop_window.grid_columnconfigure(0, weight=1)
    
    # Buttons
    buttons = [
        ("Average price", mean_laptop),
        ("Median price", median_laptop),
        ("Standard deviation price", standard_deviation_laptop),
        ("The most expensive laptop", expensive_laptop),
        ("The most cheapest laptop", cheapest_laptop),
        ("Laptop brands", count_brand_laptop),
        ("Operating system", os_laptop),
        ("Histogram laptop price", histogram_laptop)
    ]
    
    for i, (text, command) in enumerate(buttons):
        button = Button(laptop_window, text=text, command=command, bg="black", fg="white")
        button.grid(row=i, column=0, sticky="ew", padx=20, pady=30)
    
            
    laptop_window.mainloop()
    

df_laptop = pd.read_csv("Data/Laptop.csv", delimiter=";")

# Calculing mean, median and standard deviation of laptop prices using Pandas
def mean_laptop():
    avg_price = round(df_laptop["price"].mean(), 2)
    messagebox.showinfo("Average Price of Laptop", f"The average price of all laptop is: {avg_price} PLN.")
    print(f"The average price of all laptop is: {avg_price} PLN.")
    
def median_laptop():
    median_price = round(df_laptop['price'].median(), 2)
    messagebox.showinfo("Median Price of Laptop", f"The median of all laptop prices is: {median_price} PLN.")
    print(f"The median of all laptop prices is: {median_price} PLN.")
    
    
def standard_deviation_laptop():
    std_dev_price = round(df_laptop["price"].std(), 2)
    messagebox.showinfo("Standard Deviation Laptop", f"Standard deviation price of all laptop is: {std_dev_price} PLN.")
    print(f"Standard deviation price of all laptop is: {std_dev_price} PLN.")
    
    
    
# Finding the most expensive and cheapest laptop 
def expensive_laptop():
    laptop = df_laptop[df_laptop['price'] == df_laptop['price'].max()] 
    result_brand = laptop[['brand', 'model']].to_string(header = False, index = False)
    result_price = laptop[['price']].to_string(header = False, index = False)
    messagebox.showinfo("The most expensive laptop", f"The most expensive laptop is {result_brand} whose price is {result_price} PLN.")
    print(f"The most expensive laptop is {result_brand} whose price is {result_price} PLN.")
    
def cheapest_laptop():
    laptop = df_laptop[df_laptop['price'] == df_laptop['price'].min()]
    result_brand = laptop[['brand', 'model']].to_string(header = False, index = False)
    result_price = laptop[['price']].to_string(header = False, index = False)
    messagebox.showinfo("The most cheapest laptop", f"The most cheapest laptop is {result_brand} whose price is {result_price} PLN.")
    print(f"The most cheapest laptop is {result_brand} whose price is {result_price} PLN.")
    
    
    
# Counting brands laptop and creating a bar chart
def count_brand_laptop():
    brand_counts = df_laptop['brand'].value_counts()

    plt.bar(brand_counts.index, brand_counts)

    plt.xlabel('Brand laptop')
    plt.ylabel('Number of laptops')
    plt.title('Laptop number chart')

    plt.tight_layout()
    plt.show()
    
    

# Chart showing operating system
def os_laptop():
    operating_system_counts = df_laptop['os'].value_counts()

    plt.figure(figsize=(5, 5))
    plt.pie(operating_system_counts, labels=operating_system_counts.index, autopct='%1.1f%%', startangle=50)
    plt.title('Share of individual operating systems')
    plt.axis('equal')
    plt.show()



# Laptop price histogram
def histogram_laptop():
    plt.hist(df_laptop['price'], bins=20, color="Green")
    plt.xlabel("Price")
    plt.ylabel("Number of laptops")
    plt.title("Laptop price distribution")
    plt.grid(True)
    plt.show()
