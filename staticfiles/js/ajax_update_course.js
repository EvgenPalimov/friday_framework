window.onload = () => {
    // $('#course_update').click();
    $('.update_course_ajax').on('click', 'button[type="button"]', (e) => {
        let t_href = e.target.value;
        $.ajax({
            url: '/course-list/',
            type: 'POST',
            data: jQuery.param({id: t_href, method: 'detail'}),
            success: function (response) {
                console.log(response);
                $('.update_course').html(response)
                $('#course_update_id').trigger('click');

            },
           error: function(error){
				console.log(error);
			}
        });
        e.preventDefault();
    })

}


