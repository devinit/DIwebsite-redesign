/* eslint no-new: 0 */
import gmaps from 'google-maps';
import $ from 'jquery';

export default function initGmaps (selector = '.media-map__location', APIKey = undefined) {
    const $el = $(selector);
    const el = $el[0];
    if (!el) return;

    if (APIKey) {
        gmaps.KEY = APIKey;
    }

    const [lat, lng] = $el.attr('data-latlng').split(',').map(val => parseFloat(val));
    const latlng = {lat, lng};

    console.log(latlng);

    gmaps.load(google => {
        const opts = {
            center: latlng,
            zoom: 2,
            zoomControl: true,
            zoomControlOptions: {
                style: google.maps.ZoomControlStyle.SMALL,
            },
            disableDoubleClickZoom: false,
            mapTypeControl: false,
            scaleControl: false,
            scrollwheel: false,
            panControl: true,
            streetViewControl: false,
            draggable: true,
            overviewMapControl: false,
            overviewMapControlOptions: {
                opened: false,
            },
            mapTypeId: google.maps.MapTypeId.ROADMAP,
            styles: [
                {
                    "featureType": "administrative.country",
                    "elementType": "geometry",
                    "stylers": [
                        {
                            "visibility": "simplified"
                        },
                        {
                            "hue": "#ff0000"
                        }
                    ]
                }
            ],
        };
        const locations = $('.media-map__location')
            .map(function() {
                const [lat, lng] = $(this).data('latlng').split(',').map(val => parseFloat(val));
                const latlng = {lat, lng};
                return {
                    title: $(this).data('title'),
                    desc: '',
                    tel: '',
                    email: '',
                    web: '',
                    position: latlng,
                    icon: '/assets/img/map-pin.png',
                };
            })
            .get();

        const map = new google.maps.Map(el, opts);

        locations.forEach(location => new google.maps.Marker({
            icon: location.icon,
            position: location.position,
            map: map,
            title: location.title,
            desc: location.desc,
            tel: location.tel,
            email: location.email,
            web: location.web,
        }));

    });

}
