Shop = list()

def Store(): #จัดกลุ่มข้อมูลให้อยู่ในกลุ่ม
  print("---------------------\nรองเท้า น้อนเต้ย \n---------------------")
  print('[1]NIKE\n[2]ADIDAS\n[3]KITO\n[4]แสดงรายการสินค้า')
  Select = input('\nกรุณาเลือกยี่ห้อ')
  if Select == '1' : F1() #selectเสร็จ ถ้าเราเลือกf1 ก็จะแสดงผลให้เราเลือกตัวที่1
  elif Select == '2' : F2()
  elif Select == '3' : F3()
  elif Select == '4' : Shop2()
  else: Store()

def F1() :
  print("\n--------------\nNIKE\n--------------") #แสดงค่าว่าจะให้เราเลือกรุ่นอะไร
  print('[1]Nike zoom\n[2]Nike Air \n[3]Nike m200')
  F1Price(int(input("\nเลือกรุ่น: "))) #จากนั้นก็จะเก็บค่าเป็นค่า n   ในf1price

def F1Price(n):
  if n == 1:
    print("Nike Air ราคา 4000 บาท  ส่วนลด 10%")
    Shop.append(['Nike zoom','4000','10%','3600']) #appendคือเอาค่าไปต่อท้ายเรื่อยๆ
    Store()
    
  elif n == 2:
    print("Nike Air ราคา 2500 บาท  ส่วนลด 10%")
    Shop.append(['Nike Air','2500','10%','2160'])
    Store()
  elif n == 3:
    print("Nike m200 ราคา 3000 บาท  ส่วนลด 10%")
    Shop.append(['Nike m200','3000','10%','2700'])
    Store()
  else : print("ขออภัย ทางร้านไม่มีสินค้า") , F1() #ถ้าเราพิมพ์นอก็จะปริ้นคำนั้น จากนั้นก็จะเริ่มที่f1

def F2():
  print("\n--------------\nADIDAS\n--------------")
  print('[1] Adidas U1\n[2] Adidas U2\n[3] Adidas U2')
  F2Price(int(input("\nเลือกรุ่น: ")))


def F2Price(n):
  if n == 1:
    print("Adidas U1 ราคา 5000 บาท  ส่วนลด 40%")
    Shop.append(['Adidas U1 ','5000','40%','3000'])
    Store()
  elif n == 2:
    print("Adidas U2 ราคา 6000 บาท ส่วนลด 40%")
    Shop.append(['Adidas U2 ','6000','30%','3600'])
    Store()
  elif n == 3:
    print("Adidas U3 ราคา 4000 บาท  ส่วนลด 40%")
    Shop.append(['Adidas U3','4000','40%','2400'])
    Store()
  else : print("ขออภัย ทางร้านไม่มีสินค้า") , F2()
    
def F3():
  print("\n--------------\nKITO\n--------------")
  print('[1]KITO K1\n[2KITO K2\n[3]KITO K3')
  F3Price(int(input("\nเลือกรุ่น: ")))

def F3Price(n):
  if n == 1:
    print("KITO K1 ราคา 1290 บาท  ส่วนลด 20%")
    Shop.append(['KITO K1','1290','20%','1032'])
    Store()
  elif n == 2:
    print("KITO K2  ราคา 2691 บาท  ส่วนลด 20%")
    Shop.append(['KITO K2','2691','20%','2152'])
    Store()
  elif n == 3:
    print("KITO K3 ราคา 1290 บาท  ส่วนลด 20%")
    Shop.append(['KITO K3','1290','20%','1032'])
    Store()
  else : print("ขออภัย ทางร้านไม่มีสินค้า") , F3()

def Shop2():
  sum = 0 #กำหนดเป็น0 เพื่อจะเก็บเป็นค่าราคารวม
  print("\n---------------------------------------------------------------------------------")
  print("รุ่นรองเท้า                 ราคา                   ส่วนลด                     จ่ายจริง")
  print("-----------------------------------------------------------------------------------")
  for i in Shop: #ไปเอาค่าจากชอปที่เป็นแนวตั้ง เอาเข้ามา
    for k in i:  #ค่าแนวนอน
      print(k.ljust(25),end="") #k.j คือเว้นวรรคไปซ้ายทำไหร่
    print()
  for i in range(len(Shop)) : sum = sum + int(Shop[i][3])
  print("-----------------------------------------------------------------------------------")
  print("รวมเป็นเงิน                                                                  %d"%sum)
  exit
Store()