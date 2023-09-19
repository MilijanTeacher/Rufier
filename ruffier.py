''' Module for calculating the results of Ruffier tests.
 
The sum of the three tries at pulse readings (before strain, right after strain, and after a short break)
ideally, there should be no more than 200 beats per minute.
We propose that the children measure their pulse for 15 seconds,
and find the result of beats per minute by multiplying by 4:
   S = 4 * (P1 + P2 + P3)
The further the result is from the ideal 200 beats, the worse it is.
Traditionally, tables are given by values divided by 10.
 
Ruffier index  
   IR = (S - 200) / 10
is evaluated corresponding to age according to the table:
        7-8             9-10                11-12               13-14               15+ (only for adolescents!)

perfect     < 6.5           < 5                 < 3.5               < 2                 < 0.5  
good    >= 6.5 и < 12   >= 5 и < 10.5       >= 3.5 и < 9        >= 2 и < 7.5        >= 0.5 и < 6
satisfactory  >= 12 и < 17    >= 10.5 и < 15.5    >= 9 и < 14         >= 7.5 и < 12.5     >= 6 и < 11
weak  >= 17 и < 21    >= 15.5 и < 19.5    >= 14 и < 18        >= 12.5 и < 16.5    >= 11 и < 15
unsatisfactory   >= 21           >= 19.5             >= 18               >= 16.5             >= 15

the result “unsatisfactory” is 4 from the result “weak” for all ages,
“weak” is separated from “satisfactory” by 5, and “good” from “satisfactory” by 5.5
 
so we will write a function ruffier_result(r_index, level) which will produce
the calculated Ruffier index and level “unsatisfactory” for the tested age, and produce a result
 
'''
# here the lines which produce the result are given
txt_index = "Your Ruffier index: "
txt_workheart = "Heart efficiency: "
txt_nodata = '''
there is no data for that age'''
txt_res = []
txt_res.append('''low.
Go see your doctor ASAP!''')
txt_res.append('''satisfactory.
Go see your doctor!''')
txt_res.append('''average.
It might be worth additional tests at the doctor.''')
txt_res.append('''
higher than average''')
txt_res.append('''
high''')

def ruffier_index(P1, P2, P3):
   ''' it returns the index value according to the three pulse calculations for comparison with the table'''
   return (4*(P1+P2+P3)-200)/100

def neud_level(age):
   ''' the options with an age of less than 7 and with adults have to be processed separately,
   here we select the level “unsatisfactory” only within the table:
   for the age of 7, “unsatisfactory” is an index of 21, then onwards every 2 years it decreases by 1.5 until the level of 15 at age 15–16 '''
   n = (min(age,15)-7)//2
   result= 21 - n*1.5
   return result
    
def ruffier_result(r_index, level):
   ''' the function obtains a Ruffier index and interprets it,
   we return the readiness level: a number from 0 to 4
   (the higher the readiness level, the better).  '''
   if r_index >= level: #rindex = 9 a level mi je 16.5
      return 0
   level = level - 4
   if r_index >= level:#rindex = 9 a level mi je 12.5
      return 1
   level = level - 5
   if r_index >= level: #rindex = 9 a level mi je 7.5
      return 2
   level = level - 5.5
   if r_index >= level:#rindex = 9 a level mi je 1.95
      return 3
   else:
      return 4
   


def test(P1, P2, P3, age):
   ''' this function can be used from outside the module for calculating the Ruffier index.
   We return the ready texts that just need to be written in the necessary place
   We use the constants used at the beginning of this module for texts. '''
   if age < 7:
      return (txt_index + "0", txt_nodata)
   else:
      ruff_index = ruffier_index(P1,P2,P3)# dobijam koji mi je index na osnovu unesnih podataka
      result = txt_res[ruffier_result(ruff_index,neud_level(age))]
      res = txt_index + str(ruff_index) + "\n" + txt_workheart + result
      return res

