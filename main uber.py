import json
d=[{'identity':1,'name':'laxmi','current location':'userinput','destination':'userinput','isheriding':False,'payment_optioons':'cash or online'},{'identity':2,'name':'rajasri','current location':'userinput','destination':'userinput','isheriding':False,'payment_optioons':'cash or online'},{'identity':3,'name':'jyotsna','current location':'userinput','destination':'userinput','isheriding':False,'payment_optioons':'cash or online'},{'identity':4,'name':'jyothi','current location':'userinput','destination':'userinput','isheriding':False,'payment_optioons':'cash or online'},{'identity':5,'name':'mahanandha','current location':'userinput','destination':'userinput','isheriding':False,'payment_optioons':'cash or online'},{'identity':6,'name':'sunil','current location':'userinput','destination':'userinput','isheriding':False,'payment_optioons':'cash or online'},{'identity':7,'name':'sajith','current location':'userinput','destination':'userinput','isheriding':False,'payment_optioons':'cash or online'},{'identity':8,'name':'sainath','current location':'userinput','destination':'userinput','isheriding':False,'payment_optioons':'cash or online'},{'identity':9,'name':'srinivas','current location':'userinput','destination':'userinput','isheriding':False,'payment_optioons':'cash or online'},{'identity':10,'name':'venkatesh','current location':'userinput','destination':'userinput','isheriding':False,'payment_optioons':'cash or online'}]
def rider(d):
    comformation=input('enter the decion yes or no type(you want to go to the ride): ')
    if comformation=='yes':
        print('comfirm')
        print('your ride is on the way please dont cancel the ride')
        otp=int(input('enter the otp'))
        print('message....OTP...of your ride',otp)
        print('driver ask the user,please spell out the otp for the comformation',otp)
        amount=0
        index=int(input('enter the number according their ids 1 to upto 10: '))
        # same_as_index=input('enter the same number as index: ')
        while True:
            if index==index:
                list_feedback=[]
                list_rating=[]
                d[index]['current location']=input('enter the current location: ')
                d[index]['destination']=input('enter the destination of the user: ')
                km=int(input('enter how many kilometre you want go: '))
                d[index]['isheriding']=True
                car=input('enter the type of the car')
                money_for_1km=int(input('enter the amount according to type of car booking 1 km: '))
                d[index]['car']=km*money_for_1km
                d[index]['payment_options']=input('enter the payment as per ur wish online or offline: ')
                feedback=input('enter the feedback')
                list_feedback.append(feedback)
                d[index]['feedback']=list_feedback
                rating=int(input('enter the rating in numbers 1 to 5 in the range: '))
                list_rating.append(rating*'*')
                d[index]['rating']=list_rating
                import time
                print("exact time of the ride starts: ", end ="")# printing the start time
                print(time.ctime())
                time.sleep(50)# using sleep() to hault the code execution
                print("Time taken for the current place to destination place: ", end ="")# printing the end time
                print(time.ctime())
                phone_comformation=input('enter the desicion like yes or no type: ')
                if phone_comformation=='yes':
                    p_no=input('enter the mobile number of the rider: ')
                    d[index]['phonenumber']=p_no
                    print('phone call is connecting to rider:',p_no)
                else:
                    print('not interested to communicate with rider')
                with open('main uber.json','a') as f:
                    json_string=json.dump(d[index],f,indent=4)
                f.close()
                print(d[index]) 
            break    
    else:
        print('Your ride is cancelled')
rider(d)

