"""#if Condition (1)
print("This is BMI Calcukator!")
height=float(input("enter height in meters : "))
weight=float(input("enter weight in kilograms : "))
BMI=weight/(height)**2
if BMI >= 30:
    print("bmi is: ", BMI, "Obesity")
elif BMI >=25 and BMI<=29:
    print("bmi is: ", BMI, "Overweight")
elif BMI >=18.5 and BMI <=25:
    print("bmi is: ", BMI, "Normal")
elif BMI <18.5:
    print("bmi is: ", BMI, "underweight")
else:
    print("enter accurate value!!")"""

#if condition (2)

def country_name(city):
    cities = {"Australia":["Sydney","Melbourne","Brisbane","Perth"],
              "UAE":["Dubai","Abu Dhabi","Sharjah","Ajman"],
              "India":["Mumbai","Bangalore","Chennai","Delhi"]}
    for country, city_list in cities.items():
        if city in city_list:
            return country
    return "City not found in database"

city_name = input("Enter a city name: ")
country = country_name(city_name)
print(f"{city_name} belongs to: {country}")





