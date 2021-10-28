print("Welcome to the ticket portal.")
height = int(input("Please enter your height in cm: "))
age = int(input("How old are you?: "))

photo_price = 3
bill = 0


if height >= 120:
  
  if age <= 12 :
    bill = 5
    print(f"Child tickets cost ${bill}")

  if age <= 18:
    bill = 7
    print(f"Youth ticket cost ${bill}")

  if age > 18:
    bill = 12
    print(f"Adult ticket cost ${bill}")

  photo_consent = input("Do you want a photo of you taken? Yes or No :").lower()

  if photo_consent == "yes":
    #Add $3 to their bill.
    print(f"Total to pay is {(bill + photo_price)}")
  
  print(f"Total to pay is ${bill}")

else:
  print("Sorry, you need to grow taller before you can ride. ")

  
