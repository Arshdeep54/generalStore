import pandas as pd
import matplotlib.pyplot as plt

ownerStock_df=pd.read_csv('D:\python project 12\ownerStock.csv',index_col=0)


costlistSeries=pd.read_csv('D:\python project 12\costlist.csv',index_col=0)
sellingSeries=pd.read_csv('D:\python project 12\sellist.csv',index_col=0)

costlist=costlistSeries.iloc[:,0].to_list()
sellingList=sellingSeries.iloc[:,0].to_list()

def updateCsv():
    costlistSeries=pd.Series(costlist)
    sellingSeries=pd.Series(sellingList)
    ownerStock_df.to_csv(r'D:\python project 12\ownerStock.csv')
    costlistSeries.to_csv('D:\python project 12\costlist.csv')
    sellingSeries.to_csv('D:\python project 12\sellist.csv')
   
updateCsv()

codelist=[]
quanlist=[]

def checkItemCode(itemcode):
        if itemcode in ownerStock_df.itemCode:
            return True
        else: 
            return False

def add_item(itemcode,itemname,addQuantity,cost_price,sell_price):
     if itemcode-1 in ownerStock_df.itemCode:
        filt=(ownerStock_df["itemCode"]==itemcode)
        ownerStock_df.loc[filt,"quantity"]+=addQuantity
        totalCostPricelist=ownerStock_df.loc[filt,"costPrice"]*addQuantity
        totalCostPrice=int(totalCostPricelist.values[0])
        costlist.append(totalCostPrice)
        updateCsv()
     else:
        ownerStock_df.loc[len(ownerStock_df)]=[itemcode,itemname,addQuantity,cost_price,sell_price]  


def showCharts():
      
      netp=sum(sellingList)-sum(costlist)
      plt.plot(costlist,label="Purchase Rate")
      plt.plot(sellingList,label="Sell Rate")
      plt.ylabel("Rupees")
      plt.xlabel("nth purchase/sell")
      plt.legend()
      plt.title("Profit = Rs. %i" %netp)
      plt.show()
      

def checkStock(itemCode,quantity):      
    if itemCode-1 in ownerStock_df.itemCode :
        if quantity <= ownerStock_df.loc[itemCode-1,"quantity"]:
            return True
    else: return False


def showBill(codeList,quanlist):
    pricel=[]
    inamel=[]
    for x in range(len(codelist)):
          if checkStock(codelist[x],quanlist[x])==False:
               return 0
          else:
              
              y=codelist[x]
              pricel.append(ownerStock_df.loc[y-1,"price"])
              inamel.append(ownerStock_df.loc[y-1,"itemName"])
    
    print(pd.DataFrame({"itemCode": pd.Series(codeList),"itemname": pd.Series(inamel),"quantity": pd.Series(quanlist),"Price": pd.Series(pricel)}))
    price=0
    for x in pricel:
        temp=x*quanlist[pricel.index(x)]
        price=price+temp
    print("                     ")
    print("You have to pay Rs.",price) 
    totalSellPrice=price   
    sellingList.append(totalSellPrice)
    for x in codelist:
        filt=(ownerStock_df["itemCode"]==x)
        ownerStock_df.loc[filt,"quantity"]-=quanlist[codelist.index(x)]   
        updateCsv()


while True:
    print(" ")
    print("Welcome to the general Store ..umm can i know who you are?")
    print("1. The Owner")
    print("2. A Customer")
    print(" ")
    whoru=int(input("Enter the corresponding integer  "))
    print(" ")
    loop=True
    while loop==True:
         if whoru==1:
            passw = input("enter password  ")
            if passw=="arsh":
                print("                     ")
                print("Welcome Sir ")
                print("                     ")
                print("What would You like to do ")
                print("1.View stock ")
                print("2.Add stock ") 
                print("3.view last week business")
                print("4.Umm Nothing,Wanna GoBack")
                print("                     ")
                owner_einput=int(input("Enter the corresponding integer  "))
                if owner_einput==1:
                    print(ownerStock_df)
                elif owner_einput==2:
                    itemcode_input=int(input("Enter the itemCode of the item  " ))
                    if checkItemCode(itemcode_input)==False:
                     iname_input=input("Enter the Name of the item  " )
                     cp_input=int(input("Enter the Cost Price of the item  " ))
                     sp_input=int(input("Enter the Selling Price of the item  " ))
                    else:
                         cp_input=ownerStock_df.loc[itemcode_input-1,"costPrice"]
                         sp_input=ownerStock_df.loc[itemcode_input-1,"price"]
                         iname_input=ownerStock_df.loc[itemcode_input-1,"itemName"]
                    quanO_input=int(input("Enter the Quantity of the item  " ))
                    add_item(itemcode_input,iname_input,quanO_input,cp_input,sp_input)
                    print(ownerStock_df)
                    pass
                elif owner_einput==3:
                   showCharts()
                elif owner_einput==4:
                    loop=False
                    pass
            else:
                print("wrong Password")
                break    
         elif whoru==2:
           print("welcome ,What would you like to buy ")
           print(ownerStock_df.loc[:,ownerStock_df.columns!="costPrice"])
           while True:
                 itemCode_customer=int(input("Enter the iteCode of the item from above stock,print 0 if nothing more  "))
                 if itemCode_customer==0:
                    break
                 codelist.append(itemCode_customer)
                 itemQuan_customer=int(input("Enter the quantity int the units mentioned in above stock  "))
                 print(" ")
                 quanlist.append(itemQuan_customer)
           showBill(codelist,quanlist)
           print("Thank You")  
           break  

    
