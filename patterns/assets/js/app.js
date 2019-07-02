import fastClick from 'fastclick';
import $ from 'jquery';

import childTabIndex from './utils/childTabIndex';
import skipLinks from './utils/skipLinks';
import iframer from './utils/iframer';
import mNav from './utils/mNav';
import initGmaps from './utils/gmaps';
import accordion from './utils/accordion';
import initSVGmap from './utils/svgmap';
import setupSharing from './utils/social';
import sectionSharing from './utils/sectionSharing';
import copyText from './utils/copyText';
import chapterNav from './utils/chapterNav';

function globals () {

    // FastClick
    fastClick(document.body);

    // iframe video in body content
    iframer();

    // Small Screen Navigation
    mNav(
        '#navigation-primary-toggle',
        'navigation-primary-toggle--active',
        '#navigation-primary',
        'navigation-primary--active'
    );

    // Set child tab index for nav
    childTabIndex(
        '#navigation-primary-toggle',
        '#navigation-primary',
        'navigation-primary--active',
        960
    );

    // Chapter nav
    chapterNav();

    // gmaps
    initGmaps('#map', 'AIzaSyAZAIjZtkBlsF0ZqvrlkvyLfVn6Bju6bJ4');

    // Accordion
    accordion(
        '.accordion__list-item',
        'accordion__list-item--active',
        '.accordion__content',
        'accordion__content--active'
    );

    // social
    setupSharing();
    copyText(
        '.js-copy-field',
        '.js-copy-trigger'
    );
    sectionSharing();
}

$(function run () {
    console.log('ᕕ( ᐛ )ᕗ Running...');
    globals();
});
