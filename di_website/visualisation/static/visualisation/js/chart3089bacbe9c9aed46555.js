(window.webpackJsonp=window.webpackJsonp||[]).push([[69],{1635:function(e,t,r){"use strict";e.exports={sunburstcolorway:{valType:"colorlist",role:"style",editType:"calc",description:["Sets the default sunburst slice colors. Defaults to the main","`colorway` used for trace colors. If you specify a new","list here it can still be extended with lighter and darker","colors, see `extendsunburstcolors`."].join(" ")},extendsunburstcolors:{valType:"boolean",dflt:!0,role:"style",editType:"calc",description:["If `true`, the sunburst slice colors (whether given by `sunburstcolorway` or","inherited from `colorway`) will be extended to three times its","original length by first repeating every color 20% lighter then","each color 20% darker. This is intended to reduce the likelihood","of reusing the same color when you have many slices, but you can","set `false` to disable.","Colors provided in the trace, using `marker.colors`, are never","extended."].join(" ")}}},1711:function(e,t,r){"use strict";e.exports={moduleType:"trace",name:"sunburst",basePlotModule:r(1712),categories:[],animatable:!0,attributes:r(1308),layoutAttributes:r(1635),supplyDefaults:r(1713),supplyLayoutDefaults:r(1714),calc:r(1309).calc,crossTraceCalc:r(1309).crossTraceCalc,plot:r(1636).plot,style:r(1637).style,colorbar:r(632),meta:{description:["Visualize hierarchal data spanning outward radially from root to leaves.","The sunburst sectors are determined by the entries in *labels* or *ids*","and in *parents*."].join(" ")}}},1712:function(e,t,r){"use strict";var o=r(107);t.name="sunburst",t.plot=function(e,r,s,l){o.plotBasePlot(t.name,e,r,s,l)},t.clean=function(e,r,s,l){o.cleanBasePlot(t.name,e,r,s,l)}},1713:function(e,t,r){"use strict";var o=r(6),s=r(1308),l=r(623).defaults,a=r(644).handleText,n=r(207),i=n.hasColorscale,c=n.handleDefaults;e.exports=function(e,t,r,n){function u(r,l){return o.coerce(e,t,s,r,l)}var d=u("labels"),p=u("parents");if(d&&d.length&&p&&p.length){var h=u("values");h&&h.length?u("branchvalues"):u("count"),u("level"),u("maxdepth"),u("marker.line.width")&&u("marker.line.color",n.paper_bgcolor),u("marker.colors");var b=t._hasColorscale=i(e,"marker","colors")||(e.marker||{}).coloraxis;b&&c(e,t,n,u,{prefix:"marker.",cLetter:"c"}),u("leaf.opacity",b?1:.7);var f=u("text");u("texttemplate"),t.texttemplate||u("textinfo",Array.isArray(f)?"text+label":"label"),u("hovertext"),u("hovertemplate");a(e,t,n,u,"auto",{moduleHasSelected:!1,moduleHasUnselected:!1,moduleHasConstrain:!1,moduleHasCliponaxis:!1,moduleHasTextangle:!1,moduleHasInsideanchor:!1}),u("insidetextorientation"),l(t,n,u),t._length=null}else t.visible=!1}},1714:function(e,t,r){"use strict";var o=r(6),s=r(1635);e.exports=function(e,t){function r(r,l){return o.coerce(e,t,s,r,l)}r("sunburstcolorway",t.colorway),r("extendsunburstcolors")}},273:function(e,t,r){"use strict";e.exports=r(1711)}}]);