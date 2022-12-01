var images = ['/static/image/wool.png','/static/image/yarn2-removebg-preview.png','/static/image/marnie-removebg-preview.png'];
var i=0;
function slideShow(){
    document.getElementById("main").src=images[i];

    if (i<images.length-1){
        i++;
    }
    else{
        i=0;
    }
    setTimeout("slideShow()",3000);
}
window.onload = slideShow;
