z=[]
r = 0
while True:
    b=input('Pai store\n Nike[n]\n Adidas[a]\n VANS[v]\n แสดงรายการ[s]\n ออกจากระบบ[x]\n')
    b=b.lower()
    if b=='n':
        print('**********Nike**********')
        print(' 1) Nike Epic React [n1]\n 2) Nike Zoom Fly 3 [n2]\n 3) Nike Zoom Pegasus [n3]')
        Nikelist = ["Nike Epic React      3800      20%      ","Nike Zoom Fly 3      5800      20%      ","Nike Zoom Pegasus    4600      20%      "]
        Nikeprice1 = [3800,5800,4600]
        Nikeprice2 = [Nikeprice1[0]*20/100,Nikeprice1[1]*20/100,Nikeprice1[2]*20/100]
        Nikeprice3 = [Nikeprice1[0]-Nikeprice2[0],Nikeprice1[1]-Nikeprice2[1],Nikeprice1[2]-Nikeprice2[2]]
        c=input('ป้อนรายการสินค้า(รหัสสินค้า)')
        if c=='n1':r += Nikeprice3[0]
        elif c=='n2':r += Nikeprice3[1]
        elif c=='n3':r += Nikeprice3[2]
        z.append(c)
        print('\n**********ข้อมูลได้เข้าสู่ระบบแล้ว*********\n')
   
    elif b=='a':
        print('**********Adidas**********')
        print(' 1) Supercourt [a1]\n 2) Supercourt RX [a2]\n 3) Continental 80 [a3]')
        Adidaslist = ["Supercourt           4000      30%      ","Supercourt RX        5000      30%      ","Continental 80       3500      30%      "]
        Adidasprice1 = [4000,5000,3500]
        Adidasprice2 = [Adidasprice1[0]*30/100,Adidasprice1[1]*30/100,Adidasprice1[2]*30/100]
        Adidasprice3 = [Adidasprice1[0]-Adidasprice2[0],Adidasprice1[1]-Adidasprice2[1],Adidasprice1[2]-Adidasprice2[2]]
        c=input('ป้อนรายการสินค้า(รหัสสินค้า)')
        if c=='a1':r += Adidasprice3[0]
        elif c=='a2':r += Adidasprice3[1]
        elif c=='a3':r += Adidasprice3[2]
        z.append(c)
        print('\n**********ข้อมูลได้เข้าสู่ระบบแล้ว*********\n')
   
    elif b=='v':
        print('**********VANS**********')
        print(' 1) VANS COMFYCUSH[v1]\n 2) VANS OLD SKOOL [v2]\n 3) VANS SPORT SUEDE [v3]')
        VANSlist = ["VANS COMFYCUSH       3200      50%      ","VANS OLD SKOOL       2400      50%      ","VANS SPORT SUEDE     2800      50%      "]
        VANSprice1 = [3200,2400,2800]
        VANSprice2 = [VANSprice1[0]*50/100,VANSprice1[1]*50/100,VANSprice1[2]*50/100]
        VANSprice3 = [VANSprice1[0]-VANSprice2[0],VANSprice1[1]-VANSprice2[1],VANSprice1[2]-VANSprice2[2]]
        c=input('ป้อนรายการสินค้า(รหัสสินค้า)')
        if c=='v1':r += VANSprice3[0]
        elif c=='v2':r += VANSprice3[1]
        elif c=='v3':r += VANSprice3[2]
        z.append(c)
        print('\n**********ข้อมูลได้เข้าสู่ระบบแล้ว*********\n')
    
    elif b=='s':
        print('{0:-<60}'.format(""))
        print('{0:<6}{1:<19}{2:<9}{3:<12}{4:<5}'.format('','รุ่น','ราคา','ส่วนลด','จ่ายจริง'))
        print('{0:-<60}'.format(""))
        count=0
        for d in z:
            count+=1
            print(count,end=")")
            if d=='n1':print (Nikelist[0],Nikeprice3[0])
            elif d=='n2':print(Nikelist[1],Nikeprice3[1])
            elif d=='n3':print(Nikelist[2],Nikeprice3[2])
            elif d=='a1':print(Adidaslist[0],Adidasprice3[0])
            elif d=='a2':print(Adidaslist[1],Adidasprice3[1])
            elif d=='a3':print(Adidaslist[2],Adidasprice3[2])
            elif d=='v1':print(VANSlist[0],VANSprice3[0])
            elif d=='v2':print(VANSlist[1],VANSprice3[1])
            elif d=='v3':print(VANSlist[2],VANSprice3[2])
        print('{0:-<60}'.format(""))
        print('รวมเป็นเงิน                                 ',r)
        print('{0:-<60}'.format(""))
        continue
    elif b=='x':
        break
print('ทำคำสั่งถัดไป')