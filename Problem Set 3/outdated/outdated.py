# create list with the name of all months
months =[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Loop forever
while True:
    # Get user input
    Date = input("Date: ").strip()
    try:
        # Split the date by /
        month ,day ,year = Date.split("/")
        # Check if is in between 1 and 12 and day between 1 and 31
        if (int(month) >=1 and int(month) <=12 and int(day) >=1 and int(day) <=31):
            break
    except:
        try:
            # Split the date by space
            if "," in Date:
                Date = Date.strip()
                o_month,o_day ,year = Date.split(" ")
            # Find the number of the month
            # else:
            for x in range(len(months)):
                if o_month == months[x]:
                    month = x+1
                    day = o_day.strip(",")
                
            # Remove the comma from the day
            # day = o_day.replace(",","")
            # then we can check if month is in between 1 and 12 and day between 1 and 31
            if (int(month) >=1 and int(month) <=12 and int(day) >=1 and int(day) <=31):
                break
        except:
            print()
            pass
        
print(f"{year.strip()}-{int(month):02}-{int(day):02}")
            