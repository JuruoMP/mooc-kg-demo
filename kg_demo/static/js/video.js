var video = document.getElementById('video');
//使用事件监听方式捕捉事件
video.addEventListener("timeupdate",function(){
    var timeDisplay;
    var lastHandle = 0;
	timeDisplay = Math.floor(video.currentTime);
	//console.log(Math.floor(video.currentTime))
	if(timeDisplay != lastHandle){
	    vm.activeGraph(timeDisplay);
	    lastHandle = timeDisplay;
	}
},false);