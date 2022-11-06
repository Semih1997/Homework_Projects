flight_classes = {"First": range(1, 21), "Business": range(21, 51), "Economy": range(51, 101)}
handbag_weight_limits = {"First": 20, "Business": 14, "Economy": 8}
liquid_quantity_limits = {"First": 4, "Business": 3, "Economy": 2}
erormsg = ["Liquid carriage exceeds the limit.","Invalid weight in handbag."]
travmsg = ["Safe travels in First Class.","Safe travels in Business Class.","Safe travels in Economy Class."]
while True:
    ticket_number = int(input("Enter the ticket number: "))
    while not ticket_number in range(1, 101):
        ticket_number = int(input("Please, the ticket number as an integer between 0-100: "))
    handbag_weight = float(input("Enter the weight in (kg): "))
    while handbag_weight < 0:
        handbag_weight = float(input("Please, enter a valid (non-negative) weight in (kg): "))   
    liquid_quantity = float(input("Enter the liquid quantity in (L): "))
    while liquid_quantity < 0:
        liquid_quantity = float(input("Please, enter a valid (non-negative) liquid quantity in (L): "))
    current_flight_class = None
    for key in flight_classes:
        if ticket_number in flight_classes[key]:
            current_flight_class = key
            break
    handbag_weight_limit = handbag_weight_limits[current_flight_class]
    liquid_quantity_limit = liquid_quantity_limits[current_flight_class]
    
    if (handbag_weight in range(1, 21) and handbag_weight > 20) or (handbag_weight in range(21, 51) and handbag_weight > 14) or (handbag_weight in range(51, 101) and handbag_weight > 8):
        print(erormsg[1])
        
    if (liquid_quantity in range(1, 21) and liquid_quantity >4) or (liquid_quantity in range(21, 51) and liquid_quantity >3) or (liquid_quantity in range(51, 101) and liquid_quantity >2):
        print(erormsg[0])
        
        print("Unsafe Condition! You cannot travel in that case.")
    else: 
        if ticket_number in range(1, 21):
            print(travmsg[0])
        elif ticket_number in range(21, 51):
            print(travmsg[1])
        else:
            print(travmsg[2])
    break