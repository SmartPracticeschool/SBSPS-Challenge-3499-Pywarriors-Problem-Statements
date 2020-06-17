def bill_count(amount,bills):

    if min(bills)>amount:
 
       print("invalid")
    
       exit()
   
    elif amount<0:
    
       print("invalid")
      
       exit()
   
    for i in bills:
     
       if i<0:
         
           print("invalid")
     
           exit()
       
       elif i not in [2000,500,200,100,50,20,10,5,2,1]:
 
           print("invalid")
    
           exit()
  
    lens=len(bills)
  
    notecounter=[]
   
    for i in range(0,lens):
   
         notecounter.append(0)
   
    mini=0
    
    bills.sort(reverse=True)
   
    for i,j in zip(bills,notecounter):
    
         if amount>=i:
        
                j=amount//i
         
                amount=amount-j*i
        
                mini=mini+j
  
    print(mini)

amount=100

bills=[1,10,20]

bill_count(amount,bills)
       
