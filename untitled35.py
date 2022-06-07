#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 15:11:00 2022

@author: riddhiekajain
"""

class parent():
    
    def menu(dish):
        if dish=="burger":
            print("You can add following toppings")
            print("More cheese / Add jalapeno")
        elif dish=="iced_americano":
            print("You can add following toppings")
            print("Add chocolate flavour / Add caramel flavour")
            
        else:
            print("Please enter valid dish")
            
    def final_amount(dish, add_ons):
        if dish=="burger" and add_ons=="cheese":
            print("you need to pay 5 USD")
        elif dish=="burger" and add_ons=="jalapeno":
            print("you need to pay 7 USD")
        elif dish== "iced_americano" and add_ons=="caramel":
            print("you need to pay 450 USD")
            
class child1(parent):
    
    def __init__(self, dish):
        self.new_dish = dish
    def get_menu(self):
        parent.menu(self.new_dish)
        
class child2(parent):
    
    def __init__(self, dish, addons):
        self.new_dish = dish
        self.addons = addons
        
    def get_final_amount(self):
        parent.final_amount(self.new_dish, self.addons)
        
child1_object=child1("burger")
child1_object.get_menu()

child2_object=child2("burger", "jalapeno")
child2_object.get_final_amount()