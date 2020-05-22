#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Hotel():
    def __init__(self):
        self.data = {}
        self.addHotel()

    def addHotel(self):
        name = input("Enter Hotel name: ")
        if self.data.get(name, False):
            print("Hotel with same name already exist!..")
            self.addHotelAgain()
        else:
            self.data[name]={}
            self.addRoom(name)

    def addRoom(self, name):
        room_no = input("Enter Room Number: ")
        self.data[name][room_no]={"amenities": [], "amenitiesList": [], "cost": 0}
        i = 0
        while i < 5:
            self.addAllAmenities(name, room_no)
            i += 1
        self.addAmenitiesAgain(name, room_no)

    def addAllAmenities(self, name, roomNo):
        item = input("Enter the amenities name: ")
        price = input("Enter amenities price in $ (should be a number): ")
        self.data[name][roomNo]["amenities"].append({item:price})
        self.data[name][roomNo]["amenitiesList"].append(item)
        self.data[name][roomNo]["cost"] += int(price)


    def addAmenities(self, name, roomNo):
        item = input("Enter the amenities name: ")
        price = input("Enter amenities price in $ (should be a number): ")
        self.data[name][roomNo]["amenities"].append({item:price})
        self.data[name][roomNo]["amenitiesList"].append(item)
        self.data[name][roomNo]["cost"] += int(price)
        self.addAmenitiesAgain(name, roomNo)


    def addHotelAgain(self):
        add_hotel = input("Do you want to add New Hotel (Yes/No): ")
        if add_hotel.lower() == "yes":
            self.addHotel()
        elif add_hotel.lower() == "no":
            self.show()
        else:
            print("Invalid Input")
            self.addHotelAgain()

    def addRoomAgain(self, name):
        add_room = input("Do you want to add more Room(Yes/No): ")
        if add_room.lower() == "yes":
            self.addRoom(name)
        elif add_room.lower() == "no":
            self.addHotelAgain()
        else:
            print("Invalid Input")
            self.addRoomAgain(name)


    def addAmenitiesAgain(self, name, roomNo):
        add_amenities = input("Do you want to add more amenities(Yes/No): ")
        if add_amenities.lower() == "yes":
            self.addAmenities(name, roomNo)
        elif add_amenities.lower() == "no":
            self.addRoomAgain(name)
        else:
            print("Invalid Input")
            self.addAmenitiesAgain(name, roomNo)

    def show(self, budget=0):
        for hotel_name, room_info in self.data.items():
            context = "\nRoom No {0} have the amenities like {1}, and room price is ${2}."
            if budget == 0:
                data = '\n\n\n{0} Hotel have following rooms\n'.format(hotel_name)
                for room, amenti_info in room_info.items():
                    amenti = ', '.join(amenti_info['amenitiesList'])
                    cost = amenti_info['cost']
                    data += context.format(room, amenti, cost)
                print(data)
            else:
                data = '\n\n\n{0} Hotel have following rooms matching your budget\n'.format(hotel_name)
                availability = False
                for room, amenti_info in room_info.items():
                    cost = amenti_info['cost']
                    if cost <= budget:
                        amenti = ', '.join(amenti_info['amenitiesList'])
                        availability = True
                        data += context.format(room, amenti, cost)
                if availability:
                    print(data)
                else:
                    print("\n\n\nNo room available for your budget in hotel {0}".format(hotel_name))
            print("\n***********************************************************\n")
        if budget == 0:
            self.getUserBudget()

    def getUserBudget(self):
        print("\n***********************************************************\n")
        budget = int(input("Please enter your budget: "))
        if budget > 1:
            self.show(budget)
        else:
            print("Invalid Budget range")
            self.getUserBudget()


Hotel()

