jQuery(document).ready(function ($) {


    "use strict";

    $('.nav-link').each(function () {
        let location = window.location.protocol + '//' + window.location.host + window.location.pathname;
        let link = this.href;
        if (location == link) {
            $(this).parent().addClass('active')
        }
    })

    // Login/Register form
// Author: Ian Pirro
//------------------------------------
// Form will change from login to register and visa-versa based
// on if the user is already "registered"
// "Usernames" min-len is 5 chars
//
// Could be annoying... but fun anyways


// These users "already exist"
    var users = [
        {name: 'ianpirro'},
        {name: 'joeschmoe'},
        {name: 'superdev'}
    ]

    var loginform = {

        init: function () {
            this.bindUserBox();
        },

        bindUserBox: function () {
            var result = {};

            $(".form").delegate("input[name='un']", 'blur', function () {
                var $self = $(this);

                // this grep would be replaced by $.post tp check db for user
                result = $.grep(users, function (elem, i) {
                    return (elem.name == $self.val());
                });

                // This would be callback
                if (result.length === 1) {
                    if ($("div.login-wrap").hasClass('register')) {
                        loginform.revertForm();
                        return;
                    } else {
                        return;
                    }
                }

                if (!$("div.login-wrap").hasClass('register')) {
                    if ($("input[name='un']").val().length > 4)
                        loginform.switchForm();
                }

            });
        },
        switchForm: function () {
            var $html = $("div.login-wrap").addClass('register');
            $html.children('h2').html('Register');
            $html.find(".form input[name='pw']").after("<input type='password' placeholder='Re-type password' name='rpw' />");
            $html.find('button').html('Sign up');
            $html.find('a p').html('Have an account? Sign in');
        },
        revertForm: function () {
            var $html = $("div.login-wrap").removeClass('register');
            $html.children('h2').html('Login');
            $html.find(".form input[name='rpw']").remove();
            $html.find('button').html('Sign in');
            $html.find('a p').html("Don't have an account? Register");
        },
        submitForm: function () {
            // ajax to handle register or login
        }

    } // loginform {}


// Init login form
    loginform.init();


// vertical align box
    (function (elem) {
        elem.css("margin-top", Math.floor(($(window).height() / 2) - (elem.height() / 2)));
    }($(".login-wrap")));

    $(window).resize(function () {
        $(".login-wrap").css("margin-top", Math.floor(($(window).height() / 2) - ($(".login-wrap").height() / 2)));

    });
    // Page loading animation

    $("#preloader").animate({
        'opacity': '0'
    }, 600, function () {
        setTimeout(function () {
            $("#preloader").css("visibility", "hidden").fadeOut();
        }, 300);
    });


    $(window).scroll(function () {
        var scroll = $(window).scrollTop();
        var box = $('.header-text').height();
        var header = $('header').height();

        if (scroll >= box - header) {
            $("header").addClass("background-header");
        } else {
            $("header").removeClass("background-header");
        }
    });

    if ($('.owl-clients').length) {
        $('.owl-clients').owlCarousel({
            loop: true,
            nav: false,
            dots: true,
            items: 1,
            margin: 30,
            autoplay: false,
            smartSpeed: 700,
            autoplayTimeout: 6000,
            responsive: {
                0: {
                    items: 1,
                    margin: 0
                },
                460: {
                    items: 1,
                    margin: 0
                },
                576: {
                    items: 3,
                    margin: 20
                },
                992: {
                    items: 5,
                    margin: 30
                }
            }
        });
    }

    if ($('.owl-banner').length) {
        $('.owl-banner').owlCarousel({
            loop: true,
            nav: true,
            dots: true,
            items: 3,
            margin: 10,
            autoplay: false,
            smartSpeed: 700,
            autoplayTimeout: 6000,
            responsive: {
                0: {
                    items: 1,
                    margin: 0
                },
                460: {
                    items: 1,
                    margin: 0
                },
                576: {
                    items: 1,
                    margin: 10
                },
                992: {
                    items: 3,
                    margin: 10
                }
            }
        });
    }

});
