FacebookGroupCollecctor
=====================================
(v.1 - September 27, 2015)

FacebookGroupCollector are a set of scripts (html and javascript) to collect facebook group information and parse it into JSON format. The effective scripts are fetch.html and json2.js. The rest are data grabbed from the Facebook Group: eg, [Asian American Chicago Network (AACN)](https://www.facebook.com/groups/asianamericanchicagonetwork/).

Ruby Versions
---------------
fetch.html was run with Ruby 2.2.3 (x64) (Download from: http://rubyinstaller.org/downloads/). Other version above 2.2.0 should work as well. After installing Ruby, please type "gem install serve" in Command Prompt to install serve package (Full instructions: http://get-serve.com/get-started).

What You Need Before you Start
-------------------------------
You need to know the GroupID of the group you would like to collect data from (Get groupID using: https://lookup-id.com/), and modify "appId" field in line 15 and "groupID" field in line 61 in fetch.html.

You also need the permission from Facebook to run the app. To be continued in this section...

Setup and Go
-------------
1. Open Command Prompt from the foder where fetch.html and json2.js locate, and type "serve".
2. Open a browser, eg, Chrome, and make sure that your browser does not block popped out websites.
3. Type "localhost:4000" in the search area and press enter. You would see a list of files including fetch.html.
4. Click on fetch.html and the button "Read Data on console and download".

