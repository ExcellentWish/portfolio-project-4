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
