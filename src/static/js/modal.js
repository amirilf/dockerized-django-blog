$('#exampleModal').on('show.bs.modal', function(event) {
    let title = $(event.relatedTarget).text()
    let body = $(event.relatedTarget).data('body')
    $(this).find('.modal-body').html(body)
    $(this).find('.modal-title').html(title)
})