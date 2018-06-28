$('button').on('click', function(event){
    event.preventDefault();
    var element = $(this);

    $.ajax({
        url : '/add_to_fav/',
        type : 'POST',
        data : { music_id : $(this).attr("data-id")},

        success : function(response){
            if (response == 'False'){
                element.attr("class", "glyphicon glyphicon-star-empty");
            } else {
                element.attr("class", "glyphicon glyphicon-star");
            }
        }
    });
});

//$('.music-form').submit('click', function(event){
//    event.preventDefault();
//    console.log($(this).serialize())
//    var post_url = "/post_url/";
//    $.ajax({
//        type: "POST",
//        data: $(this).serialize(),
//        url: post_url,
//        success: function(data){
//            console.log(data)
//           console.log("success!")
//        },
//        error: function(data){
//            console.log("error")
//            console.log(data)
//        }
//    })
//});

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

