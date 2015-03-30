var get = function() {
    $.ajax({
        url: pageURL + '/calc',
        type: 'GET',
        contentType: 'application/json',
        success: function(response) {
            drawings = JSON.parse(response.result);
            console.log(drawings);
            for(var i = 0;i<drawings.length;i++){
                console.log(drawings[i]);
            }
        }
    });
}
var makeObj = function(key1,val1,key2,val2) {
    return {key1: val1,key2: val2};
}
var posObj = function(pos){
    return {'xPos': pos.x,'yPos': pos.y};
}
var relPos = function(e,that) {
    var off = that.offset();
    return {'x': e.pageX-off.left, 'y': e.pageY-off.top}
}
var drawing = [];
var add = function(e,that) {
    drawing.push(posObj(relPos(e,that)));
    return false;
}
var isdown = false;
var move = function(e,that) {
    if(isdown){
        add(e,that);
    }
}
var down = function(e,that) {
    //draw()
    add(e,that);
    isdown = true;
}
var up = function(e) {
    isdown = false;
    if(drawing.length>0){
        send(drawing);
        drawing=[];
    }
}
var send = function(data){
    $.ajax({
        url: pageURL + '/add',
        data: JSON.stringify(data),
        type: 'POST',
        contentType: 'application/json',
        success: function(r,s,x) {console.log("Success. Server responded with " + x.status);}
    });
}