var removeBtn = document.getElementsByClassName("remove_button");
console.log (removeBtn);

for (var i =0; i<removeBtn.length; i++){
    var removeBtnAction = removeBtn[i];
    removeBtnAction.addEventListener("click",function(e){
        var btn = e.target;
        var h3 = btn.parentNode.remove();
        console.log("delete clicked");
    })
}
