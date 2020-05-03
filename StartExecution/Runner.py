import unittest

from HtmlTestRunner import HTMLTestRunner

from testcase.login import Login

testList = [Login]
testLoad = unittest.TestLoader()

TestList = []
for testCase in testList:
    testSuite = testLoad.loadTestsFromTestCase(testCase)
    TestList.append(testSuite)

newSuite = unittest.TestSuite(TestList)
runner = unittest.TextTestRunner()
runner=HTMLTestRunner(output='Report_dir')
runner.run(newSuite)
