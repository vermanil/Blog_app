/**
 * Created by vermanil on 10/28/17.
 */

$(document).ready(function(){
	$("#get-data-form").submit(function(e) {

        var input = document.getElementById("image");
        var fReader = new FileReader();
        fReader.readAsDataURL(input.files[0]);
        fReader.onloadend = function (event) {
            var img = document.getElementById("image");
            img.src = event.target.result;
            console.log(event)
        var content = tinymce.get("texteditor").getContent();
        var title = $('#title').val();
        var author = $('#author').val();
        var image = $('#image').val();
        var date = $('#datetime').val();

        $("#data-container").html(content);
        var data = {
            "title": title,
            "author": author,
            "image": img.src,
            "date": date,
            "content": content,
            "csrfmiddlewaretoken": document.getElementsByName('csrfmiddlewaretoken')[0].value
        }

        console.log(data)
           $.post( "/saveArticle", data).done(function( status ) {
                   if(status == "0")
               {
                   alert(" Wrong Credentials entered")
               }
               else {
                   $(location).attr('href','blogs');
                   }

        });
        return false;
    }

});
    });
