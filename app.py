import streamlit as st
import pickle
model = pickle.load(open('/Users/rajeevjoshi/Downloads/RF_model.pkl','rb'))

def main():
    string = "Car Price Predictor"
    st.set_page_config(page_title=string, page_icon="🚗") 
    st.title("Car Price Predictor")
    st.markdown("##### Are you planning to buy new car ?\n##### So let's try evaluating the price based on your inputs.")
    _left, mid, _right = st.columns([1,5,10])
    with mid:
       st.image(
            "https://media2.giphy.com/media/cWWwLuxISKDRMyuqGB/giphy.gif?cid=ecf05e47ar2uwxm3xvoc30ogvz4ks96bho6ksszjrjvhw2h8&rid=giphy.gif&ct=g",
            width=550, # Manually Adjust the width of the image as per requirement
               )
    st.write('')
    st.write('')
    power = st.number_input('The power ( in hp ):', 33,779, step = 4 , key = 'Power')
    displacement = st.number_input('The diplacement ( in cc ):', 624 , 6752 , step = 8 , key = 'Displacement')
    mileage = st.number_input('The mileage of car :', 3.4 , 28.4 , step = 0.5 , key = 'Mileage')
    airbags = st.radio("Number of airbags :",(0,1,2,3,4,5,6,7,8,9,10,14), key = 'Airbags')
    seats = st.radio("Number of seats :",(2,4,5,6,7,8,9), key = 'Seats')
    Manufacturer_Audi = st.selectbox('Which company do you want?', ('Tata', 'Datsun', 'Renault', 'Maruti Suzuki', 'Hyundai', 'Premier', 'Toyota',
                 'Nissan', 'Volkswagen', 'Ford', 'Mahindra', 'Fiat', 'Honda',
                 'Jeep' ,'Isuzu', 'Skoda', 'Audi', 'Dc', 'Mini',
                 'Jaguar', 'Bmw', 'Porsche', 'Lexus', 'Maserati','Lamborghini', 'Bentley',
                 'Ferrari', 'Force', 'Volvo' , 'Land Rover Rover' , 'Kia', 
                 'Mitsubishi', 'Maruti Suzuki R', 'Land Rover','Aston Martin'), key = 'Manufacturer')

    dict_manufacturer = {'Tata' : 30, 'Datsun' : 3, 'Renault':28, 'Maruti Suzuki' : 20, 'Hyundai' : 10, 'Premier':27, 'Toyota' : 31,
                 'Nissan' : 25, 'Volkswagen':32, 'Ford' : 8, 'Mahindra' : 19, 'Fiat' : 6, 'Honda' : 9,
                 'Jeep' : 13,'Isuzu' : 11, 'Skoda' : 29, 'Audi': 0, 'Dc' : 4, 'Mini' : 23,
                 'Jaguar' : 12, 'Bmw' : 2, 'Porsche' : 26, 'Lexus':18, 'Maserati' : 22,'Lamborghini':15, 'Bentley' : 1,
                 'Ferrari' : 5, 'Force' : 7, 'Volvo' : 33 , 'Land Rover Rover' : 17 , 'Kia': 14, 
                 'Mitsubishi' : 24, 'Maruti Suzuki R' : 21, 'Land Rover' : 16}   

    list_manufacturer = ['Manufacturer_Audi', 'Manufacturer_Bentley',
       'Manufacturer_Bmw', 'Manufacturer_Datsun', 'Manufacturer_Dc',
       'Manufacturer_Ferrari', 'Manufacturer_Fiat', 'Manufacturer_Force',
       'Manufacturer_Ford', 'Manufacturer_Honda', 'Manufacturer_Hyundai',
       'Manufacturer_Isuzu', 'Manufacturer_Jaguar', 'Manufacturer_Jeep',
       'Manufacturer_Kia', 'Manufacturer_Lamborghini',
       'Manufacturer_Land_Rover', 'Manufacturer_Land_Rover_Rover',
       'Manufacturer_Lexus', 'Manufacturer_Mahindra',
       'Manufacturer_Maruti_Suzuki', 'Manufacturer_Maruti_Suzuki_R',
       'Manufacturer_Maserati', 'Manufacturer_Mini',
       'Manufacturer_Mitsubishi', 'Manufacturer_Nissan',
       'Manufacturer_Porsche', 'Manufacturer_Premier',
       'Manufacturer_Renault', 'Manufacturer_Skoda', 'Manufacturer_Tata',
       'Manufacturer_Toyota', 'Manufacturer_Volkswagen',
       'Manufacturer_Volvo']
   
    list_feat = []
    if(Manufacturer_Audi != 'Aston Martin'):
        if(Manufacturer_Audi):
            for i in range(0,34):
                if (dict_manufacturer[Manufacturer_Audi] != i):
                   list_feat.append(0)
                else:
                   list_feat.append(1)
        
            Manufacturer_Audi = list_feat[0]
            Manufacturer_Bentley = list_feat[1]
            Manufacturer_Bmw = list_feat[2]
            Manufacturer_Datsun = list_feat[3]
            Manufacturer_Dc = list_feat[4]
            Manufacturer_Ferrari = list_feat[5]
            Manufacturer_Fiat = list_feat[6]
            Manufacturer_Force = list_feat[7]
            Manufacturer_Ford = list_feat[8]
            Manufacturer_Honda = list_feat[9]
            Manufacturer_Hyundai = list_feat[10]
            Manufacturer_Isuzu = list_feat[11]
            Manufacturer_Jaguar = list_feat[12]
            Manufacturer_Jeep = list_feat[13]
            Manufacturer_Kia = list_feat[14]
            Manufacturer_Lamborghini = list_feat[15]
            Manufacturer_Land_Rover = list_feat[16]
            Manufacturer_Land_Rover_Rover = list_feat[17]
            Manufacturer_Lexus = list_feat[18]
            Manufacturer_Mahindra = list_feat[19]
            Manufacturer_Maruti_Suzuki = list_feat[20]
            Manufacturer_Maruti_Suzuki_R = list_feat[21]
            Manufacturer_Maserati = list_feat[22]
            Manufacturer_Mini = list_feat[23]
            Manufacturer_Mitsubishi = list_feat[24]
            Manufacturer_Nissan = list_feat[25]
            Manufacturer_Porsche = list_feat[26]
            Manufacturer_Premier = list_feat[27]
            Manufacturer_Renault = list_feat[28]
            Manufacturer_Skoda = list_feat[29]
            Manufacturer_Tata = list_feat[30]
            Manufacturer_Toyota = list_feat[31]
            Manufacturer_Volkswagen = list_feat[32]
            Manufacturer_Volvo = list_feat[33]

    elif(Manufacturer_Audi == 'Aston Martin'):
        Manufacturer_Audi = 0
        Manufacturer_Bentley = 0
        Manufacturer_Bmw = 0
        Manufacturer_Datsun = 0
        Manufacturer_Dc = 0
        Manufacturer_Ferrari = 0
        Manufacturer_Fiat = 0
        Manufacturer_Force = 0
        Manufacturer_Ford = 0
        Manufacturer_Honda = 0
        Manufacturer_Hyundai = 0
        Manufacturer_Isuzu = 0
        Manufacturer_Jaguar = 0
        Manufacturer_Jeep = 0
        Manufacturer_Kia = 0
        Manufacturer_Lamborghini = 0
        Manufacturer_Land_Rover = 0
        Manufacturer_Land_Rover_Rover = 0
        Manufacturer_Lexus = 0
        Manufacturer_Mahindra = 0
        Manufacturer_Maruti_Suzuki = 0
        Manufacturer_Maruti_Suzuki_R = 0
        Manufacturer_Maserati = 0
        Manufacturer_Mini = 0
        Manufacturer_Mitsubishi = 0
        Manufacturer_Nissan = 0
        Manufacturer_Porsche = 0
        Manufacturer_Premier = 0
        Manufacturer_Renault = 0
        Manufacturer_Skoda = 0
        Manufacturer_Tata = 0
        Manufacturer_Toyota = 0
        Manufacturer_Volkswagen = 0
        Manufacturer_Volvo = 0
   

    Fuel_Type_Petrol = st.selectbox('What is the fuel type of the car ?',('Petrol','Diesel', 'Hybrid', 'CNG + Petrol'), key='Fuel_Type')
    if(Fuel_Type_Petrol=='Petrol'):
        Fuel_Type_Petrol=1
        Fuel_Type_Diesel=0
        Fuel_Type_Hybrid=0
    elif(Fuel_Type_Petrol=='Diesel'):
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=1
        Fuel_Type_Hybrid=0
    elif(Fuel_Type_Petrol=='Hybrid'):
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=0
        Fuel_Type_Hybrid=1
    else:
        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=0
        Fuel_Type_Hybrid=0
 
    Gear_Type_Automatic = st.selectbox('What is gear type?',('Automatic','CVT','DCT','Manual','AMT'), key = 'Gear_Type')
    if(Gear_Type_Automatic=='Automatic'):
        Gear_Type_Automatic=1
        Gear_Type_CVT = 0
        Gear_Type_DCT = 0
        Gear_Type_Manual=0
    elif(Gear_Type_Automatic=='CVT'):
        Gear_Type_Automatic=0
        Gear_Type_CVT = 1
        Gear_Type_DCT = 0
        Gear_Type_Manual=0
    elif(Gear_Type_Automatic=='DCT'):
        Gear_Type_Automatic=0
        Gear_Type_CVT = 0
        Gear_Type_DCT = 1
        Gear_Type_Manual=0
    elif(Gear_Type_Automatic=='Manual'):
        Gear_Type_Automatic=0
        Gear_Type_CVT = 0
        Gear_Type_DCT = 0
        Gear_Type_Manual=1
    else:
        Gear_Type_Automatic=0
        Gear_Type_CVT = 0
        Gear_Type_DCT = 0
        Gear_Type_Manual=0
     
    Drivetrain_AWD = st.selectbox('Select Drive Train:',('AWD (All Wheel Drive)','FWD (Front Wheel Drive)','RWD (Rear Wheel Drive)','4WD'), key = 'Drivetrain')
    if(Drivetrain_AWD == 'AWD (All Wheel Drive)'):
       Drivetrain_AWD = 1
       Drivetrain_FWD = 0
       Drivetrain_RWD = 0
    elif(Drivetrain_AWD == 'FWD (Front Wheel Drive)'):
       Drivetrain_AWD = 0
       Drivetrain_FWD = 1
       Drivetrain_RWD = 0
    elif(Drivetrain_AWD == 'RWD (Rear Wheel Drive)'):
       Drivetrain_AWD = 0
       Drivetrain_FWD = 0
       Drivetrain_RWD = 1
    else:
       Drivetrain_AWD = 0
       Drivetrain_FWD = 0
       Drivetrain_RWD = 0 

    if st.button("Estimate Price", key = 'predict'):
        Model = model #get_model
        prediction = Model.predict([[power,displacement,airbags,seats,mileage,Manufacturer_Audi,Manufacturer_Bentley,Manufacturer_Bmw,Manufacturer_Datsun,Manufacturer_Dc,Manufacturer_Ferrari,Manufacturer_Fiat,
                                        Manufacturer_Force,Manufacturer_Ford,Manufacturer_Honda,Manufacturer_Hyundai,Manufacturer_Isuzu,Manufacturer_Jaguar,Manufacturer_Jeep, Manufacturer_Kia,Manufacturer_Lamborghini,
                                        Manufacturer_Land_Rover,Manufacturer_Land_Rover_Rover,Manufacturer_Lexus,Manufacturer_Mahindra,Manufacturer_Maruti_Suzuki, Manufacturer_Maruti_Suzuki_R, Manufacturer_Maserati,
                                        Manufacturer_Mini,Manufacturer_Mitsubishi,Manufacturer_Nissan,Manufacturer_Porsche, Manufacturer_Premier,Manufacturer_Renault,Manufacturer_Skoda,Manufacturer_Tata,Manufacturer_Toyota,
                                        Manufacturer_Volkswagen,Manufacturer_Volvo,Fuel_Type_Petrol,Fuel_Type_Diesel,Fuel_Type_Hybrid,Gear_Type_Automatic, Gear_Type_CVT,Gear_Type_DCT, Gear_Type_Manual,Drivetrain_AWD,Drivetrain_FWD,Drivetrain_RWD]])
        output = round(prediction[0],2)
        if output < 0:
            st.warning("Price of car having such inputs can not be estimated !!")

        else:
            st.success("The price of such car would be {} ".format(output))

        #except:
            #st.warning("Opps!! Something went wrong\nTry again!")   

if __name__ == '__main__':
    main()
