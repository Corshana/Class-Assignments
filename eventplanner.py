attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
system = "audio system" if attendees > 100 else "projector"
print(system)

#task 3 
user = input("Would you like vegetarin food? (yes,no)" )
food = "Veggie Delight Caterers" if user == ("yes") else "Gourmet Meals Caterers"
print(food)