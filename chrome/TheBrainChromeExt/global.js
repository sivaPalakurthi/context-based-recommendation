var url = "http://ec2-54-251-178-149.ap-southeast-1.compute.amazonaws.com/exp1/browserHistory";
var name = "";
chrome.history.onVisited.addListener(function (hi) {

if(name === "") 
{
name = prompt("Please Enter your name : ", "Name:");
}

var obj = {};
obj.name = name;
obj.url = hi.url;
obj.date = hi.lastVisitTime;
obj.browser='yes';
/*
console.log("Visited " + hi.url);
console.log("Count " + hi.visitCount);
console.log("LastVisit  " + hi.lastVisitTime);
console.log("typedCount  " + hi.typedCount);
console.log("typedCount  " + hi.id);
*/
var xhr = new XMLHttpRequest();
xhr.open("POST", url);
xhr.setRequestHeader('Content-Type', 'application/json');
xhr.onreadystatechange = function () {
    if (xhr.readyState == 4 && xhr.status == 200) {
		console.log('Success Response : ' + xhr.responseText);
    }
}
console.log('Sending Object : ' + JSON.stringify(obj));
xhr.send(JSON.stringify(obj));
})
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