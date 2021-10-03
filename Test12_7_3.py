money = int(input("Введите сумму")) #100000
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0} 
a = float(per_cent['ТКБ']) #Банк ТКБ
TKb = int(money/100*a)
b = float(per_cent['СКБ']) #Банк СКБ
CKb = int(money/100*b)
c = float(per_cent['ВТБ']) #Банк ВТБ
BTb = int(money/100*c)
e = float(per_cent['СБЕР']) #Банк СБЕР
SBER = int(money/100*e)
s = []
s.append(TKb)
s.append(CKb)
s.append(BTb)
s.append(SBER)
print(s) #Список с расщитаными процентами от заданной суммы
list.sort(s) #Сортировка списка
deposit = s[-1] 
print("Максимальная сумма, которую вы можете заработать - " +str(deposit))

