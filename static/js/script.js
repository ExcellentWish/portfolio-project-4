$(document).ready(function() {
    console.log('Working')
    $("#id_requested_date").datepicker({ dateFormat: 'dd/mm/yy' });

    // Prevents dates in the past from being submitted on the reservation form

    function checkDate() {
        $("#reservation-enquiry").one('submit', (function (e) {
            e.preventDefault();
            var $this = $(this)
            var selectedDate = $('#id_requested_date').datepicker('getDate');
            console.log(selectedDate)
            if ((selectedDate.getTime() < Date.now())) {
                alert("Selected date is in the past, please choose a date in the future.");
            } else {
                console.log("Selected date is NOT in the past");
                $this.submit();
            }
        }))
    }
    checkDate()
    
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