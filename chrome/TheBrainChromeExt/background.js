//var url = "http://ec2-54-255-130-4.ap-southeast-1.compute.amazonaws.com/exp1/browserHistory";
var url = "http://localhost:8000/recommend";

var name = "";

function saveChanges(name, callback) {
	chrome.storage.sync.set({'name': name}, callback);
}
function prepData(name, tab, impBrowser){
	var obj = "?";
	obj += "user="+name+"&";
	obj += "url="+tab.url+"&";
	obj += "title="+tab.title+"&";
	obj += "timestamp="+tab.lastVisitTime;
	return obj;
}

function sendData(obj, callback){

	xhr = new XMLHttpRequest();
	xhr.open("GET", url+obj);
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.onreadystatechange = function () {
		if (xhr.readyState == 4 && xhr.status == 200) {
			console.log('Success Response : ' + xhr.responseText);
                        chrome.storage.sync.set({'response': xhr.responseText}, callback);
			//callback("success");
			
		} else {
			console.log('Response Failed');
			callback("failed");
		}
	}
	xhr.send(JSON.stringify(obj));
}

chrome.history.onVisited.addListener(function (tab) {
	chrome.storage.sync.get("name", function(obj){	
		if(obj.name === "" || obj.name === undefined) 
		{
			name = prompt("Please Enter your name : ", "");
			saveChanges(name, function(){
				data = prepData(name, tab, false);
				sendData(data,function(st){console.log("Send data response"+st)});
			})
		} else {
			data = prepData(obj.name, tab, false);
			sendData(data,function(st){console.log("Send data response"+st)});
		}
	});
	
		/*
		console.log("Visited " + hi.url);
		console.log("Count " + hi.visitCount);
		console.log("LastVisit  " + hi.lastVisitTime);
		console.log("typedCount  " + hi.typedCount);
		console.log("typedCount  " + hi.id);
		*/		
})
//chrome.browserAction.onClicked.addListener(function (tab) {
//	chrome.storage.sync.get("name", function(obj){	
//		if(obj.name === "" || obj.name === undefined) 
//		{
//			name = prompt("Please Enter your name : ", "");
//			saveChanges(name, function(){
//				data = prepData(name, tab, true);
//				sendData(data);
//			})
//		} else {
//			data = prepData(name, tab, true);
//			sendData(data, function(status){
//				if(status == "success")
//				{
//					chrome.browserAction.setBadgeText({text:"Imp",tabId:tab.id});
//				}
//				else
//				{
//					chrome.browserAction.setBadgeText({text:"Fail",tabId:tab.id});
//				}
//			});
//		}
//	});
//});

/*
chrome.tabs.onActivated.addListener(function (activeInfo) {
console.log("Activated : tab : " + activeInfo.tabId);
//console.log("Active @ ");
chrome.tabs.get(activeInfo.tabId, function (currTab) {

console.log("Active URL " + currTab.url);
});

});

chrome.tabs.onCreated.addListener(function (tab) {
//console.log('Created');
})
chrome.tabs.onUpdated.addListener(function (id, changeInfo, tab) {
//console.log('Updated ' + id + " : URL : " + tab.url);
})

chrome.tabs.query({'active': true}, function(tabs) {
  //console.log('Hi');
  //console.log(tabs.url);
  
  //chrome.tabs.update(tabs[0].id, {url: "http://googl.com"});
});
*/
