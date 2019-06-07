import fastClick from 'fastclick';
import $ from 'jquery';

import skipLinks from './utils/skipLinks';
import iframer from './utils/iframer';
import mNav from './utils/mNav';
import initGmaps from './utils/gmaps';
import accordion from './utils/accordion';

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

    // gmaps
    initGmaps('#map', 'AIzaSyAZAIjZtkBlsF0ZqvrlkvyLfVn6Bju6bJ4');

    // Accordion
    accordion(
        '.accordion__list-item',
        'accordion__list-item--active',
        '.accordion__content',
        'accordion__content--active'
    );
}

$(function run () {
    console.log('ᕕ( ᐛ )ᕗ Running...');
    globals();
});