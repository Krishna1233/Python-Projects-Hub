  
print("================================")
print("     BIRTH DATE CALCULATOR")
print("================================")

# Personal Information

name = input("Enter your full name: ")

day = int(input("Enter your birth date : "))

month = int(input("Enter your birth month: "))

year = int(input("Enter your birth year: "))

print(day, "\\", month,"\\", year)

# Checking Birth Date

if day >= 1 and day <= 31:

    print("Birth date accepted")

else:
    print("Invalid birth date")


# Checking Birth Month

if month >= 1 and month <= 12:

    print("Birth month accepted")

else:
    print("Invalid birth month")


# Calculating Mulank

total = 0

for a in str(day):
    total = total + int(a)

while total > 9:
    new_total = 0

    for a in str(total):
        new_total = new_total + int(a)

    total = new_total

print("--------------------------------")
print("Your name is:", name)
print("Your birth date:", day, month, year)
print("Your Mulank is:", total)


# Ruling Planet

if total == 1:
    print("Sun is your ruling planet.","Every morning offer water to Sun from a copper pot, add a pinch of red sandalwood." , "Mantra:- Om Ghrini Suryaya Namah..",
"Time: 7 AM...108 times",)

elif total == 2:
    print("Moon is your ruling planet","Touch your mother's feet before sleeping.","Mantra:- Om Som Somaya Namah..,",
"Time: 9 PM, 108 times")

elif total == 3:
    print("Jupiter is your ruling planet","On Thursday, apply saffron tilak on forehead.","Donate yellow dal in a temple.",
"Mantra: `Om Brim Brihaspataye Namah`",
"Time: 8 AM...108 times")

elif total == 4:
    print("Rahu is your ruling planet","On Saturday, flow black sesame seeds in water. ,Don't wear artificial jewelry.",
"Mantra: `Om Ram Rahave Namah`",
"Time: 10 PM...108 times")

elif total == 5:
    print("Mercury is your ruling planet","On Wednesday, keep green cardamom in your pocket. Gift green clothes to your sister."
"Mantra: `Om Bum Budhaya Namah`",
"Time: 12 PM...108 times")

elif total == 6:
    print("Venus is your ruling planet","On Friday, wear white clothes." ,"use perfume .",
"Mantra: `Om Shum Shukraya Namah`",
"Time: 7 PM... 108 times")

elif total == 7:
    print("Ketu is your ruling planet","Daily feed a dog with roti. Wear gold in your ear.",
"Mantra: `Om Kem Ketave Namah`",
"Time: 5 PM...108 times")

elif total == 8:
    print("Saturn is your ruling planet","On Saturday, light a mustard oil diya under a Peepal tree.",
"Mantra: `Om Sham Shanaishcharaya Namah`",
"Time: 6 PM.. 108 times")

elif total == 9:
    print("Mars is your ruling planet","On Tuesday, donate red lentils.", "Eat sitting on the floor.",
"Mantra: `Om Am Angarakaya Namah`..",
"Time: 6 AM... 108 times")

else:
    print("Error")

print("================================")
print("       THANK YOU!")
print("================================")
