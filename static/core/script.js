// AJAX enable for searching contacts
$(function () {
	$('#search').keyup(function () {
		$.ajax({
			method: 'POST',
			url: '/contacts/search/',
			data: {
				'search_text': $('#search').val(),
				'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
			},
			success: function (data) {
				$('#search-results').html(data);
			},
			dataType: 'html'
		});
	});
});


$(document).ready(function() {
	// if (('#search').value == '') {
	// 	$('#search-results').remove();
	// }
});





