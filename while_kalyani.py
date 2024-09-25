name=str(input("enter the any name:"))
gender=str(input("enter the gender (M/F):"))
age=int(input("enter the age:"))
pro_gram=0
pro_name = []
status = True
while status:  
        product = input("enter the product:")
        pro_name.append(product)                          #list_append
        product_gram =int(input("enter the product gram:"))  
        pro_gram += product_gram
        choice = input("do you want to more add Y/N :")
        if choice == "Y" :
            status = True
        else :
            status = False 
gold_price = 5000
total_gold_price =gold_price*pro_gram
making_charges=845
total_making_charges=product_gram*making_charges

if gender=="M":
    if age>=65:
        if total_gold_price>=21000 and total_gold_price<31000:
            discount =20

        elif total_gold_price>=31000 and total_gold_price<51000:
            discount =30

        elif total_gold_price>=51000:
            discount=35

    elif age<65:
        if total_gold_price>=21000 and total_gold_price<31000:
            discount=10

        elif total_gold_price>=31000 and total_gold_price<51000:
            discount=20

        elif total_gold_price>=51000:
            discount=25

elif gender=="F":
    if age>=65:
        if total_gold_price>=21000 and total_gold_price<31000:
            discount=25

        elif total_gold_price>=31000 and total_gold_price<51000:
            discount=35

        elif total_gold_price>=51000:
            discount=40
    elif age<65:
        if total_gold_price>=21000 and total_gold_price<31000:
            discount=15

        elif total_gold_price>=31000 and total_gold_price<51000:
            discount=25

        elif total_gold_price>=51000:
            discount=30

dis_price =total_gold_price*discount/100
after_dis_amount =total_gold_price-dis_price           


net_amount=after_dis_amount+total_making_charges
print(f"""_____________________Kalyan jwellers________________________
      _____________________________Tax invoice _________________________
      name: {name}
        age:   {age}
        gender  {gender}
        product {pro_name}
        weight  {pro_gram} gm
        ________________________________________________________________
        total gold price {total_gold_price}
        discount ={discount}
        dis price={dis_price}
        making charges per gram={making_charges}
        _________________________________________________________________
        net amount ={net_amount}
         __________________________________________________________________
         have a nice day
        """)


  

   
