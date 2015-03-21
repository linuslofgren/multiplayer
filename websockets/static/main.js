var get_players = function() {
    $.getJSON(pageURL + '/calc', {
    }, function(data) {
        if(data.result != "None"){
            players = data.result;
        }
    });
    return false;
}
var add = function() {
    $.getJSON(pageURL + '/add');
    return false;
}