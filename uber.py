print("_________________________WELL COME TO UBER APP__________________________")
dect={"star market":10,"Dmart":30,"KSR raily":40,"Nandi hills":60,"Shivaji market":33}
d={'mini':7,'auto':5,'prime sedon':10,'prime play':13,'prime suv':15,'hourly rental km':300}
phonenos={'a':9553880630,'b':7993948903,'c':9705615402,'d':7893592978,'e':88859512978}
def rider(destination,cars,phone):
    comformation=input('enter the decion yes or no type: ')
    if comformation=='yes':
        print('comfirm')
        print('your ride is on the way please dont cancel the ride')
        rounds=int(input("enter how many times do you want take  rounds::"))
        km=int(input("enter the how many km you want:"))
        km_amount=0
        amount=0
        index=1
        while index<=rounds:
            amount=dect[destination]*5
            km_amount=d[cars]*km
            time=dect[destination]*60
            index=index+1
        print(phonenos)
        p_no=0
        phone_comformation=input('enter the desicion like yes or no type: ')
        if phone_comformation=='yes':
            p_no=phonenos[phone]
            print('phone call is connecting to rider:',p_no)
        else:
            print('not interested to communicate with rider')
        print("time taking",time,"min for",destination)
        print('your cab is arrival within 15 minuts')
        print("total amount",amount)
        print('total amount for the vehicles:',km_amount)

    else:
        print('Your ride is cancelled')
destination=input("enter the destination places: ")
cars=input("enter the cab which you want: ")
phone=input('enter the phonenos as person name: ')
rider(destination,cars,phone)