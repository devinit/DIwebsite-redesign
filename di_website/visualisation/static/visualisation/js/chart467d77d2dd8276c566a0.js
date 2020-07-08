(window.webpackJsonp=window.webpackJsonp||[]).push([[56],{1143:function(e,t,o){"use strict";e.exports=o(1183)},1183:function(e,t,o){"use strict";e.exports={attributes:o(684),layoutAttributes:o(597),supplyDefaults:o(715).supplyDefaults,crossTraceDefaults:o(715).crossTraceDefaults,supplyLayoutDefaults:o(729).supplyLayoutDefaults,calc:o(926),crossTraceCalc:o(730).crossTraceCalc,plot:o(731).plot,style:o(758).style,styleOnSelect:o(758).styleOnSelect,hoverPoints:o(927).hoverPoints,eventData:o(1184),selectPoints:o(928),moduleType:"trace",name:"box",basePlotModule:o(409),categories:["cartesian","svg","symbols","oriented","box-violin","showLegend","boxLayout","zoomScale"],meta:{description:["Each box spans from quartile 1 (Q1) to quartile 3 (Q3).","The second quartile (Q2, i.e. the median) is marked by a line inside the box.","The fences grow outward from the boxes' edges,","by default they span +/- 1.5 times the interquartile range (IQR: Q3-Q1),","The sample mean and standard deviation as well as notches and","the sample, outlier and suspected outliers points can be optionally","added to the box plot.","The values and positions corresponding to each boxes can be input","using two signatures.","The first signature expects users to supply the sample values in the `y`","data array for vertical boxes (`x` for horizontal boxes).","By supplying an `x` (`y`) array, one box per distinct `x` (`y`) value is drawn","If no `x` (`y`) {array} is provided, a single box is drawn.","In this case, the box is positioned with the trace `name` or with `x0` (`y0`) if provided.","The second signature expects users to supply the boxes corresponding Q1, median and Q3","statistics in the `q1`, `median` and `q3` data arrays respectively.","Other box features relying on statistics namely `lowerfence`, `upperfence`, `notchspan`","can be set directly by the users.","To have plotly compute them or to show sample points besides the boxes,","users can set the `y` data array for vertical boxes (`x` for horizontal boxes)","to a 2D array with the outer length corresponding","to the number of boxes in the traces and the inner length corresponding the sample size."].join(" ")}}},1184:function(e,t,o){"use strict";e.exports=function(e,t){return t.hoverOnBox&&(e.hoverOnBox=t.hoverOnBox),"xVal"in t&&(e.x=t.xVal),"yVal"in t&&(e.y=t.yVal),t.xa&&(e.xaxis=t.xa),t.ya&&(e.yaxis=t.ya),e}},412:function(e,t,o){"use strict";var a=o(398),i=o(391).hovertemplateAttrs,n=o(391).texttemplateAttrs,r=o(396),s=o(406),l=o(444),d=o(387).extendFlat,c=s({editType:"calc",arrayOk:!0,colorEditType:"style",description:""}),p=d({},a.marker.line.width,{dflt:0}),h=d({width:p,editType:"calc"},r("marker.line")),u=d({line:h,editType:"calc"},r("marker"),{opacity:{valType:"number",arrayOk:!0,dflt:1,min:0,max:1,role:"style",editType:"style",description:"Sets the opacity of the bars."}});e.exports={x:a.x,x0:a.x0,dx:a.dx,y:a.y,y0:a.y0,dy:a.dy,text:a.text,texttemplate:n({editType:"plot"},{keys:l.eventDataKeys}),hovertext:a.hovertext,hovertemplate:i({},{keys:l.eventDataKeys}),textposition:{valType:"enumerated",role:"info",values:["inside","outside","auto","none"],dflt:"none",arrayOk:!0,editType:"calc",description:["Specifies the location of the `text`.","*inside* positions `text` inside, next to the bar end","(rotated and scaled if needed).","*outside* positions `text` outside, next to the bar end","(scaled if needed), unless there is another bar stacked on","this one, then the text gets pushed inside.","*auto* tries to position `text` inside the bar, but if","the bar is too small and no bar is stacked on this one","the text is moved outside."].join(" ")},insidetextanchor:{valType:"enumerated",values:["end","middle","start"],dflt:"end",role:"info",editType:"plot",description:["Determines if texts are kept at center or start/end points in `textposition` *inside* mode."].join(" ")},textangle:{valType:"angle",dflt:"auto",role:"info",editType:"plot",description:["Sets the angle of the tick labels with respect to the bar.","For example, a `tickangle` of -90 draws the tick labels","vertically. With *auto* the texts may automatically be","rotated to fit with the maximum size in bars."].join(" ")},textfont:d({},c,{description:"Sets the font used for `text`."}),insidetextfont:d({},c,{description:"Sets the font used for `text` lying inside the bar."}),outsidetextfont:d({},c,{description:"Sets the font used for `text` lying outside the bar."}),constraintext:{valType:"enumerated",values:["inside","outside","both","none"],role:"info",dflt:"both",editType:"calc",description:["Constrain the size of text inside or outside a bar to be no","larger than the bar itself."].join(" ")},cliponaxis:d({},a.cliponaxis,{description:["Determines whether the text nodes","are clipped about the subplot axes.","To show the text nodes above axis lines and tick labels,","make sure to set `xaxis.layer` and `yaxis.layer` to *below traces*."].join(" ")}),orientation:{valType:"enumerated",role:"info",values:["v","h"],editType:"calc+clearAxisTypes",description:["Sets the orientation of the bars.","With *v* (*h*), the value of the each bar spans","along the vertical (horizontal)."].join(" ")},base:{valType:"any",dflt:null,arrayOk:!0,role:"info",editType:"calc",description:["Sets where the bar base is drawn (in position axis units).","In *stack* or *relative* barmode,","traces that set *base* will be excluded","and drawn in *overlay* mode instead."].join(" ")},offset:{valType:"number",dflt:null,arrayOk:!0,role:"info",editType:"calc",description:["Shifts the position where the bar is drawn","(in position axis units).","In *group* barmode,","traces that set *offset* will be excluded","and drawn in *overlay* mode instead."].join(" ")},width:{valType:"number",dflt:null,min:0,arrayOk:!0,role:"info",editType:"calc",description:["Sets the bar width (in position axis units)."].join(" ")},marker:u,offsetgroup:{valType:"string",role:"info",dflt:"",editType:"calc",description:["Set several traces linked to the same position axis","or matching axes to the same","offsetgroup where bars of the same position coordinate will line up."].join(" ")},alignmentgroup:{valType:"string",role:"info",dflt:"",editType:"calc",description:["Set several traces linked to the same position axis","or matching axes to the same","alignmentgroup. This controls whether bars compute their positional","range dependently or independently."].join(" ")},selected:{marker:{opacity:a.selected.marker.opacity,color:a.selected.marker.color,editType:"style"},textfont:a.selected.textfont,editType:"style"},unselected:{marker:{opacity:a.unselected.marker.opacity,color:a.unselected.marker.color,editType:"style"},textfont:a.unselected.textfont,editType:"style"},r:a.r,t:a.t,_deprecated:{bardir:{valType:"enumerated",role:"info",editType:"calc",values:["v","h"],description:"Renamed to `orientation`."}}}},432:function(e,t,o){"use strict";var a=o(380),i=o(382),n=o(381),r=o(434),s=o(488),l=o(395).getAxisGroup,d=o(412),c=a.coerceFont;function p(e,t,o,a){var i=t.orientation,n=t[{v:"x",h:"y"}[i]+"axis"],r=l(o,n)+i,s=o._alignmentOpts||{},d=a("alignmentgroup"),c=s[r];c||(c=s[r]={});var p=c[d];p?p.traces.push(t):p=c[d]={traces:[t],alignmentIndex:Object.keys(c).length,offsetGroups:{}};var h=a("offsetgroup"),u=p.offsetGroups,f=u[h];h&&(f||(f=u[h]={offsetIndex:Object.keys(u).length}),t._offsetIndex=f.offsetIndex)}function h(e,t,o,i,n,r){var s=!(!1===(r=r||{}).moduleHasSelected),l=!(!1===r.moduleHasUnselected),d=!(!1===r.moduleHasConstrain),p=!(!1===r.moduleHasCliponaxis),h=!(!1===r.moduleHasTextangle),u=!(!1===r.moduleHasInsideanchor),f=!!r.hasPathbar,m=Array.isArray(n)||"auto"===n,y=m||"inside"===n,x=m||"outside"===n;if(y||x){var v=c(i,"textfont",o.font),b=a.extendFlat({},v),g=!(e.textfont&&e.textfont.color);if(g&&delete b.color,c(i,"insidetextfont",b),f){var T=a.extendFlat({},v);g&&delete T.color,c(i,"pathbar.textfont",T)}x&&c(i,"outsidetextfont",v),s&&i("selected.textfont.color"),l&&i("unselected.textfont.color"),d&&i("constraintext"),p&&i("cliponaxis"),h&&i("textangle"),i("texttemplate")}y&&u&&i("insidetextanchor")}e.exports={supplyDefaults:function(e,t,o,l){function c(o,i){return a.coerce(e,t,d,o,i)}if(r(e,t,l,c)){c("orientation",t.x&&!t.y?"h":"v"),c("base"),c("offset"),c("width"),c("text"),c("hovertext"),c("hovertemplate");var p=c("textposition");h(e,t,l,c,p,{moduleHasSelected:!0,moduleHasUnselected:!0,moduleHasConstrain:!0,moduleHasCliponaxis:!0,moduleHasTextangle:!0,moduleHasInsideanchor:!0}),s(e,t,c,o,l);var u=(t.marker.line||{}).color,f=n.getComponentMethod("errorbars","supplyDefaults");f(e,t,u||i.defaultLine,{axis:"y"}),f(e,t,u||i.defaultLine,{axis:"x",inherit:"y"}),a.coerceSelectionMarkerOpacity(t,c)}else t.visible=!1},crossTraceDefaults:function(e,t){var o;function i(e){return a.coerce(o._input,o,d,e)}if("group"===t.barmode)for(var n=0;n<e.length;n++)"bar"===(o=e[n]).type&&(o._input,p(0,o,t,i))},handleGroupingDefaults:p,handleText:h}},434:function(e,t,o){"use strict";var a=o(380),i=o(381);e.exports=function(e,t,o,n){var r,s=n("x"),l=n("y");if(i.getComponentMethod("calendars","handleTraceDefaults")(e,t,["x","y"],o),s){var d=a.minRowLength(s);l?r=Math.min(d,a.minRowLength(l)):(r=d,n("y0"),n("dy"))}else{if(!l)return 0;r=a.minRowLength(l),n("x0"),n("dx")}return t._length=r,r}},444:function(e,t,o){"use strict";e.exports={TEXTPAD:3,eventDataKeys:["value","label"]}},488:function(e,t,o){"use strict";var a=o(382),i=o(401).hasColorscale,n=o(403);e.exports=function(e,t,o,r,s){o("marker.color",r),i(e,"marker")&&n(e,t,s,o,{prefix:"marker.",cLetter:"c"}),o("marker.line.color",a.defaultLine),i(e,"marker.line")&&n(e,t,s,o,{prefix:"marker.line.",cLetter:"c"}),o("marker.line.width"),o("marker.opacity"),o("selected.marker.color"),o("unselected.marker.color")}},597:function(e,t,o){"use strict";e.exports={boxmode:{valType:"enumerated",values:["group","overlay"],dflt:"overlay",role:"info",editType:"calc",description:["Determines how boxes at the same location coordinate","are displayed on the graph.","If *group*, the boxes are plotted next to one another","centered around the shared location.","If *overlay*, the boxes are plotted over one another,","you might need to set *opacity* to see them multiple boxes.","Has no effect on traces that have *width* set."].join(" ")},boxgap:{valType:"number",min:0,max:1,dflt:.3,role:"style",editType:"calc",description:["Sets the gap (in plot fraction) between boxes of","adjacent location coordinates.","Has no effect on traces that have *width* set."].join(" ")},boxgroupgap:{valType:"number",min:0,max:1,dflt:.3,role:"style",editType:"calc",description:["Sets the gap (in plot fraction) between boxes of","the same location coordinate.","Has no effect on traces that have *width* set."].join(" ")}}},684:function(e,t,o){"use strict";var a=o(398),i=o(412),n=o(408),r=o(391).hovertemplateAttrs,s=o(387).extendFlat,l=a.marker,d=l.line;e.exports={y:{valType:"data_array",editType:"calc+clearAxisTypes",description:["Sets the y sample data or coordinates.","See overview for more info."].join(" ")},x:{valType:"data_array",editType:"calc+clearAxisTypes",description:["Sets the x sample data or coordinates.","See overview for more info."].join(" ")},x0:{valType:"any",role:"info",editType:"calc+clearAxisTypes",description:["Sets the x coordinate for single-box traces","or the starting coordinate for multi-box traces","set using q1/median/q3.","See overview for more info."].join(" ")},y0:{valType:"any",role:"info",editType:"calc+clearAxisTypes",description:["Sets the y coordinate for single-box traces","or the starting coordinate for multi-box traces","set using q1/median/q3.","See overview for more info."].join(" ")},dx:{valType:"number",role:"info",editType:"calc",description:["Sets the x coordinate step for multi-box traces","set using q1/median/q3."].join(" ")},dy:{valType:"number",role:"info",editType:"calc",description:["Sets the y coordinate step for multi-box traces","set using q1/median/q3."].join(" ")},name:{valType:"string",role:"info",editType:"calc+clearAxisTypes",description:["Sets the trace name.","The trace name appear as the legend item and on hover.","For box traces, the name will also be used for the position","coordinate, if `x` and `x0` (`y` and `y0` if horizontal) are","missing and the position axis is categorical"].join(" ")},q1:{valType:"data_array",role:"info",editType:"calc+clearAxisTypes",description:["Sets the Quartile 1 values.","There should be as many items as the number of boxes desired."].join(" ")},median:{valType:"data_array",role:"info",editType:"calc+clearAxisTypes",description:["Sets the median values.","There should be as many items as the number of boxes desired."].join(" ")},q3:{valType:"data_array",role:"info",editType:"calc+clearAxisTypes",description:["Sets the Quartile 3 values.","There should be as many items as the number of boxes desired."].join(" ")},lowerfence:{valType:"data_array",role:"info",editType:"calc",description:["Sets the lower fence values.","There should be as many items as the number of boxes desired.","This attribute has effect only under the q1/median/q3 signature.","If `lowerfence` is not provided but a sample (in `y` or `x`) is set,","we compute the lower as the last sample point below 1.5 times the IQR."].join(" ")},upperfence:{valType:"data_array",role:"info",editType:"calc",description:["Sets the upper fence values.","There should be as many items as the number of boxes desired.","This attribute has effect only under the q1/median/q3 signature.","If `upperfence` is not provided but a sample (in `y` or `x`) is set,","we compute the lower as the last sample point above 1.5 times the IQR."].join(" ")},notched:{valType:"boolean",role:"info",editType:"calc",description:["Determines whether or not notches are drawn.","Notches displays a confidence interval around the median.","We compute the confidence interval as median +/- 1.57 * IQR / sqrt(N),","where IQR is the interquartile range and N is the sample size.","If two boxes' notches do not overlap there is 95% confidence their medians differ.","See https://sites.google.com/site/davidsstatistics/home/notched-box-plots for more info.","Defaults to *false* unless `notchwidth` or `notchspan` is set."].join(" ")},notchwidth:{valType:"number",min:0,max:.5,dflt:.25,role:"style",editType:"calc",description:["Sets the width of the notches relative to","the box' width.","For example, with 0, the notches are as wide as the box(es)."].join(" ")},notchspan:{valType:"data_array",role:"info",editType:"calc",description:["Sets the notch span from the boxes' `median` values.","There should be as many items as the number of boxes desired.","This attribute has effect only under the q1/median/q3 signature.","If `notchspan` is not provided but a sample (in `y` or `x`) is set,","we compute it as 1.57 * IQR / sqrt(N),","where N is the sample size."].join(" ")},boxpoints:{valType:"enumerated",values:["all","outliers","suspectedoutliers",!1],role:"style",editType:"calc",description:["If *outliers*, only the sample points lying outside the whiskers","are shown","If *suspectedoutliers*, the outlier points are shown and","points either less than 4*Q1-3*Q3 or greater than 4*Q3-3*Q1","are highlighted (see `outliercolor`)","If *all*, all sample points are shown","If *false*, only the box(es) are shown with no sample points","Defaults to *suspectedoutliers* when `marker.outliercolor` or","`marker.line.outliercolor` is set.","Defaults to *all* under the q1/median/q3 signature.","Otherwise defaults to *outliers*."].join(" ")},jitter:{valType:"number",min:0,max:1,role:"style",editType:"calc",description:["Sets the amount of jitter in the sample points drawn.","If *0*, the sample points align along the distribution axis.","If *1*, the sample points are drawn in a random jitter of width","equal to the width of the box(es)."].join(" ")},pointpos:{valType:"number",min:-2,max:2,role:"style",editType:"calc",description:["Sets the position of the sample points in relation to the box(es).","If *0*, the sample points are places over the center of the box(es).","Positive (negative) values correspond to positions to the","right (left) for vertical boxes and above (below) for horizontal boxes"].join(" ")},boxmean:{valType:"enumerated",values:[!0,"sd",!1],role:"style",editType:"calc",description:["If *true*, the mean of the box(es)' underlying distribution is","drawn as a dashed line inside the box(es).","If *sd* the standard deviation is also drawn.","Defaults to *true* when `mean` is set.","Defaults to *sd* when `sd` is set","Otherwise defaults to *false*."].join(" ")},mean:{valType:"data_array",role:"info",editType:"calc",description:["Sets the mean values.","There should be as many items as the number of boxes desired.","This attribute has effect only under the q1/median/q3 signature.","If `mean` is not provided but a sample (in `y` or `x`) is set,","we compute the mean for each box using the sample values."].join(" ")},sd:{valType:"data_array",role:"info",editType:"calc",description:["Sets the standard deviation values.","There should be as many items as the number of boxes desired.","This attribute has effect only under the q1/median/q3 signature.","If `sd` is not provided but a sample (in `y` or `x`) is set,","we compute the standard deviation for each box using the sample values."].join(" ")},orientation:{valType:"enumerated",values:["v","h"],role:"style",editType:"calc+clearAxisTypes",description:["Sets the orientation of the box(es).","If *v* (*h*), the distribution is visualized along","the vertical (horizontal)."].join(" ")},quartilemethod:{valType:"enumerated",values:["linear","exclusive","inclusive"],dflt:"linear",role:"info",editType:"calc",description:["Sets the method used to compute the sample's Q1 and Q3 quartiles.","The *linear* method uses the 25th percentile for Q1 and 75th percentile for Q3","as computed using method #10 (listed on http://www.amstat.org/publications/jse/v14n3/langford.html).","The *exclusive* method uses the median to divide the ordered dataset into two halves","if the sample is odd, it does not include the median in either half -","Q1 is then the median of the lower half and","Q3 the median of the upper half.","The *inclusive* method also uses the median to divide the ordered dataset into two halves","but if the sample is odd, it includes the median in both halves -","Q1 is then the median of the lower half and","Q3 the median of the upper half."].join(" ")},width:{valType:"number",min:0,role:"info",dflt:0,editType:"calc",description:["Sets the width of the box in data coordinate","If *0* (default value) the width is automatically selected based on the positions","of other box traces in the same subplot."].join(" ")},marker:{outliercolor:{valType:"color",dflt:"rgba(0, 0, 0, 0)",role:"style",editType:"style",description:"Sets the color of the outlier sample points."},symbol:s({},l.symbol,{arrayOk:!1,editType:"plot"}),opacity:s({},l.opacity,{arrayOk:!1,dflt:1,editType:"style"}),size:s({},l.size,{arrayOk:!1,editType:"calc"}),color:s({},l.color,{arrayOk:!1,editType:"style"}),line:{color:s({},d.color,{arrayOk:!1,dflt:n.defaultLine,editType:"style"}),width:s({},d.width,{arrayOk:!1,dflt:0,editType:"style"}),outliercolor:{valType:"color",role:"style",editType:"style",description:["Sets the border line color of the outlier sample points.","Defaults to marker.color"].join(" ")},outlierwidth:{valType:"number",min:0,dflt:1,role:"style",editType:"style",description:["Sets the border line width (in px) of the outlier sample points."].join(" ")},editType:"style"},editType:"plot"},line:{color:{valType:"color",role:"style",editType:"style",description:"Sets the color of line bounding the box(es)."},width:{valType:"number",role:"style",min:0,dflt:2,editType:"style",description:"Sets the width (in px) of line bounding the box(es)."},editType:"plot"},fillcolor:a.fillcolor,whiskerwidth:{valType:"number",min:0,max:1,dflt:.5,role:"style",editType:"calc",description:["Sets the width of the whiskers relative to","the box' width.","For example, with 1, the whiskers are as wide as the box(es)."].join(" ")},offsetgroup:i.offsetgroup,alignmentgroup:i.alignmentgroup,selected:{marker:a.selected.marker,editType:"style"},unselected:{marker:a.unselected.marker,editType:"style"},text:s({},a.text,{description:["Sets the text elements associated with each sample value.","If a single string, the same string appears over","all the data points.","If an array of string, the items are mapped in order to the","this trace's (x,y) coordinates.","To be seen, trace `hoverinfo` must contain a *text* flag."].join(" ")}),hovertext:s({},a.hovertext,{description:"Same as `text`."}),hovertemplate:r({description:["N.B. This only has an effect when hovering on points."].join(" ")}),hoveron:{valType:"flaglist",flags:["boxes","points"],dflt:"boxes+points",role:"info",editType:"style",description:["Do the hover effects highlight individual boxes ","or sample points or both?"].join(" ")}}},715:function(e,t,o){"use strict";var a=o(380),i=o(381),n=o(382),r=o(432).handleGroupingDefaults,s=o(616),l=o(684);function d(e,t,o,n){function r(e){var t=0;return e&&e.length&&(t+=1,a.isArrayOrTypedArray(e[0])&&e[0].length&&(t+=1)),t}function d(t){return a.validate(e[t],l[t])}var c,p=o("y"),h=o("x");if("box"===t.type){var u=o("q1"),f=o("median"),m=o("q3");t._hasPreCompStats=u&&u.length&&f&&f.length&&m&&m.length,c=Math.min(a.minRowLength(u),a.minRowLength(f),a.minRowLength(m))}var y,x,v=r(p),b=r(h),g=v&&a.minRowLength(p),T=b&&a.minRowLength(h);if(t._hasPreCompStats)switch(String(b)+String(v)){case"00":var w=d("x0")||d("dx");y=(d("y0")||d("dy"))&&!w?"h":"v",x=c;break;case"10":y="v",x=Math.min(c,T);break;case"20":y="h",x=Math.min(c,h.length);break;case"01":y="h",x=Math.min(c,g);break;case"02":y="v",x=Math.min(c,p.length);break;case"12":y="v",x=Math.min(c,T,p.length);break;case"21":y="h",x=Math.min(c,h.length,g);break;case"11":x=0;break;case"22":var k,q=!1;for(k=0;k<h.length;k++)if("category"===s(h[k])){q=!0;break}if(q)y="v",x=Math.min(c,T,p.length);else{for(k=0;k<p.length;k++)if("category"===s(p[k])){q=!0;break}q?(y="h",x=Math.min(c,h.length,g)):(y="v",x=Math.min(c,T,p.length))}}else v>0?(y="v",x=b>0?Math.min(T,g):Math.min(g)):b>0?(y="h",x=Math.min(T)):x=0;if(x){t._length=x;var S=o("orientation",y);t._hasPreCompStats?"v"===S&&0===b?(o("x0",0),o("dx",1)):"h"===S&&0===v&&(o("y0",0),o("dy",1)):"v"===S&&0===b?o("x0"):"h"===S&&0===v&&o("y0"),i.getComponentMethod("calendars","handleTraceDefaults")(e,t,["x","y"],n)}else t.visible=!1}function c(e,t,o,i){var n=i.prefix,r=a.coerce2(e,t,l,"marker.outliercolor"),s=o("marker.line.outliercolor"),d="outliers";t._hasPreCompStats?d="all":(r||s)&&(d="suspectedoutliers");var c=o(n+"points",d);c?(o("jitter","all"===c?.3:0),o("pointpos","all"===c?-1.5:0),o("marker.symbol"),o("marker.opacity"),o("marker.size"),o("marker.color",t.line.color),o("marker.line.color"),o("marker.line.width"),"suspectedoutliers"===c&&(o("marker.line.outliercolor",t.marker.color),o("marker.line.outlierwidth")),o("selected.marker.color"),o("unselected.marker.color"),o("selected.marker.size"),o("unselected.marker.size"),o("text"),o("hovertext")):delete t.marker;var p=o("hoveron");"all"!==p&&-1===p.indexOf("points")||o("hovertemplate"),a.coerceSelectionMarkerOpacity(t,o)}e.exports={supplyDefaults:function(e,t,o,i){function r(o,i){return a.coerce(e,t,l,o,i)}if(d(e,t,r,i),!1!==t.visible){var s=t._hasPreCompStats;s&&(r("lowerfence"),r("upperfence")),r("line.color",(e.marker||{}).color||o),r("line.width"),r("fillcolor",n.addOpacity(t.line.color,.5));var p=!1;if(s){var h=r("mean"),u=r("sd");h&&h.length&&(p=!0,u&&u.length&&(p="sd"))}r("boxmean",p),r("whiskerwidth"),r("width"),r("quartilemethod");var f=!1;if(s){var m=r("notchspan");m&&m.length&&(f=!0)}else a.validate(e.notchwidth,l.notchwidth)&&(f=!0);r("notched",f)&&r("notchwidth"),c(e,t,r,{prefix:"box"})}},crossTraceDefaults:function(e,t){var o,i;function n(e){return a.coerce(i._input,i,l,e)}for(var s=0;s<e.length;s++){var d=(i=e[s]).type;"box"!==d&&"violin"!==d||(o=i._input,"group"===t[d+"mode"]&&r(o,i,t,n))}},handleSampleDefaults:d,handlePointsDefaults:c}},729:function(e,t,o){"use strict";var a=o(381),i=o(380),n=o(597);function r(e,t,o,i,n){for(var r=n+"Layout",s=!1,l=0;l<o.length;l++){var d=o[l];if(a.traceIs(d,r)){s=!0;break}}s&&(i(n+"mode"),i(n+"gap"),i(n+"groupgap"))}e.exports={supplyLayoutDefaults:function(e,t,o){r(0,0,o,(function(o,a){return i.coerce(e,t,n,o,a)}),"box")},_supply:r}},730:function(e,t,o){"use strict";var a=o(384),i=o(380),n=o(395).getAxisGroup,r=["v","h"];function s(e,t,o,r){var s,l,d,c=t.calcdata,p=t._fullLayout,h=r._id,u=h.charAt(0),f=[],m=0;for(s=0;s<o.length;s++)for(d=c[o[s]],l=0;l<d.length;l++)f.push(r.c2l(d[l].pos,!0)),m+=(d[l].pts2||[]).length;if(f.length){var y=i.distinctVals(f),x=y.minDiff/2;a.minDtick(r,y.minDiff,y.vals[0],!0);var v=p["violin"===e?"_numViolins":"_numBoxes"],b="group"===p[e+"mode"]&&v>1,g=1-p[e+"gap"],T=1-p[e+"groupgap"];for(s=0;s<o.length;s++){var w,k,q,S,M,j,A=(d=c[o[s]])[0].trace,P=d[0].t,_=A.width,D=A.side;if(_)w=k=S=_/2,q=0;else if(w=x,b){var L=n(p,r._id)+A.orientation,O=(p._alignmentOpts[L]||{})[A.alignmentgroup]||{},I=Object.keys(O.offsetGroups||{}).length,H=I||v;k=w*g*T/H,q=2*w*(((I?A._offsetIndex:P.num)+.5)/H-.5)*g,S=w*g/H}else k=w*g*T,q=0,S=w;P.dPos=w,P.bPos=q,P.bdPos=k,P.wHover=S;var Q,V,C,z,R,B,F=q+k,G=Boolean(_);if("positive"===D?(M=w*(_?1:.5),Q=F,j=Q=q):"negative"===D?(M=Q=q,j=w*(_?1:.5),V=F):(M=j=w,Q=V=F),(A.boxpoints||A.points)&&m>0){var N=A.pointpos,E=A.jitter,Z=A.marker.size/2,W=0;N+E>=0&&((W=F*(N+E))>M?(G=!0,R=Z,C=W):W>Q&&(R=Z,C=M)),W<=M&&(C=M);var K=0;N-E<=0&&((K=-F*(N-E))>j?(G=!0,B=Z,z=K):K>V&&(B=Z,z=j)),K<=j&&(z=j)}else C=M,z=j;var U=new Array(d.length);for(l=0;l<d.length;l++)U[l]=d[l].pos;A._extremes[h]=a.findExtremes(r,U,{padded:G,vpadminus:z,vpadplus:C,vpadLinearized:!0,ppadminus:{x:B,y:R}[u],ppadplus:{x:R,y:B}[u]})}}}e.exports={crossTraceCalc:function(e,t){for(var o=e.calcdata,a=t.xaxis,i=t.yaxis,n=0;n<r.length;n++){for(var l=r[n],d="h"===l?i:a,c=[],p=0;p<o.length;p++){var h=o[p],u=h[0].t,f=h[0].trace;!0!==f.visible||"box"!==f.type&&"candlestick"!==f.type||u.empty||(f.orientation||"v")!==l||f.xaxis!==a._id||f.yaxis!==i._id||c.push(p)}s("box",e,c,d)}},setPositionOffset:s}},731:function(e,t,o){"use strict";var a=o(383),i=o(380),n=o(386);function r(e,t,o,n){var r,s,l=t.pos,d=t.val,c=n.bPos,p=n.wdPos||0,h=n.bPosPxOffset||0,u=o.whiskerwidth||0,f=o.notched||!1,m=f?1-2*o.notchwidth:1;Array.isArray(n.bdPos)?(r=n.bdPos[0],s=n.bdPos[1]):(r=n.bdPos,s=n.bdPos);var y=e.selectAll("path.box").data("violin"!==o.type||o.box.visible?i.identity:[]);y.enter().append("path").style("vector-effect","non-scaling-stroke").attr("class","box"),y.exit().remove(),y.each((function(e){if(e.empty)return"M0,0Z";var t=l.c2l(e.pos+c,!0),n=l.l2p(t)+h,y=l.l2p(t-r)+h,x=l.l2p(t+s)+h,v=l.l2p(t-p)+h,b=l.l2p(t+p)+h,g=l.l2p(t-r*m)+h,T=l.l2p(t+s*m)+h,w=d.c2p(e.q1,!0),k=d.c2p(e.q3,!0),q=i.constrain(d.c2p(e.med,!0),Math.min(w,k)+1,Math.max(w,k)-1),S=void 0===e.lf||!1===o.boxpoints,M=d.c2p(S?e.min:e.lf,!0),j=d.c2p(S?e.max:e.uf,!0),A=d.c2p(e.ln,!0),P=d.c2p(e.un,!0);"h"===o.orientation?a.select(this).attr("d","M"+q+","+g+"V"+T+"M"+w+","+y+"V"+x+(f?"H"+A+"L"+q+","+T+"L"+P+","+x:"")+"H"+k+"V"+y+(f?"H"+P+"L"+q+","+g+"L"+A+","+y:"")+"ZM"+w+","+n+"H"+M+"M"+k+","+n+"H"+j+(0===u?"":"M"+M+","+v+"V"+b+"M"+j+","+v+"V"+b)):a.select(this).attr("d","M"+g+","+q+"H"+T+"M"+y+","+w+"H"+x+(f?"V"+A+"L"+T+","+q+"L"+x+","+P:"")+"V"+k+"H"+y+(f?"V"+P+"L"+g+","+q+"L"+y+","+A:"")+"ZM"+n+","+w+"V"+M+"M"+n+","+k+"V"+j+(0===u?"":"M"+v+","+M+"H"+b+"M"+v+","+j+"H"+b))}))}function s(e,t,o,a){var r=t.x,s=t.y,l=a.bdPos,d=a.bPos,c=o.boxpoints||o.points;i.seedPseudoRandom();var p=e.selectAll("g.points").data(c?function(e){return e.forEach((function(e){e.t=a,e.trace=o})),e}:[]);p.enter().append("g").attr("class","points"),p.exit().remove();var h=p.selectAll("path").data((function(e){var t,a,n=e.pts2,r=Math.max((e.max-e.min)/10,e.q3-e.q1),s=1e-9*r,p=.01*r,h=[],u=0;if(o.jitter){if(0===r)for(u=1,h=new Array(n.length),t=0;t<n.length;t++)h[t]=1;else for(t=0;t<n.length;t++){var f=Math.max(0,t-5),m=n[f].v,y=Math.min(n.length-1,t+5),x=n[y].v;"all"!==c&&(n[t].v<e.lf?x=Math.min(x,e.lf):m=Math.max(m,e.uf));var v=Math.sqrt(p*(y-f)/(x-m+s))||0;v=i.constrain(Math.abs(v),0,1),h.push(v),u=Math.max(v,u)}a=2*o.jitter/(u||1)}for(t=0;t<n.length;t++){var b=n[t],g=b.v,T=o.jitter?a*h[t]*(i.pseudoRandom()-.5):0,w=e.pos+d+l*(o.pointpos+T);"h"===o.orientation?(b.y=w,b.x=g):(b.x=w,b.y=g),"suspectedoutliers"===c&&g<e.uo&&g>e.lo&&(b.so=!0)}return n}));h.enter().append("path").classed("point",!0),h.exit().remove(),h.call(n.translatePoints,r,s)}function l(e,t,o,n){var r,s,l=t.pos,d=t.val,c=n.bPos,p=n.bPosPxOffset||0,h=o.boxmean||(o.meanline||{}).visible;Array.isArray(n.bdPos)?(r=n.bdPos[0],s=n.bdPos[1]):(r=n.bdPos,s=n.bdPos);var u=e.selectAll("path.mean").data("box"===o.type&&o.boxmean||"violin"===o.type&&o.box.visible&&o.meanline.visible?i.identity:[]);u.enter().append("path").attr("class","mean").style({fill:"none","vector-effect":"non-scaling-stroke"}),u.exit().remove(),u.each((function(e){var t=l.c2l(e.pos+c,!0),i=l.l2p(t)+p,n=l.l2p(t-r)+p,u=l.l2p(t+s)+p,f=d.c2p(e.mean,!0),m=d.c2p(e.mean-e.sd,!0),y=d.c2p(e.mean+e.sd,!0);"h"===o.orientation?a.select(this).attr("d","M"+f+","+n+"V"+u+("sd"===h?"m0,0L"+m+","+i+"L"+f+","+n+"L"+y+","+i+"Z":"")):a.select(this).attr("d","M"+n+","+f+"H"+u+("sd"===h?"m0,0L"+i+","+m+"L"+n+","+f+"L"+i+","+y+"Z":""))}))}e.exports={plot:function(e,t,o,n){var d=t.xaxis,c=t.yaxis;i.makeTraceGroups(n,o,"trace boxes").each((function(e){var t,o,i=a.select(this),n=e[0],p=n.t,h=n.trace;(p.wdPos=p.bdPos*h.whiskerwidth,!0!==h.visible||p.empty)?i.remove():("h"===h.orientation?(t=c,o=d):(t=d,o=c),r(i,{pos:t,val:o},h,p),s(i,{x:d,y:c},h,p),l(i,{pos:t,val:o},h,p))}))},plotBoxAndWhiskers:r,plotPoints:s,plotBoxMean:l}},758:function(e,t,o){"use strict";var a=o(383),i=o(382),n=o(386);e.exports={style:function(e,t,o){var r=o||a.select(e).selectAll("g.trace.boxes");r.style("opacity",(function(e){return e[0].trace.opacity})),r.each((function(t){var o=a.select(this),r=t[0].trace,s=r.line.width;function l(e,t,o,a){e.style("stroke-width",t+"px").call(i.stroke,o).call(i.fill,a)}var d=o.selectAll("path.box");if("candlestick"===r.type)d.each((function(e){if(!e.empty){var t=a.select(this),o=r[e.dir];l(t,o.line.width,o.line.color,o.fillcolor),t.style("opacity",r.selectedpoints&&!e.selected?.3:1)}}));else{l(d,s,r.line.color,r.fillcolor),o.selectAll("path.mean").style({"stroke-width":s,"stroke-dasharray":2*s+"px,"+s+"px"}).call(i.stroke,r.line.color);var c=o.selectAll("path.point");n.pointStyle(c,r,e)}}))},styleOnSelect:function(e,t,o){var a=t[0].trace,i=o.selectAll("path.point");a.selectedpoints?n.selectedPointStyle(i,a):n.pointStyle(i,a,e)}}},926:function(e,t,o){"use strict";var a=o(385),i=o(384),n=o(380),r=o(390).BADNUM,s=n._;e.exports=function(e,t){var o,l,x,v,b,g,T=e._fullLayout,w=i.getFromId(e,t.xaxis||"x"),k=i.getFromId(e,t.yaxis||"y"),q=[],S="violin"===t.type?"_numViolins":"_numBoxes";"h"===t.orientation?(x=w,v="x",b=k,g="y"):(x=k,v="y",b=w,g="x");var M,j,A,P,_,D,L=function(e,t,o,i){var r,s=t+"0"in e,l="d"+t in e;if(t in e||s&&l)return o.makeCalcdata(e,t);r=s?e[t+"0"]:"name"in e&&("category"===o.type||a(e.name)&&-1!==["linear","log"].indexOf(o.type)||n.isDateTime(e.name)&&"date"===o.type)?e.name:i;for(var d="multicategory"===o.type?o.r2c_just_indices(r):o.d2c(r,0,e[t+"calendar"]),c=e._length,p=new Array(c),h=0;h<c;h++)p[h]=d;return p}(t,g,b,T[S]),O=n.distinctVals(L),I=O.vals,H=O.minDiff/2,Q="all"===(t.boxpoints||t.points)?n.identity:function(e){return e.v<M.lf||e.v>M.uf};if(t._hasPreCompStats){var V=t[v],C=function(e){return x.d2c((t[e]||[])[o])},z=1/0,R=-1/0;for(o=0;o<t._length;o++){var B=L[o];if(a(B)){if((M={}).pos=M[g]=B,M.q1=C("q1"),M.med=C("median"),M.q3=C("q3"),j=[],V&&n.isArrayOrTypedArray(V[o]))for(l=0;l<V[o].length;l++)(D=x.d2c(V[o][l]))!==r&&(d(_={v:D,i:[o,l]},t,[o,l]),j.push(_));if(M.pts=j.sort(c),P=(A=M[v]=j.map(p)).length,M.med!==r&&M.q1!==r&&M.q3!==r&&M.med>=M.q1&&M.q3>=M.med){var F=C("lowerfence");M.lf=F!==r&&F<=M.q1?F:h(M,A,P);var G=C("upperfence");M.uf=G!==r&&G>=M.q3?G:u(M,A,P);var N=C("mean");M.mean=N!==r?N:P?n.mean(A,P):(M.q1+M.q3)/2;var E=C("sd");M.sd=N!==r&&E>=0?E:P?n.stdev(A,P,M.mean):M.q3-M.q1,M.lo=f(M),M.uo=m(M);var Z=C("notchspan");Z=Z!==r&&Z>0?Z:y(M,P),M.ln=M.med-Z,M.un=M.med+Z;var W=M.lf,K=M.uf;t.boxpoints&&A.length&&(W=Math.min(W,A[0]),K=Math.max(K,A[P-1])),t.notched&&(W=Math.min(W,M.ln),K=Math.max(K,M.un)),M.min=W,M.max=K}else{var U;n.warn(["Invalid input - make sure that q1 <= median <= q3","q1 = "+M.q1,"median = "+M.med,"q3 = "+M.q3].join("\n")),U=M.med!==r?M.med:M.q1!==r?M.q3!==r?(M.q1+M.q3)/2:M.q1:M.q3!==r?M.q3:0,M.med=U,M.q1=M.q3=U,M.lf=M.uf=U,M.mean=M.sd=U,M.ln=M.un=U,M.min=M.max=U}z=Math.min(z,M.min),R=Math.max(R,M.max),M.pts2=j.filter(Q),q.push(M)}}t._extremes[x._id]=i.findExtremes(x,[z,R],{padded:!0})}else{var J=x.makeCalcdata(t,v),X=function(e,t){for(var o=e.length,a=new Array(o+1),i=0;i<o;i++)a[i]=e[i]-t;return a[o]=e[o-1]+t,a}(I,H),Y=I.length,$=function(e){for(var t=new Array(e),o=0;o<e;o++)t[o]=[];return t}(Y);for(o=0;o<t._length;o++)if(D=J[o],a(D)){var ee=n.findBin(L[o],X);ee>=0&&ee<Y&&(d(_={v:D,i:o},t,o),$[ee].push(_))}var te=1/0,oe=-1/0,ae=t.quartilemethod,ie="exclusive"===ae,ne="inclusive"===ae;for(o=0;o<Y;o++)if($[o].length>0){var re,se;if((M={}).pos=M[g]=I[o],j=M.pts=$[o].sort(c),P=(A=M[v]=j.map(p)).length,M.min=A[0],M.max=A[P-1],M.mean=n.mean(A,P),M.sd=n.stdev(A,P,M.mean),M.med=n.interp(A,.5),P%2&&(ie||ne))ie?(re=A.slice(0,P/2),se=A.slice(P/2+1)):ne&&(re=A.slice(0,P/2+1),se=A.slice(P/2)),M.q1=n.interp(re,.5),M.q3=n.interp(se,.5);else M.q1=n.interp(A,.25),M.q3=n.interp(A,.75);M.lf=h(M,A,P),M.uf=u(M,A,P),M.lo=f(M),M.uo=m(M);var le=y(M,P);M.ln=M.med-le,M.un=M.med+le,te=Math.min(te,M.ln),oe=Math.max(oe,M.un),M.pts2=j.filter(Q),q.push(M)}t._extremes[x._id]=i.findExtremes(x,t.notched?J.concat([te,oe]):J,{padded:!0})}return function(e,t){if(n.isArrayOrTypedArray(t.selectedpoints))for(var o=0;o<e.length;o++){for(var a=e[o].pts||[],i={},r=0;r<a.length;r++)i[a[r].i]=r;n.tagSelected(a,t,i)}}(q,t),q.length>0?(q[0].t={num:T[S],dPos:H,posLetter:g,valLetter:v,labels:{med:s(e,"median:"),min:s(e,"min:"),q1:s(e,"q1:"),q3:s(e,"q3:"),max:s(e,"max:"),mean:"sd"===t.boxmean?s(e,"mean ± σ:"):s(e,"mean:"),lf:s(e,"lower fence:"),uf:s(e,"upper fence:")}},T[S]++,q):[{t:{empty:!0}}]};var l={text:"tx",hovertext:"htx"};function d(e,t,o){for(var a in l)n.isArrayOrTypedArray(t[a])&&(Array.isArray(o)?n.isArrayOrTypedArray(t[a][o[0]])&&(e[l[a]]=t[a][o[0]][o[1]]):e[l[a]]=t[a][o])}function c(e,t){return e.v-t.v}function p(e){return e.v}function h(e,t,o){return 0===o?e.q1:Math.min(e.q1,t[Math.min(n.findBin(2.5*e.q1-1.5*e.q3,t,!0)+1,o-1)])}function u(e,t,o){return 0===o?e.q3:Math.max(e.q3,t[Math.max(n.findBin(2.5*e.q3-1.5*e.q1,t),0)])}function f(e){return 4*e.q1-3*e.q3}function m(e){return 4*e.q3-3*e.q1}function y(e,t){return 0===t?0:1.57*(e.q3-e.q1)/Math.sqrt(t)}},927:function(e,t,o){"use strict";var a=o(384),i=o(380),n=o(397),r=o(382),s=i.fillText;function l(e,t,o,s){var l,d,c,p,h,u,f,m,y,x,v,b,g,T,w=e.cd,k=e.xa,q=e.ya,S=w[0].trace,M=w[0].t,j="violin"===S.type,A=[],P=M.bdPos,_=M.wHover,D=function(e){return c.c2l(e.pos)+M.bPos-c.c2l(u)};j&&"both"!==S.side?("positive"===S.side&&(y=function(e){var t=D(e);return n.inbox(t,t+_,x)},b=P,g=0),"negative"===S.side&&(y=function(e){var t=D(e);return n.inbox(t-_,t,x)},b=0,g=P)):(y=function(e){var t=D(e);return n.inbox(t-_,t+_,x)},b=g=P),T=j?function(e){return n.inbox(e.span[0]-h,e.span[1]-h,x)}:function(e){return n.inbox(e.min-h,e.max-h,x)},"h"===S.orientation?(h=t,u=o,f=T,m=y,l="y",c=q,d="x",p=k):(h=o,u=t,f=y,m=T,l="x",c=k,d="y",p=q);var L=Math.min(1,P/Math.abs(c.r2c(c.range[1])-c.r2c(c.range[0])));function O(e){return(f(e)+m(e))/2}x=e.maxHoverDistance-L,v=e.maxSpikeDistance-L;var I=n.getDistanceFunction(s,f,m,O);if(n.getClosest(w,I,e),!1===e.index)return[];var H=w[e.index],Q=S.line.color,V=(S.marker||{}).color;r.opacity(Q)&&S.line.width?e.color=Q:r.opacity(V)&&S.boxpoints?e.color=V:e.color=S.fillcolor,e[l+"0"]=c.c2p(H.pos+M.bPos-g,!0),e[l+"1"]=c.c2p(H.pos+M.bPos+b,!0),e[l+"LabelVal"]=H.pos;var C=l+"Spike";e.spikeDistance=O(H)*v/x,e[C]=c.c2p(H.pos,!0);var z={},R=["med","q1","q3","min","max"];(S.boxmean||(S.meanline||{}).visible)&&R.push("mean"),(S.boxpoints||S.points)&&R.push("lf","uf");for(var B=0;B<R.length;B++){var F=R[B];if(F in H&&!(H[F]in z)){z[H[F]]=!0;var G=H[F],N=p.c2p(G,!0),E=i.extendFlat({},e);E.attr=F,E[d+"0"]=E[d+"1"]=N,E[d+"LabelVal"]=G,E[d+"Label"]=(M.labels?M.labels[F]+" ":"")+a.hoverLabelText(p,G),E.hoverOnBox=!0,"mean"===F&&"sd"in H&&"sd"===S.boxmean&&(E[d+"err"]=H.sd),e.name="",e.spikeDistance=void 0,e[C]=void 0,E.hovertemplate=!1,A.push(E)}}return A}function d(e,t,o){for(var a,r,l,d=e.cd,c=e.xa,p=e.ya,h=d[0].trace,u=c.c2p(t),f=p.c2p(o),m=n.quadrature((function(e){var t=Math.max(3,e.mrc||0);return Math.max(Math.abs(c.c2p(e.x)-u)-t,1-3/t)}),(function(e){var t=Math.max(3,e.mrc||0);return Math.max(Math.abs(p.c2p(e.y)-f)-t,1-3/t)})),y=!1,x=0;x<d.length;x++){r=d[x];for(var v=0;v<(r.pts||[]).length;v++){var b=m(l=r.pts[v]);b<=e.distance&&(e.distance=b,y=[x,v])}}if(!y)return!1;l=(r=d[y[0]]).pts[y[1]];var g,T=c.c2p(l.x,!0),w=p.c2p(l.y,!0),k=l.mrc||1;return a=i.extendFlat({},e,{index:l.i,color:(h.marker||{}).color,name:h.name,x0:T-k,x1:T+k,y0:w-k,y1:w+k,spikeDistance:e.distance,hovertemplate:h.hovertemplate}),"h"===h.orientation?(g=p,a.xLabelVal=l.x,a.yLabelVal=r.pos):(g=c,a.xLabelVal=r.pos,a.yLabelVal=l.y),a[g._id.charAt(0)+"Spike"]=g.c2p(r.pos,!0),s(l,h,a),a}e.exports={hoverPoints:function(e,t,o,a){var i,n=e.cd[0].trace.hoveron,r=[];return-1!==n.indexOf("boxes")&&(r=r.concat(l(e,t,o,a))),-1!==n.indexOf("points")&&(i=d(e,t,o)),"closest"===a?i?[i]:r:i?(r.push(i),r):r},hoverOnBoxes:l,hoverOnPoints:d}},928:function(e,t,o){"use strict";e.exports=function(e,t){var o,a,i=e.cd,n=e.xaxis,r=e.yaxis,s=[];if(!1===t)for(o=0;o<i.length;o++)for(a=0;a<(i[o].pts||[]).length;a++)i[o].pts[a].selected=0;else for(o=0;o<i.length;o++)for(a=0;a<(i[o].pts||[]).length;a++){var l=i[o].pts[a],d=n.c2p(l.x),c=r.c2p(l.y);t.contains([d,c],null,l.i,e)?(s.push({pointNumber:l.i,x:n.c2d(l.x),y:r.c2d(l.y)}),l.selected=1):l.selected=0}return s}}}]);