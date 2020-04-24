# SeleniumWithPython
Automation with Selenium And Python

IDE- Pycharm

1 -> Install selenium using cmd prompt.

     C:\Users\kumar>pip install selenium
     C:\Users\kumar>pip list
              Package    Version
              ---------- -------
              pip        20.0.2
              pytz       2019.3
              selenium   3.141.0
              setuptools 41.2.0
              urllib3    1.25.9
              
 2 -> Set the driver path
 
       Way 1:
         driver = webdriver.Chrome(executable_path=r"C:\Users\kumar\AppData\Local\Programs\Python\Python38-32\Scripts\chromedriver.exe")
          driver.get("http://www.newtours.demoaut.com/")
       Way 1: 
           i) Simply paste the chromedriver.exe under C:\Users\kumar\AppData\Local\Programs\Python\Python37\Scripts
           ii) Now write the simple code as below:
                driver=webdriver.Chrome()
                driver.get("http://www.newtours.demoaut.com/")
