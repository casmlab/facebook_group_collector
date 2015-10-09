from selenium import webdriver
from Tkinter import *
import os, tkMessageBox

class Application(Frame):

    def __init__(self,master):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
        self.warning='Finished \n'

    def createWidgets(self):

        self.label1=Label(self,text='Please input Facebook public group ID below')
        self.label1.pack()

        self.entry=Entry(self,width=50)
        self.entry.pack()
        self.menu=Menu(self,tearoff=0)
        self.menu.add_command(label='Cut',command=lambda: self.event_generate('<Control-x>'))
        self.menu.add_separator()
        self.menu.add_command(label='Copy',command=lambda: self.event_generate('<Control-c>'))
        self.menu.add_separator()
        self.menu.add_command(label='Paste',command=lambda: self.event_generate('<Control-v>'))
        def popup(event):
            self.menu.post(event.x_root,event.y_root)
        self.entry.bind("<Button-3>",popup)

        self.button=Button(self,text='Get Group Feed',command=self.fetch)
        self.button.pack()

    def startServe(self):
        os.system('serve')

    def fetch(self):
        gid = self.entry.get()

        f = open('fetchNow.html', 'w')

        message = """<!DOCTYPE html>
        <html>
        <head>
          <title>Fetch Group</title>
          <meta charset="utf-8">
          <meta keywords="facebook group collector">
          <script src="json2.js"></script>
        </head>
        <body>
          <p>Hello, world!</p>
          <script>
          // setup javascript sdk
          window.fbAsyncInit = function() {
            FB.init({
              appId      : '1065187026859191',
              xfbml      : true,
              version    : 'v2.4'
            });
          };
          (function(d, s, id){
             var js, fjs = d.getElementsByTagName(s)[0];
             if (d.getElementById(id)) {return;}
             js = d.createElement(s); js.id = id;
             js.src = "//connect.facebook.net/en_US/sdk.js";
             fjs.parentNode.insertBefore(js, fjs);
           }(document, 'script', 'facebook-jssdk'));
          // end setup javascript sdk
          </script>
          <script>
          </script>
          <script>
          var groupID = '""" + gid + """';
          var pageCount = 1;
          function readData() {
              FB.getLoginStatus(function(response) {
                if (response.status === 'connected') {
                  // the user is logged in and has authemticated your app
                  console.log("connected");
                  // var uid = response.authResponse.userID;
                  var accessToken = response.authResponse.accessToken;
                  var url = groupID + "/feed?fields=caption,created_time,description,from,id,link,message,message_tags,name,story,type,updated_time,comments{comments{object,parent,message},from,id,message,created_time,object},likes{id,name}";
                  grabData(url, accessToken);
                  // nextPage();
                } else {
                    console.log("not logged in");
                    FB.login();
                    // the user isn't logged in to Facebook
                  };
              });
          }
          function grabData(url, accessToken) {
            FB.api(
              url,
              {fields: 'posts'},
              {access_token : accessToken},
              function (response) {
                console.log("get response");
                // console.log(response);
                
                // transfer response object to string, and save as json txt file.
                if (response && !response.error) {
                  // console.log(response);
                  var t = JSON.stringify(response);
                  console.log(t);
                  saveFile(t);
                } else {
                  console.log("some error!");
                }
                // set request interval to meet the limit of Facebook.
                setTimeout(function() {
                    // if next page exists, go to next page and grab the data
                    try {
                      console.log(pageCount);
                      nextPage = response["paging"]["next"];
                      console.log("nextPage exists! try grab next page");
                      // var nextPage = response["paging"]["next"];
                      grabData(nextPage, accessToken);
                      
                      pageCount += 1;   
                    }
                    catch(e) {
                      console.log("till the end of pages!");
                      console.log(pageCount);
                    };
                }, 10000);
                
              }
            );
          }
          function saveFile(data) {
            var url = 'data:text/json;charset=utf8,' + encodeURIComponent(data);
            window.open(url, '_blank');
            window.focus();
          }  // var sur-fix = "?fields=";
          // var query = "posts{message,comments{message,comments}}";
          // var id =
          
          </script>
          <button onclick="readData()">Read Data on console and download</button>
        
        </body>
        <footer>
        </footer>
        </html>
        """
        f.write(message)
        f.close()

        driver = webdriver.Firefox()
        driver.get('http://localhost:4000/fetchNow.html')

window=Tk()
window.title('Facebook Public Group Feed Collector GUI')
window.geometry('500x150')
app=Application(window)
window.mainloop()
print app.warning
