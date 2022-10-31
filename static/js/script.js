$(document).ready(function() {
    console.log('Working')
    $("#id_requested_date").datepicker({ dateFormat: 'dd/mm/yy' });

    function initMap() {
        // The location of Bottega Pia 41.7312638,12.6584794
        const bottega = {
            lat: 41.7312638,
            lng: 12.6584794
        };
        // The map, centered at Bottega Pia
        const map = new google.maps.Map(document.getElementById("map"), {
            zoom: 20,
            center: bottega,
        });
        // The marker, positioned at Bottega Pia
        const marker = new google.maps.Marker({
            position: bottega,
            map: map,
        });
    }

    window.initMap = initMap;
    
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