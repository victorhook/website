$(document).ready(function() {

    const SKILL_BARS = $(".skillbar");
    let skillbar;

    for (var i = 0; i < SKILL_BARS.length; i++) {
        skillbar = $(SKILL_BARS[i]);
        skillbar.width(10 * skillbar.data("value") + "%");
    }

 });

