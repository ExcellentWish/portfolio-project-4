$(document).ready(function () {
    console.log('Working')
    $("#id_requested_date").datepicker({
        dateFormat: 'dd/mm/yy'
    });

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

    // If there is a form error, shake the form 
    function formError() {
        if ($(".alert.alert-danger").length) {
            $("#full-form").addClass("animate__animated animate__shakeX");
        }
    }

    formError()

    // // Hide the email input on 'Update Details' page
    function disableEmail() {
        $("#customer-details-form>#div_id_email>.controls>.emailinput").attr("disabled", true);
    }
    disableEmail()
    // Remove disabled attribute so that the form can be submitted without throwing errors
    function removeDisableAttrOnSubmit() {
        $("#customer-details-form").one('submit', (function (e) {
            e.preventDefault();
            var $this = $(this);
            $("#customer-details-form>.full-form>#div_id_email>.emailinput").attr("disabled", false);
            $this.submit();
        }));
    }
    removeDisableAttrOnSubmit()

    // Opens the modal on delete_reservation
    function deleteModal() {
        $("#delete-reservation").on('click', function () {
            $('#confirmationModal').modal('show');
        });

        $(".close").on('click', function () {
            $('#confirmationModal').modal('hide');
        });
    }
    deleteModal()

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
    initMap()
});