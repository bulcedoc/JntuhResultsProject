from django.shortcuts import render
from django.http import HttpResponse
def check(request , to): 
 roll = str(to).strip().upper()
 from selenium import webdriver
 from selenium.webdriver.common.by import By
 import os
 try:
  driver = webdriver.Edge() 
  driver.get("http://tkrec.in/")
  driver.find_element(By.XPATH,('//*[@id="login-username"]')).send_keys(roll)
  driver.find_element(By.XPATH,('//*[@id="login-password"]')).send_keys(roll)
  driver.find_element(By.XPATH,('//*[@id="loginform"]/div[3]/div/button')).click()
  driver.find_element(By.XPATH,('//*[@id="navbarNavDropdown"]/ul[1]/li[3]/a')).click()
  name = driver.find_element(By.XPATH,('/html/body/main/div[2]/div[1]/table/tbody/tr[3]/td[2]')).text
  per = driver.find_elements(By.XPATH, ('/html/body/main/div[2]/div[2]/div[1]/table/tbody/tr/td[1]'))
  classes = []
  for e in per[:-1]:
   classes.append(e.text)
  total_conducted = per[-1].text
  par = driver.find_elements(By.XPATH, ('/html/body/main/div[2]/div[2]/div[1]/table/tbody/tr/td[2]'))
  c_conducted = []
  for e1 in par[:-1]:
    c_conducted.append(e1.text)
  total_attended = par[-1].text
  pep = driver.find_elements(By.XPATH, ('/html/body/main/div[2]/div[2]/div[1]/table/tbody/tr/td[3]'))
  c_attended = []
  for e2 in pep[:-1] :
    c_attended.append(e2.text)
  total_per = pep[-1].text
  psp = driver.find_elements(By.XPATH, ('/html/body/main/div[2]/div[2]/div[1]/table/tbody/tr/td[4]'))
  c_per = []
  for e3 in psp:
    c_per.append(e3.text)
  driver.quit()
  dic = []
  i=0
  while i<len(classes):
     se={"subject":classes[i],
         "c_c" : c_conducted[i],
         "c_a" : c_attended[i],
         "c_p" : c_per[i]} 
     dic.append(se)
     i=i+1
  context = { 'name' : name,
              't_c': total_conducted,
              't_a': total_attended,
              't_p': total_per,
              'dic': dic
            }
  return render(request,'att.html',context)
 except:
  return render(request,'went.html')

def see(request):
  from teamapp.forms import Login
  if request.method == "POST":
   form = Login(request.POST, request.FILES)
   if form.is_valid():
    roll = form.cleaned_data.get("roll")
    return resu(request,roll)
  else:  
   context = {
    'form':Login
   }


  return render(request,'home.html',context)

def sign(request):
  from teamapp.forms import Sign
  context = {
   'form':Sign()
  }

  return render(request,'sign.html',context)
def resu(request,ro):
 try:
  subject_codes = []
  subject_names = []
  subject_grades = []
  subject_credits = []
  from selenium import webdriver
  from selenium.webdriver.common.by import By
  from selenium.webdriver.chrome.options import Options
  import os
  driver = webdriver.Edge()
  roll_number = str(ro).strip().upper()
  exam_code = [1323,1358,1404,1430,1467,1504,1356,1363,1381,1435,1448,1481,1503,1391,1425,1449,1496,1560,1437,1447,1476,1501,1565,1454,1491,1550,1502,1555,1545,1580]
  for code in exam_code:
     code = str(code)
     driver.get("http://results.jntuh.ac.in/resultAction?degree=btech&examCode="+code+"&etype=r17&result=null&grad=null&type=null&htno="+roll_number)
     try:
        text_value = driver.find_element(By.CSS_SELECTOR,('#myForm > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > div')).text
        if text_value=='invalid hallticket number':
         pass
     except:
        subject = driver.find_elements(By.XPATH,('/html/body/form/div[1]/table/tbody/tr/td[1]'))
        for e in subject[1:]:
           subject_codes.append(e.text)
        sn = driver.find_elements(By.XPATH,('/html/body/form/div[1]/table/tbody/tr/td[2]'))      
        for e in sn[1:]:
           subject_names.append(e.text)
        sg = driver.find_elements(By.XPATH,('/html/body/form/div[1]/table/tbody/tr/td[3]'))      
        for e in sg[1:]:
           subject_grades.append(e.text)
        sc = driver.find_elements(By.XPATH,('/html/body/form/div[1]/table/tbody/tr/td[4]'))   
        for e in sc[1:]:
           subject_credits.append(e.text)
  driver.quit()
  if subject_codes:
   deta = []
   sof = {}
   for i in range(len(subject_codes)):
    deta.append({'code': subject_codes[i], 's_name': subject_names[i], 's_grade': subject_grades[i], 's_credit': subject_credits[i]})
   for i in deta:
    sof.update({ i['code']: [i['s_name'],i['s_grade'],i['s_credit']]})
   c = []
   for i in sof: 
    c.append([i,sof.get(i)[0],sof.get(i)[1],sof.get(i)[2]])

   context = {
       'c':c
        }    
  
   return HttpResponse(c)
  else:
   return render(request,'went.html')
 except:
  return render(request,'went.html')


def flop(request):
   return render(request,'went.html')
