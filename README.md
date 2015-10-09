FacebookGroupCollecctor
=====================================
(v.1 - September 27, 2015)

FacebookGroupCollector are a set of scripts (html and javascript) to collect facebook group information and parse it into JSON format. The effective scripts are fetchGUI.py and json2.js. The rest are helpful files for developers and data grabbed from the Facebook Group: eg, [Asian American Chicago Network (AACN)](https://www.facebook.com/groups/asianamericanchicagonetwork/).

Ruby Versions
---------------
You need to run with Ruby 2.2.3 (x64) (Download from: http://rubyinstaller.org/downloads/) to start a localhost before you run .py file. Other version above 2.2.0 should work as well. After installing Ruby, please type "gem install serve" in Command Prompt to install serve package (Full instructions: http://get-serve.com/get-started).

What You Need Before you Start
-------------------------------
You need to know the GroupID of the group you would like to collect data from (Get groupID using: https://lookup-id.com/), and input it in the GUI. Please make sure the group you would like to access is a public group.

Your Facebook account also need to be granted at least Tester permission to modify and run the app.

Setup and Go
-------------
1. Download fetchGUI.py and json2.js, and make sure that you have Firefox browser.
2. Open Command Prompt from the folder where fetchGUI.py and json2.js locate, and type "serve".
3. Run fetchGUI.py with Python 2.7, and a webpage tab would pop up in Firefox.
4. At the first time you click the button on the webpage, a Facebook website about your verification would show up. Click Okay. If error shows up, it means you have not been granted permission.
5. Click the button again, and windows to save data webpages would pop up.
6. Save webpages to your computer.
