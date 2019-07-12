

$(function () {

    $('.move_font').click(function () {
        $('.move_cont').show(1)
    });
    $('.pub_img1').click(function () {
        $("[type=file]").click()
    });
    $('.text_area').click(function () {
        $('.text_pub').show(1)
    });

    $('.comm').click(function () {
        $('.comm_form').show(1)
    });


});
// $(function () {
//     $('.comm_form').submit(function () {
//
//
//         $.ajax({
//             url: "../comment/{}",
//             type: 'POST',
//             data: $(this).serialize(),
//             cache: false,
//             success: function (data) {
//                 // alert(data)
//                 if (data['status']=='SUCCESS'){
//                     var comment_html = '<p>' + data['text'] + '</p>';
//                     $('#comment_list').prepend(comment_html)
//                 }
//             }
//         });
//         return false;
//     })
// });


