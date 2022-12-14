window.onload = () => {
    // $('#type_course_update').click();
    $('.update_type_course_ajax').on('click', 'button[type="button"]', (e) => {
        let t_href = e.target.value;
        $.ajax({
            url: '/type-course-list/',
            type: 'POST',
            data: jQuery.param({id: t_href, method: 'detail'}),
            success: function (response) {
                console.log(response);
                $('.update_type').html(response)
                $('#type_course_update_id').trigger('click');

            },
           error: function(error){
				console.log(error);
			}
        });
        e.preventDefault();
    })

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

     $('.update_category_ajax').on('click', 'button[type="button"]', (e) => {
        let t_href = e.target.value;
        $.ajax({
            url: '/category-list/',
            type: 'POST',
            data: jQuery.param({id: t_href, method: 'detail'}),
            success: function (response) {
                console.log(response);
                $('.update_category').html(response)
                $('#category_update_id').trigger('click');

            },
           error: function(error){
				console.log(error);
			}
        });
        e.preventDefault();
    })

    $('.update_student_ajax').on('click', 'button[type="button"]', (e) => {
        let t_href = e.target.value;
        $.ajax({
            url: '/students-list/',
            type: 'POST',
            data: jQuery.param({id: t_href, method: 'detail'}),
            success: function (response) {
                console.log(response);
                $('.update_student').html(response)
                $('#student_update_id').trigger('click');

            },
           error: function(error){
				console.log(error);
			}
        });
        e.preventDefault();
    })

     $('.update_teacher_ajax').on('click', 'button[type="button"]', (e) => {
        let t_href = e.target.value;
        $.ajax({
            url: '/teachers-list/',
            type: 'POST',
            data: jQuery.param({id: t_href, method: 'detail'}),
            success: function (response) {
                console.log(response);
                $('.update_teacher').html(response)
                $('#teacher_update_id').trigger('click');

            },
           error: function(error){
				console.log(error);
			}
        });
        e.preventDefault();
    })

}


