class MuftiAirline:
    def __init__(self, passport, name, destination, seat_num, email):
        self.passport = passport
        self.name = name
        self.destination = destination
        self.seat_num = seat_num
        self.email = email
        self.following = None

def reserve(begin, num):
    if begin is None:
        begin = MuftiAirline("", "", "", 0, "")
        details(begin)
        begin.seat_num = num
        print(f"\n\t Seat booking successful!")
        print(f"\n\t your seat number is: Seat A-{num}")
        return begin, num + 1
    elif num > 15:
        print("\n\t\t Seat Full.")
        return begin, num
    else:
        current = begin
        while current.following:
            current = current.following
        current.following = MuftiAirline("", "", "", 0, "")
        current = current.following
        details(current)
        current.seat_num = num
        print(f"\n\t Seat booking successful!")
        print(f"\n\t your seat number is: Seat A-{num}")
        return begin, num + 1

def details(passenger):
    passenger.passport = input("\n\t Enter your passport number:")
    passenger.name = input("\n\t Enter your name:")
    passenger.email = input("\n\t Enter your email address:")
    passenger.destination = input("\n\t Enter the Destination :")

def save_file(begin):
    with open("mufti_records.txt", "w") as file:
        current = begin
        while current:
            file.write(f"{current.passport.ljust(6)}")
            file.write(f"{current.name.ljust(15)}")
            file.write(f"{current.email.ljust(15)}")
            file.write(f"{current.destination.ljust(15)}\n")
            current = current.following
    print("\n\n\t Details have been saved to a file (mufti_records.txt)")

def display(begin):
    current = begin
    while current:
        print("\n\n Passport Number : %-6s" % current.passport)
        print("         name : %-15s" % current.name)
        print("      email address: %-15s" % current.email)
        print("      Seat number: A-%d" % current.seat_num)
        print("     Destination:%-15s" % current.destination)
        print("\n++=====================================================++")
        current = current.following

def cancel(begin):
    passport = input("\n\n Enter passport number to delete record?:")
    if begin.passport == passport:
        dummy = begin
        begin = begin.following
        del dummy
        print(" Booking has been deleted")
        return begin

    current = begin
    while current.following:
        if current.following.passport == passport:
            dummy = current.following
            current.following = current.following.following
            del dummy
            print(" Booking has been deleted")
            return begin
        current = current.following
    print("Passport number is wrong please check your passport")
    return begin

def main():
    begin = None
    num = 1
    while True:
        print("\n\n\t\t ************************")
        print("\n\t\t                   welcome to Kathar airline system                   ")
        print("\n\t\t   ***********************")
        print("\n\n\n\t\t Please enter your choice from below (1-4):")
        print("\n\n\t\t 1. Reservation")
        print("\n\n\t\t 2. Cancel")
        print("\n\n\t\t 3. DISPLAY RECORDS")
        print("\n\n\t\t 4. EXIT")
        print("\n\n\t\t feel free to contact ")
        choice = input("\n\n\t\t Enter your choice :")
        
        if choice == '1':
            begin, num = reserve(begin, num)
        elif choice == '2':
            begin = cancel(begin)
        elif choice == '3':
            display(begin)
        elif choice == '4':
            save_file(begin)
            break
        else:
            print("\n\n\t SORRY INVALID CHOICE!")
            print("\n\n\t PLEASE CHOOSE FROM 1-4")
            print("\n\n\t Do not forget to choose from 1-4")

if __name__ == "__main__":
    main()
