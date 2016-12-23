$(document).ready(function () {

    var theme_btn = $("#highcontrast");
    var lang_select = $("#language-selector");


    /*CHECK COOKIE FOR THEME PREFERENCES*/
    if (getCookie('theme') == 'dark') {
        add_dark();
    } else if (getCookie('theme') == 'normal') {
        remove_dark();
    } else {
        add_dark();
    }

    /*BUTTON OUTLINE STYLE HANDLER*/
    $(function () {
        function outliner(job) {
            var btns = ['.btn-primary', '.btn-info', '.btn-danger', '.btn-warning', '.btn-secondary'];
            for (var i = 0; i < btns.length; i++) {
                var outline = btns[i] + '-outline';
                if (job == 'add') {
                    $(btns[i]).removeClass(btns[i].substr(1)).addClass(outline.substr(1));
                } else {
                    $(outline).removeClass(outline.substr(1)).addClass(btns[i].substr(1));
                }
            }
        }

        window.outliner = outliner;
    });


    /*BUTTON OUTLINE STYLE HANDLER*/
    function btn_outliner(job) {
        var btns = ['.btn-primary', '.btn-info', '.btn-danger', '.btn-warning', '.btn-secondary'];
        for (var i = 0; i < btns.length; i++) {
            var outline = btns[i] + '-outline';
            if (job == 'add') {
                $(btns[i]).removeClass(btns[i].substr(1)).addClass(outline.substr(1));
            } else {
                $(outline).removeClass(outline.substr(1)).addClass(btns[i].substr(1));
            }
        }
    }


    /*STOP DARK THEME*/
    function remove_dark() {
        $("#dark").remove();
        theme_btn.removeClass("dark");
        theme_btn.text(gettext('High Contrast View'));
        btn_outliner();
        setCookie('theme', 'normal', 5);

    }

    /*START DARK THEME*/
    function add_dark() {
        var dark_css = '<link id="dark" rel="stylesheet" type="text/css" href="/static/css/idego_dark.css"/>';
        var cssLink = $(dark_css);
        $("head").append(cssLink);
        theme_btn.addClass("dark");
        theme_btn.text(gettext('Standard View')).blur();
        btn_outliner('add');
        setCookie('theme', 'dark', 5);
    }

    /*HIGH CONTRAST THEME CHANGER*/
    theme_btn.click(function (e) {
        e.preventDefault();
        if (theme_btn.hasClass("dark"))
            remove_dark();
        else
            add_dark();
    });

    function setCookie(cname, cvalue, exdays) {
        var d = new Date();
        d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
        var expires = "expires=" + d.toUTCString();
        document.cookie = cname + "=" + cvalue + "; " + expires;
    }


    function getCookie(cname) {
        var name = cname + "=";
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) == ' ') c = c.substring(1);
            if (c.indexOf(name) == 0) return c.substring(name.length, c.length);
        }
        return "";
    }


    /*LANGUAGE CHANGE SUBMIT TRIGGER*/
    lang_select.change(function () {
        var dropdown_value = this.value;
        $("#lang-form").submit();
    });

});