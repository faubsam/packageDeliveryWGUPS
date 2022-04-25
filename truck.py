from datetime import datetime, timedelta

import package_delivery




class Truck:
    max_packages = 16
    speed = 18
    
    # there are more trucks than drivers, so this tells us whether or not the truck currently has a driver assigned
     

    def __init__(self, label, has_driver, start_hour=8, start_minute=0):
        self.has_driver = has_driver
        self.label = label
        # list of all packages that been loaded onto the truck
        self.truck_packages = []
        # address where the truck is currently located
        self.current_location = None
        # number of package that are currently loaded on the truck
        self.current_packages = 0
        # the miles traveled by the truck during the day
        self.miles_traveled = 0
        # the time it takes to deliver the next package on the truck
        self.time_to_deliver = 0
        # the total time in minutes since the truck has left the hub facility
        self.time_elapsed = 0
        self.day_start_time = datetime.now().replace(hour=start_hour, minute=start_minute ,second=0,microsecond=0)
        self.current_time = self.day_start_time
        self.deliveries_complete_time = self.day_start_time + timedelta(minutes=self.time_elapsed)

    # load a package onto the truck and update the current packages count
    def add_package(self, package):
        if self.current_packages >= self.max_packages:
            print("Package limit reached for this truck. Cannot add package with id: " + package.id) 
        else:
            self.truck_packages.append(package)
            self.current_packages += 1

    # move to the truck to a new address and update the truck's location
    def move_truck(self, distance, dest_addr):
        if self.has_driver is False:
            print("Truck has no driver")
        else:
            # calculate the distance to the next delivery address
            distance_to_next_stop = distance
            # update the miles traveled by this truck
            self.miles_traveled += distance_to_next_stop
            # calculate the time to deliver the next package
            self.time_to_deliver = (distance/self.speed)*60
            # update the total time elapsed since the truck left the hub
            self.time_elapsed += self.time_to_deliver
            # update the truck's location to the next delivery address
            self.current_location = dest_addr

    def deliver_package(self, package):
        if self.has_driver is False:
            print("Truck has no driver")
        else: 
            count = 0
            # remove the package from the truck's list of packages
            for pack in self.truck_packages:
                if pack.id == package.id:
                    self.truck_packages.remove(pack)
                count += 1
                # timestamp the package delivery
                pack.delivery_time = self.current_time + timedelta(minutes=self.time_to_deliver)
            # update the count of packages currently in the truck
            self.current_packages -= 1
            # update the current_time tracker
            if (self.current_time >= datetime.now().replace(hour=10,minute=20)):
                
                for i in range(len(self.truck_packages)):
                    if self.truck_packages[i].id == 9:
                        self.truck_packages[i].address = "410 S State St"
                        break
            self.current_time += timedelta(minutes=self.time_to_deliver)
            
            

    