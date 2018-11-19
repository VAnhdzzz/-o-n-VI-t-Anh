var songContainer = document.getElementById("song_container");
console.log(songContainer);

var song = songContainer.getElementsByClassName("song");
console.log(song);

for (var i=0;i<song.length;i++){
    var title = song[i].getElementsByClassName("title");
    var artist = song[i].getElementsByClassName("artist");
    console.log(i,title,artist);
}

var del = document.getElementsByClassName("del");

for (var i = 0;i <del.length;i++){
    var delAction =  del[i];
    delAction.addEventListener("click", function(e){
        var dl = e.target
        var i = dl.parentNode.remove();
        console.log("del clicked")
    })

    
}


var edit = document.getElementsByClassName("edit");
for (var i =0;i<edit.length;i++){
    var ea = edit[i];
    ea.addEventListener("click",function(e){
        var editAction = e.target;
        var div = editAction.parentNode;
        var u= div.getAttribute("song_id");
        console.log (u);
    }) 
}
var more = document.getElementsByClassName("more");

for (let i =0; i< more.length; i++){
    var moreAction = more[i];


    moreAction.addEventListener("click",function(e){
       var a = e.target;
        console.log(i,title,artist);
    })  
}



