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

        // An array with the coordinates of the boundaries of Bucaramanga, extracted manually from the GADM database
        var BucaramangaDelimiters = [
            { lng: -73.077796936035,  lat: 7.18019914627087 },
            { lng: -73.0765991210938, lat: 7.17500114440924 },
            { lng: -73.0805969238281, lat: 7.16109991073608 },
            { lng: -73.081199645996,  lat: 7.14789915084839 },
            { lng: -73.0748977661132, lat: 7.13860082626343 },
            { lng: -73.0655975341797, lat: 7.13280010223394 },
            { lng: -73.0626983642578, lat: 7.12929916381836 },
            { lng: -73.0673980712889, lat: 7.1263999938966  },
            { lng: -73.0759963989258, lat: 7.10970115661621 },
            { lng: -73.084098815918,  lat: 7.10449981689459 },
            { lng: -73.0943984985352, lat: 7.09769916534424 },
            { lng: -73.1088027954102, lat: 7.08269977569586 },
            { lng: -73.1156997680664, lat: 7.07289981842052 },
            { lng: -73.1231994628906, lat: 7.07060003280645 },
            { lng: -73.1300964355469, lat: 7.05680179595953 },
            { lng: -73.1393966674804, lat: 7.05340003967291 },
            { lng: -73.1473999023437, lat: 7.05050086975098 },
            { lng: -73.152099609375,  lat: 7.05919981002808 },
            { lng: -73.1601028442383, lat: 7.06330013275158 },
            { lng: -73.1688003540039, lat: 7.06389999389648 },
            { lng: -73.1802978515624, lat: 7.06629991531383 },
            { lng: -73.1843032836913, lat: 7.07320117950451 },
            { lng: -73.1860961914062, lat: 7.08760023117071 },
            { lng: -73.1884002685546, lat: 7.1096010208131  },
            { lng: -73.1815032958984, lat: 7.12750101089489 },
            { lng: -73.1780014038085, lat: 7.15230083465588 },
            { lng: -73.1781005859374, lat: 7.17660093307501 },
            { lng: -73.1763000488281, lat: 7.18930006027233 },
            { lng: -73.1770782470703, lat: 7.19456291198725 },
            { lng: -73.1682968139647, lat: 7.19389915466314 },
            { lng: -73.1636962890624, lat: 7.1995987892152  },
            { lng: -73.1591033935547, lat: 7.20250082016003 },
            { lng: -73.1452026367187, lat: 7.211100101471   },
            { lng: -73.1360015869141, lat: 7.21739912033081 },
            { lng: -73.1261978149414, lat: 7.22079992294312 },
            { lng: -73.1199035644531, lat: 7.22370100021362 },
            { lng: -73.1118011474609, lat: 7.2241997718811  },
            { lng: -73.1078033447265, lat: 7.22540187835699 },
            { lng: -73.1054992675781, lat: 7.22540187835699 },
            { lng: -73.1054992675781, lat: 7.22129917144787 },
            { lng: -73.1048965454102, lat: 7.21269989013683 },
            { lng: -73.1048965454102, lat: 7.20340108871466 },
            { lng: -73.1031036376953, lat: 7.19760084152222 },
            { lng: -73.0973968505859, lat: 7.1911988258363  },
            { lng: -73.0915985107421, lat: 7.18540000915522 },
            { lng: -73.0864028930664, lat: 7.18370008468634 },
            { lng: -73.077796936035,  lat: 7.18019914627087 }
        ];

        // Construct the polygon.
        var BucaramangaPolygon = new google.maps.Polygon({
            paths: BucaramangaDelimiters,
            strokeColor: '#FF0000',
            strokeOpacity: 0.8,
            strokeWeight: 3,
            fillColor: '#FF0000',
            fillOpacity: 0.35
        });

    });

}
