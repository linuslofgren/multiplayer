var connect = function() {
    $('a#connect').bind("click", function() {
        $.getJSON(pageURL + '/calc', {
        }, function(data) {
            //$("#h").text(data.result);
            draw(data.result);
        });
        return false;
    });
}