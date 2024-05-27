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
                box.classList.add('sticky-box')
            } else {
                header.classList.remove('sticky')
                box.classList.remove('sticky-box')
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

    // Listen for changes in the checkbox
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
    
})(jQuery);

