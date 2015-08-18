var jq = document.createElement('script');
jq.src = "http://code.jquery.com/jquery-2.1.3.min.js";
document.getElementsByTagName('head')[0].appendChild(jq);

var info = function(){
    $(".success").show("slow", function(){
        $(this).hide(2000)
    });
    
}

var times = function(){
    $.ajax({
        type: 'PUT',
        url: '/times',
        dataType: 'json',
        success: function(response){ info(); },
        error: function(req, err){ info(); }
    });
};
