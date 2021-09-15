# from pie_clone import PiEncrypt
from piencrypt import pie
import random
import unittest
import os


Texts = ['Hi', 'Solo', 'Sid', 'Test', 'Lily', 'Python', 'Throttlerz', 'Password', 'Good Morning', 'Good Evening']   

class TestClac(unittest.TestCase): 
        def test_quantity(self):  
            for i in range(800):
                data = []
                for i in range(5):
                    r = random.choice(Texts)
                    data.append(r)   
                input = ", ".join(data) 
                try:
                    r = pie.PiEncrypt('pic.png')
                    r.get_data()
                    r.hide_data(input)
                    output = r.read_data()
                    r.revert()
                except Exception as e:
                    raise ValueError(e)
            return output

        def test_quality(self):

            for i in range(10):
                data = []
                for i in range(5000):
                    r = random.choice(Texts)
                    data.append(r)

                input = ", ".join(data)

                try:
                    r = pie.PiEncrypt('pic.png')
                    r.get_data()
                    r.hide_data(input)
                    output = r.read_data()
                    r.revert()
                except Exception as e:
                    raise ValueError(e)
            return output


def infile_test():
    for i in range(10):
        data = []
        for i in range(5000):
            r = random.choice(Texts)
            data.append(r)
  
        input = ", ".join(data)
        try:
            r = pie.PiEncrypt('pic.png')
            r.get_data()
            r.hide_data(input)
            output = r.read_data()
            r.revert()
            print(output, end=r" %FINISHED% ")
        except Exception as e:
            raise ValueError(e)
  
if   __name__ == "__main__":
    unittest.main()
    # infile_test()



