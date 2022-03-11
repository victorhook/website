const SCROLL_NEAR = 400;

const sections = $('.image-content');
const images = $('.front-image-frame');
for (section of sections) {
    $(section).css('opacity', '1');
}
/*
document.addEventListener('scroll', e => {

    for (obj of $('.fadeIn')) {
        let top = $(obj).position().top;
        let middle = top + obj.clientHeight / 2;

        let middleScreen = window.pageYOffset + window.outerHeight/2-150;
        let dPos = Math.abs(middleScreen - middle);

        let perc = (dPos / middle) * 5;
        $(obj).css('opacity', 1-perc)
    }

    for (let i = 0; i < 3; i++) {
        let section = $(sections[i]);
        let image = $(images[i]);

        let top = section.position().top;
        let middle = top + sections[0].clientHeight / 2;

        let middleScreen = window.pageYOffset + window.outerHeight/2-150;
        let dPos = Math.abs(middleScreen - middle);

        let perc = (dPos / middle) * 3;
        let rotation = 20;

        section.css('opacity', 1-perc)
        perc *= perc;
        image.css({
            '-webkit-transform' : `rotate3d(0, 1, 5, ${perc*rotation}deg)`,
            '-moz-transform'    : `rotate3d(0, 1, 5, ${perc*rotation}deg)`,
            '-ms-transform'     : `rotate3d(0, 1, 5, ${perc*rotation}deg)`,
            '-o-transform'      : `rotate3d(0, 1, 5, ${perc*rotation}deg)`,
            'transform'         : `rotate3d(0, 1, 5, ${perc*rotation}deg)`
            });

    }
})
*/