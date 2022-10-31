
$(document).ready(function() {
    console.log('Working')
    $("#id_requested_date").datepicker({ dateFormat: 'dd/mm/yy' });

    function initMap() {
        // The location of Bottega Pia 41.7312638,12.6584794
        const uluru = {
            lat: 41.7312638,
            lng: 12.6584794
        };
        // The map, centered at Bottega Pia
        const map = new google.maps.Map(document.getElementById("map"), {
            zoom: 20,
            center: uluru,
        });
        // The marker, positioned at Uluru
        const marker = new google.maps.Marker({
            position: uluru,
            map: map,
        });
    }

    window.initMap = initMap;
});