(window.webpackJsonp=window.webpackJsonp||[]).push([[53],{1047:function(e,t,i){"use strict";var o=i(3).extendFlat,a=i(218),s=i(115).dash,n=i(252),r=i(788),l=r.INCREASING.COLOR,d=r.DECREASING.COLOR,c=a.line;function p(e){return{line:{color:o({},c.color,{dflt:e}),width:c.width,dash:s,editType:"style"},editType:"style"}}e.exports={x:{valType:"data_array",editType:"calc+clearAxisTypes",description:["Sets the x coordinates.","If absent, linear coordinate will be generated."].join(" ")},open:{valType:"data_array",editType:"calc",description:"Sets the open values."},high:{valType:"data_array",editType:"calc",description:"Sets the high values."},low:{valType:"data_array",editType:"calc",description:"Sets the low values."},close:{valType:"data_array",editType:"calc",description:"Sets the close values."},line:{width:o({},c.width,{description:[c.width,"Note that this style setting can also be set per","direction via `increasing.line.width` and","`decreasing.line.width`."].join(" ")}),dash:o({},s,{description:[s.description,"Note that this style setting can also be set per","direction via `increasing.line.dash` and","`decreasing.line.dash`."].join(" ")}),editType:"style"},increasing:p(l),decreasing:p(d),text:{valType:"string",role:"info",dflt:"",arrayOk:!0,editType:"calc",description:["Sets hover text elements associated with each sample point.","If a single string, the same string appears over","all the data points.","If an array of string, the items are mapped in order to","this trace's sample points."].join(" ")},hovertext:{valType:"string",role:"info",dflt:"",arrayOk:!0,editType:"calc",description:"Same as `text`."},tickwidth:{valType:"number",min:0,max:.5,dflt:.3,role:"style",editType:"calc",description:["Sets the width of the open/close tick marks","relative to the *x* minimal interval."].join(" ")},hoverlabel:o({},n.hoverlabel,{split:{valType:"boolean",role:"info",dflt:!1,editType:"style",description:["Show hover information (open, close, high, low) in","separate labels."].join(" ")}})}},1115:function(e,t,i){"use strict";var o=i(15),a=i(3);e.exports=function(e,t,i,s){var n=i("x"),r=i("open"),l=i("high"),d=i("low"),c=i("close");if(i("hoverlabel.split"),o.getComponentMethod("calendars","handleTraceDefaults")(e,t,["x"],s),r&&l&&d&&c){var p=Math.min(r.length,l.length,d.length,c.length);return n&&(p=Math.min(p,a.minRowLength(n))),t._length=p,p}}},1116:function(e,t,i){"use strict";var o=i(3),a=o._,s=i(80),n=i(25).BADNUM;function r(e,t,i,o){return{o:e,h:t,l:i,c:o}}function l(e,t,i,r,l){for(var d=r.makeCalcdata(t,"open"),c=r.makeCalcdata(t,"high"),p=r.makeCalcdata(t,"low"),h=r.makeCalcdata(t,"close"),u=Array.isArray(t.text),f=Array.isArray(t.hovertext),y=!0,m=null,x=[],v=0;v<i.length;v++){var b=i[v],g=d[v],T=c[v],w=p[v],k=h[v];if(b!==n&&g!==n&&T!==n&&w!==n&&k!==n){k===g?null!==m&&k!==m&&(y=k>m):y=k>g,m=k;var S=l(g,T,w,k);S.pos=b,S.yc=(g+k)/2,S.i=v,S.dir=y?"increasing":"decreasing",S.x=S.pos,S.y=[w,T],u&&(S.tx=t.text[v]),f&&(S.htx=t.hovertext[v]),x.push(S)}else x.push({pos:b,empty:!0})}return t._extremes[r._id]=s.findExtremes(r,o.concat(p,c),{padded:!0}),x.length&&(x[0].t={labels:{open:a(e,"open:")+" ",high:a(e,"high:")+" ",low:a(e,"low:")+" ",close:a(e,"close:")+" "}}),x}e.exports={calc:function(e,t){var i=s.getFromId(e,t.xaxis),a=s.getFromId(e,t.yaxis),n=function(e,t,i){var a=i._minDiff;if(!a){var s,n=e._fullData,r=[];for(a=1/0,s=0;s<n.length;s++){var l=n[s];if("ohlc"===l.type&&!0===l.visible&&l.xaxis===t._id){r.push(l);var d=t.makeCalcdata(l,"x");l._xcalc=d;var c=o.distinctVals(d).minDiff;c&&isFinite(c)&&(a=Math.min(a,c))}}for(a===1/0&&(a=1),s=0;s<r.length;s++)r[s]._minDiff=a}return a*i.tickwidth}(e,i,t),d=t._minDiff;t._minDiff=null;var c=t._xcalc;t._xcalc=null;var p=l(e,t,c,a,r);return t._extremes[i._id]=s.findExtremes(i,c,{vpad:d/2}),p.length?(o.extendFlat(p[0].t,{wHover:d/2,tickLen:n}),p):[{t:{empty:!0}}]},calcCommon:l}},1117:function(e,t,i){"use strict";var o=i(80),a=i(3),s=i(646),n=i(52),r=i(3).fillText,l=i(788),d={increasing:l.INCREASING.SYMBOL,decreasing:l.DECREASING.SYMBOL};function c(e,t,i,o){var a,r,l=e.cd,d=e.xa,c=l[0].trace,p=l[0].t,h=c.type,u="ohlc"===h?"l":"min",f="ohlc"===h?"h":"max",y=p.bPos||0,m=p.bdPos||p.tickLen,x=p.wHover,v=Math.min(1,m/Math.abs(d.r2c(d.range[1])-d.r2c(d.range[0])));function b(e){var i=function(e){return e.pos+y-t}(e);return s.inbox(i-x,i+x,a)}function g(e){var t=e[u],o=e[f];return t===o||s.inbox(t-i,o-i,a)}function T(e){return(b(e)+g(e))/2}a=e.maxHoverDistance-v,r=e.maxSpikeDistance-v;var w=s.getDistanceFunction(o,b,g,T);if(s.getClosest(l,w,e),!1===e.index)return null;var k=l[e.index];if(k.empty)return null;var S=c[k.dir],j=S.line.color;return n.opacity(j)&&S.line.width?e.color=j:e.color=S.fillcolor,e.x0=d.c2p(k.pos+y-m,!0),e.x1=d.c2p(k.pos+y+m,!0),e.xLabelVal=k.pos,e.spikeDistance=T(k)*r/a,e.xSpike=d.c2p(k.pos,!0),e}function p(e,t,i,s){var n=e.cd,r=e.ya,l=n[0].trace,d=n[0].t,p=[],h=c(e,t,i,s);if(!h)return[];var u=n[h.index].hi||l.hoverinfo,f=u.split("+");if(!("all"===u||-1!==f.indexOf("y")))return[];for(var y=["high","open","close","low"],m={},x=0;x<y.length;x++){var v,b=y[x],g=l[b][h.index],T=r.c2p(g,!0);g in m?(v=m[g]).yLabel+="<br>"+d.labels[b]+o.hoverLabelText(r,g):((v=a.extendFlat({},h)).y0=v.y1=T,v.yLabelVal=g,v.yLabel=d.labels[b]+o.hoverLabelText(r,g),v.name="",p.push(v),m[g]=v)}return p}function h(e,t,i,a){var s=e.cd,n=e.ya,l=s[0].trace,p=s[0].t,h=c(e,t,i,a);if(!h)return[];var u=s[h.index],f=h.index=u.i,y=u.dir;function m(e){return p.labels[e]+o.hoverLabelText(n,l[e][f])}var x=u.hi||l.hoverinfo,v=x.split("+"),b="all"===x,g=b||-1!==v.indexOf("y"),T=b||-1!==v.indexOf("text"),w=g?[m("open"),m("high"),m("low"),m("close")+"  "+d[y]]:[];return T&&r(u,l,w),h.extraText=w.join("<br>"),h.y0=h.y1=n.c2p(u.yc,!0),[h]}e.exports={hoverPoints:function(e,t,i,o){return e.cd[0].trace.hoverlabel.split?p(e,t,i,o):h(e,t,i,o)},hoverSplit:p,hoverOnPoints:h}},1118:function(e,t,i){"use strict";e.exports=function(e,t){var i,o=e.cd,a=e.xaxis,s=e.yaxis,n=[],r=o[0].t.bPos||0;if(!1===t)for(i=0;i<o.length;i++)o[i].selected=0;else for(i=0;i<o.length;i++){var l=o[i];t.contains([a.c2p(l.pos+r),s.c2p(l.yc)],null,l.i,e)?(n.push({pointNumber:l.i,x:a.c2d(l.pos),y:s.c2d(l.yc)}),l.selected=1):l.selected=0}return n}},1213:function(e,t,i){"use strict";var o=i(3).extendFlat,a=i(1047),s=i(893);function n(e){return{line:{color:o({},s.line.color,{dflt:e}),width:s.line.width,editType:"style"},fillcolor:s.fillcolor,editType:"style"}}e.exports={x:a.x,open:a.open,high:a.high,low:a.low,close:a.close,line:{width:o({},s.line.width,{description:[s.line.width.description,"Note that this style setting can also be set per","direction via `increasing.line.width` and","`decreasing.line.width`."].join(" ")}),editType:"style"},increasing:n(a.increasing.line.color.dflt),decreasing:n(a.decreasing.line.color.dflt),text:a.text,hovertext:a.hovertext,whiskerwidth:o({},s.whiskerwidth,{dflt:0}),hoverlabel:a.hoverlabel}},1334:function(e,t,i){"use strict";e.exports={moduleType:"trace",name:"candlestick",basePlotModule:i(649),categories:["cartesian","svg","showLegend","candlestick","boxLayout"],meta:{description:["The candlestick is a style of financial chart describing","open, high, low and close for a given `x` coordinate (most likely time).","The boxes represent the spread between the `open` and `close` values and","the lines represent the spread between the `low` and `high` values","Sample points where the close value is higher (lower) then the open","value are called increasing (decreasing).","By default, increasing candles are drawn in green whereas","decreasing are drawn in red."].join(" ")},attributes:i(1213),layoutAttributes:i(810),supplyLayoutDefaults:i(934).supplyLayoutDefaults,crossTraceCalc:i(935).crossTraceCalc,supplyDefaults:i(1335),calc:i(1336),plot:i(936).plot,layerName:"boxlayer",style:i(960).style,hoverPoints:i(1117).hoverPoints,selectPoints:i(1118)}},1335:function(e,t,i){"use strict";var o=i(3),a=i(52),s=i(1115),n=i(1213);function r(e,t,i,o){var s=i(o+".line.color");i(o+".line.width",t.line.width),i(o+".fillcolor",a.addOpacity(s,.5))}e.exports=function(e,t,i,a){function l(i,a){return o.coerce(e,t,n,i,a)}s(e,t,l,a)?(l("line.width"),r(e,t,l,"increasing"),r(e,t,l,"decreasing"),l("text"),l("hovertext"),l("whiskerwidth"),a._requestRangeslider[t.xaxis]=!0):t.visible=!1}},1336:function(e,t,i){"use strict";var o=i(3),a=i(80),s=i(1116).calcCommon;function n(e,t,i,o){return{min:i,q1:Math.min(e,o),med:o,q3:Math.max(e,o),max:t}}e.exports=function(e,t){var i=e._fullLayout,r=a.getFromId(e,t.xaxis),l=a.getFromId(e,t.yaxis),d=r.makeCalcdata(t,"x"),c=s(e,t,d,l,n);return c.length?(o.extendFlat(c[0].t,{num:i._numBoxes,dPos:o.distinctVals(d).minDiff/2,posLetter:"x",valLetter:"y"}),i._numBoxes++,c):[{t:{empty:!0}}]}},256:function(e,t,i){"use strict";e.exports=i(1334)},650:function(e,t,i){"use strict";var o=i(218),a=i(154).hovertemplateAttrs,s=i(154).texttemplateAttrs,n=i(112),r=i(46),l=i(679),d=i(32).extendFlat,c=r({editType:"calc",arrayOk:!0,colorEditType:"style",description:""}),p=d({},o.marker.line.width,{dflt:0}),h=d({width:p,editType:"calc"},n("marker.line")),u=d({line:h,editType:"calc"},n("marker"),{opacity:{valType:"number",arrayOk:!0,dflt:1,min:0,max:1,role:"style",editType:"style",description:"Sets the opacity of the bars."}});e.exports={x:o.x,x0:o.x0,dx:o.dx,y:o.y,y0:o.y0,dy:o.dy,text:o.text,texttemplate:s({editType:"plot"},{keys:l.eventDataKeys}),hovertext:o.hovertext,hovertemplate:a({},{keys:l.eventDataKeys}),textposition:{valType:"enumerated",role:"info",values:["inside","outside","auto","none"],dflt:"none",arrayOk:!0,editType:"calc",description:["Specifies the location of the `text`.","*inside* positions `text` inside, next to the bar end","(rotated and scaled if needed).","*outside* positions `text` outside, next to the bar end","(scaled if needed), unless there is another bar stacked on","this one, then the text gets pushed inside.","*auto* tries to position `text` inside the bar, but if","the bar is too small and no bar is stacked on this one","the text is moved outside."].join(" ")},insidetextanchor:{valType:"enumerated",values:["end","middle","start"],dflt:"end",role:"info",editType:"plot",description:["Determines if texts are kept at center or start/end points in `textposition` *inside* mode."].join(" ")},textangle:{valType:"angle",dflt:"auto",role:"info",editType:"plot",description:["Sets the angle of the tick labels with respect to the bar.","For example, a `tickangle` of -90 draws the tick labels","vertically. With *auto* the texts may automatically be","rotated to fit with the maximum size in bars."].join(" ")},textfont:d({},c,{description:"Sets the font used for `text`."}),insidetextfont:d({},c,{description:"Sets the font used for `text` lying inside the bar."}),outsidetextfont:d({},c,{description:"Sets the font used for `text` lying outside the bar."}),constraintext:{valType:"enumerated",values:["inside","outside","both","none"],role:"info",dflt:"both",editType:"calc",description:["Constrain the size of text inside or outside a bar to be no","larger than the bar itself."].join(" ")},cliponaxis:d({},o.cliponaxis,{description:["Determines whether the text nodes","are clipped about the subplot axes.","To show the text nodes above axis lines and tick labels,","make sure to set `xaxis.layer` and `yaxis.layer` to *below traces*."].join(" ")}),orientation:{valType:"enumerated",role:"info",values:["v","h"],editType:"calc+clearAxisTypes",description:["Sets the orientation of the bars.","With *v* (*h*), the value of the each bar spans","along the vertical (horizontal)."].join(" ")},base:{valType:"any",dflt:null,arrayOk:!0,role:"info",editType:"calc",description:["Sets where the bar base is drawn (in position axis units).","In *stack* or *relative* barmode,","traces that set *base* will be excluded","and drawn in *overlay* mode instead."].join(" ")},offset:{valType:"number",dflt:null,arrayOk:!0,role:"info",editType:"calc",description:["Shifts the position where the bar is drawn","(in position axis units).","In *group* barmode,","traces that set *offset* will be excluded","and drawn in *overlay* mode instead."].join(" ")},width:{valType:"number",dflt:null,min:0,arrayOk:!0,role:"info",editType:"calc",description:["Sets the bar width (in position axis units)."].join(" ")},marker:u,offsetgroup:{valType:"string",role:"info",dflt:"",editType:"calc",description:["Set several traces linked to the same position axis","or matching axes to the same","offsetgroup where bars of the same position coordinate will line up."].join(" ")},alignmentgroup:{valType:"string",role:"info",dflt:"",editType:"calc",description:["Set several traces linked to the same position axis","or matching axes to the same","alignmentgroup. This controls whether bars compute their positional","range dependently or independently."].join(" ")},selected:{marker:{opacity:o.selected.marker.opacity,color:o.selected.marker.color,editType:"style"},textfont:o.selected.textfont,editType:"style"},unselected:{marker:{opacity:o.unselected.marker.opacity,color:o.unselected.marker.color,editType:"style"},textfont:o.unselected.textfont,editType:"style"},r:o.r,t:o.t,_deprecated:{bardir:{valType:"enumerated",role:"info",editType:"calc",values:["v","h"],description:"Renamed to `orientation`."}}}},679:function(e,t,i){"use strict";e.exports={TEXTPAD:3,eventDataKeys:["value","label"]}},788:function(e,t,i){"use strict";e.exports={INCREASING:{COLOR:"#3D9970",SYMBOL:"▲"},DECREASING:{COLOR:"#FF4136",SYMBOL:"▼"}}},810:function(e,t,i){"use strict";e.exports={boxmode:{valType:"enumerated",values:["group","overlay"],dflt:"overlay",role:"info",editType:"calc",description:["Determines how boxes at the same location coordinate","are displayed on the graph.","If *group*, the boxes are plotted next to one another","centered around the shared location.","If *overlay*, the boxes are plotted over one another,","you might need to set *opacity* to see them multiple boxes.","Has no effect on traces that have *width* set."].join(" ")},boxgap:{valType:"number",min:0,max:1,dflt:.3,role:"style",editType:"calc",description:["Sets the gap (in plot fraction) between boxes of","adjacent location coordinates.","Has no effect on traces that have *width* set."].join(" ")},boxgroupgap:{valType:"number",min:0,max:1,dflt:.3,role:"style",editType:"calc",description:["Sets the gap (in plot fraction) between boxes of","the same location coordinate.","Has no effect on traces that have *width* set."].join(" ")}}},893:function(e,t,i){"use strict";var o=i(218),a=i(650),s=i(113),n=i(154).hovertemplateAttrs,r=i(32).extendFlat,l=o.marker,d=l.line;e.exports={y:{valType:"data_array",editType:"calc+clearAxisTypes",description:["Sets the y sample data or coordinates.","See overview for more info."].join(" ")},x:{valType:"data_array",editType:"calc+clearAxisTypes",description:["Sets the x sample data or coordinates.","See overview for more info."].join(" ")},x0:{valType:"any",role:"info",editType:"calc+clearAxisTypes",description:["Sets the x coordinate for single-box traces","or the starting coordinate for multi-box traces","set using q1/median/q3.","See overview for more info."].join(" ")},y0:{valType:"any",role:"info",editType:"calc+clearAxisTypes",description:["Sets the y coordinate for single-box traces","or the starting coordinate for multi-box traces","set using q1/median/q3.","See overview for more info."].join(" ")},dx:{valType:"number",role:"info",editType:"calc",description:["Sets the x coordinate step for multi-box traces","set using q1/median/q3."].join(" ")},dy:{valType:"number",role:"info",editType:"calc",description:["Sets the y coordinate step for multi-box traces","set using q1/median/q3."].join(" ")},name:{valType:"string",role:"info",editType:"calc+clearAxisTypes",description:["Sets the trace name.","The trace name appear as the legend item and on hover.","For box traces, the name will also be used for the position","coordinate, if `x` and `x0` (`y` and `y0` if horizontal) are","missing and the position axis is categorical"].join(" ")},q1:{valType:"data_array",role:"info",editType:"calc+clearAxisTypes",description:["Sets the Quartile 1 values.","There should be as many items as the number of boxes desired."].join(" ")},median:{valType:"data_array",role:"info",editType:"calc+clearAxisTypes",description:["Sets the median values.","There should be as many items as the number of boxes desired."].join(" ")},q3:{valType:"data_array",role:"info",editType:"calc+clearAxisTypes",description:["Sets the Quartile 3 values.","There should be as many items as the number of boxes desired."].join(" ")},lowerfence:{valType:"data_array",role:"info",editType:"calc",description:["Sets the lower fence values.","There should be as many items as the number of boxes desired.","This attribute has effect only under the q1/median/q3 signature.","If `lowerfence` is not provided but a sample (in `y` or `x`) is set,","we compute the lower as the last sample point below 1.5 times the IQR."].join(" ")},upperfence:{valType:"data_array",role:"info",editType:"calc",description:["Sets the upper fence values.","There should be as many items as the number of boxes desired.","This attribute has effect only under the q1/median/q3 signature.","If `upperfence` is not provided but a sample (in `y` or `x`) is set,","we compute the lower as the last sample point above 1.5 times the IQR."].join(" ")},notched:{valType:"boolean",role:"info",editType:"calc",description:["Determines whether or not notches are drawn.","Notches displays a confidence interval around the median.","We compute the confidence interval as median +/- 1.57 * IQR / sqrt(N),","where IQR is the interquartile range and N is the sample size.","If two boxes' notches do not overlap there is 95% confidence their medians differ.","See https://sites.google.com/site/davidsstatistics/home/notched-box-plots for more info.","Defaults to *false* unless `notchwidth` or `notchspan` is set."].join(" ")},notchwidth:{valType:"number",min:0,max:.5,dflt:.25,role:"style",editType:"calc",description:["Sets the width of the notches relative to","the box' width.","For example, with 0, the notches are as wide as the box(es)."].join(" ")},notchspan:{valType:"data_array",role:"info",editType:"calc",description:["Sets the notch span from the boxes' `median` values.","There should be as many items as the number of boxes desired.","This attribute has effect only under the q1/median/q3 signature.","If `notchspan` is not provided but a sample (in `y` or `x`) is set,","we compute it as 1.57 * IQR / sqrt(N),","where N is the sample size."].join(" ")},boxpoints:{valType:"enumerated",values:["all","outliers","suspectedoutliers",!1],role:"style",editType:"calc",description:["If *outliers*, only the sample points lying outside the whiskers","are shown","If *suspectedoutliers*, the outlier points are shown and","points either less than 4*Q1-3*Q3 or greater than 4*Q3-3*Q1","are highlighted (see `outliercolor`)","If *all*, all sample points are shown","If *false*, only the box(es) are shown with no sample points","Defaults to *suspectedoutliers* when `marker.outliercolor` or","`marker.line.outliercolor` is set.","Defaults to *all* under the q1/median/q3 signature.","Otherwise defaults to *outliers*."].join(" ")},jitter:{valType:"number",min:0,max:1,role:"style",editType:"calc",description:["Sets the amount of jitter in the sample points drawn.","If *0*, the sample points align along the distribution axis.","If *1*, the sample points are drawn in a random jitter of width","equal to the width of the box(es)."].join(" ")},pointpos:{valType:"number",min:-2,max:2,role:"style",editType:"calc",description:["Sets the position of the sample points in relation to the box(es).","If *0*, the sample points are places over the center of the box(es).","Positive (negative) values correspond to positions to the","right (left) for vertical boxes and above (below) for horizontal boxes"].join(" ")},boxmean:{valType:"enumerated",values:[!0,"sd",!1],role:"style",editType:"calc",description:["If *true*, the mean of the box(es)' underlying distribution is","drawn as a dashed line inside the box(es).","If *sd* the standard deviation is also drawn.","Defaults to *true* when `mean` is set.","Defaults to *sd* when `sd` is set","Otherwise defaults to *false*."].join(" ")},mean:{valType:"data_array",role:"info",editType:"calc",description:["Sets the mean values.","There should be as many items as the number of boxes desired.","This attribute has effect only under the q1/median/q3 signature.","If `mean` is not provided but a sample (in `y` or `x`) is set,","we compute the mean for each box using the sample values."].join(" ")},sd:{valType:"data_array",role:"info",editType:"calc",description:["Sets the standard deviation values.","There should be as many items as the number of boxes desired.","This attribute has effect only under the q1/median/q3 signature.","If `sd` is not provided but a sample (in `y` or `x`) is set,","we compute the standard deviation for each box using the sample values."].join(" ")},orientation:{valType:"enumerated",values:["v","h"],role:"style",editType:"calc+clearAxisTypes",description:["Sets the orientation of the box(es).","If *v* (*h*), the distribution is visualized along","the vertical (horizontal)."].join(" ")},quartilemethod:{valType:"enumerated",values:["linear","exclusive","inclusive"],dflt:"linear",role:"info",editType:"calc",description:["Sets the method used to compute the sample's Q1 and Q3 quartiles.","The *linear* method uses the 25th percentile for Q1 and 75th percentile for Q3","as computed using method #10 (listed on http://www.amstat.org/publications/jse/v14n3/langford.html).","The *exclusive* method uses the median to divide the ordered dataset into two halves","if the sample is odd, it does not include the median in either half -","Q1 is then the median of the lower half and","Q3 the median of the upper half.","The *inclusive* method also uses the median to divide the ordered dataset into two halves","but if the sample is odd, it includes the median in both halves -","Q1 is then the median of the lower half and","Q3 the median of the upper half."].join(" ")},width:{valType:"number",min:0,role:"info",dflt:0,editType:"calc",description:["Sets the width of the box in data coordinate","If *0* (default value) the width is automatically selected based on the positions","of other box traces in the same subplot."].join(" ")},marker:{outliercolor:{valType:"color",dflt:"rgba(0, 0, 0, 0)",role:"style",editType:"style",description:"Sets the color of the outlier sample points."},symbol:r({},l.symbol,{arrayOk:!1,editType:"plot"}),opacity:r({},l.opacity,{arrayOk:!1,dflt:1,editType:"style"}),size:r({},l.size,{arrayOk:!1,editType:"calc"}),color:r({},l.color,{arrayOk:!1,editType:"style"}),line:{color:r({},d.color,{arrayOk:!1,dflt:s.defaultLine,editType:"style"}),width:r({},d.width,{arrayOk:!1,dflt:0,editType:"style"}),outliercolor:{valType:"color",role:"style",editType:"style",description:["Sets the border line color of the outlier sample points.","Defaults to marker.color"].join(" ")},outlierwidth:{valType:"number",min:0,dflt:1,role:"style",editType:"style",description:["Sets the border line width (in px) of the outlier sample points."].join(" ")},editType:"style"},editType:"plot"},line:{color:{valType:"color",role:"style",editType:"style",description:"Sets the color of line bounding the box(es)."},width:{valType:"number",role:"style",min:0,dflt:2,editType:"style",description:"Sets the width (in px) of line bounding the box(es)."},editType:"plot"},fillcolor:o.fillcolor,whiskerwidth:{valType:"number",min:0,max:1,dflt:.5,role:"style",editType:"calc",description:["Sets the width of the whiskers relative to","the box' width.","For example, with 1, the whiskers are as wide as the box(es)."].join(" ")},offsetgroup:a.offsetgroup,alignmentgroup:a.alignmentgroup,selected:{marker:o.selected.marker,editType:"style"},unselected:{marker:o.unselected.marker,editType:"style"},text:r({},o.text,{description:["Sets the text elements associated with each sample value.","If a single string, the same string appears over","all the data points.","If an array of string, the items are mapped in order to the","this trace's (x,y) coordinates.","To be seen, trace `hoverinfo` must contain a *text* flag."].join(" ")}),hovertext:r({},o.hovertext,{description:"Same as `text`."}),hovertemplate:n({description:["N.B. This only has an effect when hovering on points."].join(" ")}),hoveron:{valType:"flaglist",flags:["boxes","points"],dflt:"boxes+points",role:"info",editType:"style",description:["Do the hover effects highlight individual boxes ","or sample points or both?"].join(" ")}}},934:function(e,t,i){"use strict";var o=i(15),a=i(3),s=i(810);function n(e,t,i,a,s){for(var n=s+"Layout",r=!1,l=0;l<i.length;l++){var d=i[l];if(o.traceIs(d,n)){r=!0;break}}r&&(a(s+"mode"),a(s+"gap"),a(s+"groupgap"))}e.exports={supplyLayoutDefaults:function(e,t,i){n(0,0,i,(function(i,o){return a.coerce(e,t,s,i,o)}),"box")},_supply:n}},935:function(e,t,i){"use strict";var o=i(80),a=i(3),s=i(83).getAxisGroup,n=["v","h"];function r(e,t,i,n){var r,l,d,c=t.calcdata,p=t._fullLayout,h=n._id,u=h.charAt(0),f=[],y=0;for(r=0;r<i.length;r++)for(d=c[i[r]],l=0;l<d.length;l++)f.push(n.c2l(d[l].pos,!0)),y+=(d[l].pts2||[]).length;if(f.length){var m=a.distinctVals(f),x=m.minDiff/2;o.minDtick(n,m.minDiff,m.vals[0],!0);var v=p["violin"===e?"_numViolins":"_numBoxes"],b="group"===p[e+"mode"]&&v>1,g=1-p[e+"gap"],T=1-p[e+"groupgap"];for(r=0;r<i.length;r++){var w,k,S,j,I,_,A=(d=c[i[r]])[0].trace,L=d[0].t,P=A.width,M=A.side;if(P)w=k=j=P/2,S=0;else if(w=x,b){var D=s(p,n._id)+A.orientation,O=(p._alignmentOpts[D]||{})[A.alignmentgroup]||{},q=Object.keys(O.offsetGroups||{}).length,C=q||v;k=w*g*T/C,S=2*w*(((q?A._offsetIndex:L.num)+.5)/C-.5)*g,j=w*g/C}else k=w*g*T,S=0,j=w;L.dPos=w,L.bPos=S,L.bdPos=k,L.wHover=j;var N,R,F,Q,H,V,E=S+k,z=Boolean(P);if("positive"===M?(I=w*(P?1:.5),N=E,_=N=S):"negative"===M?(I=N=S,_=w*(P?1:.5),R=E):(I=_=w,N=R=E),(A.boxpoints||A.points)&&y>0){var B=A.pointpos,G=A.jitter,Z=A.marker.size/2,W=0;B+G>=0&&((W=E*(B+G))>I?(z=!0,H=Z,F=W):W>N&&(H=Z,F=I)),W<=I&&(F=I);var Y=0;B-G<=0&&((Y=-E*(B-G))>_?(z=!0,V=Z,Q=Y):Y>R&&(V=Z,Q=_)),Y<=_&&(Q=_)}else F=I,Q=_;var K=new Array(d.length);for(l=0;l<d.length;l++)K[l]=d[l].pos;A._extremes[h]=o.findExtremes(n,K,{padded:z,vpadminus:Q,vpadplus:F,vpadLinearized:!0,ppadminus:{x:V,y:H}[u],ppadplus:{x:H,y:V}[u]})}}}e.exports={crossTraceCalc:function(e,t){for(var i=e.calcdata,o=t.xaxis,a=t.yaxis,s=0;s<n.length;s++){for(var l=n[s],d="h"===l?a:o,c=[],p=0;p<i.length;p++){var h=i[p],u=h[0].t,f=h[0].trace;!0!==f.visible||"box"!==f.type&&"candlestick"!==f.type||u.empty||(f.orientation||"v")!==l||f.xaxis!==o._id||f.yaxis!==a._id||c.push(p)}r("box",e,c,d)}},setPositionOffset:r}},936:function(e,t,i){"use strict";var o=i(24),a=i(3),s=i(81);function n(e,t,i,s){var n,r,l="h"===i.orientation,d=t.val,c=t.pos,p=!!c.rangebreaks,h=s.bPos,u=s.wdPos||0,f=s.bPosPxOffset||0,y=i.whiskerwidth||0,m=i.notched||!1,x=m?1-2*i.notchwidth:1;Array.isArray(s.bdPos)?(n=s.bdPos[0],r=s.bdPos[1]):(n=s.bdPos,r=s.bdPos);var v=e.selectAll("path.box").data("violin"!==i.type||i.box.visible?a.identity:[]);v.enter().append("path").style("vector-effect","non-scaling-stroke").attr("class","box"),v.exit().remove(),v.each((function(e){if(e.empty)return"M0,0Z";var t=c.c2l(e.pos+h,!0),s=c.l2p(t-n)+f,v=c.l2p(t+r)+f,b=p?(s+v)/2:c.l2p(t)+f,g=i.whiskerwidth,T=p?s*g+(1-g)*b:c.l2p(t-u)+f,w=p?v*g+(1-g)*b:c.l2p(t+u)+f,k=c.l2p(t-n*x)+f,S=c.l2p(t+r*x)+f,j=d.c2p(e.q1,!0),I=d.c2p(e.q3,!0),_=a.constrain(d.c2p(e.med,!0),Math.min(j,I)+1,Math.max(j,I)-1),A=void 0===e.lf||!1===i.boxpoints,L=d.c2p(A?e.min:e.lf,!0),P=d.c2p(A?e.max:e.uf,!0),M=d.c2p(e.ln,!0),D=d.c2p(e.un,!0);l?o.select(this).attr("d","M"+_+","+k+"V"+S+"M"+j+","+s+"V"+v+(m?"H"+M+"L"+_+","+S+"L"+D+","+v:"")+"H"+I+"V"+s+(m?"H"+D+"L"+_+","+k+"L"+M+","+s:"")+"ZM"+j+","+b+"H"+L+"M"+I+","+b+"H"+P+(0===y?"":"M"+L+","+T+"V"+w+"M"+P+","+T+"V"+w)):o.select(this).attr("d","M"+k+","+_+"H"+S+"M"+s+","+j+"H"+v+(m?"V"+M+"L"+S+","+_+"L"+v+","+D:"")+"V"+I+"H"+s+(m?"V"+D+"L"+k+","+_+"L"+s+","+M:"")+"ZM"+b+","+j+"V"+L+"M"+b+","+I+"V"+P+(0===y?"":"M"+T+","+L+"H"+w+"M"+T+","+P+"H"+w))}))}function r(e,t,i,o){var n=t.x,r=t.y,l=o.bdPos,d=o.bPos,c=i.boxpoints||i.points;a.seedPseudoRandom();var p=e.selectAll("g.points").data(c?function(e){return e.forEach((function(e){e.t=o,e.trace=i})),e}:[]);p.enter().append("g").attr("class","points"),p.exit().remove();var h=p.selectAll("path").data((function(e){var t,o,s=e.pts2,n=Math.max((e.max-e.min)/10,e.q3-e.q1),r=1e-9*n,p=.01*n,h=[],u=0;if(i.jitter){if(0===n)for(u=1,h=new Array(s.length),t=0;t<s.length;t++)h[t]=1;else for(t=0;t<s.length;t++){var f=Math.max(0,t-5),y=s[f].v,m=Math.min(s.length-1,t+5),x=s[m].v;"all"!==c&&(s[t].v<e.lf?x=Math.min(x,e.lf):y=Math.max(y,e.uf));var v=Math.sqrt(p*(m-f)/(x-y+r))||0;v=a.constrain(Math.abs(v),0,1),h.push(v),u=Math.max(v,u)}o=2*i.jitter/(u||1)}for(t=0;t<s.length;t++){var b=s[t],g=b.v,T=i.jitter?o*h[t]*(a.pseudoRandom()-.5):0,w=e.pos+d+l*(i.pointpos+T);"h"===i.orientation?(b.y=w,b.x=g):(b.x=w,b.y=g),"suspectedoutliers"===c&&g<e.uo&&g>e.lo&&(b.so=!0)}return s}));h.enter().append("path").classed("point",!0),h.exit().remove(),h.call(s.translatePoints,n,r)}function l(e,t,i,s){var n,r,l=t.val,d=t.pos,c=!!d.rangebreaks,p=s.bPos,h=s.bPosPxOffset||0,u=i.boxmean||(i.meanline||{}).visible;Array.isArray(s.bdPos)?(n=s.bdPos[0],r=s.bdPos[1]):(n=s.bdPos,r=s.bdPos);var f=e.selectAll("path.mean").data("box"===i.type&&i.boxmean||"violin"===i.type&&i.box.visible&&i.meanline.visible?a.identity:[]);f.enter().append("path").attr("class","mean").style({fill:"none","vector-effect":"non-scaling-stroke"}),f.exit().remove(),f.each((function(e){var t=d.c2l(e.pos+p,!0),a=d.l2p(t-n)+h,s=d.l2p(t+r)+h,f=c?(a+s)/2:d.l2p(t)+h,y=l.c2p(e.mean,!0),m=l.c2p(e.mean-e.sd,!0),x=l.c2p(e.mean+e.sd,!0);"h"===i.orientation?o.select(this).attr("d","M"+y+","+a+"V"+s+("sd"===u?"m0,0L"+m+","+f+"L"+y+","+a+"L"+x+","+f+"Z":"")):o.select(this).attr("d","M"+a+","+y+"H"+s+("sd"===u?"m0,0L"+f+","+m+"L"+a+","+y+"L"+f+","+x+"Z":""))}))}e.exports={plot:function(e,t,i,s){var d=t.xaxis,c=t.yaxis;a.makeTraceGroups(s,i,"trace boxes").each((function(e){var t,i,a=o.select(this),s=e[0],p=s.t,h=s.trace;(p.wdPos=p.bdPos*h.whiskerwidth,!0!==h.visible||p.empty)?a.remove():("h"===h.orientation?(t=c,i=d):(t=d,i=c),n(a,{pos:t,val:i},h,p),r(a,{x:d,y:c},h,p),l(a,{pos:t,val:i},h,p))}))},plotBoxAndWhiskers:n,plotPoints:r,plotBoxMean:l}},960:function(e,t,i){"use strict";var o=i(24),a=i(52),s=i(81);e.exports={style:function(e,t,i){var n=i||o.select(e).selectAll("g.trace.boxes");n.style("opacity",(function(e){return e[0].trace.opacity})),n.each((function(t){var i=o.select(this),n=t[0].trace,r=n.line.width;function l(e,t,i,o){e.style("stroke-width",t+"px").call(a.stroke,i).call(a.fill,o)}var d=i.selectAll("path.box");if("candlestick"===n.type)d.each((function(e){if(!e.empty){var t=o.select(this),i=n[e.dir];l(t,i.line.width,i.line.color,i.fillcolor),t.style("opacity",n.selectedpoints&&!e.selected?.3:1)}}));else{l(d,r,n.line.color,n.fillcolor),i.selectAll("path.mean").style({"stroke-width":r,"stroke-dasharray":2*r+"px,"+r+"px"}).call(a.stroke,n.line.color);var c=i.selectAll("path.point");s.pointStyle(c,n,e)}}))},styleOnSelect:function(e,t,i){var o=t[0].trace,a=i.selectAll("path.point");o.selectedpoints?s.selectedPointStyle(a,o):s.pointStyle(a,o,e)}}}}]);