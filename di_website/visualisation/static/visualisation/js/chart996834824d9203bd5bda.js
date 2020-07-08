(window.webpackJsonp=window.webpackJsonp||[]).push([[59],{1039:function(e,t,r){"use strict";var a=r(150).hovertemplateAttrs,o=r(150).texttemplateAttrs,i=r(781),l=r(206),n=r(1034),s=r(59),c=r(111),p=r(32).extendFlat,h=r(109).overrideAll,d=i.line,u=i.marker;e.exports=h({lon:i.lon,lat:i.lat,mode:p({},l.mode,{dflt:"markers",description:["Determines the drawing mode for this scatter trace.","If the provided `mode` includes *text* then the `text` elements","appear at the coordinates. Otherwise, the `text` elements","appear on hover."].join(" ")}),text:p({},l.text,{description:["Sets text elements associated with each (lon,lat) pair","If a single string, the same string appears over","all the data points.","If an array of string, the items are mapped in order to the","this trace's (lon,lat) coordinates.","If trace `hoverinfo` contains a *text* flag and *hovertext* is not set,","these elements will be seen in the hover labels."].join(" ")}),texttemplate:o({editType:"plot"},{keys:["lat","lon","text"]}),hovertext:p({},l.hovertext,{description:["Sets hover text elements associated with each (lon,lat) pair","If a single string, the same string appears over","all the data points.","If an array of string, the items are mapped in order to the","this trace's (lon,lat) coordinates.","To be seen, trace `hoverinfo` must contain a *text* flag."].join(" ")}),line:{color:d.color,width:d.width},connectgaps:l.connectgaps,marker:p({symbol:{valType:"string",dflt:"circle",role:"style",arrayOk:!0,description:["Sets the marker symbol.","Full list: https://www.mapbox.com/maki-icons/","Note that the array `marker.color` and `marker.size`","are only available for *circle* symbols."].join(" ")},angle:{valType:"number",dflt:"auto",role:"style",arrayOk:!0,description:["Sets the marker orientation from true North, in degrees clockwise.","When using the *auto* default, no rotation would be applied","in perspective views which is different from using a zero angle."].join(" ")},allowoverlap:{valType:"boolean",dflt:!1,role:"style",description:["Flag to draw all symbols, even if they overlap."].join(" ")},opacity:u.opacity,size:u.size,sizeref:u.sizeref,sizemin:u.sizemin,sizemode:u.sizemode},c("marker")),fill:i.fill,fillcolor:l.fillcolor,textfont:n.layers.symbol.textfont,textposition:n.layers.symbol.textposition,below:{valType:"string",role:"info",description:["Determines if this scattermapbox trace's layers are to be inserted","before the layer with the specified ID.","By default, scattermapbox layers are inserted","above all the base layers.","To place the scattermapbox layers above every other layer, set `below` to *''*."].join(" ")},selected:{marker:l.selected.marker},unselected:{marker:l.unselected.marker},hoverinfo:p({},s.hoverinfo,{flags:["lon","lat","text","name"]}),hovertemplate:a()},"calc","nested")},1123:function(e,t,r){"use strict";var a=r(105);e.exports=function(e,t,r){var o={},i=r[t.subplot]._subplot.mockAxis,l=e.lonlat;return o.lonLabel=a.tickText(i,i.c2l(l[0]),!0).text,o.latLabel=a.tickText(i,i.c2l(l[1]),!0).text,o}},1124:function(e,t,r){"use strict";var a=r(622),o=r(6),i=r(650),l=o.fillText,n=r(25).BADNUM;e.exports=function(e,t,r){var s=e.cd,c=s[0].trace,p=e.xa,h=e.ya,d=e.subplot,u=360*(t>=0?Math.floor((t+180)/360):Math.ceil((t-180)/360)),f=t-u;if(a.getClosest(s,(function(e){var t=e.lonlat;if(t[0]===n)return 1/0;var a=o.modHalf(t[0],360),i=t[1],l=d.project([a,i]),s=l.x-p.c2p([f,i]),c=l.y-h.c2p([a,r]),u=Math.max(3,e.mrc||0);return Math.max(Math.sqrt(s*s+c*c)-u,1-3/u)}),e),!1!==e.index){var m=s[e.index],y=m.lonlat,v=[o.modHalf(y[0],360)+u,y[1]],x=p.c2p(v),b=h.c2p(v),g=m.mrc||1;e.x0=x-g,e.x1=x+g,e.y0=b-g,e.y1=b+g;var w={};w[c.subplot]={_subplot:d};var k=c._module.formatLabels(m,c,w);return e.lonLabel=k.lonLabel,e.latLabel=k.latLabel,e.color=i(c,m),e.extraText=function(e,t,r){if(e.hovertemplate)return;var a=(t.hi||e.hoverinfo).split("+"),o=-1!==a.indexOf("all"),i=-1!==a.indexOf("lon"),n=-1!==a.indexOf("lat"),s=t.lonlat,c=[];function p(e){return e+"°"}o||i&&n?c.push("("+p(s[0])+", "+p(s[1])+")"):i?c.push(r.lon+p(s[0])):n&&c.push(r.lat+p(s[1]));(o||-1!==a.indexOf("text"))&&l(t,e,c);return c.join("<br>")}(c,m,s[0].t.labels),e.hovertemplate=c.hovertemplate,[e]}}},1239:function(e,t,r){"use strict";var a=r(111),o=r(150).hovertemplateAttrs,i=r(59),l=r(1039),n=r(32).extendFlat;e.exports=n({lon:l.lon,lat:l.lat,z:{valType:"data_array",editType:"calc",description:["Sets the points' weight.","For example, a value of 10 would be equivalent to having 10 points of weight 1","in the same spot"].join(" ")},radius:{valType:"number",role:"info",editType:"plot",arrayOk:!0,min:1,dflt:30,description:["Sets the radius of influence of one `lon` / `lat` point in pixels.","Increasing the value makes the densitymapbox trace smoother, but less detailed."].join(" ")},below:{valType:"string",role:"info",editType:"plot",description:["Determines if the densitymapbox trace will be inserted","before the layer with the specified ID.","By default, densitymapbox traces are placed below the first","layer of type symbol","If set to '',","the layer will be inserted above every existing layer."].join(" ")},text:l.text,hovertext:l.hovertext,hoverinfo:n({},i.hoverinfo,{flags:["lon","lat","z","text","name"]}),hovertemplate:o(),showlegend:n({},i.showlegend,{dflt:!1})},a("",{cLetter:"z",editTypeOverride:"calc"}))},1428:function(e,t,r){"use strict";e.exports={attributes:r(1239),supplyDefaults:r(1429),colorbar:r(725),formatLabels:r(1123),calc:r(1430),plot:r(1431),hoverPoints:r(1433),eventData:r(1434),getBelow:function(e,t){for(var r=t.getMapLayers(),a=0;a<r.length;a++){var o=r[a],i=o.id;if("symbol"===o.type&&"string"==typeof i&&-1===i.indexOf("plotly-"))return i}},moduleType:"trace",name:"densitymapbox",basePlotModule:r(1059),categories:["mapbox","gl","showLegend"],meta:{hr_name:"density_mapbox",description:["Draws a bivariate kernel density estimation with a Gaussian kernel","from `lon` and `lat` coordinates and optional `z` values using a colorscale."].join(" ")}}},1429:function(e,t,r){"use strict";var a=r(6),o=r(151),i=r(1239);e.exports=function(e,t,r,l){function n(r,o){return a.coerce(e,t,i,r,o)}var s=n("lon")||[],c=n("lat")||[],p=Math.min(s.length,c.length);p?(t._length=p,n("z"),n("radius"),n("below"),n("text"),n("hovertext"),n("hovertemplate"),o(e,t,l,n,{prefix:"",cLetter:"z"})):t.visible=!1}},1430:function(e,t,r){"use strict";var a=r(12),o=r(6).isArrayOrTypedArray,i=r(25).BADNUM,l=r(209),n=r(6)._;e.exports=function(e,t){for(var r=t._length,s=new Array(r),c=t.z,p=o(c)&&c.length,h=0;h<r;h++){var d=s[h]={},u=t.lon[h],f=t.lat[h];if(d.lonlat=a(u)&&a(f)?[+u,+f]:[i,i],p){var m=c[h];d.z=a(m)?m:i}}return l(e,t,{vals:p?c:[0,1],containerStr:"",cLetter:"z"}),r&&(s[0].t={labels:{lat:n(e,"lat:")+" ",lon:n(e,"lon:")+" "}}),s}},1431:function(e,t,r){"use strict";var a=r(1432),o=r(758).traceLayerPrefix;function i(e,t){this.type="densitymapbox",this.subplot=e,this.uid=t,this.sourceId="source-"+t,this.layerList=[["heatmap",o+t+"-heatmap"]],this.below=null}var l=i.prototype;l.update=function(e){var t=this.subplot,r=this.layerList,o=a(e),i=t.belowLookup["trace-"+this.uid];t.map.getSource(this.sourceId).setData(o.geojson),i!==this.below&&(this._removeLayers(),this._addLayers(o,i),this.below=i);for(var l=0;l<r.length;l++){var n=r[l],s=n[0],c=n[1],p=o[s];t.setOptions(c,"setLayoutProperty",p.layout),"visible"===p.layout.visibility&&t.setOptions(c,"setPaintProperty",p.paint)}},l._addLayers=function(e,t){for(var r=this.subplot,a=this.layerList,o=this.sourceId,i=0;i<a.length;i++){var l=a[i],n=l[0],s=e[n];r.addLayer({type:n,id:l[1],source:o,layout:s.layout,paint:s.paint},t)}},l._removeLayers=function(){for(var e=this.subplot.map,t=this.layerList,r=t.length-1;r>=0;r--)e.removeLayer(t[r][1])},l.dispose=function(){var e=this.subplot.map;this._removeLayers(),e.removeSource(this.sourceId)},e.exports=function(e,t){var r=t[0].trace,o=new i(e,r.uid),l=o.sourceId,n=a(t),s=o.below=e.belowLookup["trace-"+r.uid];return e.map.addSource(l,{type:"geojson",data:n.geojson}),o._addLayers(n,s),o}},1432:function(e,t,r){"use strict";var a=r(12),o=r(6),i=r(57),l=r(207),n=r(25).BADNUM,s=r(895).makeBlank;e.exports=function(e){var t=e[0].trace,r=!0===t.visible&&0!==t._length,c=t._opts={heatmap:{layout:{visibility:"none"},paint:{}},geojson:s()};if(!r)return c;var p,h=[],d=t.z,u=t.radius,f=o.isArrayOrTypedArray(d)&&d.length,m=o.isArrayOrTypedArray(u);for(p=0;p<e.length;p++){var y=e[p],v=y.lonlat;if(v[0]!==n){var x={};if(f){var b=y.z;x.z=b!==n?b:0}m&&(x.r=a(u[p])&&u[p]>0?+u[p]:0),h.push({type:"Feature",geometry:{type:"Point",coordinates:v},properties:x})}}var g=l.extractOpts(t),w=g.reversescale?l.flipScale(g.colorscale):g.colorscale,k=w[0][1],z=["interpolate",["linear"],["heatmap-density"],0,i.opacity(k)<1?k:i.addOpacity(k,0)];for(p=1;p<w.length;p++)z.push(w[p][0],w[p][1]);var L=["interpolate",["linear"],["get","z"],g.min,0,g.max,1];return o.extendFlat(c.heatmap.paint,{"heatmap-weight":f?L:1/(g.max-g.min),"heatmap-color":z,"heatmap-radius":m?{type:"identity",property:"r"}:t.radius,"heatmap-opacity":t.opacity}),c.geojson={type:"FeatureCollection",features:h},c.heatmap.layout.visibility="visible",c}},1433:function(e,t,r){"use strict";var a=r(6),o=r(105),i=r(1124);e.exports=function(e,t,r){var l=i(e,t,r);if(l){var n=l[0],s=n.cd,c=s[0].trace,p=s[n.index];if(delete n.color,"z"in p){var h=n.subplot.mockAxis;n.z=p.z,n.zLabel=o.tickText(h,h.c2l(p.z),"hover").text}return n.extraText=function(e,t,r){if(e.hovertemplate)return;var o=(t.hi||e.hoverinfo).split("+"),i=-1!==o.indexOf("all"),l=-1!==o.indexOf("lon"),n=-1!==o.indexOf("lat"),s=t.lonlat,c=[];function p(e){return e+"°"}i||l&&n?c.push("("+p(s[0])+", "+p(s[1])+")"):l?c.push(r.lon+p(s[0])):n&&c.push(r.lat+p(s[1]));(i||-1!==o.indexOf("text"))&&a.fillText(t,e,c);return c.join("<br>")}(c,p,s[0].t.labels),[n]}}},1434:function(e,t,r){"use strict";e.exports=function(e,t){return e.lon=t.lon,e.lat=t.lat,e.z=t.z,e}},240:function(e,t,r){"use strict";e.exports=r(1428)},650:function(e,t,r){"use strict";var a=r(57),o=r(205);e.exports=function(e,t){var r,i;if("lines"===e.mode)return(r=e.line.color)&&a.opacity(r)?r:e.fillcolor;if("none"===e.mode)return e.fill?e.fillcolor:"";var l=t.mcc||(e.marker||{}).color,n=t.mlcc||((e.marker||{}).line||{}).color;return(i=l&&a.opacity(l)?l:n&&a.opacity(n)&&(t.mlw||((e.marker||{}).line||{}).width)?n:"")?a.opacity(i)<.3?a.addOpacity(i,.3):i:(r=(e.line||{}).color)&&a.opacity(r)&&o.hasLines(e)&&e.line.width?r:e.fillcolor}},725:function(e,t,r){"use strict";e.exports={min:"zmin",max:"zmax"}}}]);