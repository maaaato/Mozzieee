var jq = document.createElement('script');
jq.src = "http://code.jquery.com/jquery-2.1.3.min.js";
document.getElementsByTagName('head')[0].appendChild(jq);

var times = function(){
    $.ajax({
        type: 'PUT',
        url: '/times',
        dataType: 'json',
           success: function(response){ console.log(response); },
           error: function(req, err){ console.log(err); }
    });
};
