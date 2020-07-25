
#################################################################################
# Author(s):  AbdulBaseer Mahmood
# Username(s):   AbdulBaseer Mahmood
#

# Purpose:     A desktop notification application that notifies the user about the Coronavirus cases
#################################################################################
# Acknowledgements:
#
#
#################################################################################
    #   these are packages and mudules

from win10toast import ToastNotifier
import requests
from bs4 import BeautifulSoup




class Corona:
    def __init__(self):

        self.title =  "cases of Covid-19"
        self.dataMechanism()



    def notificationMessage(self, message):
        """This function generates the notification after any interval we assign to the function and a toast message
        pops up on our computer

        :param message: this parameter is the message in string form. It is just to show what our content is about
        :return:   none
        """
        object = ToastNotifier()
        object.show_toast(self.title, message, duration=4, icon_path=None)

    def codensedForm(self,soup):
        """

        :param soup: this is our html data
        :return:  it returns dictionary form of the list of our data
        """
        myDataStr = ""

        for baseer in soup.find_all('tr'):        #this loops finds all 'table row' tag from html
            myDataStr += baseer.get_text()         # this converts it into text form only

        listForm = " ".join(myDataStr.split())
        splitForm = listForm.split("\n\n")
        l = splitForm[0].split(" ")
        base = l[0: 40]


        someInitial = 2
        for delete in range(len(base) - 1):
            if someInitial > len(base):
                break
            base.pop(someInitial)
            someInitial += 3

        someInitialtwo = 1
        for delete in range(len(base) - 1):
            if someInitialtwo > len(base):
                break
            base.pop(someInitialtwo)
            someInitialtwo += 2

        res_dct = {base[i]: base[i + 1] for i in range(0, len(base), 2)}         #this converts our list into dictionary

        return res_dct

    def getDate(self, url):
        r = requests.get(url)
        return r.text


    def dataMechanism(self):

        myHtmlData = self.getDate("https://www.bbc.com/news/world-51235105")

        soupParse = BeautifulSoup(myHtmlData, 'html.parser')

        data = self.codensedForm(soupParse)

        countries = ['US', 'Brazil', 'UK', 'Mexico', 'Italy', 'India', 'France', 'Spain', 'Peru', 'Iran']
        for item in countries:

            if item in data.keys():

                nText = f"Total case in {item}: {data[item]}"
                #
                self.notificationMessage(nText)




if __name__ == "__main__":

    while True:

        corona = Corona()
