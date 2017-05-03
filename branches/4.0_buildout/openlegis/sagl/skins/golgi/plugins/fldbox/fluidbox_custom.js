/**
 * Gambit Torchbox Lightbox Javascript Library
 * Author Benjamin Intal - Gambit Technologies Inc
 * Version 1.1
 * License: Proprietary, Gambit Technologies Inc & Benjamin Intal
 */
(function () {

    this.GambitTorchbox = function (settings) {
        if (typeof settings === 'undefined') {
            settings = {};
        }
        var defaults = {
            'selector': '.gambit_torchbox',
            'highres_attribute': 'data-hires',
            'caption_attribute': 'title',
            'navigation': true,
            'key_navigation': true,
            'mobile_behavior': 'open', // 'none' or 'open',
            'mobile_width': 800
        };

        for (var key in defaults) {
            if (!settings.hasOwnProperty(key)) {
                settings[key] = defaults[key];
            }
        }

        this.settings = settings;
        this.start();
    };

    /**
     * Start our lightbox script
     */
    GambitTorchbox.prototype.start = function () {
        document.addEventListener('DOMContentLoaded', function () {

            // Listen for clicks and check if they match our lightbox selector
            document.querySelector('body').addEventListener('click', function (e) {

                var matches = document.querySelectorAll(this.settings.selector);
                var i, k;

                // Check if the anchor tag clicked has a torchbox child (happens when the image is small and the anchor is block)
                if (e.target.tagName === 'A' && e.target.children.length) {
                    for (k = 0; k < e.target.children.length; k++) {
                        for (i = 0; i < matches.length; i++) {
                            if (matches[i] === e.target.children[k]) {
                                this.open(matches[i]);
                                e.preventDefault();
                                return false;
                            }
                        }
                    }
                }

                // Check if the torchboxed image itself was clicked
                for (i = 0; i < matches.length; i++) {
                    if (matches[i] === e.target) {
                        this.open(e.target);
                        e.preventDefault();
                        return false;
                    }
                }

            }.bind(this));
        }.bind(this));

        // Listen for keypressess if enabled. Monitor keypress for left, right or ESC.
        if (this.settings.key_navigation) {
            document.addEventListener('keydown', function (event) {
                // If Torchbox is open
                if (document.querySelector('.gambit_torchbox_image')) {
                    if (event.keyCode === 39) {
                        this.next()
                    }
                    if (event.keyCode === 37) {
                        this.prev()
                    }
                    if (event.keyCode === 27) {
                        this.close()
                    }
                }
            }.bind(this));
        }

        // Makes sure our lightbox is always in the center of the screen
        window.addEventListener('resize', this.debounce(this.refreshPosition.bind(this), 250).bind(this));
    };




    // Returns a function, that, as long as it continues to be invoked, will not
    // be triggered. The function will be called after it stops being called for
    // N milliseconds. If `immediate` is passed, trigger the function on the
    // leading edge, instead of the trailing.
    // @see http://davidwalsh.name/javascript-debounce-function
    GambitTorchbox.prototype.debounce = function (func, wait, immediate) {
        var timeout;
        return function () {
            var context = this, args = arguments;
            var later = function () {
                timeout = null;
                if (!immediate) {
                    func.apply(context, args);
                }
            };
            var callNow = immediate && !timeout;
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
            if (callNow) {
                func.apply(context, args);
            }
        };
    };





    /**
     * Moves the lightbox back to the center of the screen
     */
    GambitTorchbox.prototype.refreshPosition = function () {
        if (document.querySelector('.gambit_torchbox_image') === null) {
            return;
        }

        var img = document.querySelector('.gambit_torchbox_image');
        var newImg = document.querySelector('.gambit_torchbox_image');
        img = img.parent;

        var newWidth, newHeight;
        if (img.offsetHeight / img.offsetWidth > window.innerHeight / window.innerWidth) {
            newHeight = Math.max(window.innerHeight - 100, window.innerHeight * 0.9);
            newWidth = img.offsetWidth / img.offsetHeight * newHeight;
        } else {
            newWidth = Math.max(window.innerWidth - 100, window.innerWidth * 0.9);
            newHeight = img.offsetHeight / img.offsetWidth * newWidth;
        }
        newImg.style.height = newHeight + 'px';
        newImg.style.width = newWidth + 'px';

        var x = window.innerWidth / 2 - newWidth / 2 + window.pageXOffset;
        var y = window.innerHeight / 2 - newHeight / 2 + window.pageYOffset;

        newImg.style.transition = 'all .4s';
        newImg.style.webkitTransform = 'translateX(' + x + 'px) translateY(' + y + 'px) scale(1)';
        newImg.style.transform = 'translateX(' + x + 'px) translateY(' + y + 'px) scale(1)';

        // Move the caption if there is one
        var newCaption = document.querySelector('.gambit_torchbox_caption');
        if (newCaption) {
            newCaption.style.width = newWidth + 'px';
            newCaption.style.webkitTransform = 'translateX(' + x + 'px) translateY(' + (y + newHeight + 1) + 'px) translateY(-100%)';
            newCaption.style.transform = 'translateX(' + x + 'px) translateY(' + (y + newHeight + 1) + 'px)  translateY(-100%)';
        }

        // Move the button prev button if there is one
        var button = document.querySelector('.gambit_torchbox_prev');
        if (button) {

            button.style.webkitTransform = 'translateX(' + (x + newWidth + 1) + 'px) translateY(' + (y - 1) + 'px)  translateX(-200%)';
            button.style.transform = 'translateX(' + (x + newWidth + 1) + 'px) translateY(' + (y - 1) + 'px)  translateX(-200%)';
        }

        // Move the button next button if there is one
        button = document.querySelector('.gambit_torchbox_next');
        if (button) {
            button.style.webkitTransform = 'translateX(' + (x + newWidth + 1) + 'px) translateY(' + (y - 1) + 'px)  translateX(-100%)';
            button.style.transform = 'translateX(' + (x + newWidth + 1) + 'px) translateY(' + (y - 1) + 'px)  translateX(-100%)';
        }
    };




    /**
     * Opens the lightbox for the element el
     * @param	img				DomElement	The element to create the lightbox for
     * @param	originateFrom	String		The location where to animate the lightbox from.
     *										Used mostly for switching between prev/next images
     */
    GambitTorchbox.prototype.open = function (img, originateFrom) {

        // Different behavior in mobile devices
        if (window.innerWidth <= this.settings.mobile_width) {
            if (this.settings.mobile_behavior === 'open') {

                // Only do this if we have a data-hires attribute
                var url = img.getAttribute(this.settings.highres_attribute);
                if (url && url.trim() !== '') {
                    window.open(url, '_self');
                }
            }
            return;
        }

        if (this.opening) {
            return;
        }
        this.opening = true;

        // Remember that we're opening to prevent successive calls
        setTimeout(function () {
            this.opening = null;
        }.bind(this), 500);

        if (typeof originateFrom === 'undefined') {
            originateFrom = 'image';
        }

        // Get the offset of the current image
        var rect = img.getBoundingClientRect(),
            newImg, position, transform;

        position = {
            top: rect.top + window.pageYOffset,
            left: rect.left + window.pageXOffset
        };

        // Create the lightbox image depending on the image element provided
        if (img.tagName === 'IMG') {
            newImg = document.createElement('IMG');
            newImg.setAttribute('src', img.getAttribute('src'));

        } else if (img.tagName === 'DIV') {
            newImg = document.createElement('DIV');

            newImg.style.background = img.style.background;
            newImg.style.backgroundImage = img.style.backgroundImage;
            newImg.style.backgroundSize = img.style.backgroundSize;
            newImg.style.backgroundPosition = img.style.backgroundPosition;
            newImg.style.backgroundColor = img.style.backgroundColor;
            newImg.style.backgroundRepeat = img.style.backgroundRepeat;
            newImg.style.backgroundOrigin = img.style.backgroundOrigin;
            newImg.style.backgroundClip = img.style.backgroundClip;

        }
        newImg.classList.add('gambit_torchbox_image');

        // Remember some parameters that we will need for the closing method
        newImg.openedFrom = originateFrom;
        newImg.parent = img;

        // Add the lightbox image
        document.querySelector('body').appendChild(newImg);

        // Calculate the final dimensions of the image to almost fit the screen
        var newWidth, newHeight;
        if (img.offsetHeight / img.offsetWidth > window.innerHeight / window.innerWidth) {
            newHeight = Math.max(window.innerHeight - 100, window.innerHeight * 0.9);
            newWidth = img.offsetWidth / img.offsetHeight * newHeight;
        } else {
            newWidth = Math.max(window.innerWidth - 100, window.innerWidth * 0.9);
            newHeight = img.offsetHeight / img.offsetWidth * newWidth;
        }
        newImg.style.height = newHeight + 'px';
        newImg.style.width = newWidth + 'px';

        position.left -= (newWidth - img.offsetWidth) / 2;
        position.top -= (newHeight - img.offsetHeight) / 2;
        var scale = img.offsetHeight / newHeight;

        newImg.style.transition = 'none';

        var x = window.innerWidth / 2 - newWidth / 2 + window.pageXOffset;
        var y = window.innerHeight / 2 - newHeight / 2 + window.pageYOffset;

        // Create the animation for the movement of the lightbox for it's final position
        if (originateFrom === 'left') {
            transform = 'translateX(' + x + 'px) translateY(' + y + 'px) translateX(-50%)';

            newImg.style.webkitTransform = transform;
            newImg.style.transform = transform;
            newImg.style.opacity = '0';

        } else if (originateFrom === 'right') {
            transform = 'translateX(' + x + 'px) translateY(' + y + 'px) translateX(50%)';

            newImg.style.webkitTransform = transform;
            newImg.style.transform = transform;
            newImg.style.opacity = '0';

        } else { // Originate from image
            transform = 'translateX(' + position.left + 'px)' +
                ' translateY(' + position.top + 'px)' +
                ' scale(' + scale + ')';

            newImg.style.webkitTransform = transform;
            newImg.style.transform = transform;
            newImg.style.opacity = img.style.opacity;
        }
        newImg.origTransform = 'translateX(' + position.left + 'px) translateY(' + position.top + 'px) scale(' + scale + ')';

        // Start animating, we need to delay this since we just added in the lightbox image
        setTimeout(function () {
            transform = 'scale(1) translateX(' + x + 'px) translateY(' + y + 'px)';

            newImg.style.transition = 'all .4s';
            newImg.style.opacity = '1';
            newImg.style.webkitTransform = transform;
            newImg.style.transform = transform;
        }, 100);


        // Start loading the hires image after all the animation ends
        this.loadHighResTimeout = setTimeout(function () {
            this.loadHiRes(newImg);
        }.bind(this), 551);

        // To create the illusion that we just enlarged the image, high the original image
        img.origOpacity = img.style.opacity;
        if (originateFrom === 'image') {
            img.style.opacity = 0;
        }

        // Create the background if it doesn't exist yet
        if (!document.querySelector('.gambit_torchbox_bg')) {
            var newBGDiv = document.createElement('DIV');
            newBGDiv.classList.add('gambit_torchbox_bg');
            document.querySelector('body').appendChild(newBGDiv);

            setTimeout(function () {
                newBGDiv.classList.add('open');
            }, 100);

            newBGDiv.addEventListener('click', this.close.bind(this));
        }
        newImg.addEventListener('click', this.close.bind(this));

        // Add the title/caption
        if (img.getAttribute(this.settings.caption_attribute) !== null &&
             img.getAttribute(this.settings.caption_attribute).trim() !== '') {
            var newCaption = document.createElement('DIV');
            newCaption.classList.add('gambit_torchbox_caption');
            newCaption.style.width = newWidth + 'px';

            transform = 'translateX(' + x + 'px) translateY(' + (y + newHeight + 1) + 'px) translateY(-100%)';
            newCaption.style.webkitTransform = transform;
            newCaption.style.transform = transform;
            newCaption.innerHTML = img.getAttribute(this.settings.caption_attribute);
            document.querySelector('body').appendChild(newCaption);

            setTimeout(function () {
                var newCaption = document.querySelector('.gambit_torchbox_caption');
                if (newCaption) {
                    newCaption.classList.add('open');
                }
            }, 100);
        }

        // Check and see if there's a next photo available
        var matches = document.querySelectorAll(this.settings.selector),
            hasNext = false,
            hasPrev = false;

        for (var i = 0; i < matches.length; i++) {
            if (matches[i] === img) {
                if (i > 0) {
                    hasPrev = true;
                    img.prevImg = matches[i - 1];
                }
                if (i < matches.length - 1) {
                    hasNext = true;
                    img.nextImg = matches[i + 1];
                }
                break;
            }
        }

        // Create the prev/next buttons
        if (this.settings.navigation) {

            if (hasPrev) {
                newImg.classList.add('hasprev');
                var prevDiv = document.createElement('DIV');
                prevDiv.classList.add('gambit_torchbox_prev');

                transform = 'translateX(' + (x + newWidth + 1) + 'px) translateY(' + (y - 1) + 'px)  translateX(-200%)';
                prevDiv.style.webkitTransform = transform;
                prevDiv.style.transform = transform;

                document.querySelector('body').appendChild(prevDiv);

                prevDiv.addEventListener('click', this.prev.bind(this));
            }

            if (hasNext) {
                newImg.classList.add('hasnext');
                var nextDiv = document.createElement('DIV');
                nextDiv.classList.add('gambit_torchbox_next');

                transform = 'translateX(' + (x + newWidth + 1) + 'px) translateY(' + (y - 1) + 'px) translateX(-100%)';
                nextDiv.style.webkitTransform = transform;
                nextDiv.style.transform = transform;

                document.querySelector('body').appendChild(nextDiv);

                nextDiv.addEventListener('click', this.next.bind(this));
            }

            setTimeout(function () {
                var button = document.querySelector('.gambit_torchbox_prev');
                if (button) {
                    button.classList.add('open');
                }
                button = document.querySelector('.gambit_torchbox_next');
                if (button) {
                    button.classList.add('open');
                }
            }, 100);
        }
    };



    /**
     * Closes the current lightbox
     * @param returnTo	String	The location to move the image when closing
     * @param removeBG	Boolean	If false, the black background will not be removed. 
     * 							Used for moving between next/prev images
     */
    GambitTorchbox.prototype.close = function (returnTo, removeBG) {
        if (!document.querySelector('.gambit_torchbox_image')) {
            return;
        }

        if (typeof returnTo !== 'string') {
            returnTo = 'origin';
        }
        if (typeof removeBG === 'undefined') {
            removeBG = true;
        }
        if (this.closing === true) {
            return;
        }
        this.closing = true;

        // Remove the caption
        var newCaption = document.querySelector('.gambit_torchbox_caption');
        if (newCaption) {
            newCaption.parentNode.removeChild(newCaption);
        }

        // Remove the prev button
        var button = document.querySelector('.gambit_torchbox_prev');
        if (button) {
            button.parentNode.removeChild(button);
        }

        // Remove the next button
        button = document.querySelector('.gambit_torchbox_next');
        if (button) {
            button.parentNode.removeChild(button);
        }

        // Stop the high res image from loading
        if (this.loadHighResTimeout) {
            clearTimeout(this.loadHighResTimeout);
        }

        // Remove the background
        var bg;
        if (removeBG) {
            bg = document.querySelector('.gambit_torchbox_bg');
            bg.classList.remove('open');
        }

        // Calculate the position to return to
        var img = document.querySelector('.gambit_torchbox_image');
        if (returnTo === 'origin') {
            if (img.openedFrom === 'left') {
                returnTo = 'right';
            } else if (img.openedFrom === 'right') {
                returnTo = 'left';
            }
        }

        // Move the image to its closing position
        if (returnTo === 'left') {
            img.style.webkitTransform = img.style.transform + ' translateX(-50%)';
            img.style.transform = img.style.transform + ' translateX(-50%)';
            img.style.opacity = 0;
            img.parent.style.transition = 'opacity .4s ease-in-out';
        } else if (returnTo === 'right') {
            img.style.webkitTransform = img.style.transform + ' translateX(50%)';
            img.style.transform = img.style.transform + ' translateX(50%)';
            img.style.opacity = 0;
            img.parent.style.transition = 'opacity .4s ease-in-out';
        } else {
            img.style.webkitTransform = img.origTransform;
            img.style.transform = img.origTransform;
            img.style.opacity = img.parent.origOpacity;
            img.parent.style.transition = 'none';
        }

        // Stop the high res image from loading
        this.stopHiRes();

        // Remove the animating elements when we're done
        setTimeout(function () {
            if (img && img.parent) {
                img.parent.style.opacity = img.parent.origOpacity;
            }
            if (bg) {
                bg.parentNode.removeChild(bg);
            }
            if (img) {
                img.parentNode.removeChild(img);
            }

            this.closing = false;
        }.bind(this), 500);

    };





    /**
     * Show the next image if there is one
     */
    GambitTorchbox.prototype.next = function () {
        if (this.opening || this.closing) {
            return;
        }
        var img = document.querySelector('.gambit_torchbox_image');
        if (!img || !img.parent || !img.parent.nextImg) {
            return;
        }

        this.close('left', false);
        this.open(img.parent.nextImg, 'right');
    };


    /**
     * Show the next image if there is one
     */
    GambitTorchbox.prototype.prev = function () {
        if (this.opening || this.closing) {
            return;
        }
        var img = document.querySelector('.gambit_torchbox_image');
        if (!img || !img.parent || !img.parent.prevImg) {
            return;
        }

        this.close('right', false);
        this.open(img.parent.prevImg, 'left');
    };



    /**
     * Stops the current high resolution image loading if any
     */
    GambitTorchbox.prototype.stopHiRes = function () {
        this.highResLoader = null;

        // Remove loading icon
        var el = document.querySelector('.gambit_torchbox_loading_icon');
        if (el) {
            el.parentNode.removeChild(el);
        }

        // Remove the flicker workaround
        if (this.cloned) {
            this.cloned.parentNode.removeChild(this.cloned);
            this.cloned = null;
        }
        el = document.querySelector('.gambit_torchbox_flicker_workaround');
        if (el) {
            el.parentNode.removeChild(el);
        }
    };


    /**
     * Starts the high resolution image loading for the lightboxed image
     */
    GambitTorchbox.prototype.loadHiRes = function (lightboxImage) {
        if (typeof lightboxImage === 'undefined') {
            lightboxImage = document.querySelector('.gambit_torchbox_image');
        }
        var parent = lightboxImage.parent;

        // Only do this if we have a data-hires attribute
        var url = parent.getAttribute(this.settings.highres_attribute);
        if (!url) {
            return;
        }

        // Create the loading icon
        var loadingIcon = document.createElement('DIV');
        loadingIcon.classList.add('gambit_torchbox_loading_icon');
        loadingIcon.classList.add('la-ball-clip-rotate');
        loadingIcon.classList.add('la-sm');
        loadingIcon.appendChild(document.createElement('DIV'));
        document.querySelector('body').appendChild(loadingIcon);

        // We need to delay this to show the loading icon animation
        setTimeout(function () {
            var loadingIcon = document.querySelector('.gambit_torchbox_loading_icon');
            if (loadingIcon) {
                loadingIcon.classList.add('open');
            }
        }, 100);

        // Create the preloader
        var img = new Image();
        img.lightboxImage = lightboxImage;
        img.onload = function () {

            // Get the loaded image
            var url = this.getAttribute('src');

            // Only do this if the lightbox for this image is still present
            if (!this.lightboxImage) {
                return;
            }
            var parent = this.lightboxImage.parent;
            if (!parent) {
                return;
            }
            var lightboxImage = this.lightboxImage;

            // The image flickers when we swap img src attributes
            // A workaround for this is to clone the existing image and make it persist
            // for a bit until the swap is complete, then remove the cloned image
            this.cloned = lightboxImage.cloneNode(true);
            this.cloned.classList.add('gambit_torchbox_flicker_workaround');
            document.querySelector('body').appendChild(this.cloned);

            // Swap the lowres image with the hires one
            if (parent.tagName === 'IMG') {
                lightboxImage.setAttribute('src', url);
            } else if (parent.tagName === 'DIV') {
                lightboxImage.style.backgroundImage = 'url(' + url + ')';
            }

            // Remove the workaround when we are done
            setTimeout(function () {
                if (this.cloned && this.cloned.parentNode) {
                    this.cloned.parentNode.removeChild(this.cloned);
                }
                this.cloned = null;
            }.bind(this), 500);

            // Remove the loading icon since we are done
            var loadingIcon = document.querySelector('.gambit_torchbox_loading_icon');
            if (loadingIcon) {
                loadingIcon.parentNode.removeChild(loadingIcon);
            }

            // Free up memory
            this.highResLoaderer = null;
        };

        // Start loading
        img.setAttribute('src', url);
        this.highResLoaderer = img;

        // Free memory
        img = null;
    };

}());