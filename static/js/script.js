$(document).ready(function() {
    console.log('Working')
    $("#id_requested_date").datepicker({ dateFormat: 'dd/mm/yy' });

    
    function screenSize() {
        if (window.innerWidth < 994) {
            $('#map').addClass('hidden');
        } else {
            $('#map').removeClass('hidden');
        }
    }

    function debounce(func, wait, immediate) {
        var timeout;
        return function () {
            var context = this,
                args = arguments;
            var later = function () {
                timeout = null;
                if (!immediate) func.apply(context, args);
            };
            var callNow = immediate && !timeout;
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
            if (callNow) func.apply(context, args);
        };
    }
    
    var screenChangeEfficient = debounce(function () {
        screenSize();
    }, 150);


    window.addEventListener('resize', screenChangeEfficient);
    
    screenSize();
});