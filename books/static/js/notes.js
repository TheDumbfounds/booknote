function deleteNote(note, slug, id){
  $(note).parentsUntil('.note').parent().remove()
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
    error: function(err){}
  })
}

$modal = $('#noteModal')
$modal.modal()

function triggerModal(noteId=''){
  $.ajax({
    method: 'GET',
    url: '/books/modal/' + noteId,
    data: {
      'csrf_token': csrf_token, // pass it to the form as a hidden input
    },
    success: function(data){
      $modal.html(data)
      $modal.modal('open')
    },
    error: function(err){}
  })
}
