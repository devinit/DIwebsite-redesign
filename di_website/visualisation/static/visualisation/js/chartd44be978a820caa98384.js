(window.webpackJsonp=window.webpackJsonp||[]).push([[72,70,71,73,150],{1064:function(e,r,t){"use strict";var a=t(15).traceIs,i=t(237);function n(e){return{v:"x",h:"y"}[e.orientation||"v"]}function o(e,r){var t=n(e),i=a(e,"box-violin"),o=a(e._fullInput||{},"candlestick");return i&&!o&&r===t&&void 0===e[t]&&void 0===e[t+"0"]}e.exports=function(e,r,t,l){"-"===t("type",(l.splomStash||{}).type)&&(!function(e,r){if("-"!==e.type)return;var t,l=e._id,s=l.charAt(0);-1!==l.indexOf("scene")&&(l=s);var d=function(e,r,t){for(var a=0;a<e.length;a++){var i=e[a];if("splom"===i.type&&i._length>0&&(i["_"+t+"axes"]||{})[r])return i;if((i[t+"axis"]||t)===r){if(o(i,t))return i;if((i[t]||[]).length||i[t+"0"])return i}}}(r,l,s);if(!d)return;if("histogram"===d.type&&s==={v:"y",h:"x"}[d.orientation||"v"])return void(e.type="linear");var c=s+"calendar",f=d[c],u={noMultiCategory:!a(d,"cartesian")||a(d,"noMultiCategory")};"box"===d.type&&d._hasPreCompStats&&s==={h:"x",v:"y"}[d.orientation||"v"]&&(u.noMultiCategory=!0);if(o(d,s)){var v=n(d),g=[];for(t=0;t<r.length;t++){var h=r[t];a(h,"box-violin")&&(h[s+"axis"]||s)===l&&(void 0!==h[v]?g.push(h[v][0]):void 0!==h.name?g.push(h.name):g.push("text"),h[c]!==f&&(f=void 0))}e.type=i(g,f,u)}else if("splom"===d.type){var y=d.dimensions[d._axesDim[l]];y.visible&&(e.type=i(y.values,f,u))}else e.type=i(d[s]||[d[s+"0"]],f,u)}(r,l.data),"-"===r.type?r.type="linear":e.type=r.type)}},758:function(e,r,t){"use strict";var a=t(12),i=t(15),n=t(3),o=t(220),l=t(62),s=t(230),d=t(236),c=t(231),f=t(774),u=t(759),v=t(228),g=t(60).WEEKDAY_PATTERN,h=t(60).HOUR_PATTERN;function y(e,r,t){function i(t,a){return n.coerce(e,r,l.rangebreaks,t,a)}if(i("enabled")){var o=i("bounds");if(o&&o.length>=2){var s,d,c="";if(2===o.length)for(s=0;s<2;s++)if(d=b(o[s])){c=g;break}var f=i("pattern",c);if(f===g)for(s=0;s<2;s++)(d=b(o[s]))&&(r.bounds[s]=o[s]=d-1);if(f)for(s=0;s<2;s++)switch(d=o[s],f){case g:if(!a(d))return void(r.enabled=!1);if((d=+d)!==Math.floor(d)||d<0||d>=7)return void(r.enabled=!1);r.bounds[s]=o[s]=d;break;case h:if(!a(d))return void(r.enabled=!1);if((d=+d)<0||d>24)return void(r.enabled=!1);r.bounds[s]=o[s]=d}if(!1===t.autorange){var u=t.range;if(u[0]<u[1]){if(o[0]<u[0]&&o[1]>u[1])return void(r.enabled=!1)}else if(o[0]>u[0]&&o[1]<u[1])return void(r.enabled=!1)}}else{var v=i("values");if(!v||!v.length)return void(r.enabled=!1);i("dvalue")}}}e.exports=function(e,r,t,a,h){var p=a.letter,b=a.font||{},w=a.splomStash||{},m=t("visible",!a.visibleDflt),x=r._template||{},k=r.type||x.type||"-";"date"===k&&i.getComponentMethod("calendars","handleDefaults")(e,r,"calendar",a.calendar);v(r,h);var _=!r.isValidRange(e.range);_&&a.reverseDflt&&(_="reversed"),!t("autorange",_)||"linear"!==k&&"-"!==k||t("rangemode"),t("range"),r.cleanRange(),f(e,r,t,a),"category"===k||a.noHover||t("hoverformat");var C=t("color"),A=C!==l.color.dflt?C:b.color,D=w.label||h._dfltTitle[p];if(c(e,r,t,k,a,{pass:1}),!m)return r;t("title.text",D),n.coerceFont(t,"title.font",{family:b.family,size:Math.round(1.2*b.size),color:A}),s(e,r,t,k),c(e,r,t,k,a,{pass:2}),d(e,r,t,a),u(e,r,t,{dfltColor:C,bgColor:a.bgColor,showGrid:a.showGrid,attributes:l}),(r.showline||r.ticks)&&t("mirror"),a.automargin&&t("automargin");var z,M="multicategory"===k;a.noTickson||"category"!==k&&!M||!r.ticks&&!r.showgrid||(M&&(z="boundaries"),t("tickson",z));M&&(t("showdividers")&&(t("dividercolor"),t("dividerwidth")));if("date"===k)if(o(e,r,{name:"rangebreaks",inclusionAttr:"enabled",handleItemDefaults:y}),r.rangebreaks.length){for(var R=0;R<r.rangebreaks.length;R++)if(r.rangebreaks[R].pattern===g){r._hasDayOfWeekBreaks=!0;break}if(v(r,h),h._has("scattergl")||h._has("splom"))for(var T=0;T<a.data.length;T++){var S=a.data[T];"scattergl"!==S.type&&"splom"!==S.type||(S.visible=!1,n.warn(S.type+" traces do not work on axes with rangebreaks. Setting trace "+S.index+" to `visible: false`."))}}else delete r.rangebreaks;return r};var p={sun:1,mon:2,tue:3,wed:4,thu:5,fri:6,sat:7};function b(e){if("string"==typeof e)return p[e.substr(0,3).toLowerCase()]}},759:function(e,r,t){"use strict";var a=t(61).mix,i=t(113).lightFraction,n=t(3);e.exports=function(e,r,t,o){var l=(o=o||{}).dfltColor;function s(t,a){return n.coerce2(e,r,o.attributes,t,a)}var d=s("linecolor",l),c=s("linewidth");t("showline",o.showLine||!!d||!!c)||(delete r.linecolor,delete r.linewidth);var f=s("gridcolor",a(l,o.bgColor,o.blend||i).toRgbString()),u=s("gridwidth");if(t("showgrid",o.showGrid||!!f||!!u)||(delete r.gridcolor,delete r.gridwidth),!o.noZeroLine){var v=s("zerolinecolor",l),g=s("zerolinewidth");t("zeroline",o.showGrid||!!v||!!g)||(delete r.zerolinecolor,delete r.zerolinewidth)}}},774:function(e,r,t){"use strict";e.exports=function(e,r,t,a){if("category"===r.type){var i,n=e.categoryarray,o=Array.isArray(n)&&n.length>0;o&&(i="array");var l,s=t("categoryorder",i);"array"===s&&(l=t("categoryarray")),o||"array"!==s||(s=r.categoryorder="trace"),"trace"===s?r._initialCategories=[]:"array"===s?r._initialCategories=l.slice():(l=function(e,r){var t,a,i,n=r.dataAttr||e._id.charAt(0),o={};if(r.axData)t=r.axData;else for(t=[],a=0;a<r.data.length;a++){var l=r.data[a];l[n+"axis"]===e._id&&t.push(l)}for(a=0;a<t.length;a++){var s=t[a][n];for(i=0;i<s.length;i++){var d=s[i];null!=d&&(o[d]=1)}}return Object.keys(o)}(r,a).sort(),"category ascending"===s?r._initialCategories=l:"category descending"===s&&(r._initialCategories=l.reverse()))}}},885:function(e,r){}}]);