var players = {};
var draw = function(result){
    var array = result;
    var canvas = $("#canvas")[0];
    var ctx = canvas.getContext("2d");
    ctx.fillStyle = "white";
    ctx.fillRect(0,0,canvas.width,canvas.height);
    ctx.fillStyle = "black";
    ctx.beginPath();
    ctx.moveTo(array[0].xPos,array[0].yPos);
    for(var i = 0;i<array.length;i++){
        ctx.lineTo(array[i].xPos,array[i].yPos);
    }
    ctx.stroke();
}
$(function(){
    $('canvas#canvas').mousedown(function(e) {return down(e,$(this))});
    $('canvas#canvas').mousemove(function(e) {return move(e,$(this))});
    $('canvas#canvas').mouseup(function(e) {return up(e)});
});