(function ($) {
    "use strict";

    const cart = []
    
    // Dropdown on mouse hover
    $(document).ready(function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 992) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        
        function readyApp(){
            const btn = document.querySelector('.auto-click');
            if(btn) {
                btn.click()
            }
        }

        function animateOffers(){
            const items = document.querySelectorAll('.offer-img')
            let count = 0;
            const len = items.length - 1;
            const interval = setInterval(function(){
                const item = $(items[count])
                if(!item.hasClass('close') && count <= len){
                    item.addClass('close');
                    item.width('0px')
                    item.height('0px')
                   
                    setTimeout(function(){
                        item.removeClass('close');
                        item.width('')
                        item.height('')
                        // console.log(len)
                        // console.log(count)
                        count++;
                        
                        if(count > len) count = 0
                
                    }, 1500)
                    
                }
                
            }, 5000)
        }
        
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);
        readyApp()
        animateOffers()
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Vendor carousel
    $('.vendor-carousel').owlCarousel({
        loop: true,
        margin: 29,
        nav: false,
        autoplay: true,
        smartSpeed: 1000,
        responsive: {
            0:{
                items:2
            },
            576:{
                items:3
            },
            768:{
                items:4
            },
            992:{
                items:5
            },
            1200:{
                items:6
            }
        }
    });


    // Related carousel
    $('.related-carousel').owlCarousel({
        loop: true,
        margin: 29,
        nav: false,
        autoplay: true,
        smartSpeed: 1000,
        responsive: {
            // 0:{
            //     items:1
            // },
            // 576:{
            //     items:2
            // },
            // 768:{
            //     items:3
            // },
            // 992:{
            //     items:4
            // }
            0:{
                items:2
            },
            576:{
                items:3
            },
            768:{
                items:4
            },
            992:{
                items:5
            },
            1200:{
                items:6
            }
        }
    });


    // Product Quantity
    // $('.quantity button').on('click', function () {
    //     var button = $(this);
    //     var oldValue = button.parent().parent().find('input').val();
    //     if (button.hasClass('btn-plus')) {
    //         var newVal = parseFloat(oldValue) + 1;
    //     } else {
    //         if (oldValue > 0) {
    //             var newVal = parseFloat(oldValue) - 1;
    //         } else {
    //             newVal = 0;
    //         }
    //     }
        
    //     // button.parent().find('input').val(newVal)
    //     button.parent().parent().find('input').val(newVal);
    // });

    $('.filter').on('click', function(){
        var filterbar = $('.filterbar')
        if(filterbar.hasClass('hide')) {
            filterbar.removeClass('hide')
        }
        else {
            filterbar.addClass('hide')
        }
    })

    $('.filter').on('click', function(e){
        $(e).preventDefault()

        cart.push({
            id:'ON:'+cart.length,
            name: '',
            price: '',
            cartgory: ''
        })
        
    })

    const header = document.querySelector('#header')
    const sticky = header.offsetTop
    const box = document.querySelector('#categories')
    // const sticky_box = box.offsetTop

    $(window).on('scroll', function(){
        function stickyHeader(){
            if(window.pageYOffset > sticky) {
                header.classList.add('sticky')
                if(box) box.classList.add('sticky-box')
            } else {
                header.classList.remove('sticky')
                if(box) box.classList.remove('sticky-box')
            }
         
            // if((window.pageYOffset + 100) > sticky_box) {
            //     alert('@@@@'+window.pageYOffset)
            //     box.classList.add('sticky-box')
            // } else {
            //     box.classList.remove('sticky-box')
            // }
        }

        stickyHeader()
    })

    const colorBox = document.querySelectorAll('.filter_box_color');
    const sizeBox = document.querySelectorAll('.filter_box_size');
    const colorForm = document.querySelectorAll('.color_form');
    const sizeForm = document.querySelectorAll('.size_form');

    for( var i=0; i < sizeForm.length; i++){ 
        sizeForm[i].addEventListener("submit",(event) => {
            event.preventDefault();
            // Perform validation and processing here
        });
    }
    for( var i=0; i < colorForm.length; i++){ 
        colorForm[i].addEventListener("submit",(event) => {
            event.preventDefault();
            // Perform validation and processing here
        });
    }
    for( var i=0; i < sizeBox.length; i++){ 
        sizeBox[i].addEventListener("change",filterProductBySize);
    }
    for( var i=0; i < colorBox.length; i++){ 
        colorBox[i].addEventListener("change",filterProductByColor);
    }

    function filterProductByColor(ev){
       for( var i=0; i < colorBox.length; i++){
            colorBox[i].checked=false;
       }
       
       this.checked=true;
       storeTriggerCheckbox(this.id);
       this.form.submit();
    }
    
    function filterProductBySize(){
       
       for( var i=0; i < sizeBox.length; i++){
        sizeBox[i].checked=false;
       }
       this.checked=true;
       storeTriggerCheckbox(this.id)
       this.form.submit();

    }

    function storeTriggerCheckbox(id) {
        // Store the checkbox state in localStorage
        localStorage.setItem('triggerCheckbox', id);
    }

    function findTriggerCheckbox() {
        // Check if a trigger checkbox was stored in localStorage
        var storedCheckbox = localStorage.getItem('triggerCheckbox');
        if (storedCheckbox) {
            console.log('Trigger checkbox: ' + storedCheckbox);
            try{
                document.querySelector('#'+storedCheckbox).checked=true;
                if(storedCheckbox.indexOf('color') > -1 ){
                    document.querySelector('#size-all').checked=true;
                }
                if(storedCheckbox.indexOf('size') > -1 ){
                    document.querySelector('#color-all').checked=true;
                }
            } catch (e) {}
            
            // You can perform additional actions based on the stored checkbox value

            // Clear the stored checkbox data
            localStorage.removeItem('triggerCheckbox');
        }
        else {
            try{
                document.querySelector('#color-all').checked=true;
                document.querySelector('#size-all').checked=true;
            } catch (e) {}
        }
    }

    //Check checkbox on shopping mall
    findTriggerCheckbox()

    var slider = $("#slider");
    var thumb = $("#thumb");
    var slidesPerPage = 4; //globaly define number of elements per page
    var syncedSecondary = true;
    slider.owlCarousel({
        items: 1,
        slideSpeed: 2000,
        nav: false,
        autoplay: false, 
        dots: false,
        loop: true,
        responsiveRefreshRate: 200
    }).on('changed.owl.carousel', syncPosition);
    thumb
        .on('initialized.owl.carousel', function() {
            thumb.find(".owl-item").eq(0).addClass("current");
        })
        .owlCarousel({
            items: slidesPerPage,
            dots: false,
            nav: true,
            item: 4,
            smartSpeed: 200,
            slideSpeed: 500,
            slideBy: slidesPerPage, 
            navText: ['<svg width="18px" height="18px" viewBox="0 0 20 20"><path style="fill:none;stroke-width: 1px;stroke: #000;" d="M9.554,1.001l-8.607,8.607l8.607,8.606"/></svg>', '<svg width="25px" height="25px" viewBox="0 0 11 20" version="1.1"><path style="fill:none;stroke-width: 1px;stroke: #000;" d="M1.054,18.214l8.606,-8.606l-8.606,-8.607"/></svg>'],
            responsiveRefreshRate: 100
        }).on('changed.owl.carousel', syncPosition2);
    function syncPosition(el) {
        var count = el.item.count - 1;
        var current = Math.round(el.item.index - (el.item.count / 2) - .5);
        if (current < 0) {
            current = count;
        }
        if (current > count) {
            current = 0;
        }
        thumb
            .find(".owl-item")
            .removeClass("current")
            .eq(current)
            .addClass("current");
        var onscreen = thumb.find('.owl-item.active').length - 1;
        var start = thumb.find('.owl-item.active').first().index();
        var end = thumb.find('.owl-item.active').last().index();
        if (current > end) {
            thumb.data('owl.carousel').to(current, 100, true);
        }
        if (current < start) {
            thumb.data('owl.carousel').to(current - onscreen, 100, true);
        }
    }
    function syncPosition2(el) {
        if (syncedSecondary) {
            var number = el.item.index;
            slider.data('owl.carousel').to(number, 100, true);
        }
    }
    thumb.on("click", ".owl-item", function(e) {
        e.preventDefault();
        var number = $(this).index();
        slider.data('owl.carousel').to(number, 300, true);
    });


    $(".qtyminus").on("click",function(){
        var now = $(".qty").val();
        if ($.isNumeric(now)){
            $("#form-qty-minus").submit()
        }
    })            
    $(".qtyplus").on("click",function(){
        var now = $(".qty").val();
        if ($.isNumeric(now)){ 
            $("#form-qty-plus").submit();
        }
    });

    $('#form-qty-plus').on('submit', function(event) {
        event.preventDefault(); 

        var formData = $(this).serialize();
        var action = $(this).attr('action');

        req('POST', action, formData, 'json',function(data){
            $(".qty").val(parseInt(data.quantity));
            $("#cart-qty").text(parseInt(data.len));
        });
    });

    $('#form-qty-minus').on('submit', function(event) {
        event.preventDefault(); 

        var formData = $(this).serialize();
        var action = $(this).attr('action');

        req('POST', action, formData, 'json',function(data){
            $(".qty").val(parseInt(data.quantity));
            $("#cart-qty").text(parseInt(data.len));
        });
    });
    
    $('#form-add-to-cart').on('submit', function(event) {
        event.preventDefault(); 

        var formData = $(this).serialize();
        var action = $(this).attr('action');

        req('POST', action, formData, 'json',function(data){
            $("#cart-qty").text(parseInt(data.len));
            $(".qty").val(parseInt(data.quantity));
            console.log($("#cart-qty"))
        });
    });

    $('#productf-color').on('submit', function(event) {
        event.preventDefault(); 

        var formData = $(this).serialize();
        var action = $(this).attr('action');

        req('POST', action, formData, 'json',function(data){
            
            // console.log()
        });
    });

    function req(type, url, data, dtype, _) {
        $.ajax({
            type: type,
            url, url,
            data: data,
            dataType: dtype,
            success: function(response) {
               console.log('Form submitted successfully:', response);
               _(response);
            },
            error: function(xhr, status, error) {
               console.error('Error submitting form:', error);
            }
          
        })
    }
    
})(jQuery);

