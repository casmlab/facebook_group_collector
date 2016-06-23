
  // setup javascript sdk
  window.fbAsyncInit = function() {
    FB.init({
      appId      : 'your_app_id',
      xfbml      : true,
      version    : 'v2.6'
    });
//     FB.getLoginStatus(function(response) {
//   if (response.status === 'connected') {
//     console.log('Logged in.');
//   }
//   else {
//     FB.login();
//   }
// });
  };
  (function(d, s, id){
     var js, fjs = d.getElementsByTagName(s)[0];
     if (d.getElementById(id)) {return;}
     js = d.createElement(s); js.id = id;
     js.src = "//connect.facebook.net/en_US/sdk.js";
     fjs.parentNode.insertBefore(js, fjs);
   }(document, 'script', 'facebook-jssdk'));
  // end setup javascript sdk

  var pageCount = 1;
  var groupID;
  var json = [];

  function readData(link) {
  	// extract the name of the group
  	// var link = "https://www.facebook.com/groups/asianamericanchicagonetwork/";
    var link = document.getElementById("GET-link").value;

  	var regroup = /https:\/\/www.facebook.com\/groups\/(.*?)\/(.*?)/;
  	// var regroup = new RegExp("https:\/\/www.facebook.com\/groups\/(.*?)\/");
  	var repage = /https:\/\/www.facebook.com\/(.*?)\//;
  	var name;
  	var url;
  	// var type;

  	// if name is a group name, use this
  	// search?q=asianamericanchicagonetwork&type=group
  	// if name is a page name, use name
  	// to grab group id
  	if (link.match(regroup)) {
  		name = link.match(regroup)[1];
      url = "search?q=" + name + "&type=group";
        // type = "group";
  	} else if (link.match(repage)) {
  		name = link.match(repage)[1];
  		url = name;
  		// type = "page";
  	} else {
  		console.log("Wrong link");
      var pro = document.createElement('p');
      pro.textContent = "Wrong link";
      document.getElementById('content').appendChild(pro);
  		return;
  	}

    var pagename = document.createElement('p');
    pagename.textContent = "Page name: " + name;
    document.getElementById('content').appendChild(pagename);

	FB.getLoginStatus(function(response) {
		if (response.status === 'connected') {
		  // the user is logged in and has authemticated your app
		  console.log("connected");
		  // var uid = response.authResponse.userID;
		  var accessToken = response.authResponse.accessToken;
		  // console.log(url)
		  grabID(url, accessToken);

		  // getPosts(groupID, accessToken);
		  // nextPage();
		} else {
		    console.log("not logged in");
		    FB.login();
		    // the user isn't logged in to Facebook
		  };
	});
  }

  function grabID(url, accessToken) {
  	FB.api(
  		url,
  		{access_token : accessToken},
  		function (response) {
	        // console.log("get response");
	        // console.log(response);
	        
	        // transfer response object to string, and save as json txt file.
	        if (response && !response.error) {
	          // console.log(response);
	          var t = JSON.stringify(response);
	          // console.log(t);

	          if (response["data"]) {
	          	groupID = response["data"][0]["id"];
	          } else {
	          	groupID = response["id"];
	          }
	          
            var pageid = document.createElement('p');
            pageid.textContent = "Page id: " + groupID;
            document.getElementById('content').appendChild(pageid);
	          // console.log(groupID);
	          // saveFile(t);
	        } else {
	          console.log("some error when grab id!");
	        }
	        // console.log(groupID);
	        var url2 = groupID + "/feed?fields=caption,created_time,description,from,id,link,message,message_tags,name,story,type,updated_time,comments{comments{object,parent,message,from,id,created_time},from,id,message,created_time,object},likes{id,name}";
	        // console.log(url2);
          var pro = document.createElement('p');
          pro.id = "process"
          pro.textContent = "Grabbing data, please wait.";
          document.getElementById('content').appendChild(pro);

	        getPosts(url2, accessToken);

		}
	)
	// return groupID;
	// var url2 = groupID + "/feed?fields=caption,created_time,description,from,id,link,message,message_tags,name,story,type,updated_time,comments{comments{object,parent,message,from,id,created_time},from,id,message,created_time,object},likes{id,name}";
	// console.log(url2);

  }

  function getPosts(url2, accessToken) {
  	// console.log(groupID);
  	// var url2 = groupID + "/feed?fields=caption,created_time,description,from,id,link,message,message_tags,name,story,type,updated_time,comments{comments{object,parent,message,from,id,created_time},from,id,message,created_time,object},likes{id,name}";

  	// var pageCount = 0

  	FB.api(
  		url2,
  		{fields: 'posts'},
      	{access_token : accessToken},
      	function (response) {
        	// console.log("get response");
        	// console.log(url2);
        // console.log(response);
        
        // transfer response object to string, and save as json txt file.
        	if (response && !response.error) {
          // console.log(response);
          		// var t = JSON.stringify(response);
          		// console.log(t);
              // json.push(t);
              json.push(response);

        	} else {
          		console.log("some error when get posts!");
              var pro = document.getElementById('process');
              pro.textContent = "some error when get posts!";
              return;
        	}
        // set request interval to meet the limit of Facebook.
        	setTimeout(function() {
            // if next page exists, go to next page and grab the data
            	try {
              		console.log(pageCount);
              		nextPage = response["paging"]["next"];
              		console.log("nextPage exists! trying to grab next page");
              // var nextPage = response["paging"]["next"];
              		getPosts(nextPage, accessToken);
              
              		pageCount += 1;   

                  document.getElementById('process').textContent = "Grabbing page" + pageCount.toString();
            	}
            	catch(e) {
              		console.log("the end of pages!");
              		console.log(pageCount);

                  // saveFile(t);
                  // download json file use blob
                  var blob = new Blob([JSON.stringify(json)], {type: "application/json"});
                  var url3 = URL.createObjectURL(blob);

                  var a = document.createElement('a');
                  a.download = "raw_data_sample.json";
                  a.href = url3;
                  a.textContent = "Download raw_data_sample.json";
                  document.getElementById('content').appendChild(a);

                  var pro = document.getElementById('process');
                  pro.textContent = "Complete. Click the link to download."
            	};
        	}, 10000);
        
      	}
    );

  }
