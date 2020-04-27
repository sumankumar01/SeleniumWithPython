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
       Way 2: 
           i) Simply paste the chromedriver.exe under C:\Users\kumar\AppData\Local\Programs\Python\Python37\Scripts
           ii) Now write the simple code as below:
                driver=webdriver.Chrome()
                driver.get("http://www.newtours.demoaut.com/")    
  
  3 -> Python unit Testing Framework
      
        1. Pytest
        2. Nose Test
        3. Unittest

            3 -> Html report using UnitTest and HtmlReporter
![Image description](https://github.com/sumankumar01/SeleniumWithPython/blob/master/images/Capture.JPG?raw=true)

  4 -> Generate allure Report.
       downloads the allure zip file and set the environment variable
       https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.10.0/
       install the allure
       pip install allure-pytest
       
       import pytest
import unittest
import HtmlTestRunner
from HtmlTestRunner import HTMLTestRunner
import allure

@allure.story('Your Story here')
@allure.feature('Your Feature here')
class CodeVlidation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Executed Before the all the method executed in class')

    @classmethod
    def tearDownClass(cls):
        print('xecuted after the all the method executed in class')


    def setUp(self):
        print("Setup the environment")
    def tearDown(self):
        print("cleaning the environment")
    
    def testcase1(self):

        print("running the test case1")
        self.assertEqual(2, 2)

    def testcase2(self):
        print("running the test case2")
        self.assertEqual(2, 3)

# def suite():
#     suite = unittest.TestSuite()
#         ##   suite.addTest (CodeVlidation("testcase1"))
#         ##   suite.addTest (CodeVlidation("testcase2"))
#     suite.addTest(unittest.makeSuite(CodeVlidation))
#     return suite
#
# if __name__ == '__main__':
#     runner = unittest.TextTestRunner()
#     test_suite = suite()
#     runner.run (test_suite)

if __name__ == '__main__':

    testList = [CodeVlidation]
    testLoad = unittest.TestLoader()

    TestList = []
    for testCase in testList:
        testSuite = testLoad.loadTestsFromTestCase(testCase)
        TestList.append(testSuite)

    newSuite = unittest.TestSuite(TestList)
    runner = unittest.TextTestRunner()
    runner=HTMLTestRunner(output='example_dir')
    runner.run(newSuite)


then run from cmd
  D:\import\UnitTestPython>python -m pytest UnitTest12345.py --alluredir ./results
  D:\import\UnitTestPython>allure serve ./results/    
    detailed step -- PythonAllure.blogspot.com
     
       
