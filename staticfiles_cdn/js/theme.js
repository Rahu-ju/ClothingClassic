


    $('#scrollTop').on('click', function () {
        $('html, body').animate({
            scrollTop: 0
        }, 1000);
    });

    // ------------------------------------------------------- //
    //    Colour form control 
    // ------------------------------------------------------ //

    $('.btn-colour').on('click', function (e) {
        var button = $(this);

        if (button.attr('data-allow-multiple') === undefined) {
            button.parents('.colours-wrapper').find('.btn-colour').removeClass('active');
        }

        button.toggleClass('active');
    });

    // ------------------------------------------------------- //
    //  Button-style form labels used in detail.html
    // ------------------------------------------------------ //

    $('.detail-option-btn-label').on('click', function () {
        var button = $(this);

        button.parents('.detail-option').find('.detail-option-btn-label').removeClass('active');

        button.toggleClass('active');
    });


    // ------------------------------------------------------- //
    //   Circle Slider
    // ------------------------------------------------------ //
    var circleSlider = $('.circle-slider');
    circleSlider.on({
        'initialized.owl.carousel': function () {
            // we add ..mh-full-screen to the parent section to avoid items below the carousel jumping before the carousel loads
            circleSlider.parents('section').removeClass('mh-full-screen');
        }
    }).owlCarousel({
        loop: true,
        margin: 0,
        smartSpeed: 500,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1,
                nav: false,
                dots: true
            },
            600: {
                items: 1,
                nav: false,
                dots: true
            },
            1120: {
                items: 1,
                dots: false,
                nav: true
            }
        },
        onRefresh: function () {
            circleSlider.find('.item').height('');
        },
        onRefreshed: function () {
            var maxHeight = 0;
            var items = circleSlider.find('.item');
            items.each(function () {
                var itemHeight = $(this).outerHeight();
                if (itemHeight > maxHeight) {
                    maxHeight = itemHeight;
                }
            });
            items.height(maxHeight);
        }
    });
    // ------------------------------------------------------- //
    //   Home Slider
    // ------------------------------------------------------ //
    var homeSlider = $('.home-slider');
    homeSlider.owlCarousel({
        loop: true,
        margin: 0,
        smartSpeed: 500,
        responsiveClass: true,
        
        responsive: {
            0: {
                items: 1,
                nav: false,
                dots: true
            },
            600: {
                items: 1,
                nav: false,
                dots: true
            },
            1120: {
                items: 1,
                dots: false,
                nav: true
            }
        },
        onRefresh: function () {
            homeSlider.find('.item').height('');
        },
        onRefreshed: function () {
            var maxHeight = 0;
            var items = homeSlider.find('.item');
            items.each(function () {
                var itemHeight = $(this).height();
                if (itemHeight > maxHeight) {
                    maxHeight = itemHeight;
                }
            });
            items.height(maxHeight);
        }
    });

    // ------------------------------------------------------- //
    //   Home Full Slider
    // ------------------------------------------------------ //

    var homeFullSlider = $('.home-full-slider');
    homeFullSlider.owlCarousel({
        // autoplay start the slider docu(https://owlcarousel2.github.io/OwlCarousel2/docs/api-options.html)
        autoplay: true,
        loop: true,
        margin: 0,
        smartSpeed: 500,
        responsiveClass: true,
        
        responsive: {
            0: {
                items: 1,
                nav: false,
                dots: true
            },
            600: {
                items: 1,
                nav: false,
                dots: true
            },
            1120: {
                items: 1,
                dots: false,
                nav: true
            }
        },
        onRefresh: function () {
            homeFullSlider.find('.item').height('');
        },
        onRefreshed: function () {
            var maxHeight = 0;
            var items = homeFullSlider.find('.item');
            items.each(function () {
                var itemHeight = $(this).height();
                if (itemHeight > maxHeight) {
                    maxHeight = itemHeight;
                }
            });
            items.height(maxHeight);
        }
    });


    // ------------------------------------------------------- //
    //   Product Slider
    // ------------------------------------------------------ //
    $('.product-slider').owlCarousel({
        loop: false,
        margin: 0,
        nav: false,
        dots: true,
        
        smartSpeed: 400,
        responsiveClass: true,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            1000: {
                items: 5
            }
        }
    });

    // ------------------------------------------------------- //
    // Detail Carousel with thumbs
    // ------------------------------------------------------ //
    $('.detail-slider').owlCarousel({
        loop: true,
        items: 1,
        thumbs: true,
        thumbsPrerendered: true,
        dots: false,
        responsiveClass: false
    });


    // ------------------------------------------------------- //
    // Detail Full Carousel
    // ------------------------------------------------------ //
    $('.detail-full').owlCarousel({
        loop: true,
        items: 1,
        dots: true,
        responsiveClass: false
    });

    // ------------------------------------------------------- //
    // Brands Slider
    // ------------------------------------------------------ -//

    var brandsSlider = $('.brands-slider');
    brandsSlider.owlCarousel({
        loop: true,
        margin: 20,
        dots: true,
        nav: false,
        smartSpeed: 400,
        responsiveClass: true,
        responsive: {
            0: {
                items: 2
            },
            600: {
                items: 3
            },
            1000: {
                items: 6,
                loop: false
            }
        },
        onRefresh: function () {
            brandsSlider.find('.item').height('');
        },
        onRefreshed: function () {
            var maxHeight = 0;
            var items = brandsSlider.find('.item');
            items.each(function () {
                var itemHeight = $(this).height();
                if (itemHeight > maxHeight) {
                    maxHeight = itemHeight;
                }
            });
            if (maxHeight > 0) {
                items.height(maxHeight);
            }
        }
    });

    // ------------------------------------------------------- //
    //   Smooth Scroll
    // ------------------------------------------------------- //

    var smoothScroll = new SmoothScroll('a[data-smooth-scroll]', {
        offset: 80
    });

    // ------------------------------------------------------- //
    //   Object Fit Images
    // ------------------------------------------------------- //    

    objectFitImages();


    