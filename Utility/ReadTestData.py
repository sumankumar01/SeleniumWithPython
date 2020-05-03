import json
import TestResourecs
class jsonFiledata:
    def __init__(self):
        with open("/PythonSelenium/TestResourecs/testdata.json") as f:
            self.data = json.load(f)
        self.returnValue=""

    def testdata(self,field,value):
        self.field= field
        self.value=value
        for key, value in self.data.items():
            if key == self.field:
                for Value in self.data[key]:
                    print('Name: ' + Value[self.value])
                    self.returnValue= Value[self.value]
                break
        return self.returnValue