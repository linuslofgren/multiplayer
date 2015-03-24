var get_players = function() {
    $.getJSON(pageURL + '/calc', {
    }, function(data) {
        if(data.result != "None"){
            players = data.result;
        }
    });
    return false;
}
var add = function(e) {
    $.getJSON(pageURL + '/add' + '/' + e.pageX + '/' + e.pageY);
    return false;
}
var isdown = false;
var move = function(e) {
    if(isdown){
        add(e)
    }
}
var down = function(e) {
    isdown = true;
}
var up = function(e) {
    isdown = false;
}