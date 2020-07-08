(window.webpackJsonp=window.webpackJsonp||[]).push([[43],{1062:function(e,t,r){"use strict";e.exports=function(e,t){for(var r,a=e._fullData.length,n=0;n<a;n++){var i=e._fullData[n];if(i.index!==t.index&&("carpet"===i.type&&(r||(r=i),i.carpet===t.carpet)))return i}return r}},1512:function(e,t,r){"use strict";var a=r(398),n=r(399),i=r(391).hovertemplateAttrs,o=r(391).texttemplateAttrs,l=r(396),s=r(387).extendFlat,c=a.marker,p=a.line,f=c.line;e.exports={carpet:{valType:"string",role:"info",editType:"calc",description:["An identifier for this carpet, so that `scattercarpet` and","`contourcarpet` traces can specify a carpet plot on which","they lie"].join(" ")},a:{valType:"data_array",editType:"calc",description:"Sets the a-axis coordinates."},b:{valType:"data_array",editType:"calc",description:"Sets the b-axis coordinates."},mode:s({},a.mode,{dflt:"markers"}),text:s({},a.text,{description:["Sets text elements associated with each (a,b) point.","If a single string, the same string appears over","all the data points.","If an array of strings, the items are mapped in order to the","the data points in (a,b).","If trace `hoverinfo` contains a *text* flag and *hovertext* is not set,","these elements will be seen in the hover labels."].join(" ")}),texttemplate:o({editType:"plot"},{keys:["a","b","text"]}),hovertext:s({},a.hovertext,{description:["Sets hover text elements associated with each (a,b) point.","If a single string, the same string appears over","all the data points.","If an array of strings, the items are mapped in order to the","the data points in (a,b).","To be seen, trace `hoverinfo` must contain a *text* flag."].join(" ")}),line:{color:p.color,width:p.width,dash:p.dash,shape:s({},p.shape,{values:["linear","spline"]}),smoothing:p.smoothing,editType:"calc"},connectgaps:a.connectgaps,fill:s({},a.fill,{values:["none","toself","tonext"],dflt:"none",description:["Sets the area to fill with a solid color.","Use with `fillcolor` if not *none*.","scatterternary has a subset of the options available to scatter.","*toself* connects the endpoints of the trace (or each segment","of the trace if it has gaps) into a closed shape.","*tonext* fills the space between two traces if one completely","encloses the other (eg consecutive contour lines), and behaves like","*toself* if there is no trace before it. *tonext* should not be","used if one trace does not enclose the other."].join(" ")}),fillcolor:a.fillcolor,marker:s({symbol:c.symbol,opacity:c.opacity,maxdisplayed:c.maxdisplayed,size:c.size,sizeref:c.sizeref,sizemin:c.sizemin,sizemode:c.sizemode,line:s({width:f.width,editType:"calc"},l("marker.line")),gradient:c.gradient,editType:"calc"},l("marker")),textfont:a.textfont,textposition:a.textposition,selected:a.selected,unselected:a.unselected,hoverinfo:s({},n.hoverinfo,{flags:["a","b","text","name"]}),hoveron:a.hoveron,hovertemplate:i()}},1532:function(e,t,r){"use strict";e.exports=r(1626)},1626:function(e,t,r){"use strict";e.exports={attributes:r(1512),supplyDefaults:r(1627),colorbar:r(418),formatLabels:r(1628),calc:r(1629),plot:r(1630),style:r(426).style,styleOnSelect:r(426).styleOnSelect,hoverPoints:r(1631),selectPoints:r(494),eventData:r(1632),moduleType:"trace",name:"scattercarpet",basePlotModule:r(409),categories:["svg","carpet","symbols","showLegend","carpetDependent","zoomScale"],meta:{hrName:"scatter_carpet",description:["Plots a scatter trace on either the first carpet axis or the","carpet axis with a matching `carpet` attribute."].join(" ")}}},1627:function(e,t,r){"use strict";var a=r(380),n=r(457),i=r(389),o=r(431),l=r(435),s=r(475),c=r(436),p=r(442),f=r(1512);e.exports=function(e,t,r,u){function h(r,n){return a.coerce(e,t,f,r,n)}h("carpet"),t.xaxis="x",t.yaxis="y";var x=h("a"),d=h("b"),y=Math.min(x.length,d.length);if(y){t._length=y,h("text"),h("texttemplate"),h("hovertext"),h("mode",y<n.PTS_LINESONLY?"lines+markers":"lines"),i.hasLines(t)&&(l(e,t,r,u,h),s(e,t,h),h("connectgaps")),i.hasMarkers(t)&&o(e,t,r,u,h,{gradient:!0}),i.hasText(t)&&c(e,t,u,h);var v=[];(i.hasMarkers(t)||i.hasText(t))&&(h("marker.maxdisplayed"),v.push("points")),h("fill"),"none"!==t.fill&&(p(e,t,r,h),i.hasLines(t)||s(e,t,h)),"tonext"!==t.fill&&"toself"!==t.fill||v.push("fills"),"fills"!==h("hoveron",v.join("+")||"points")&&h("hovertemplate"),a.coerceSelectionMarkerOpacity(t,h)}else t.visible=!1}},1628:function(e,t,r){"use strict";e.exports=function(e,t){var r={},a=t._carpet,n=a.ab2ij([e.a,e.b]),i=Math.floor(n[0]),o=n[0]-i,l=Math.floor(n[1]),s=n[1]-l,c=a.evalxy([],i,l,o,s);return r.yLabel=c[1].toFixed(3),r}},1629:function(e,t,r){"use strict";var a=r(385),n=r(422),i=r(414),o=r(416),l=r(428).calcMarkerSize,s=r(1062);e.exports=function(e,t){var r=t._carpetTrace=s(e,t);if(r&&r.visible&&"legendonly"!==r.visible){var c;t.xaxis=r.xaxis,t.yaxis=r.yaxis;var p,f,u=t._length,h=new Array(u),x=!1;for(c=0;c<u;c++)if(p=t.a[c],f=t.b[c],a(p)&&a(f)){var d=r.ab2xy(+p,+f,!0),y=r.isVisible(+p,+f);y||(x=!0),h[c]={x:d[0],y:d[1],a:p,b:f,vis:y}}else h[c]={x:!1,y:!1};return t._needsCull=x,h[0].carpet=r,h[0].trace=t,l(t,u),n(e,t),i(h,t),o(h,t),h}}},1630:function(e,t,r){"use strict";var a=r(492),n=r(384),i=r(386);e.exports=function(e,t,r,o){var l,s,c,p=r[0][0].carpet,f={xaxis:n.getFromId(e,p.xaxis||"x"),yaxis:n.getFromId(e,p.yaxis||"y"),plot:t.plot};for(a(e,f,r,o),l=0;l<r.length;l++)s=r[l][0].trace,c=o.selectAll("g.trace"+s.uid+" .js-line"),i.setClipUrl(c,r[l][0].carpet._clipPathId,e)}},1631:function(e,t,r){"use strict";var a=r(476),n=r(380).fillText;e.exports=function(e,t,r,i){var o=a(e,t,r,i);if(o&&!1!==o[0].index){var l=o[0];if(void 0===l.index){var s=1-l.y0/e.ya._length,c=e.xa._length,p=c*s/2,f=c-p;return l.x0=Math.max(Math.min(l.x0,f),p),l.x1=Math.max(Math.min(l.x1,f),p),o}var u=l.cd[l.index];l.a=u.a,l.b=u.b,l.xLabelVal=void 0,l.yLabelVal=void 0;var h=l.trace,x=h._carpet,d=h._module.formatLabels(u,h);l.yLabel=d.yLabel,delete l.text;var y=[];if(!h.hovertemplate){var v=(u.hi||h.hoverinfo).split("+");-1!==v.indexOf("all")&&(v=["a","b","text"]),-1!==v.indexOf("a")&&m(x.aaxis,u.a),-1!==v.indexOf("b")&&m(x.baxis,u.b),y.push("y: "+l.yLabel),-1!==v.indexOf("text")&&n(u,h,y),l.extraText=y.join("<br>")}return o}function m(e,t){var r;r=e.labelprefix&&e.labelprefix.length>0?e.labelprefix.replace(/ = $/,""):e._hovertitle,y.push(r+": "+t.toFixed(3)+e.labelsuffix)}}},1632:function(e,t,r){"use strict";e.exports=function(e,t,r,a,n){var i=a[n];return e.a=i.a,e.b=i.b,e.y=i.y,e}},414:function(e,t,r){"use strict";var a=r(380);e.exports=function(e,t){for(var r=0;r<e.length;r++)e[r].i=r;a.mergeArray(t.text,e,"tx"),a.mergeArray(t.texttemplate,e,"txt"),a.mergeArray(t.hovertext,e,"htx"),a.mergeArray(t.customdata,e,"data"),a.mergeArray(t.textposition,e,"tp"),t.textfont&&(a.mergeArrayCastPositive(t.textfont.size,e,"ts"),a.mergeArray(t.textfont.color,e,"tc"),a.mergeArray(t.textfont.family,e,"tf"));var n=t.marker;if(n){a.mergeArrayCastPositive(n.size,e,"ms"),a.mergeArrayCastPositive(n.opacity,e,"mo"),a.mergeArray(n.symbol,e,"mx"),a.mergeArray(n.color,e,"mc");var i=n.line;n.line&&(a.mergeArray(i.color,e,"mlc"),a.mergeArrayCastPositive(i.width,e,"mlw"));var o=n.gradient;o&&"none"!==o.type&&(a.mergeArray(o.type,e,"mgt"),a.mergeArray(o.color,e,"mgc"))}}},416:function(e,t,r){"use strict";var a=r(380);e.exports=function(e,t){a.isArrayOrTypedArray(t.selectedpoints)&&a.tagSelected(e,t)}},418:function(e,t,r){"use strict";e.exports={container:"marker",min:"cmin",max:"cmax"}},422:function(e,t,r){"use strict";var a=r(401).hasColorscale,n=r(421),i=r(389);e.exports=function(e,t){i.hasLines(t)&&a(t,"line")&&n(e,t,{vals:t.line.color,containerStr:"line",cLetter:"c"}),i.hasMarkers(t)&&(a(t,"marker")&&n(e,t,{vals:t.marker.color,containerStr:"marker",cLetter:"c"}),a(t,"marker.line")&&n(e,t,{vals:t.marker.line.color,containerStr:"marker.line",cLetter:"c"}))}},426:function(e,t,r){"use strict";var a=r(383),n=r(386),i=r(381);function o(e,t,r){n.pointStyle(e.selectAll("path.point"),t,r)}function l(e,t,r){n.textPointStyle(e.selectAll("text"),t,r)}e.exports={style:function(e){var t=a.select(e).selectAll("g.trace.scatter");t.style("opacity",(function(e){return e[0].trace.opacity})),t.selectAll("g.points").each((function(t){o(a.select(this),t.trace||t[0].trace,e)})),t.selectAll("g.text").each((function(t){l(a.select(this),t.trace||t[0].trace,e)})),t.selectAll("g.trace path.js-line").call(n.lineGroupStyle),t.selectAll("g.trace path.js-fill").call(n.fillGroupStyle),i.getComponentMethod("errorbars","style")(t)},stylePoints:o,styleText:l,styleOnSelect:function(e,t,r){var a=t[0].trace;a.selectedpoints?(n.selectedPointStyle(r.selectAll("path.point"),a),n.selectedTextStyle(r.selectAll("text"),a)):(o(r,a,e),l(r,a,e))}}},428:function(e,t,r){"use strict";var a=r(385),n=r(380),i=r(384),o=r(390).BADNUM,l=r(389),s=r(422),c=r(414),p=r(416);function f(e,t,r,a,n,o,s){var c=t._length,p=e._fullLayout,f=r._id,u=a._id,h=p._firstScatter[x(t)]===t.uid,y=(d(t,p,r,a)||{}).orientation,v=t.fill;r._minDtick=0,a._minDtick=0;var m={padded:!0},g={padded:!0};s&&(m.ppad=g.ppad=s);var b=c<2||n[0]!==n[c-1]||o[0]!==o[c-1];b&&("tozerox"===v||"tonextx"===v&&(h||"h"===y))?m.tozero=!0:(t.error_y||{}).visible||"tonexty"!==v&&"tozeroy"!==v&&(l.hasMarkers(t)||l.hasText(t))||(m.padded=!1,m.ppad=0),b&&("tozeroy"===v||"tonexty"===v&&(h||"v"===y))?g.tozero=!0:"tonextx"!==v&&"tozerox"!==v||(g.padded=!1),f&&(t._extremes[f]=i.findExtremes(r,n,m)),u&&(t._extremes[u]=i.findExtremes(a,o,g))}function u(e,t){if(l.hasMarkers(e)){var r,a=e.marker,o=1.6*(e.marker.sizeref||1);if(r="area"===e.marker.sizemode?function(e){return Math.max(Math.sqrt((e||0)/o),3)}:function(e){return Math.max((e||0)/o,3)},n.isArrayOrTypedArray(a.size)){var s={type:"linear"};i.setConvert(s);for(var c=s.makeCalcdata(e.marker,"size"),p=new Array(t),f=0;f<t;f++)p[f]=r(c[f]);return p}return r(a.size)}}function h(e,t){var r=x(t),a=e._firstScatter;a[r]||(a[r]=t.uid)}function x(e){var t=e.stackgroup;return e.xaxis+e.yaxis+e.type+(t?"-"+t:"")}function d(e,t,r,a){var n=e.stackgroup;if(n){var i=t._scatterStackOpts[r._id+a._id][n],o="v"===i.orientation?a:r;return"linear"===o.type||"log"===o.type?i:void 0}}e.exports={calc:function(e,t){var r,l,x,y,v,m,g=e._fullLayout,b=i.getFromId(e,t.xaxis||"x"),k=i.getFromId(e,t.yaxis||"y"),_=b.makeCalcdata(t,"x"),A=k.makeCalcdata(t,"y"),M=t._length,S=new Array(M),w=t.ids,L=d(t,g,b,k),z=!1;h(g,t);var T,C="x",P="y";for(L?(n.pushUnique(L.traceIndices,t._expandedIndex),(r="v"===L.orientation)?(P="s",T="x"):(C="s",T="y"),v="interpolate"===L.stackgaps):f(e,t,b,k,_,A,u(t,M)),l=0;l<M;l++){var O=S[l]={},I=a(_[l]),F=a(A[l]);I&&F?(O[C]=_[l],O[P]=A[l]):L&&(r?I:F)?(O[T]=r?_[l]:A[l],O.gap=!0,v?(O.s=o,z=!0):O.s=0):O[C]=O[P]=o,w&&(O.id=String(w[l]))}if(c(S,t),s(e,t),p(S,t),L){for(l=0;l<S.length;)S[l][T]===o?S.splice(l,1):l++;if(n.sort(S,(function(e,t){return e[T]-t[T]||e.i-t.i})),z){for(l=0;l<S.length-1&&S[l].gap;)l++;for((m=S[l].s)||(m=S[l].s=0),x=0;x<l;x++)S[x].s=m;for(y=S.length-1;y>l&&S[y].gap;)y--;for(m=S[y].s,x=S.length-1;x>y;x--)S[x].s=m;for(;l<y;)if(S[++l].gap){for(x=l+1;S[x].gap;)x++;for(var j=S[l-1][T],D=S[l-1].s,U=(S[x].s-D)/(S[x][T]-j);l<x;)S[l].s=D+(S[l][T]-j)*U,l++}}}return S},calcMarkerSize:u,calcAxisExpansion:f,setFirstScatter:h,getStackOpts:d}},431:function(e,t,r){"use strict";var a=r(382),n=r(401).hasColorscale,i=r(403),o=r(389);e.exports=function(e,t,r,l,s,c){var p=o.isBubble(e),f=(e.line||{}).color;(c=c||{},f&&(r=f),s("marker.symbol"),s("marker.opacity",p?.7:1),s("marker.size"),s("marker.color",r),n(e,"marker")&&i(e,t,l,s,{prefix:"marker.",cLetter:"c"}),c.noSelect||(s("selected.marker.color"),s("unselected.marker.color"),s("selected.marker.size"),s("unselected.marker.size")),c.noLine||(s("marker.line.color",f&&!Array.isArray(f)&&t.marker.color!==f?f:p?a.background:a.defaultLine),n(e,"marker.line")&&i(e,t,l,s,{prefix:"marker.line.",cLetter:"c"}),s("marker.line.width",p?1:0)),p&&(s("marker.sizeref"),s("marker.sizemin"),s("marker.sizemode")),c.gradient)&&("none"!==s("marker.gradient.type")&&s("marker.gradient.color"))}},435:function(e,t,r){"use strict";var a=r(380).isArrayOrTypedArray,n=r(401).hasColorscale,i=r(403);e.exports=function(e,t,r,o,l,s){var c=(e.marker||{}).color;(l("line.color",r),n(e,"line"))?i(e,t,o,l,{prefix:"line.",cLetter:"c"}):l("line.color",!a(c)&&c||r);l("line.width"),(s||{}).noDash||l("line.dash")}},436:function(e,t,r){"use strict";var a=r(380);e.exports=function(e,t,r,n,i){i=i||{},n("textposition"),a.coerceFont(n,"textfont",r.font),i.noSelect||(n("selected.textfont.color"),n("unselected.textfont.color"))}},438:function(e,t,r){"use strict";var a=r(382),n=r(389);e.exports=function(e,t){var r,i;if("lines"===e.mode)return(r=e.line.color)&&a.opacity(r)?r:e.fillcolor;if("none"===e.mode)return e.fill?e.fillcolor:"";var o=t.mcc||(e.marker||{}).color,l=t.mlcc||((e.marker||{}).line||{}).color;return(i=o&&a.opacity(o)?o:l&&a.opacity(l)&&(t.mlw||((e.marker||{}).line||{}).width)?l:"")?a.opacity(i)<.3?a.addOpacity(i,.3):i:(r=(e.line||{}).color)&&a.opacity(r)&&n.hasLines(e)&&e.line.width?r:e.fillcolor}},442:function(e,t,r){"use strict";var a=r(382),n=r(380).isArrayOrTypedArray;e.exports=function(e,t,r,i){var o=!1;if(t.marker){var l=t.marker.color,s=(t.marker.line||{}).color;l&&!n(l)?o=l:s&&!n(s)&&(o=s)}i("fillcolor",a.addOpacity((t.line||{}).color||o||r,.5))}},475:function(e,t,r){"use strict";e.exports=function(e,t,r){"spline"===r("line.shape")&&r("line.smoothing")}},476:function(e,t,r){"use strict";var a=r(380),n=r(397),i=r(381),o=r(438),l=r(382),s=a.fillText;e.exports=function(e,t,r,c){var p=e.cd,f=p[0].trace,u=e.xa,h=e.ya,x=u.c2p(t),d=h.c2p(r),y=[x,d],v=f.hoveron||"",m=-1!==f.mode.indexOf("markers")?3:.5;if(-1!==v.indexOf("points")){var g=function(e){var t=Math.max(m,e.mrc||0),r=u.c2p(e.x)-x,a=h.c2p(e.y)-d;return Math.max(Math.sqrt(r*r+a*a)-t,1-m/t)},b=n.getDistanceFunction(c,(function(e){var t=Math.max(3,e.mrc||0),r=1-1/t,a=Math.abs(u.c2p(e.x)-x);return a<t?r*a/t:a-t+r}),(function(e){var t=Math.max(3,e.mrc||0),r=1-1/t,a=Math.abs(h.c2p(e.y)-d);return a<t?r*a/t:a-t+r}),g);if(n.getClosest(p,b,e),!1!==e.index){var k=p[e.index],_=u.c2p(k.x,!0),A=h.c2p(k.y,!0),M=k.mrc||1;e.index=k.i;var S=p[0].t.orientation,w=S&&(k.sNorm||k.s),L="h"===S?w:k.x,z="v"===S?w:k.y;return a.extendFlat(e,{color:o(f,k),x0:_-M,x1:_+M,xLabelVal:L,y0:A-M,y1:A+M,yLabelVal:z,spikeDistance:g(k),hovertemplate:f.hovertemplate}),s(k,f,e),i.getComponentMethod("errorbars","hoverInfo")(k,f,e),[e]}}if(-1!==v.indexOf("fills")&&f._polygons){var T,C,P,O,I,F,j,D,U,G=f._polygons,E=[],N=!1,R=1/0,Z=-1/0,V=1/0,q=-1/0;for(T=0;T<G.length;T++)(P=G[T]).contains(y)&&(N=!N,E.push(P),V=Math.min(V,P.ymin),q=Math.max(q,P.ymax));if(N){var B=((V=Math.max(V,0))+(q=Math.min(q,h._length)))/2;for(T=0;T<E.length;T++)for(O=E[T].pts,C=1;C<O.length;C++)(D=O[C-1][1])>B!=(U=O[C][1])>=B&&(F=O[C-1][0],j=O[C][0],U-D&&(I=F+(j-F)*(B-D)/(U-D),R=Math.min(R,I),Z=Math.max(Z,I)));R=Math.max(R,0),Z=Math.min(Z,u._length);var J=l.defaultLine;return l.opacity(f.fillcolor)?J=f.fillcolor:l.opacity((f.line||{}).color)&&(J=f.line.color),a.extendFlat(e,{distance:e.maxHoverDistance,x0:R,x1:Z,y0:B,y1:B,color:J,hovertemplate:!1}),delete e.index,f.text&&!Array.isArray(f.text)?e.text=String(f.text):e.text=f.name,[e]}}}},482:function(e,t,r){"use strict";var a={tonextx:1,tonexty:1,tonext:1};e.exports=function(e,t,r){var n,i,o,l,s,c={},p=!1,f=-1,u=0,h=-1;for(i=0;i<r.length;i++)(o=(n=r[i][0].trace).stackgroup||"")?o in c?s=c[o]:(s=c[o]=u,u++):n.fill in a&&h>=0?s=h:(s=h=u,u++),s<f&&(p=!0),n._groupIndex=f=s;var x=r.slice();p&&x.sort((function(e,t){var r=e[0].trace,a=t[0].trace;return r._groupIndex-a._groupIndex||r.index-a.index}));var d={};for(i=0;i<x.length;i++)o=(n=x[i][0].trace).stackgroup||"",!0===n.visible?(n._nexttrace=null,n.fill in a&&(l=d[o],n._prevtrace=l||null,l&&(l._nexttrace=n)),n._ownfill=n.fill&&("tozero"===n.fill.substr(0,6)||"toself"===n.fill||"to"===n.fill.substr(0,2)&&!n._prevtrace),d[o]=n):n._prevtrace=n._nexttrace=n._ownfill=null;return x}},492:function(e,t,r){"use strict";var a=r(383),n=r(381),i=r(380),o=i.ensureSingle,l=i.identity,s=r(386),c=r(389),p=r(493),f=r(482),u=r(552).tester;function h(e,t,r,f,h,x,d){var y;!function(e,t,r,n,o){var l=r.xaxis,s=r.yaxis,p=a.extent(i.simpleMap(l.range,l.r2c)),f=a.extent(i.simpleMap(s.range,s.r2c)),u=n[0].trace;if(!c.hasMarkers(u))return;var h=u.marker.maxdisplayed;if(0===h)return;var x=n.filter((function(e){return e.x>=p[0]&&e.x<=p[1]&&e.y>=f[0]&&e.y<=f[1]})),d=Math.ceil(x.length/h),y=0;o.forEach((function(e,r){var a=e[0].trace;c.hasMarkers(a)&&a.marker.maxdisplayed>0&&r<t&&y++}));var v=Math.round(y*d/3+Math.floor(y/3)*d/7.1);n.forEach((function(e){delete e.vis})),x.forEach((function(e,t){0===Math.round((t+v)%d)&&(e.vis=!0)}))}(0,t,r,f,h);var v=!!d&&d.duration>0;function m(e){return v?e.transition():e}var g=r.xaxis,b=r.yaxis,k=f[0].trace,_=k.line,A=a.select(x),M=o(A,"g","errorbars"),S=o(A,"g","lines"),w=o(A,"g","points"),L=o(A,"g","text");if(n.getComponentMethod("errorbars","plot")(e,M,r,d),!0===k.visible){var z,T;m(A).style("opacity",k.opacity);var C=k.fill.charAt(k.fill.length-1);"x"!==C&&"y"!==C&&(C=""),f[0][r.isRangePlot?"nodeRangePlot3":"node3"]=A;var P,O,I="",F=[],j=k._prevtrace;j&&(I=j._prevRevpath||"",T=j._nextFill,F=j._polygons);var D,U,G,E,N,R,Z,V="",q="",B=[],J=i.noop;if(z=k._ownFill,c.hasLines(k)||"none"!==k.fill){for(T&&T.datum(f),-1!==["hv","vh","hvh","vhv"].indexOf(_.shape)?(D=s.steps(_.shape),U=s.steps(_.shape.split("").reverse().join(""))):D=U="spline"===_.shape?function(e){var t=e[e.length-1];return e.length>1&&e[0][0]===t[0]&&e[0][1]===t[1]?s.smoothclosed(e.slice(1),_.smoothing):s.smoothopen(e,_.smoothing)}:function(e){return"M"+e.join("L")},G=function(e){return U(e.reverse())},B=p(f,{xaxis:g,yaxis:b,connectGaps:k.connectgaps,baseTolerance:Math.max(_.width||1,3)/4,shape:_.shape,simplify:_.simplify,fill:k.fill}),Z=k._polygons=new Array(B.length),y=0;y<B.length;y++)k._polygons[y]=u(B[y]);B.length&&(E=B[0][0],R=(N=B[B.length-1])[N.length-1]),J=function(e){return function(t){if(P=D(t),O=G(t),V?C?(V+="L"+P.substr(1),q=O+"L"+q.substr(1)):(V+="Z"+P,q=O+"Z"+q):(V=P,q=O),c.hasLines(k)&&t.length>1){var r=a.select(this);if(r.datum(f),e)m(r.style("opacity",0).attr("d",P).call(s.lineGroupStyle)).style("opacity",1);else{var n=m(r);n.attr("d",P),s.singleLineStyle(f,n)}}}}}var H=S.selectAll(".js-line").data(B);m(H.exit()).style("opacity",0).remove(),H.each(J(!1)),H.enter().append("path").classed("js-line",!0).style("vector-effect","non-scaling-stroke").call(s.lineGroupStyle).each(J(!0)),s.setClipUrl(H,r.layerClipId,e),B.length?(z?(z.datum(f),E&&R&&(C?("y"===C?E[1]=R[1]=b.c2p(0,!0):"x"===C&&(E[0]=R[0]=g.c2p(0,!0)),m(z).attr("d","M"+R+"L"+E+"L"+V.substr(1)).call(s.singleFillStyle)):m(z).attr("d",V+"Z").call(s.singleFillStyle))):T&&("tonext"===k.fill.substr(0,6)&&V&&I?("tonext"===k.fill?m(T).attr("d",V+"Z"+I+"Z").call(s.singleFillStyle):m(T).attr("d",V+"L"+I.substr(1)+"Z").call(s.singleFillStyle),k._polygons=k._polygons.concat(F)):($(T),k._polygons=null)),k._prevRevpath=q,k._prevPolygons=Z):(z?$(z):T&&$(T),k._polygons=k._prevRevpath=k._prevPolygons=null),w.datum(f),L.datum(f),function(t,n,i){var o,p=i[0].trace,f=c.hasMarkers(p),u=c.hasText(p),h=ee(p),x=te,d=te;if(f||u){var y=l,k=p.stackgroup,_=k&&"infer zero"===e._fullLayout._scatterStackOpts[g._id+b._id][k].stackgaps;p.marker.maxdisplayed||p._needsCull?y=_?Q:K:k&&!_&&(y=W),f&&(x=y),u&&(d=y)}var A,M=(o=t.selectAll("path.point").data(x,h)).enter().append("path").classed("point",!0);v&&M.call(s.pointStyle,p,e).call(s.translatePoints,g,b).style("opacity",0).transition().style("opacity",1),o.order(),f&&(A=s.makePointStyleFns(p)),o.each((function(t){var n=a.select(this),i=m(n);s.translatePoint(t,i,g,b)?(s.singlePointStyle(t,i,p,A,e),r.layerClipId&&s.hideOutsideRangePoint(t,i,g,b,p.xcalendar,p.ycalendar),p.customdata&&n.classed("plotly-customdata",null!==t.data&&void 0!==t.data)):i.remove()})),v?o.exit().transition().style("opacity",0).remove():o.exit().remove(),(o=n.selectAll("g").data(d,h)).enter().append("g").classed("textpoint",!0).append("text"),o.order(),o.each((function(e){var t=a.select(this),n=m(t.select("text"));s.translatePoint(e,n,g,b)?r.layerClipId&&s.hideOutsideRangePoint(e,t,g,b,p.xcalendar,p.ycalendar):t.remove()})),o.selectAll("text").call(s.textPointStyle,p,e).each((function(e){var t=g.c2p(e.x),r=b.c2p(e.y);a.select(this).selectAll("tspan.line").each((function(){m(a.select(this)).attr({x:t,y:r})}))})),o.exit().remove()}(w,L,f);var Y=!1===k.cliponaxis?null:r.layerClipId;s.setClipUrl(w,Y,e),s.setClipUrl(L,Y,e)}function $(e){m(e).attr("d","M0,0Z")}function K(e){return e.filter((function(e){return!e.gap&&e.vis}))}function Q(e){return e.filter((function(e){return e.vis}))}function W(e){return e.filter((function(e){return!e.gap}))}function X(e){return e.id}function ee(e){if(e.ids)return X}function te(){return!1}}e.exports=function(e,t,r,n,i,c){var p,u,x=!i,d=!!i&&i.duration>0,y=f(e,t,r);((p=n.selectAll("g.trace").data(y,(function(e){return e[0].trace.uid}))).enter().append("g").attr("class",(function(e){return"trace scatter trace"+e[0].trace.uid})).style("stroke-miterlimit",2),p.order(),function(e,t,r){t.each((function(t){var n=o(a.select(this),"g","fills");s.setClipUrl(n,r.layerClipId,e);var i=t[0].trace,c=[];i._ownfill&&c.push("_ownFill"),i._nexttrace&&c.push("_nextFill");var p=n.selectAll("g").data(c,l);p.enter().append("g"),p.exit().each((function(e){i[e]=null})).remove(),p.order().each((function(e){i[e]=o(a.select(this),"path","js-fill")}))}))}(e,p,t),d)?(c&&(u=c()),a.transition().duration(i.duration).ease(i.easing).each("end",(function(){u&&u()})).each("interrupt",(function(){u&&u()})).each((function(){n.selectAll("g.trace").each((function(r,a){h(e,a,t,r,y,this,i)}))}))):p.each((function(r,a){h(e,a,t,r,y,this,i)}));x&&p.exit().remove(),n.selectAll("path:not([d])").remove()}},493:function(e,t,r){"use strict";var a=r(390),n=a.BADNUM,i=a.LOG_CLIP,o=i+.5,l=i-.5,s=r(380),c=s.segmentsIntersect,p=s.constrain,f=r(457);e.exports=function(e,t){var r,a,i,u,h,x,d,y,v,m,g,b,k,_,A,M,S,w,L=t.xaxis,z=t.yaxis,T="log"===L.type,C="log"===z.type,P=L._length,O=z._length,I=t.connectGaps,F=t.baseTolerance,j=t.shape,D="linear"===j,U=t.fill&&"none"!==t.fill,G=[],E=f.minTolerance,N=e.length,R=new Array(N),Z=0;function V(r){var a=e[r];if(!a)return!1;var i=t.linearized?L.l2p(a.x):L.c2p(a.x),s=t.linearized?z.l2p(a.y):z.c2p(a.y);if(i===n){if(T&&(i=L.c2p(a.x,!0)),i===n)return!1;C&&s===n&&(i*=Math.abs(L._m*O*(L._m>0?o:l)/(z._m*P*(z._m>0?o:l)))),i*=1e3}if(s===n){if(C&&(s=z.c2p(a.y,!0)),s===n)return!1;s*=1e3}return[i,s]}function q(e,t,r,a){var n=r-e,i=a-t,o=.5-e,l=.5-t,s=n*n+i*i,c=n*o+i*l;if(c>0&&c<s){var p=o*i-l*n;if(p*p<s)return!0}}function B(e,t){var r=e[0]/P,a=e[1]/O,n=Math.max(0,-r,r-1,-a,a-1);return n&&void 0!==S&&q(r,a,S,w)&&(n=0),n&&t&&q(r,a,t[0]/P,t[1]/O)&&(n=0),(1+f.toleranceGrowth*n)*F}function J(e,t){var r=e[0]-t[0],a=e[1]-t[1];return Math.sqrt(r*r+a*a)}var H,Y,$,K,Q,W,X,ee=f.maxScreensAway,te=-P*ee,re=P*(1+ee),ae=-O*ee,ne=O*(1+ee),ie=[[te,ae,re,ae],[re,ae,re,ne],[re,ne,te,ne],[te,ne,te,ae]];function oe(e){if(e[0]<te||e[0]>re||e[1]<ae||e[1]>ne)return[p(e[0],te,re),p(e[1],ae,ne)]}function le(e,t){return e[0]===t[0]&&(e[0]===te||e[0]===re)||(e[1]===t[1]&&(e[1]===ae||e[1]===ne)||void 0)}function se(e,t,r){return function(a,n){var i=oe(a),o=oe(n),l=[];if(i&&o&&le(i,o))return l;i&&l.push(i),o&&l.push(o);var c=2*s.constrain((a[e]+n[e])/2,t,r)-((i||a)[e]+(o||n)[e]);c&&((i&&o?c>0==i[e]>o[e]?i:o:i||o)[e]+=c);return l}}function ce(e){var t=e[0],r=e[1],a=t===R[Z-1][0],n=r===R[Z-1][1];if(!a||!n)if(Z>1){var i=t===R[Z-2][0],o=r===R[Z-2][1];a&&(t===te||t===re)&&i?o?Z--:R[Z-1]=e:n&&(r===ae||r===ne)&&o?i?Z--:R[Z-1]=e:R[Z++]=e}else R[Z++]=e}function pe(e){R[Z-1][0]!==e[0]&&R[Z-1][1]!==e[1]&&ce([$,K]),ce(e),Q=null,$=K=0}function fe(e){if(S=e[0]/P,w=e[1]/O,H=e[0]<te?te:e[0]>re?re:0,Y=e[1]<ae?ae:e[1]>ne?ne:0,H||Y){if(Z)if(Q){var t=X(Q,e);t.length>1&&(pe(t[0]),R[Z++]=t[1])}else W=X(R[Z-1],e)[0],R[Z++]=W;else R[Z++]=[H||e[0],Y||e[1]];var r=R[Z-1];H&&Y&&(r[0]!==H||r[1]!==Y)?(Q&&($!==H&&K!==Y?ce($&&K?(a=Q,i=(n=e)[0]-a[0],o=(n[1]-a[1])/i,(a[1]*n[0]-n[1]*a[0])/i>0?[o>0?te:re,ne]:[o>0?re:te,ae]):[$||H,K||Y]):$&&K&&ce([$,K])),ce([H,Y])):$-H&&K-Y&&ce([H||$,Y||K]),Q=e,$=H,K=Y}else Q&&pe(X(Q,e)[0]),R[Z++]=e;var a,n,i,o}for("linear"===j||"spline"===j?X=function(e,t){for(var r=[],a=0,n=0;n<4;n++){var i=ie[n],o=c(e[0],e[1],t[0],t[1],i[0],i[1],i[2],i[3]);o&&(!a||Math.abs(o.x-r[0][0])>1||Math.abs(o.y-r[0][1])>1)&&(o=[o.x,o.y],a&&J(o,e)<J(r[0],e)?r.unshift(o):r.push(o),a++)}return r}:"hv"===j||"vh"===j?X=function(e,t){var r=[],a=oe(e),n=oe(t);return a&&n&&le(a,n)||(a&&r.push(a),n&&r.push(n)),r}:"hvh"===j?X=se(0,te,re):"vhv"===j&&(X=se(1,ae,ne)),r=0;r<N;r++)if(a=V(r)){for(Z=0,Q=null,fe(a),r++;r<N;r++){if(!(u=V(r))){if(I)continue;break}if(D&&t.simplify){var ue=V(r+1);if(m=J(u,a),U&&(0===Z||Z===N-1)||!(m<B(u,ue)*E)){for(y=[(u[0]-a[0])/m,(u[1]-a[1])/m],h=a,g=m,b=_=A=0,d=!1,i=u,r++;r<e.length;r++){if(x=ue,ue=V(r+1),!x){if(I)continue;break}if(M=(v=[x[0]-a[0],x[1]-a[1]])[0]*y[1]-v[1]*y[0],_=Math.min(_,M),(A=Math.max(A,M))-_>B(x,ue))break;i=x,(k=v[0]*y[0]+v[1]*y[1])>g?(g=k,u=x,d=!1):k<b&&(b=k,h=x,d=!0)}if(d?(fe(u),i!==h&&fe(h)):(h!==a&&fe(h),i!==u&&fe(u)),fe(i),r>=e.length||!x)break;fe(x),a=x}}else fe(u)}Q&&ce([$||Q[0],K||Q[1]]),G.push(R.slice(0,Z))}return G}},494:function(e,t,r){"use strict";var a=r(389);e.exports=function(e,t){var r,n,i,o,l=e.cd,s=e.xaxis,c=e.yaxis,p=[],f=l[0].trace;if(!a.hasMarkers(f)&&!a.hasText(f))return[];if(!1===t)for(r=0;r<l.length;r++)l[r].selected=0;else for(r=0;r<l.length;r++)n=l[r],i=s.c2p(n.x),o=c.c2p(n.y),null!==n.i&&t.contains([i,o],!1,r,e)?(p.push({pointNumber:n.i,x:s.c2d(n.x),y:c.c2d(n.y)}),n.selected=1):n.selected=0;return p}}}]);