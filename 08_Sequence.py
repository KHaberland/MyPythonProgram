
#программа для вычисления количества продаж и среднего чека
'''
a. До 1000 р включительно
b. От 1000 р до 3000 р включительно
c. От 3000 р до 5000 р включительно
d. Выше 5000 р 
Список продаж: sales = [2033, 300.50, 1550, 2703, 5110, 2146, 4733, 7114, 1614, 3105, 3155, 853, 10114, 1315]
'''

sales = [2033, 300.50, 1550, 2703, 5110, 2146, 4733, 7114, 1614, 3105, 3155, 853, 10114, 1315]
#sales = [2033, 300, 200, 4733]
def process_sales(sales):
    #суммы
    summ1=0
    summ2=0
    summ3=0
    summ4=0
    #количества продаж
    cnt1=0
    cnt2=0
    cnt3=0
    cnt4=0
    #средний чек
    avg1=0
    avg2=0
    avg3=0
    avg4=0
    for sale in sales:
        print(sale, end = ' ')
        if sale<=1000:
            summ1 += sale
            cnt1 += 1
        elif sale<=3000:
            summ2 += sale
            cnt2 += 1    
        elif sale<=5000:
            summ3 += sale
            cnt3 += 1
        elif sale>5000:
            summ4 += sale
            cnt4 += 1        
    print ("")
    if cnt1>0: #иначе avg1 оставляем равным 0
        avg1 = summ1/cnt1
    if cnt2>0: #иначе avg1 оставляем равным 0
        avg2 = summ2/cnt2
    if cnt3>0: #иначе avg1 оставляем равным 0
        avg3 = summ3/cnt3
    if cnt4>0: #иначе avg1 оставляем равным 0
        avg4 = summ4/cnt4
    print("до 1000 включительно:          количество продаж = " + str(cnt1) + ", средний чек = " + "{:.2f}".format(avg1) + " р")
    print("от 1000 до 3000 включительно : количество продаж = " + str(cnt2) + ", средний чек = " + "{:.2f}".format(avg2) + " р")
    print("от 3000 до 5000 включительно:  количество продаж = " + str(cnt3) + ", средний чек = " + "{:.2f}".format(avg3) + " р")
    print("свыше 5000 включительно:       количество продаж = " + str(cnt4) + ", средний чек = " + "{:.2f}".format(avg4) + " р")
    print ("готово")
process_sales(sales)


