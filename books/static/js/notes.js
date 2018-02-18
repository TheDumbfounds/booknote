$('.modal').modal()
function deleteNote(slug, id){
  $.ajax({
    method: 'DELETE',
    url: slug,
    data: {
      'note_id': id,
    },
    beforeSend: function(xhr){
      xhr.setRequestHeader('X-CSRFToken', csrf_token)
    },
    success: function(){
      console.log("OKAY")
    },
    error: function(err){console.log(err)}
  })
}
