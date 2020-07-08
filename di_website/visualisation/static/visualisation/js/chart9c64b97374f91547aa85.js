(window.webpackJsonp=window.webpackJsonp||[]).push([[7],{1125:function(e,t,a){"use strict";var i=a(214).appendArrayMultiPointValues;e.exports=function(e,t){var a={curveNumber:t.index,pointNumbers:e.pts,data:t._input,fullData:t,label:e.label,color:e.color,value:e.v,percent:e.percent,text:e.text,v:e.v};return 1===e.pts.length&&(a.pointNumber=a.i=e.pts[0]),i(a,t,e.pts),"funnelarea"===t.type&&(delete a.v,delete a.i),a}},623:function(e,t,a){"use strict";var i=a(32).extendFlat;t.attributes=function(e,t){t=t||{};var a={valType:"info_array",role:"info",editType:(e=e||{}).editType,items:[{valType:"number",min:0,max:1,editType:e.editType},{valType:"number",min:0,max:1,editType:e.editType}],dflt:[0,1]},o=e.name?e.name+" ":"",r=e.trace?"trace ":"subplot ",n=t.description?" "+t.description:"",l={x:i({},a,{description:["Sets the horizontal domain of this ",o,r,"(in plot fraction).",n].join("")}),y:i({},a,{description:["Sets the vertical domain of this ",o,r,"(in plot fraction).",n].join("")}),editType:e.editType};return e.noGridCell||(l.row={valType:"integer",min:0,dflt:0,role:"info",editType:e.editType,description:["If there is a layout grid, use the domain ","for this row in the grid for this ",o,r,".",n].join("")},l.column={valType:"integer",min:0,dflt:0,role:"info",editType:e.editType,description:["If there is a layout grid, use the domain ","for this column in the grid for this ",o,r,".",n].join("")}),l},t.defaults=function(e,t,a,i){var o=i&&i.x||[0,1],r=i&&i.y||[0,1],n=t.grid;if(n){var l=a("domain.column");void 0!==l&&(l<n.columns?o=n._domains.x[l]:delete e.domain.column);var s=a("domain.row");void 0!==s&&(s<n.rows?r=n._domains.y[s]:delete e.domain.row)}var c=a("domain.x",o),d=a("domain.y",r);c[0]<c[1]||(e.domain.x=o.slice()),d[0]<d[1]||(e.domain.y=r.slice())}},626:function(e,t,a){"use strict";var i=a(206),o=a(150).hovertemplateAttrs,r=a(150).texttemplateAttrs,n=a(111),l=a(46),s=a(656),c=a(32).extendFlat,d=l({editType:"calc",arrayOk:!0,colorEditType:"style",description:""}),p=c({},i.marker.line.width,{dflt:0}),f=c({width:p,editType:"calc"},n("marker.line")),h=c({line:f,editType:"calc"},n("marker"),{opacity:{valType:"number",arrayOk:!0,dflt:1,min:0,max:1,role:"style",editType:"style",description:"Sets the opacity of the bars."}});e.exports={x:i.x,x0:i.x0,dx:i.dx,y:i.y,y0:i.y0,dy:i.dy,text:i.text,texttemplate:r({editType:"plot"},{keys:s.eventDataKeys}),hovertext:i.hovertext,hovertemplate:o({},{keys:s.eventDataKeys}),textposition:{valType:"enumerated",role:"info",values:["inside","outside","auto","none"],dflt:"none",arrayOk:!0,editType:"calc",description:["Specifies the location of the `text`.","*inside* positions `text` inside, next to the bar end","(rotated and scaled if needed).","*outside* positions `text` outside, next to the bar end","(scaled if needed), unless there is another bar stacked on","this one, then the text gets pushed inside.","*auto* tries to position `text` inside the bar, but if","the bar is too small and no bar is stacked on this one","the text is moved outside."].join(" ")},insidetextanchor:{valType:"enumerated",values:["end","middle","start"],dflt:"end",role:"info",editType:"plot",description:["Determines if texts are kept at center or start/end points in `textposition` *inside* mode."].join(" ")},textangle:{valType:"angle",dflt:"auto",role:"info",editType:"plot",description:["Sets the angle of the tick labels with respect to the bar.","For example, a `tickangle` of -90 draws the tick labels","vertically. With *auto* the texts may automatically be","rotated to fit with the maximum size in bars."].join(" ")},textfont:c({},d,{description:"Sets the font used for `text`."}),insidetextfont:c({},d,{description:"Sets the font used for `text` lying inside the bar."}),outsidetextfont:c({},d,{description:"Sets the font used for `text` lying outside the bar."}),constraintext:{valType:"enumerated",values:["inside","outside","both","none"],role:"info",dflt:"both",editType:"calc",description:["Constrain the size of text inside or outside a bar to be no","larger than the bar itself."].join(" ")},cliponaxis:c({},i.cliponaxis,{description:["Determines whether the text nodes","are clipped about the subplot axes.","To show the text nodes above axis lines and tick labels,","make sure to set `xaxis.layer` and `yaxis.layer` to *below traces*."].join(" ")}),orientation:{valType:"enumerated",role:"info",values:["v","h"],editType:"calc+clearAxisTypes",description:["Sets the orientation of the bars.","With *v* (*h*), the value of the each bar spans","along the vertical (horizontal)."].join(" ")},base:{valType:"any",dflt:null,arrayOk:!0,role:"info",editType:"calc",description:["Sets where the bar base is drawn (in position axis units).","In *stack* or *relative* barmode,","traces that set *base* will be excluded","and drawn in *overlay* mode instead."].join(" ")},offset:{valType:"number",dflt:null,arrayOk:!0,role:"info",editType:"calc",description:["Shifts the position where the bar is drawn","(in position axis units).","In *group* barmode,","traces that set *offset* will be excluded","and drawn in *overlay* mode instead."].join(" ")},width:{valType:"number",dflt:null,min:0,arrayOk:!0,role:"info",editType:"calc",description:["Sets the bar width (in position axis units)."].join(" ")},marker:h,offsetgroup:{valType:"string",role:"info",dflt:"",editType:"calc",description:["Set several traces linked to the same position axis","or matching axes to the same","offsetgroup where bars of the same position coordinate will line up."].join(" ")},alignmentgroup:{valType:"string",role:"info",dflt:"",editType:"calc",description:["Set several traces linked to the same position axis","or matching axes to the same","alignmentgroup. This controls whether bars compute their positional","range dependently or independently."].join(" ")},selected:{marker:{opacity:i.selected.marker.opacity,color:i.selected.marker.color,editType:"style"},textfont:i.selected.textfont,editType:"style"},unselected:{marker:{opacity:i.unselected.marker.opacity,color:i.unselected.marker.color,editType:"style"},textfont:i.unselected.textfont,editType:"style"},r:i.r,t:i.t,_deprecated:{bardir:{valType:"enumerated",role:"info",editType:"calc",values:["v","h"],description:"Renamed to `orientation`."}}}},636:function(e,t,a){"use strict";var i=a(24),o=a(6);function r(e){return"_"+e+"Text_minsize"}e.exports={recordMinTextSize:function(e,t,a){if(a.uniformtext.mode){var i=r(e),o=a.uniformtext.minsize,n=t.scale*t.fontSize;t.hide=n<o,a[i]=a[i]||1/0,t.hide||(a[i]=Math.min(a[i],Math.max(n,o)))}},clearMinTextSize:function(e,t){t[r(e)]=void 0},resizeText:function(e,t,a){var r=e._fullLayout,n=r["_"+a+"Text_minsize"];if(n){var l,s="hide"===r.uniformtext.mode;switch(a){case"funnelarea":case"pie":case"sunburst":l="g.slice";break;case"treemap":l="g.slice, g.pathbar";break;default:l="g.points > g.point"}t.selectAll(l).each((function(e){var t=e.transform;t&&(t.scale=s&&t.hide?0:n/t.fontSize,i.select(this).select("text").attr("transform",o.getTextTransform(t)))}))}}}},644:function(e,t,a){"use strict";var i=a(6),o=a(57),r=a(23),n=a(646),l=a(692),s=a(110).getAxisGroup,c=a(626),d=i.coerceFont;function p(e,t,a,i){var o=t.orientation,r=t[{v:"x",h:"y"}[o]+"axis"],n=s(a,r)+o,l=a._alignmentOpts||{},c=i("alignmentgroup"),d=l[n];d||(d=l[n]={});var p=d[c];p?p.traces.push(t):p=d[c]={traces:[t],alignmentIndex:Object.keys(d).length,offsetGroups:{}};var f=i("offsetgroup"),h=p.offsetGroups,u=h[f];f&&(u||(u=h[f]={offsetIndex:Object.keys(h).length}),t._offsetIndex=u.offsetIndex)}function f(e,t,a,o,r,n){var l=!(!1===(n=n||{}).moduleHasSelected),s=!(!1===n.moduleHasUnselected),c=!(!1===n.moduleHasConstrain),p=!(!1===n.moduleHasCliponaxis),f=!(!1===n.moduleHasTextangle),h=!(!1===n.moduleHasInsideanchor),u=!!n.hasPathbar,x=Array.isArray(r)||"auto"===r,m=x||"inside"===r,v=x||"outside"===r;if(m||v){var y=d(o,"textfont",a.font),g=i.extendFlat({},y),b=!(e.textfont&&e.textfont.color);if(b&&delete g.color,d(o,"insidetextfont",g),u){var T=i.extendFlat({},y);b&&delete T.color,d(o,"pathbar.textfont",T)}v&&d(o,"outsidetextfont",y),l&&o("selected.textfont.color"),s&&o("unselected.textfont.color"),c&&o("constraintext"),p&&o("cliponaxis"),f&&o("textangle"),o("texttemplate")}m&&h&&o("insidetextanchor")}e.exports={supplyDefaults:function(e,t,a,s){function d(a,o){return i.coerce(e,t,c,a,o)}if(n(e,t,s,d)){d("orientation",t.x&&!t.y?"h":"v"),d("base"),d("offset"),d("width"),d("text"),d("hovertext"),d("hovertemplate");var p=d("textposition");f(e,t,s,d,p,{moduleHasSelected:!0,moduleHasUnselected:!0,moduleHasConstrain:!0,moduleHasCliponaxis:!0,moduleHasTextangle:!0,moduleHasInsideanchor:!0}),l(e,t,d,a,s);var h=(t.marker.line||{}).color,u=r.getComponentMethod("errorbars","supplyDefaults");u(e,t,h||o.defaultLine,{axis:"y"}),u(e,t,h||o.defaultLine,{axis:"x",inherit:"y"}),i.coerceSelectionMarkerOpacity(t,d)}else t.visible=!1},crossTraceDefaults:function(e,t){var a;function o(e){return i.coerce(a._input,a,c,e)}if("group"===t.barmode)for(var r=0;r<e.length;r++)"bar"===(a=e[r]).type&&(a._input,p(0,a,t,o))},handleGroupingDefaults:p,handleText:f}},646:function(e,t,a){"use strict";var i=a(6),o=a(23);e.exports=function(e,t,a,r){var n,l=r("x"),s=r("y");if(o.getComponentMethod("calendars","handleTraceDefaults")(e,t,["x","y"],a),l){var c=i.minRowLength(l);s?n=Math.min(c,i.minRowLength(s)):(n=c,r("y0"),r("dy"))}else{if(!s)return 0;n=i.minRowLength(s),r("x0"),r("dx")}return t._length=n,n}},656:function(e,t,a){"use strict";e.exports={TEXTPAD:3,eventDataKeys:["value","label"]}},692:function(e,t,a){"use strict";var i=a(57),o=a(79).hasColorscale,r=a(151);e.exports=function(e,t,a,n,l){a("marker.color",n),o(e,"marker")&&r(e,t,l,a,{prefix:"marker.",cLetter:"c"}),a("marker.line.color",i.defaultLine),o(e,"marker.line")&&r(e,t,l,a,{prefix:"marker.line.",cLetter:"c"}),a("marker.line.width"),a("marker.opacity"),a("selected.marker.color"),a("unselected.marker.color")}},768:function(e,t,a){"use strict";var i=a(59),o=a(623).attributes,r=a(46),n=a(112),l=a(150).hovertemplateAttrs,s=a(150).texttemplateAttrs,c=a(32).extendFlat,d=r({editType:"plot",arrayOk:!0,colorEditType:"plot",description:"Sets the font used for `textinfo`."});e.exports={labels:{valType:"data_array",editType:"calc",description:["Sets the sector labels.","If `labels` entries are duplicated, we sum associated `values`","or simply count occurrences if `values` is not provided.","For other array attributes (including color) we use the first","non-empty entry among all occurrences of the label."].join(" ")},label0:{valType:"number",role:"info",dflt:0,editType:"calc",description:["Alternate to `labels`.","Builds a numeric set of labels.","Use with `dlabel`","where `label0` is the starting label and `dlabel` the step."].join(" ")},dlabel:{valType:"number",role:"info",dflt:1,editType:"calc",description:"Sets the label step. See `label0` for more info."},values:{valType:"data_array",editType:"calc",description:["Sets the values of the sectors.","If omitted, we count occurrences of each label."].join(" ")},marker:{colors:{valType:"data_array",editType:"calc",description:["Sets the color of each sector.","If not specified, the default trace color set is used","to pick the sector colors."].join(" ")},line:{color:{valType:"color",role:"style",dflt:n.defaultLine,arrayOk:!0,editType:"style",description:["Sets the color of the line enclosing each sector."].join(" ")},width:{valType:"number",role:"style",min:0,dflt:0,arrayOk:!0,editType:"style",description:["Sets the width (in px) of the line enclosing each sector."].join(" ")},editType:"calc"},editType:"calc"},text:{valType:"data_array",editType:"plot",description:["Sets text elements associated with each sector.","If trace `textinfo` contains a *text* flag, these elements will be seen","on the chart.","If trace `hoverinfo` contains a *text* flag and *hovertext* is not set,","these elements will be seen in the hover labels."].join(" ")},hovertext:{valType:"string",role:"info",dflt:"",arrayOk:!0,editType:"style",description:["Sets hover text elements associated with each sector.","If a single string, the same string appears for","all data points.","If an array of string, the items are mapped in order of","this trace's sectors.","To be seen, trace `hoverinfo` must contain a *text* flag."].join(" ")},scalegroup:{valType:"string",role:"info",dflt:"",editType:"calc",description:["If there are multiple pie charts that should be sized according to","their totals, link them by providing a non-empty group id here","shared by every trace in the same group."].join(" ")},textinfo:{valType:"flaglist",role:"info",flags:["label","text","value","percent"],extras:["none"],editType:"calc",description:["Determines which trace information appear on the graph."].join(" ")},hoverinfo:c({},i.hoverinfo,{flags:["label","text","value","percent","name"]}),hovertemplate:l({},{keys:["label","color","value","percent","text"]}),texttemplate:s({editType:"plot"},{keys:["label","color","value","percent","text"]}),textposition:{valType:"enumerated",role:"info",values:["inside","outside","auto","none"],dflt:"auto",arrayOk:!0,editType:"plot",description:["Specifies the location of the `textinfo`."].join(" ")},textfont:c({},d,{description:"Sets the font used for `textinfo`."}),insidetextorientation:{valType:"enumerated",role:"info",values:["horizontal","radial","tangential","auto"],dflt:"auto",editType:"plot",description:["Controls the orientation of the text inside chart sectors.","When set to *auto*, text may be oriented in any direction in order","to be as big as possible in the middle of a sector.","The *horizontal* option orients text to be parallel with the bottom","of the chart, and may make text smaller in order to achieve that goal.","The *radial* option orients text along the radius of the sector.","The *tangential* option orients text perpendicular to the radius of the sector."].join(" ")},insidetextfont:c({},d,{description:"Sets the font used for `textinfo` lying inside the sector."}),outsidetextfont:c({},d,{description:"Sets the font used for `textinfo` lying outside the sector."}),automargin:{valType:"boolean",dflt:!1,role:"info",editType:"plot",description:["Determines whether outside text labels can push the margins."].join(" ")},title:{text:{valType:"string",dflt:"",role:"info",editType:"plot",description:["Sets the title of the chart.","If it is empty, no title is displayed.","Note that before the existence of `title.text`, the title's","contents used to be defined as the `title` attribute itself.","This behavior has been deprecated."].join(" ")},font:c({},d,{description:["Sets the font used for `title`.","Note that the title's font used to be set","by the now deprecated `titlefont` attribute."].join(" ")}),position:{valType:"enumerated",values:["top left","top center","top right","middle center","bottom left","bottom center","bottom right"],role:"info",editType:"plot",description:["Specifies the location of the `title`.","Note that the title's position used to be set","by the now deprecated `titleposition` attribute."].join(" ")},editType:"plot"},domain:o({name:"pie",trace:!0,editType:"calc"}),hole:{valType:"number",role:"style",min:0,max:1,dflt:0,editType:"calc",description:["Sets the fraction of the radius to cut out of the pie.","Use this to make a donut chart."].join(" ")},sort:{valType:"boolean",role:"style",dflt:!0,editType:"calc",description:["Determines whether or not the sectors are reordered","from largest to smallest."].join(" ")},direction:{valType:"enumerated",values:["clockwise","counterclockwise"],role:"style",dflt:"counterclockwise",editType:"calc",description:["Specifies the direction at which succeeding sectors follow","one another."].join(" ")},rotation:{valType:"number",role:"style",min:-360,max:360,dflt:0,editType:"calc",description:["Instead of the first slice starting at 12 o'clock,","rotate to some other angle."].join(" ")},pull:{valType:"number",role:"style",min:0,max:1,dflt:0,arrayOk:!0,editType:"calc",description:["Sets the fraction of larger radius to pull the sectors","out from the center. This can be a constant","to pull all slices apart from each other equally","or an array to highlight one or more slices."].join(" ")},_deprecated:{title:{valType:"string",dflt:"",role:"info",editType:"calc",description:["Deprecated in favor of `title.text`.","Note that value of `title` is no longer a simple","*string* but a set of sub-attributes."].join(" ")},titlefont:c({},d,{description:"Deprecated in favor of `title.font`."}),titleposition:{valType:"enumerated",values:["top left","top center","top right","middle center","bottom left","bottom center","bottom right"],role:"info",editType:"calc",description:"Deprecated in favor of `title.position`."}}}},789:function(e,t,a){"use strict";var i=a(12),o=a(60),r=a(57),n={};function l(e){return function(t,a){return!!t&&(!!(t=o(t)).isValid()&&(t=r.addOpacity(t,t.getAlpha()),e[a]||(e[a]=t),t))}}function s(e,t){var a,i=JSON.stringify(e),r=t[i];if(!r){for(r=e.slice(),a=0;a<e.length;a++)r.push(o(e[a]).lighten(20).toHexString());for(a=0;a<e.length;a++)r.push(o(e[a]).darken(20).toHexString());t[i]=r}return r}e.exports={calc:function(e,t){var a,o,r=[],n=e._fullLayout,s=n.hiddenlabels||[],c=t.labels,d=t.marker.colors||[],p=t.values,f=t._length,h=t._hasValues&&f;if(t.dlabel)for(c=new Array(f),a=0;a<f;a++)c[a]=String(t.label0+a*t.dlabel);var u={},x=l(n["_"+t.type+"colormap"]),m=0,v=!1;for(a=0;a<f;a++){var y,g,b;if(h){if(y=p[a],!i(y))continue;if((y=+y)<0)continue}else y=1;void 0!==(g=c[a])&&""!==g||(g=a);var T=u[g=String(g)];void 0===T?(u[g]=r.length,(b=-1!==s.indexOf(g))||(m+=y),r.push({v:y,label:g,color:x(d[a],g),i:a,pts:[a],hidden:b})):(v=!0,(o=r[T]).v+=y,o.pts.push(a),o.hidden||(m+=y),!1===o.color&&d[a]&&(o.color=x(d[a],g)))}return("funnelarea"===t.type?v:t.sort)&&r.sort((function(e,t){return t.v-e.v})),r[0]&&(r[0].vTotal=m),r},crossTraceCalc:function(e,t){var a=(t||{}).type;a||(a="pie");var i=e._fullLayout,o=e.calcdata,r=i[a+"colorway"],l=i["_"+a+"colormap"];i["extend"+a+"colors"]&&(r=s(r,n));for(var c=0,d=0;d<o.length;d++){var p=o[d];if(p[0].trace.type===a)for(var f=0;f<p.length;f++){var h=p[f];!1===h.color&&(l[h.label]?h.color=l[h.label]:(l[h.label]=h.color=r[c%r.length],c++))}}},makePullColorFn:l,generateExtendedColors:s}},925:function(e,t,a){"use strict";var i=a(24),o=a(107),r=a(622),n=a(57),l=a(106),s=a(6),c=a(108),d=a(636),p=d.recordMinTextSize,f=d.clearMinTextSize,h=a(656).TEXTPAD,u=a(914),x=a(1125),m=a(6).isValidTextValue;function v(e,t,a){var o=a[0],n=o.trace,l=o.cx,c=o.cy;"_hasHoverLabel"in n||(n._hasHoverLabel=!1),"_hasHoverEvent"in n||(n._hasHoverEvent=!1),e.on("mouseover",(function(e){var a=t._fullLayout,d=t._fullData[n.index];if(!t._dragging&&!1!==a.hovermode){var p=d.hoverinfo;if(Array.isArray(p)&&(p=r.castHoverinfo({hoverinfo:[u.castOption(p,e.pts)],_module:n._module},a,0)),"all"===p&&(p="label+text+value+percent+name"),d.hovertemplate||"none"!==p&&"skip"!==p&&p){var f=e.rInscribed||0,h=l+e.pxmid[0]*(1-f),m=c+e.pxmid[1]*(1-f),v=a.separators,y=[];if(p&&-1!==p.indexOf("label")&&y.push(e.label),e.text=u.castOption(d.hovertext||d.text,e.pts),p&&-1!==p.indexOf("text")){var g=e.text;s.isValidTextValue(g)&&y.push(g)}e.value=e.v,e.valueLabel=u.formatPieValue(e.v,v),p&&-1!==p.indexOf("value")&&y.push(e.valueLabel),e.percent=e.v/o.vTotal,e.percentLabel=u.formatPiePercent(e.percent,v),p&&-1!==p.indexOf("percent")&&y.push(e.percentLabel);var b=d.hoverlabel,T=b.font;r.loneHover({trace:n,x0:h-f*o.r,x1:h+f*o.r,y:m,text:y.join("<br>"),name:d.hovertemplate||-1!==p.indexOf("name")?d.name:void 0,idealAlign:e.pxmid[0]<0?"left":"right",color:u.castOption(b.bgcolor,e.pts)||e.color,borderColor:u.castOption(b.bordercolor,e.pts),fontFamily:u.castOption(T.family,e.pts),fontSize:u.castOption(T.size,e.pts),fontColor:u.castOption(T.color,e.pts),nameLength:u.castOption(b.namelength,e.pts),textAlign:u.castOption(b.align,e.pts),hovertemplate:u.castOption(d.hovertemplate,e.pts),hovertemplateLabels:e,eventData:[x(e,d)]},{container:a._hoverlayer.node(),outerContainer:a._paper.node(),gd:t}),n._hasHoverLabel=!0}n._hasHoverEvent=!0,t.emit("plotly_hover",{points:[x(e,d)],event:i.event})}})),e.on("mouseout",(function(e){var a=t._fullLayout,o=t._fullData[n.index],l=i.select(this).datum();n._hasHoverEvent&&(e.originalEvent=i.event,t.emit("plotly_unhover",{points:[x(l,o)],event:i.event}),n._hasHoverEvent=!1),n._hasHoverLabel&&(r.loneUnhover(a._hoverlayer.node()),n._hasHoverLabel=!1)})),e.on("click",(function(e){var a=t._fullLayout,o=t._fullData[n.index];t._dragging||!1===a.hovermode||(t._hoverdata=[x(e,o)],r.click(t,i.event))}))}function y(e,t,a){var i=u.castOption(e.insidetextfont.color,t.pts);!i&&e._input.textfont&&(i=u.castOption(e._input.textfont.color,t.pts));var o=u.castOption(e.insidetextfont.family,t.pts)||u.castOption(e.textfont.family,t.pts)||a.family,r=u.castOption(e.insidetextfont.size,t.pts)||u.castOption(e.textfont.size,t.pts)||a.size;return{color:i||n.contrast(t.color),family:o,size:r}}function g(e,t){for(var a,i,o=0;o<e.length;o++)if((i=(a=e[o][0]).trace).title.text){var r=i.title.text;i._meta&&(r=s.templateString(r,i._meta));var n=l.tester.append("text").attr("data-notex",1).text(r).call(l.font,i.title.font).call(c.convertToTspans,t),d=l.bBox(n.node(),!0);a.titleBox={width:d.width,height:d.height},n.remove()}}function b(e,t,a){var i=a.r||t.rpx1,o=t.rInscribed;if(t.startangle===t.stopangle)return{rCenter:1-o,scale:0,rotate:0,textPosAngle:0};var r,n=t.ring,l=1===n&&Math.abs(t.startangle-t.stopangle)===2*Math.PI,s=t.halfangle,c=t.midangle,d=a.trace.insidetextorientation,p="horizontal"===d,f="tangential"===d,h="radial"===d,u="auto"===d,x=[];if(!u){var m,v=function(a,o){if(function(e,t){var a=e.startangle,i=e.stopangle;return a>t&&t>i||a<t&&t<i}(t,a)){var l=Math.abs(a-t.startangle),s=Math.abs(a-t.stopangle),c=l<s?l:s;(r="tan"===o?w(e,i,n,c,0):T(e,i,n,c,Math.PI/2)).textPosAngle=a,x.push(r)}};if(p||f){for(m=4;m>=-4;m-=2)v(Math.PI*m,"tan");for(m=4;m>=-4;m-=2)v(Math.PI*(m+1),"tan")}if(p||h){for(m=4;m>=-4;m-=2)v(Math.PI*(m+1.5),"rad");for(m=4;m>=-4;m-=2)v(Math.PI*(m+.5),"rad")}}if(l||u||p){var y=Math.sqrt(e.width*e.width+e.height*e.height);if((r={scale:o*i*2/y,rCenter:1-o,rotate:0}).textPosAngle=(t.startangle+t.stopangle)/2,r.scale>=1)return r;x.push(r)}(u||h)&&((r=T(e,i,n,s,c)).textPosAngle=(t.startangle+t.stopangle)/2,x.push(r)),(u||f)&&((r=w(e,i,n,s,c)).textPosAngle=(t.startangle+t.stopangle)/2,x.push(r));for(var g=0,b=0,M=0;M<x.length;M++){var k=x[M].scale;if(b<k&&(b=k,g=M),!u&&b>=1)break}return x[g]}function T(e,t,a,i,o){t=Math.max(0,t-2*h);var r=e.width/e.height,n=_(r,i,t,a);return{scale:2*n/e.height,rCenter:M(r,n/t),rotate:k(o)}}function w(e,t,a,i,o){t=Math.max(0,t-2*h);var r=e.height/e.width,n=_(r,i,t,a);return{scale:2*n/e.width,rCenter:M(r,n/t),rotate:k(o+Math.PI/2)}}function M(e,t){return Math.cos(t)-e*t}function k(e){return(180/Math.PI*e+720)%180-90}function _(e,t,a,i){var o=e+1/(2*Math.tan(t));return a*Math.min(1/(Math.sqrt(o*o+.5)+o),i/(Math.sqrt(e*e+i/2)+e))}function O(e,t){return e.v!==t.vTotal||t.trace.hole?Math.min(1/(1+1/Math.sin(e.halfangle)),e.ring/2):1}function S(e,t){var a=t.pxmid[0],i=t.pxmid[1],o=e.width/2,r=e.height/2;return a<0&&(o*=-1),i<0&&(r*=-1),{scale:1,rCenter:1,rotate:0,x:o+Math.abs(r)*(o>0?1:-1)/2,y:r/(1+a*a/(i*i)),outside:!0}}function L(e,t){var a,i,o,r=e.trace,n={x:e.cx,y:e.cy},l={tx:0,ty:0};l.ty+=r.title.font.size,o=A(r),-1!==r.title.position.indexOf("top")?(n.y-=(1+o)*e.r,l.ty-=e.titleBox.height):-1!==r.title.position.indexOf("bottom")&&(n.y+=(1+o)*e.r);var s,c,d=(s=e.r,c=e.trace.aspectratio,s/(void 0===c?1:c)),p=t.w*(r.domain.x[1]-r.domain.x[0])/2;return-1!==r.title.position.indexOf("left")?(p+=d,n.x-=(1+o)*d,l.tx+=e.titleBox.width/2):-1!==r.title.position.indexOf("center")?p*=2:-1!==r.title.position.indexOf("right")&&(p+=d,n.x+=(1+o)*d,l.tx-=e.titleBox.width/2),a=p/e.titleBox.width,i=j(e,t)/e.titleBox.height,{x:n.x,y:n.y,scale:Math.min(a,i),tx:l.tx,ty:l.ty}}function j(e,t){var a=e.trace,i=t.h*(a.domain.y[1]-a.domain.y[0]);return Math.min(e.titleBox.height,i/2)}function A(e){var t,a=e.pull;if(!a)return 0;if(Array.isArray(a))for(a=0,t=0;t<e.pull.length;t++)e.pull[t]>a&&(a=e.pull[t]);return a}function I(e,t){for(var a=[],i=0;i<e.length;i++){var o=e[i][0],r=o.trace,n=r.domain,l=t.w*(n.x[1]-n.x[0]),s=t.h*(n.y[1]-n.y[0]);r.title.text&&"middle center"!==r.title.position&&(s-=j(o,t));var c=l/2,d=s/2;"funnelarea"!==r.type||r.scalegroup||(d/=r.aspectratio),o.r=Math.min(c,d)/(1+A(r)),o.cx=t.l+t.w*(r.domain.x[1]+r.domain.x[0])/2,o.cy=t.t+t.h*(1-r.domain.y[0])-s/2,r.title.text&&-1!==r.title.position.indexOf("bottom")&&(o.cy-=j(o,t)),r.scalegroup&&-1===a.indexOf(r.scalegroup)&&a.push(r.scalegroup)}!function(e,t){for(var a,i,o,r=0;r<t.length;r++){var n=1/0,l=t[r];for(i=0;i<e.length;i++)if(a=e[i][0],(o=a.trace).scalegroup===l){var s;if("pie"===o.type)s=a.r*a.r;else if("funnelarea"===o.type){var c,d;o.aspectratio>1?(c=a.r,d=c/o.aspectratio):(d=a.r,c=d*o.aspectratio),c*=(1+o.baseratio)/2,s=c*d}n=Math.min(n,s/a.vTotal)}for(i=0;i<e.length;i++)if(a=e[i][0],(o=a.trace).scalegroup===l){var p=n*a.vTotal;"funnelarea"===o.type&&(p/=(1+o.baseratio)/2,p/=o.aspectratio),a.r=Math.sqrt(p)}}}(e,a)}function z(e,t){return[e*Math.sin(t),-e*Math.cos(t)]}function P(e,t,a){var i=e._fullLayout,o=a.trace,r=o.texttemplate,n=o.textinfo;if(!r&&n&&"none"!==n){var l,c=n.split("+"),d=function(e){return-1!==c.indexOf(e)},p=d("label"),f=d("text"),h=d("value"),x=d("percent"),v=i.separators;if(l=p?[t.label]:[],f){var y=u.getFirstFilled(o.text,t.pts);m(y)&&l.push(y)}h&&l.push(u.formatPieValue(t.v,v)),x&&l.push(u.formatPiePercent(t.v/a.vTotal,v)),t.text=l.join("<br>")}if(r){var g=s.castOption(o,t.i,"texttemplate");if(g){var b=function(e){return{label:e.label,value:e.v,valueLabel:u.formatPieValue(e.v,i.separators),percent:e.v/a.vTotal,percentLabel:u.formatPiePercent(e.v/a.vTotal,i.separators),color:e.color,text:e.text,customdata:s.castOption(o,e.i,"customdata")}}(t),T=u.getFirstFilled(o.text,t.pts);(m(T)||""===T)&&(b.text=T),t.text=s.texttemplateString(g,b,e._fullLayout._d3locale,b,o._meta||{})}else t.text=""}}function E(e,t){var a=e.rotate*Math.PI/180,i=Math.cos(a),o=Math.sin(a),r=(t.left+t.right)/2,n=(t.top+t.bottom)/2;e.textX=r*i-n*o,e.textY=r*o+n*i,e.noCenter=!0}e.exports={plot:function(e,t){var a=e._fullLayout,r=a._size;f("pie",a),g(t,e),I(t,r);var d=s.makeTraceGroups(a._pielayer,t,"trace").each((function(t){var d=i.select(this),f=t[0],h=f.trace;!function(e){var t,a,i,o=e[0],r=o.r,n=o.trace,l=n.rotation*Math.PI/180,s=2*Math.PI/o.vTotal,c="px0",d="px1";if("counterclockwise"===n.direction){for(t=0;t<e.length&&e[t].hidden;t++);if(t===e.length)return;l+=s*e[t].v,s*=-1,c="px1",d="px0"}for(i=z(r,l),t=0;t<e.length;t++)(a=e[t]).hidden||(a[c]=i,a.startangle=l,l+=s*a.v/2,a.pxmid=z(r,l),a.midangle=l,l+=s*a.v/2,i=z(r,l),a.stopangle=l,a[d]=i,a.largeArc=a.v>o.vTotal/2?1:0,a.halfangle=Math.PI*Math.min(a.v/o.vTotal,.5),a.ring=1-n.hole,a.rInscribed=O(a,o))}(t),d.attr("stroke-linejoin","round"),d.each((function(){var x=i.select(this).selectAll("g.slice").data(t);x.enter().append("g").classed("slice",!0),x.exit().remove();var m=[[[],[]],[[],[]]],g=!1;x.each((function(o,r){if(o.hidden)i.select(this).selectAll("path,g").remove();else{o.pointNumber=o.i,o.curveNumber=h.index,m[o.pxmid[1]<0?0:1][o.pxmid[0]<0?0:1].push(o);var n=f.cx,d=f.cy,x=i.select(this),T=x.selectAll("path.surface").data([o]);if(T.enter().append("path").classed("surface",!0).style({"pointer-events":"all"}),x.call(v,e,t),h.pull){var w=+u.castOption(h.pull,o.pts)||0;w>0&&(n+=w*o.pxmid[0],d+=w*o.pxmid[1])}o.cxFinal=n,o.cyFinal=d;var M=h.hole;if(o.v===f.vTotal){var k="M"+(n+o.px0[0])+","+(d+o.px0[1])+A(o.px0,o.pxmid,!0,1)+A(o.pxmid,o.px0,!0,1)+"Z";M?T.attr("d","M"+(n+M*o.px0[0])+","+(d+M*o.px0[1])+A(o.px0,o.pxmid,!1,M)+A(o.pxmid,o.px0,!1,M)+"Z"+k):T.attr("d",k)}else{var _=A(o.px0,o.px1,!0,1);if(M){var O=1-M;T.attr("d","M"+(n+M*o.px1[0])+","+(d+M*o.px1[1])+A(o.px1,o.px0,!1,M)+"l"+O*o.px0[0]+","+O*o.px0[1]+_+"Z")}else T.attr("d","M"+n+","+d+"l"+o.px0[0]+","+o.px0[1]+_+"Z")}P(e,o,f);var L=u.castOption(h.textposition,o.pts),j=x.selectAll("g.slicetext").data(o.text&&"none"!==L?[0]:[]);j.enter().append("g").classed("slicetext",!0),j.exit().remove(),j.each((function(){var x=s.ensureSingle(i.select(this),"text","",(function(e){e.attr("data-notex",1)})),m=s.ensureUniformFontSize(e,"outside"===L?function(e,t,a){var i=u.castOption(e.outsidetextfont.color,t.pts)||u.castOption(e.textfont.color,t.pts)||a.color,o=u.castOption(e.outsidetextfont.family,t.pts)||u.castOption(e.textfont.family,t.pts)||a.family,r=u.castOption(e.outsidetextfont.size,t.pts)||u.castOption(e.textfont.size,t.pts)||a.size;return{color:i,family:o,size:r}}(h,o,a.font):y(h,o,a.font));x.text(o.text).attr({class:"slicetext",transform:"","text-anchor":"middle"}).call(l.font,m).call(c.convertToTspans,e);var v,T=l.bBox(x.node());if("outside"===L)v=S(T,o);else if(v=b(T,o,f),"auto"===L&&v.scale<1){var w=s.ensureUniformFontSize(e,h.outsidetextfont);x.call(l.font,w),v=S(T=l.bBox(x.node()),o)}var M=v.textPosAngle,k=void 0===M?o.pxmid:z(f.r,M);if(v.targetX=n+k[0]*v.rCenter+(v.x||0),v.targetY=d+k[1]*v.rCenter+(v.y||0),E(v,T),v.outside){var _=v.targetY;o.yLabelMin=_-T.height/2,o.yLabelMid=_,o.yLabelMax=_+T.height/2,o.labelExtraX=0,o.labelExtraY=0,g=!0}v.fontSize=m.size,p(h.type,v,a),t[r].transform=v,x.attr("transform",s.getTextTransform(v))}))}function A(e,t,a,i){var r=i*(t[0]-e[0]),n=i*(t[1]-e[1]);return"a"+i*f.r+","+i*f.r+" 0 "+o.largeArc+(a?" 1 ":" 0 ")+r+","+n}}));var T=i.select(this).selectAll("g.titletext").data(h.title.text?[0]:[]);if(T.enter().append("g").classed("titletext",!0),T.exit().remove(),T.each((function(){var t,a=s.ensureSingle(i.select(this),"text","",(function(e){e.attr("data-notex",1)})),o=h.title.text;h._meta&&(o=s.templateString(o,h._meta)),a.text(o).attr({class:"titletext",transform:"","text-anchor":"middle"}).call(l.font,h.title.font).call(c.convertToTspans,e),t="middle center"===h.title.position?function(e){var t=Math.sqrt(e.titleBox.width*e.titleBox.width+e.titleBox.height*e.titleBox.height);return{x:e.cx,y:e.cy,scale:e.trace.hole*e.r*2/t,tx:0,ty:-e.titleBox.height/2+e.trace.title.font.size}}(f):L(f,r),a.attr("transform","translate("+t.x+","+t.y+")"+(t.scale<1?"scale("+t.scale+")":"")+"translate("+t.tx+","+t.ty+")")})),g&&function(e,t){var a,i,o,r,n,l,s,c,d,p,f,h,x;function m(e,t){return e.pxmid[1]-t.pxmid[1]}function v(e,t){return t.pxmid[1]-e.pxmid[1]}function y(e,a){a||(a={});var o,c,d,f,h=a.labelExtraY+(i?a.yLabelMax:a.yLabelMin),x=i?e.yLabelMin:e.yLabelMax,m=i?e.yLabelMax:e.yLabelMin,v=e.cyFinal+n(e.px0[1],e.px1[1]),y=h-x;if(y*s>0&&(e.labelExtraY=y),Array.isArray(t.pull))for(c=0;c<p.length;c++)(d=p[c])===e||(u.castOption(t.pull,e.pts)||0)>=(u.castOption(t.pull,d.pts)||0)||((e.pxmid[1]-d.pxmid[1])*s>0?(y=d.cyFinal+n(d.px0[1],d.px1[1])-x-e.labelExtraY)*s>0&&(e.labelExtraY+=y):(m+e.labelExtraY-v)*s>0&&(o=3*l*Math.abs(c-p.indexOf(e)),(f=d.cxFinal+r(d.px0[0],d.px1[0])+o-(e.cxFinal+e.pxmid[0])-e.labelExtraX)*l>0&&(e.labelExtraX+=f)))}for(i=0;i<2;i++)for(o=i?m:v,n=i?Math.max:Math.min,s=i?1:-1,a=0;a<2;a++){for(r=a?Math.max:Math.min,l=a?1:-1,(c=e[i][a]).sort(o),d=e[1-i][a],p=d.concat(c),h=[],f=0;f<c.length;f++)void 0!==c[f].yLabelMid&&h.push(c[f]);for(x=!1,f=0;i&&f<d.length;f++)if(void 0!==d[f].yLabelMid){x=d[f];break}for(f=0;f<h.length;f++){var g=f&&h[f-1];x&&!f&&(g=x),y(h[f],g)}}}(m,h),function(e,t){e.each((function(e){var a=i.select(this);if(e.labelExtraX||e.labelExtraY){var o=a.select("g.slicetext text");e.transform.targetX+=e.labelExtraX,e.transform.targetY+=e.labelExtraY,o.attr("transform",s.getTextTransform(e.transform));var r=e.cxFinal+e.pxmid[0],l="M"+r+","+(e.cyFinal+e.pxmid[1]),c=(e.yLabelMax-e.yLabelMin)*(e.pxmid[0]<0?-1:1)/4;if(e.labelExtraX){var d=e.labelExtraX*e.pxmid[1]/e.pxmid[0],p=e.yLabelMid+e.labelExtraY-(e.cyFinal+e.pxmid[1]);Math.abs(d)>Math.abs(p)?l+="l"+p*e.pxmid[0]/e.pxmid[1]+","+p+"H"+(r+e.labelExtraX+c):l+="l"+e.labelExtraX+","+d+"v"+(p-d)+"h"+c}else l+="V"+(e.yLabelMid+e.labelExtraY)+"h"+c;s.ensureSingle(a,"path","textline").call(n.stroke,t.outsidetextfont.color).attr({"stroke-width":Math.min(2,t.outsidetextfont.size/8),d:l,fill:"none"})}else a.select("path.textline").remove()}))}(x,h),g&&h.automargin){var w=l.bBox(d.node()),M=h.domain,k=r.w*(M.x[1]-M.x[0]),_=r.h*(M.y[1]-M.y[0]),O=(.5*k-f.r)/r.w,j=(.5*_-f.r)/r.h;o.autoMargin(e,"pie."+h.uid+".automargin",{xl:M.x[0]-O,xr:M.x[1]+O,yb:M.y[0]-j,yt:M.y[1]+j,l:Math.max(f.cx-f.r-w.left,0),r:Math.max(w.right-(f.cx+f.r),0),b:Math.max(w.bottom-(f.cy+f.r),0),t:Math.max(f.cy-f.r-w.top,0),pad:5})}}))}));setTimeout((function(){d.selectAll("tspan").each((function(){var e=i.select(this);e.attr("dy")&&e.attr("dy",e.attr("dy"))}))}),0)},formatSliceLabel:P,transformInsideText:b,determineInsideTextFont:y,positionTitleOutside:L,prerenderTitles:g,layoutAreas:I,attachFxHandlers:v,computeTransform:E}}}]);