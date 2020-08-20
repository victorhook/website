$(document).ready(function() {

    const IMAGES = $(".image-tag");
    const LAST_IMAGE = IMAGES.length - 1;
    var currentImage = null;
    var currentImageIndex = 0;

    $(".image-tag").click(function() {
        currentImageIndex = findIndex(this);
        activateImage();
    });

    $("#next-image-left").click(function() {
        nextImageDecrease();
    });

    $("#next-image-right").click(function() {
        nextImageIncrease();
    });


    document.onkeydown = function(e) {
        if ($("#imageModal").is(":visible")) {
            if (e.code == "ArrowLeft") {
                nextImageDecrease();
            } else if (e.code == "ArrowRight") {
                nextImageIncrease();
            }
        }
    };


    function nextImageDecrease() {
        currentImageIndex = currentImageIndex > 1 ? currentImageIndex - 1 : LAST_IMAGE;
        activateImage();
    }

    function nextImageIncrease() {
        currentImageIndex = currentImageIndex < LAST_IMAGE ? currentImageIndex + 1 : 0;
        activateImage();
    }

    function findIndex(image) {
        for (var i = 0; i < IMAGES.length; i++) {
            if (IMAGES[i].id == image.id) {
                return i;
            }
        }
    }

    function activateImage() {
        currentImage = IMAGES[currentImageIndex];
        $("#modal-image").attr('src', currentImage.id);
        $("#image-title").html(currentImage.name);

        // If clicked image has meta data, we update
        // the modal-table.
        if ($(currentImage).data("meta_data")) {
            $("#meta-date").html($(currentImage).data("date"));
            $("#meta-aperture").html($(currentImage).data("aperture"));
            $("#meta-focal").html($(currentImage).data("focal"));
            $("#meta-model").html($(currentImage).data("model"));
            $("#meta-exposure").html($(currentImage).data("exposure"));
            $("#meta-iso").html($(currentImage).data("iso"));
            $("#meta-lens").html($(currentImage).data("lens"));
            $("#meta-data").show();

        } else {
            $("#meta-data").hide();
        }
    }

});
