/* ================================================
----------------- Simple Main.js ------------- */
(function ($) {
	"use strict";
	var Simple = {
		initialised: false,
		mobile: false,
		container : $('#portfolio-item-container'),
		blogContainer : $('#blog-item-container'),
		init: function () {

			if(!this.initialised) {
				this.initialised = true;
			} else {
				return;
			}

			// Call Simple Functions
			this.pageLoadAnim();
			this.checkMobile();
			this.menuHover();
			this.mobileMenuDropdownFix();
			this.menuOnClick();
			this.stickyHeader();
			this.overlayMenuToggle();
			this.overlayMenuDropdownFix();
			this.sideMenu();
			this.sideMenuToggle();
			this.productZoom();
			this.scrollToTop();
			this.twitterFeed();
			this.flickerFeed();
			this.instagramFeed();
			this.progressBars();
			this.scrollAnimations();
			this.tooltip();
			this.popover();

			/* Call function if Owl Carousel plugin is included */
			if ( $.fn.owlCarousel ) {
				this.owlCarousels();
			}

			// Call after carousel to make it work without a problem
			this.countTo();

			/* Call function if noUiSlider plugin is included */
			if (typeof noUiSlider === "object") {
				this.filterSliders();	
			}

			/* Call function if Light Gallery plugin is included */
			if ( $.fn.lightGallery) {
				this.lightBox();
			}

			/* Matchheight for products / shop - category pares*/
			if ( $.fn.matchHeight ) {
				this.matchProducts();
			}

			var self = this;
			/* Imagesloaded plugin included in isotope.pkgd.min.js */
			/* Portfolio isotope + Blog masonry with images loaded plugin */
			if ( typeof imagesLoaded === 'function' ) {
				self.container.imagesLoaded(function () {
					self.isotopeActivate();
					// recall for plugin support
					self.isotopeFilter();
				});

				self.blogContainer.imagesLoaded(function () {
					self.blogMasonry();
				});
			}

		},
		checkMobile: function () {
			/* Mobile Detect*/
			if ( /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test( navigator.userAgent ) ) {
				this.mobile = true;
			} else {
				this.mobile = false;
			}
		},
		pageLoadAnim: function() {
			// Page Loader Animation
			if ($('#page-loader').length) {
				$('#page-loader').delay(350).fadeOut(400, function () {
					$(this).remove();
				});
			}
		},
		menuHover: function () {
			if (typeof Modernizr === "object" && Modernizr.mq('only all and (min-width: 768px)') && !Modernizr.touchevents) {
				if ($.fn.hoverIntent) {
					$('.header').find('.navbar-nav').not('.nav-overlay').hoverIntent({
						over: function() {
							var  $this = $(this);
							
							$this.addClass('open');
							if($this.find('ul, div').length) {
								$this.find('.dropdown-toggle').addClass('disabled');
							}
						},
						out: function() {
							var  $this = $(this);

							$this.removeClass('open');
							if($this.hasClass('open')) {
								$this.find('.dropdown-toggle').removeClass('disabled');
							}
						},
						selector: 'li',
						timeout: 100,
						interval: 40
					});
				}
			}
		},
		mobileMenuDropdownFix : function () {
			if ( typeof Modernizr === "object" && (Modernizr.mq('only all and (max-width: 767px)') || Modernizr.touchevents) ) {
				$('.navbar-nav').not('.nav-overlay').find('.dropdown-toggle').on('click', function (e) {
					var parent = $(this).closest('li');
	                // close all the siblings and their children
	                parent.siblings().removeClass('open').find('li').removeClass('open');
	                // open which one is clicked
	                parent.toggleClass('open');

	                // prevent
	                e.preventDefault();
	                e.stopPropagation();
				});
			}
		},
		menuOnClick: function() {
			var self = this;
			// Menu on click scroll animation for onepages
			$('.onepage-nav').find('a').on('click', function (e) {
				var target = $(this).attr('href');
				if ( target.indexOf('#') === -1 || !$(target).length ) {
					return;
				}

				var elem = $(target),
					targetPos = elem.offset().top;

				$('html, body').animate({
		            'scrollTop': targetPos
		        }, 1200);
		        e.preventDefault();
			});
		},
		stickyHeader: function () {
			// Sticky header - calls if sticky-header class is added to the header
			if ( $('.sticky-header').length && $(window).width() >= 992 ) {
				var sticky = new Waypoint.Sticky({
					element: $('.sticky-header')[0],
					stuckClass: 'fixed',
					offset: -400
				});
			}
		},
		overlayMenuToggle: function () {
			// Overlay Menu Show/Hide via .nav-open class
			$('.menu-toggle').on('click', function (e) {
				$('.navbar-container').toggleClass('nav-open');
				e.preventDefault();
			});
		},
		overlayMenuDropdownFix: function() {
			// Overlay menu sub dropdown toggle fix
			$('.nav-overlay').find('.dropdown-toggle').on('click', function (e) {
				var parent = $(this).closest('li');
                // close all the siblings and their children
                parent.siblings().removeClass('open').find('li').removeClass('open');
                // open which one is clicked
                parent.toggleClass('open');

                // prevent
                e.preventDefault();
                e.stopPropagation();
			});
		},
		sideMenu: function () {
			if ($.fn.metisMenu) {
				$('.side-menu').metisMenu();
			}
		},
		sideMenuToggle: function () {
			// Overlay Menu Show/Hide via .nav-open class
			$('.sidemenu-toggle').on('click', function (e) {
				$('.header-inside').toggleClass('open');
				e.preventDefault();
			});
		},
		owlCarousels: function () {

			/* index2.html - Boxed news Carousel */
			$('.boxed-news-carousel.owl-carousel').owlCarousel({
	            loop:false,
				margin:25,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: true,
				autoplay: true,
				autoplayTimeout: 12000,
				responsive:{
					0: {
						items:1
					},
					768: {
						items:2
					},
					1200: {
						items:3
					}
				}
	        });

	        /* Index3 - Portfolio Carousel */
	        $('.portfolio-carousel.owl-carousel').owlCarousel({
	            loop:false,
				margin:20,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: true,
				autoplay: true,
				autoplayTimeout: 15000,
				responsive:{
					0: {
						items:1
					},
					420: {
						items:2
					},
					768: {
						items:3
					},
					992: {
						items:4
					}
				}
	        });

	        /* Index4 - Latest Posts Carousel */
	        $('.latest-posts-carousel-3col.owl-carousel').owlCarousel({
	            loop:false,
				margin:30,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: true,
				autoplay: true,
				autoplayTimeout: 15000,
				responsive:{
					0: {
						items:1
					},
					420: {
						items:2
					},
					768: {
						items:3
					}
				}
	        });

	        /* Index5 - Portfolio Carousel */
	        $('.portfolio-fullwidth-carousel.owl-carousel').owlCarousel({
	            loop:false,
				margin:0,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: false,
				autoplay: true,
				autoplayTimeout: 15000,
				responsive:{
					0: {
						items:1
					},
					420: {
						items:2
					},
					768: {
						items:3
					},
					992: {
						items:4
					},
					1280: {
						items:5
					},
					1600: {
						items:6
					},
					1920: {
						items:7
					}
				}
	        });

	        /* Index6 - Latest PostsCarousel */
	        $('.latest-posts-carousel.owl-carousel').owlCarousel({
	            loop:false,
				margin:30,
				responsiveClass:true,
				nav:true,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: false,
				autoplay: true,
				autoplayTimeout: 15000,
				responsive:{
					0: {
						items:1
					},
					420: {
						items:2
					},
					768: {
						items:3
					},
					992: {
						items:4
					}
				}
	        });

	        /* Index7 - Team Carousel */
	        $('.team-carousel-sm.owl-carousel').owlCarousel({
	            loop:false,
				margin:20,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: true,
				autoplay: true,
				autoplayTimeout: 15000,
				responsive:{
					0: {
						items:1
					},
					420: {
						items:2
					},
					768: {
						items:3
					},
					992: {
						items:3
					}
				}
	        });

	        /* Index7 - Latest Carousel */
	        $('.latest-news-carousel-sm.owl-carousel').owlCarousel({
	            loop:false,
				margin:20,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: true,
				autoplay: true,
				autoplayTimeout: 15000,
				responsive:{
					0: {
						items:1
					},
					420: {
						items:2
					},
					768: {
						items:3
					},
					992: {
						items:3
					}
				}
	        });

	        /* Index8 - Portfolio 2col Carousel */
	        $('.portfolio-2col-carousel.owl-carousel').owlCarousel({
	            loop:false,
				margin:0,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: false,
				autoplay: true,
				autoplayTimeout: 15000,
				responsive:{
					0: {
						items:1
					},
					420: {
						items:2
					},
					768: {
						items:3
					},
					992: {
						items:4
					},
					1600: {
						items:5
					},
					1900: {
						items:6
					}
				}
	        });

	        /* Index9 - Clients/Partners Carousel 3col */
	        $('.clients-carousel-3col.owl-carousel').owlCarousel({
	            loop:true,
				margin:10,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: true,
				autoplay: true,
				autoplayTimeout: 15000,
				responsive:{
					0: {
						items:1
					},
					280: {
						items:2
					},
					480: {
						items:3
					},
					768: {
						items:2
					},
					992: {
						items:3
					}
				}
	        });

	        /* Index9 - Latest news list carousel */
	        $('.latest-news-list-carousel.owl-carousel').owlCarousel({
	            loop:true,
				margin:30,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: true,
				autoplay: true,
				autoplayTimeout: 18000,
				responsive:{
					0: {
						items:1
					},
					992: {
						items:2
					}
				}
	        });

	        /* Index9 - Portfolio 2row carousel */
	        $('.portfolio-2row-carousel.owl-carousel').owlCarousel({
	            loop:false,
				margin:30,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: true,
				autoplay: true,
				autoplayTimeout: 15000,
				responsive:{
					0: {
						items:1
					},
					480: {
						items:2
					},
					768: {
						items:3
					},
					992: {
						items:4
					}
				}
	        });

	        /* Index-agency5 - Latest Post Carousel */
	        $('.latest-posts-carousel-4col.owl-carousel').owlCarousel({
	            loop:false,
				margin:30,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: true,
				autoplay: true,
				autoplayTimeout: 15000,
				responsive:{
					0: {
						items:1
					},
					480: {
						items:2
					},
					768: {
						items:3
					},
					992: {
						items:4
					}
				}
	        });

	        /* Index-creative3 - Latest Projects Carousel */
	        $('.vertical-portfolio-carousel.owl-carousel').owlCarousel({
	            loop:false,
				margin:0,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: false,
				autoplay: true,
				autoplayTimeout: 15000,
				responsive:{
					0: {
						items:1
					},
					480: {
						items:2
					},
					768: {
						items:3
					},
					992: {
						items:4
					},
					1440: {
						items:5
					},
					1800: {
						items:6
					}
				}
	        });

	        /* Index-creative3 - Our Team Carousel */
	        $('.vertical-team-carousel.owl-carousel').owlCarousel({
	            loop:false,
				margin:20,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: false,
				autoplay: true,
				autoplayTimeout: 15000,
				responsive:{
					0: {
						items:1
					},
					480: {
						items:2
					},
					768: {
						items:3
					},
					992: {
						items:4
					},
					1440: {
						items:5
					},
					1800: {
						items:6
					}
				}
	        });

	        /* Index-creative3 - Our Blog Carousel */
	        $('.vertical-posts-carousel.owl-carousel').owlCarousel({
	            loop:false,
				margin:20,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: false,
				autoplay: true,
				autoplayTimeout: 15000,
				responsive:{
					0: {
						items:1
					},
					480: {
						items:2
					},
					768: {
						items:3
					},
					992: {
						items:4
					},
					1440: {
						items:5
					},
					1800: {
						items:6
					}
				}
	        });

			/* index-Blog.html -  Featured Entry Carousel */
			$('.featured-entry-carousel.owl-carousel').owlCarousel({
	            loop:false,
				margin:0,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: true,
				autoplay: true,
				autoplayTimeout: 12000,
				responsive:{
					0: {
						items:1
					},
					480: {
						items:2
					},
					768: {
						items:3
					},
					1200: {
						items:4
					}
				}
	        });

	        /* Index-medical - Latest Post Medical Carousel */
	        $('.latest-posts-medical-carousel.owl-carousel').owlCarousel({
	            loop:false,
				margin:30,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: true,
				autoplay: true,
				autoplayTimeout: 15000,
				responsive:{
					0: {
						items:1
					},
					480: {
						items:2
					},
					768: {
						items:3
					},
					992: {
						items:4
					}
				}
	        });

	        /* Index-dentist - Testimonials Carousel */
			$('.testimonials-carousel-dots.owl-carousel').owlCarousel({
	            loop:true,
				margin:30,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: true,
				autoplay: true,
				autoplayTimeout: 15000,
				responsive:{
					0: {
						items:1
					},
					768: {
						items:2
					}
				}
	        });

	        /* Index-veterinary - Testimonials Carousel */
			$('.testimonials-slider-dots.owl-carousel').owlCarousel({
	            loop:true,
				margin:0,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: true,
				autoplay: true,
				autoplayTimeout: 15000,
				items:1
	        });

			/* index-shop.html -  Top Products Carousel */
			$('.top-products-carousel.owl-carousel').owlCarousel({
	            loop:false,
				margin:20,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: true,
				autoplay: true,
				autoplayTimeout: 12000,
				responsive:{
					0: {
						items:1
					},
					420: {
						items:2
					},
					768: {
						items:3
					},
					1200: {
						items:4
					}
				}
	        });
	        
			/* index-shop.html -  Banner Slider Widget */
			$('.owl-carousel.banner-widget-slider').owlCarousel({
	            loop:true,
	            items:1,
				margin:0,
				responsiveClass:true,
				nav:false,
				dots: true,
				autoplay: true,
				autoplayTimeout: 18000
	        });

	        /* index-shop.html -  Latest News Carousel */
			$('.latest-news-carousel.owl-carousel').owlCarousel({
	            loop:false,
				margin:20,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: true,
				autoplay: true,
				autoplayTimeout: 15000,
				responsive:{
					0: {
						items:1
					},
					420: {
						items:2
					},
					768: {
						items:3
					},
					1200: {
						items:4
					}
				}
	        });

	        /* index-shop2.html -  Top Products Carousel 5col */
			$('.top-products-carousel-5col.owl-carousel').owlCarousel({
	            loop:false,
				margin:20,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: true,
				autoplay: true,
				autoplayTimeout: 12000,
				responsive:{
					0: {
						items:1
					},
					420: {
						items:2
					},
					768: {
						items:3
					},
					992: {
						items: 4
					},
					1200: {
						items:5
					}
				}
	        });

	        /* index-shop2.html -  Latest News Carousel 5col */
			$('.latest-news-carousel-5col.owl-carousel').owlCarousel({
	            loop:false,
				margin:20,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: true,
				autoplay: true,
				autoplayTimeout: 15000,
				responsive:{
					0: {
						items:1
					},
					420: {
						items:2
					},
					768: {
						items:3
					},
					992: {
						items: 4
					},
					1200: {
						items:5
					}
				}
	        });

	        /* index-shop3.html -  Trending Products Carousel */
			$('.trending-products-carousel.owl-carousel').owlCarousel({
	            loop:false,
				margin:30,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: true,
				autoplay: true,
				autoplayTimeout: 15000,
				responsive:{
					0: {
						items:1
					},
					420: {
						items:2
					},
					768: {
						items:3
					},
					992: {
						items: 4
					}
				}
	        });

	        /* Index-gym2 - Latest Post 4col Carousel */
	        $('.latest-posts-4col-carousel.owl-carousel').owlCarousel({
	            loop:false,
				margin:30,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: true,
				autoplay: true,
				autoplayTimeout: 15000,
				responsive:{
					0: {
						items:1
					},
					480: {
						items:2
					},
					768: {
						items:3
					},
					992: {
						items:4
					}
				}
	        });

			/* Product.html -  Product carousel to zoom product section */
			$('.owl-carousel.product-gallery').owlCarousel({
	            loop:false,
				margin:3,
				responsiveClass:true,
				nav:false,
				dots: false,
				autoplay: true,
				autoplayTimeout: 10000,
				responsive:{
					0:{
						items:4
					},
					480: {
						items:6
					},
					768: {
						items:6
					},
					992: {
						items:5
					},
					1200: {
						items: 6
					}
				}
	        });

			/* Similiar Carousel - compare.html - product.html  */
			$('.similiar-products-carousel.owl-carousel').owlCarousel({
	            loop:false,
				margin:20,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: true,
				autoplay: true,
				autoplayTimeout: 18000,
				responsive:{
					0: {
						items:1
					},
					420: {
						items:2
					},
					768: {
						items:3
					},
					992: {
						items:4
					},
					1200: {
						items:5
					}
				}
	        });

			/* Testimonials Slider */
			$('.testimonials-slider.owl-carousel').owlCarousel({
				items: 1,
	            loop:true,
				margin:0,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: true,
				autoplay: true,
				autoplayTimeout: 15000
	        });

			/* Clients/Partners Carousel */
	        $('.clients-carousel.owl-carousel').owlCarousel({
	            loop:true,
				margin:20,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: true,
				autoplay: true,
				autoplayTimeout: 15000,
				responsive:{
					0: {
						items:2,
						margin: 10
					},
					420: {
						items:3,
						margin: 10
					},
					768: {
						items:4,
						margin:15
					},
					992: {
						items:5
					}
				}
	        });

	        /* Team Carousel */
	        $('.team-carousel.owl-carousel').owlCarousel({
	            loop:true,
				margin:20,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: true,
				autoplay: true,
				autoplayTimeout: 15000,
				responsive:{
					0: {
						items:1
					},
					420: {
						items:2
					},
					768: {
						items:3
					},
					992: {
						items:4
					}
				}
	        });

	        /* Testimonials Carousel */
			$('.testimonials-carousel.owl-carousel').owlCarousel({
	            loop:true,
				margin:30,
				responsiveClass:true,
				nav:true,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: false,
				autoplay: true,
				autoplayTimeout: 15000,
				responsive:{
					0: {
						items:1
					},
					768: {
						items:2
					}
				}
	        });

	        /* About Slider */
			$('.about-slider.owl-carousel').owlCarousel({
				items: 1,
	            loop:true,
				margin:0,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: true,
				autoplay: true,
				autoplayTimeout: 12000
	        });

	         /* Portfolio Post - Portfolio Slider */
			$('.portfolio-post-slider.owl-carousel').owlCarousel({
	            loop:true,
	            items:1,
				margin:0,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: true,
				autoplay: true,
				autoplayTimeout: 12000,
				animateOut: 'fadeOut'
	        });

	        /* Portfolio Post - Related carousel */
			$('.portfolio-related-carousel.owl-carousel').owlCarousel({
	            loop:false,
				margin:20,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: true,
				autoplay: true,
				autoplayTimeout: 18000,
				responsive:{
					0: {
						items:1
					},
					420: {
						items:2
					},
					768: {
						items:3
					},
					992: {
						items:4
					}
				}
	        });

	        /* Blog Post - Related carousel */
			$('.blog-related-carousel.owl-carousel').owlCarousel({
	            loop:false,
				margin:20,
				responsiveClass:true,
				nav:false,
				navText: ['<i class="fa fa-angle-left">', '<i class="fa fa-angle-right">'],
				dots: true,
				autoplay: true,
				autoplayTimeout: 18000,
				responsive:{
					0: {
						items:1
					},
					600: {
						items:2
					}
				}
	        });
		},
		tooltip: function () {
			// Bootstrap Tooltip
			if ( $.fn.tooltip ) {
				$('[data-toggle="tooltip"]').tooltip();
			}
		},
		popover: function () {
			// Bootstrap Popover
			if ( $.fn.popover ) {
				$('[data-toggle="popover"]').popover({
					trigger: 'focus'
				});
			}
		},
		scrollBtnAppear: function () {
	        if ( $(window).scrollTop() >= 400 ) {
	            $('#scroll-top').addClass('fixed');
	        } else {
	            $('#scroll-top').removeClass('fixed');
	        }
		},
		scrollToTop: function () {
			$('#scroll-top').on('click', function (e) {
		        $('html, body').animate({
			            'scrollTop': 0
		        }, 1200);
				e.preventDefault();
			});
		},
		lightBox: function () {
			/* Lightbox for portfolio items and videso and etc.. */
			$('.popup-gallery').lightGallery({
				selector: '.zoom-btn',
				thumbnail:true,
				exThumbImage: 'data-thumb',
				thumbWidth: 50,
				thumbContHeight: 60
			});

			// Lightbox for video with button - see: index-agency
			$('.video-btn-section').lightGallery({
				selector: '.trigger-video-btn',
				thumbnail:false
			});
		},
		productZoom: function () {
			var self = this;
			// Product page zoom plugin settings
			if ($.fn.elevateZoom) {
				$('#product-zoom').elevateZoom({
					responsive: true,
					zoomType: 'inner', // lens or window can be used - options already set below
					borderColour: '#e1e1e1',
					zoomWindowPosition: 1,
					zoomWindowOffetx: 30,
					cursor: "crosshair", //
					zoomWindowFadeIn: 400,
					zoomWindowFadeOut: 250,
					lensBorderSize: 3, // lens border size
					lensOpacity: 1,
					lensColour: 'rgba(255, 255, 255, 0.5)', // lens color
					lensShape : "square", // circle lens shape can be uses
					lensSize : 200,
					scrollZoom : true
				});

				/* swap images for zoom on click event */
				$('.product-gallery').find('a').on('click', function (e) {
					var ez = $('#product-zoom').data('elevateZoom'),
						smallImg = $(this).data('image'),
						bigImg = $(this).data('zoom-image');

						ez.swaptheimage(smallImg, bigImg);
					e.preventDefault();
				});
			}
		},
		progressBars: function () {
			var self = this;
			// Calculate and Animate Progress 
			$('.progress-animate').waypoint( function (direction) {
				var $this =  $(this.element),
					progressVal = $this.data('width');

				$this.css({ 'width' : progressVal + '%'}, 400);
			}, {
				offset: '90%',
				triggerOnce: true 
			});
		},
		countTo: function () {
			// CountTo plugin used count animations for homepages
			if ( $.fn.countTo ) {
				if ($.fn.waypoint) {
					$('.count').waypoint( function () {
						$(this.element).countTo();
					}, {
						offset: '90%',
						triggerOnce: true 
					});
				} else {
					$('.count').countTo();
				}	
			} else { 
				// fallback if count plugin doesn't included
				// Get the data-to value and add it to element
				$('.count').each(function () {
					var $this = $(this),
						countValue = $this.data('to');
						$this.text(countValue);
				});
			}
		},
		scrollAnimations: function () {
			/* Wowy Plugin */
			if ( typeof WOW === 'function' ) {
				new WOW({
					boxClass:     'wow',      // default
					animateClass: 'animated', // default
					offset:       0          // default
				}).init();
			}
		},
		twitterFeed: function () {
			/* Twitter feed for user*/
			if ( $.fn.tweet && $('.twitter-feed-widget').length ) {
			    $('.twitter-feed-widget').tweet({
			        modpath: './assets/js/twitter/',
			        avatar_size: '',
					count: 2,
					query: 'wrapbootstrap', // change query with username if you want to display search results
					loading_text:  'searching twitter...',
			        join_text: '',
			        retweets: false,
			        template: '<div class="twitter-icon"><i class="fa fa-twitter"></i></div><div class="tweet-content">{text}{time}</div>'
			        /* etc... */
			    });
			}
		},
		flickerFeed: function () {
			/* Flickr feed plugin  */
			// credits https://www.flickr.com/photos/smanography/
			if ( $.fn.jflickrfeed ) {
				$('.flickr-widget-list').jflickrfeed({
					limit: 12,
					qstrings: {
						id: '56502208@N00' // change with you flickr id
					},
					itemTemplate: '<li>' + '<a href="{{image}}" target="_blank" title="{{title}}">' + '<img src="{{image_s}}" alt="{{title}}" />' + '</a>' + '</li>'
				});
			}
		},
		instagramFeed: function () {
			// Instagram Feed
			if ( $.fn.spectragram && $('#instafeed').length) {

				jQuery.fn.spectragram.accessData = {
				    accessToken: '2229187323.566f1cf.c41eaca370664379b822dc3b17bb1464',
				    clientID: '7c28e44736494357ba3df343b1c699fe'
				};

				jQuery('#instafeed').spectragram('getUserFeed',{
				    query: 'eonythemes',
				    max: 13,
				    size: 'medium',
				    wrapEachWith: '',
				    complete: function() {

				    	$('#instafeed.owl-carousel').owlCarousel({
				            loop:true,
							margin:0,
							responsiveClass:true,
							nav:false,
							dots: false,
							autoplay: true,
							autoplayTimeout: 15000,
							smartSpeed:800,
							responsive:{
								0: {
									items:3
								},
								480: {
									items:4
								},
								768: {
									items:6
								},
								992: {
									items:7
								},
								1200: {
									items:9
								},
								1500: {
									items:10
								},
								1900: {
									items:12
								}
							}
				        });
				    }
				});
		    }
		},
		filterSliders:function () {
			// Slider For category pages / filter price
			var priceSlider  = document.getElementById('price-slider');

			// Check if #price-slider elem is exists if not return
			// to prevent error logs
			if (priceSlider == null) return;

			noUiSlider.create(priceSlider, {
				start: [ 100, 900 ],
				connect: true,
				step: 50,
				range: {
					'min': 0,
					'max': 1000
				}
			});

			this.sliderText(priceSlider, '$');
		},
		sliderText: function(slider, currency) {
			// add slider values as a text 
			// check for currency too
			var currencyVar = (currency) ? '$' : null,
				divHandles = slider.getElementsByClassName('noUi-handle'),
				divs = [];

			// Add divs to the slider handles.
			for ( var i = 0; i < divHandles.length; i++ ){
				divs[i] = document.createElement('div');
				divHandles[i].appendChild(divs[i]);
			}

			// When the slider changes, write the value to the tooltips.
			slider.noUiSlider.on('update', function( values, handle ){
				divs[handle].innerHTML = ( currencyVar) ? (currencyVar + values[handle]) : Math.round(values[handle]);
			});
		},
		isotopeActivate: function() {
			// Trigger for isotope plugin
			if ( $.fn.isotope ) {
				var container = this.container,
					layoutMode = container.data('layoutmode');

				container.isotope({
                	itemSelector: '.portfolio-item',
                	layoutMode: (layoutMode) ? layoutMode : 'masonry'
            	});
			}
		},
		isotopeReinit: function () {
			// Recall for isotope plugin
			if ( $.fn.isotope ) {
				this.container.isotope('destroy');
				this.isotopeActivate();
			}
		},
		isotopeFilter: function () {
			// Isotope plugin filter handle
			var self = this,
				filtersContainer = $('#portfolio-filter, #nav-portfolio-filter');

			filtersContainer.find('a').on('click', function(e) {
				var $this = $(this),
					selector = $this.attr('data-filter');

				filtersContainer.find('.active').removeClass('active');

				// And filter now
				self.container.isotope({
					filter: selector,
					transitionDuration: '0.8s'
				});
				
				$this.closest('li').addClass('active');
				e.preventDefault();
			});
		},
		blogMasonry: function() {
			// Trigger for isotope plugin
			if ( $.fn.isotope ) {
				var blogContainer = this.blogContainer;

				blogContainer.isotope({
                	itemSelector: '.entry-grid',
                	layoutMode: 'masonry'
            	});
			}
		},
		matchProducts: function () {
			// Match all products (Category - Shop Pages)
			$('.products-container').each(function() {
                $(this).find('.product').matchHeight();
            });
		}
	};

	// Ready Event
	jQuery(document).ready(function () {
		// Init our app
		Simple.init();
	});

	// Load Event
	$(window).on('load', function() {
		Simple.scrollBtnAppear();
	});

	// Scroll Event
	$(window).on('scroll', function () {
		Simple.scrollBtnAppear();
	});

// Adds active state to secion navigation
$('.nav li').click(function(e) {
  //e.preventDefault();
  $('.nav li').removeClass('active');
  $(this).addClass('active');
});

	// Google Map api v3 - Map for contact pages
    if ( document.getElementById("map") && typeof google === "object" ) {
    	// Map pin coordinates and content of pin box
        var locations = [
            [
            	'<address><strong>Address:</strong> Hollywood Blvd, Los Angeles, CA, USA <br> <strong>Phone:</strong> +01 010 554 11 22 </address>',
            	34.101780,
            	-118.333655
        	]
        ];

        var map = new google.maps.Map(document.getElementById('map'), {
            zoom: 14,
            center: new google.maps.LatLng(34.101780, -118.333655), // Map Center coordinates
            scrollwheel: false,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        });

        var infowindow = new google.maps.InfoWindow();


        var marker, i;

        for ( i = 0; i < locations.length; i++ ) {  
          marker = new google.maps.Marker({
            position: new google.maps.LatLng(locations[i][1], locations[i][2]),
            map: map,
            animation: google.maps.Animation.DROP,
            icon: 'assets/images/pin.png'
          });

          google.maps.event.addListener(marker, 'click', (function (marker, i) {
            return function() {
              infowindow.setContent(locations[i][0]);
              infowindow.open(map, marker);
            }
          })(marker, i));
        }
    }

})(jQuery);



