// Animate smooth scroll
/*global $ */

$('#view-work').on('click', function () {
    const images = $('#images').position().top;
    
    $('html, body').animate(
    {
        scrollTop: images
    },
    900
    );
});