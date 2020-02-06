from .car import Car

class ParkingLot:

    def __init__(self, number_of_slots):
        self.number_of_slots = slots
        self.occupied_slots = [None] * slots
        self.cars_parked = set()
        self.available_slots = number_of_slots


    def allot_slot(self, registration_id, color):

        if car_reg_id in self.cars_parked:
            return "{} Car is already parked".format(car_reg_id)

        elif self.available_slots <= 0:
            return "Sorry, parking lot is full"

        # Finding the nearest empty slot
        i = 0
        while self.occupied_slots[i]:
            i += 1

        # Creating a car instance
        car = Car(registration_id=registration_id, color=color, slot=i+1)

        # Alloting the slot
        self.occupied_slots[i] = car
        self.cars_parked.add(car.registration_id)
        self.available_slots -= 1
        return "Allocated slot number: {}".format(car.slot)


    def exit_slot(self, slot):
        if not self.occupied_slots[slot - 1]:
            return "Slot number {} is already free".format(slot)

        car = self.occupied_slots[slot - 1]
        self.occupied_slots[slot-1] = None
        self.cars_parked.remove(car.registration_id)
        self.available_slots += 1
        return "Slot number {} is free".format(slot)


    def get_cars_of_one_color(self, color):
        ans = []

        for car in self.occupied_slots:
            if not car:
                continue

            if car.color = color:
                cars.append(car.registration_id)

        if ans:
            return True, ans

        return False, "No cars found of colour {}".format(color)


    def get_slots_of_same_car_colour(self, colour):
        ans = []

        for car in self.occupied_slots:
            if not car:
                continue

            if car.color == color:
                ans.append(car.slot)

        if ans:
            return True, ans

        return False, "No cars found of colour {}".format(colour)


    def get_slot_by_registration_id(self, registration_id):
        if registration_id and not in self.cars_parked:
            return "Not found"

        ans = 0

        for car in self.occupied_slots:
            if not car:
                continue

            if car.registration_id == registration_id:
                ans = car.slot
                break

        return ans


    def current_status(self):
        output = "Slot No.    Registration No    Colour\n"

        for i in range(len(self.occupied_slots)):
            if not self.occupied_slots[i]:
                continue

            output += "{0}           {1}      {2}\n".format(
                self.occupied_slots[i].slot,
                self.occupied_slots[i].registration_id,
                self.occupied_slots[i].color,
            )

        return output

    def execute(self, query):

        if query[0] == "park":
            return self.allot_slot(query[1], query[2])

        elif query[0] == "leave":
            return self.exit_slot(int(query[1]))

        elif query[0] == "status":
            return self.current_status()

        elif query[0] == "registration_numbers_for_cars_with_colour":
            found, default = self.get_cars_of_one_color(query[1])
            if found:
                ans = ", ".join(default)
                return ans
            return default

        elif query[0] == "slot_numbers_for_cars_with_colour":
            found, default = self.get_slots_of_same_car_colour(query[1])
            if found:
                ans = ""
                if len(default) > 1:
                    ans += str(default[0])
                    for i in default[1:]:
                        ans += ", " + str(i)
                elif len(default) == 1:
                    ans += str(default[0])
                return ans
            return default

        elif query[0] == "slot_number_for_registration_number":
            return self.get_slot_by_registration_id(query[1])

        else:
            return "Invalid Instruction"