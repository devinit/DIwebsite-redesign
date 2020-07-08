(window.webpackJsonp=window.webpackJsonp||[]).push([[67],{1081:function(e,t,a){"use strict";var i=a(387).extendFlat,n=a(387).extendDeep,r=a(394).overrideAll,l=a(406),o=a(408),s=a(400).attributes,c=a(445),u=a(388).templatedArray,d=a(569),h=a(485).FORMAT_LINK,p=l({editType:"plot",colorEditType:"plot"}),f={color:{valType:"color",editType:"plot",role:"info",description:["Sets the background color of the arc."].join(" ")},line:{color:{valType:"color",role:"info",dflt:o.defaultLine,editType:"plot",description:["Sets the color of the line enclosing each sector."].join(" ")},width:{valType:"number",role:"info",min:0,dflt:0,editType:"plot",description:["Sets the width (in px) of the line enclosing each sector."].join(" ")},editType:"calc"},thickness:{valType:"number",role:"info",min:0,max:1,dflt:1,editType:"plot",description:["Sets the thickness of the bar as a fraction of the total thickness of the gauge."].join(" ")},editType:"calc"},g={valType:"info_array",role:"info",items:[{valType:"number",editType:"plot"},{valType:"number",editType:"plot"}],editType:"plot",description:["Sets the range of this axis."].join(" ")},m=u("step",n({},f,{range:g}));e.exports={mode:{valType:"flaglist",editType:"calc",role:"info",flags:["number","delta","gauge"],dflt:"number",description:["Determines how the value is displayed on the graph.","`number` displays the value numerically in text.","`delta` displays the difference to a reference value in text.","Finally, `gauge` displays the value graphically on an axis."].join(" ")},value:{valType:"number",editType:"calc",role:"info",anim:!0,description:["Sets the number to be displayed."].join(" ")},align:{valType:"enumerated",values:["left","center","right"],role:"info",editType:"plot",description:["Sets the horizontal alignment of the `text` within the box.","Note that this attribute has no effect if an angular gauge is displayed:","in this case, it is always centered"].join(" ")},domain:s({name:"indicator",trace:!0,editType:"calc"}),title:{text:{valType:"string",role:"info",editType:"plot",description:["Sets the title of this indicator."].join(" ")},align:{valType:"enumerated",values:["left","center","right"],role:"info",editType:"plot",description:["Sets the horizontal alignment of the title.","It defaults to `center` except for bullet charts","for which it defaults to right."].join(" ")},font:i({},p,{description:["Set the font used to display the title"].join(" ")}),editType:"plot"},number:{valueformat:{valType:"string",dflt:"",role:"info",editType:"plot",description:["Sets the value formatting rule using d3 formatting mini-language","which is similar to those of Python. See",h].join(" ")},font:i({},p,{description:["Set the font used to display main number"].join(" ")}),prefix:{valType:"string",dflt:"",role:"info",editType:"plot",description:["Sets a prefix appearing before the number."].join(" ")},suffix:{valType:"string",dflt:"",role:"info",editType:"plot",description:["Sets a suffix appearing next to the number."].join(" ")},editType:"plot"},delta:{reference:{valType:"number",role:"info",editType:"calc",description:["Sets the reference value to compute the delta.","By default, it is set to the current value."].join(" ")},position:{valType:"enumerated",values:["top","bottom","left","right"],role:"info",dflt:"bottom",editType:"plot",description:["Sets the position of delta with respect to the number."].join(" ")},relative:{valType:"boolean",editType:"plot",role:"info",dflt:!1,description:["Show relative change"].join(" ")},valueformat:{valType:"string",role:"info",editType:"plot",description:["Sets the value formatting rule using d3 formatting mini-language","which is similar to those of Python. See",h].join(" ")},increasing:{symbol:{valType:"string",role:"info",dflt:d.INCREASING.SYMBOL,editType:"plot",description:["Sets the symbol to display for increasing value"].join(" ")},color:{valType:"color",role:"info",dflt:d.INCREASING.COLOR,editType:"plot",description:["Sets the color for increasing value."].join(" ")},editType:"plot"},decreasing:{symbol:{valType:"string",role:"info",dflt:d.DECREASING.SYMBOL,editType:"plot",description:["Sets the symbol to display for increasing value"].join(" ")},color:{valType:"color",role:"info",dflt:d.DECREASING.COLOR,editType:"plot",description:["Sets the color for increasing value."].join(" ")},editType:"plot"},font:i({},p,{description:["Set the font used to display the delta"].join(" ")}),editType:"calc"},gauge:{shape:{valType:"enumerated",editType:"plot",role:"info",dflt:"angular",values:["angular","bullet"],description:["Set the shape of the gauge"].join(" ")},bar:n({},f,{color:{dflt:"green"},description:["Set the appearance of the gauge's value"].join(" ")}),bgcolor:{valType:"color",role:"info",editType:"plot",description:"Sets the gauge background color."},bordercolor:{valType:"color",dflt:o.defaultLine,role:"info",editType:"plot",description:"Sets the color of the border enclosing the gauge."},borderwidth:{valType:"number",min:0,dflt:1,role:"info",editType:"plot",description:"Sets the width (in px) of the border enclosing the gauge."},axis:r({range:g,visible:i({},c.visible,{dflt:!0}),tickmode:c.tickmode,nticks:c.nticks,tick0:c.tick0,dtick:c.dtick,tickvals:c.tickvals,ticktext:c.ticktext,ticks:i({},c.ticks,{dflt:"outside"}),ticklen:c.ticklen,tickwidth:c.tickwidth,tickcolor:c.tickcolor,showticklabels:c.showticklabels,tickfont:l({description:"Sets the color bar's tick label font"}),tickangle:c.tickangle,tickformat:c.tickformat,tickformatstops:c.tickformatstops,tickprefix:c.tickprefix,showtickprefix:c.showtickprefix,ticksuffix:c.ticksuffix,showticksuffix:c.showticksuffix,separatethousands:c.separatethousands,exponentformat:c.exponentformat,showexponent:c.showexponent,editType:"plot"},"plot"),steps:m,threshold:{line:{color:i({},f.line.color,{description:["Sets the color of the threshold line."].join(" ")}),width:i({},f.line.width,{dflt:1,description:["Sets the width (in px) of the threshold line."].join(" ")}),editType:"plot"},thickness:i({},f.thickness,{dflt:.85,description:["Sets the thickness of the threshold line as a fraction of the thickness of the gauge."].join(" ")}),value:{valType:"number",editType:"calc",dflt:!1,role:"info",description:["Sets a treshold value drawn as a line."].join(" ")},editType:"plot"},description:"The gauge of the Indicator plot.",editType:"plot"}}},1082:function(e,t,a){"use strict";e.exports={defaultNumberFontSize:80,bulletNumberDomainSize:.25,bulletPadding:.025,innerRadius:.75,valueThickness:.5,titlePadding:5,horizontalPadding:10}},1163:function(e,t,a){"use strict";e.exports=a(1359)},1359:function(e,t,a){"use strict";e.exports={moduleType:"trace",name:"indicator",basePlotModule:a(1360),categories:["svg","noOpacity","noHover"],animatable:!0,attributes:a(1081),supplyDefaults:a(1361).supplyDefaults,calc:a(1362).calc,plot:a(1363),meta:{description:["An indicator is used to visualize a single `value` along with some","contextual information such as `steps` or a `threshold`, using a","combination of three visual elements: a number, a delta, and/or a gauge.","Deltas are taken with respect to a `reference`.","Gauges can be either angular or bullet (aka linear) gauges."].join(" ")}}},1360:function(e,t,a){"use strict";var i=a(392);t.name="indicator",t.plot=function(e,a,n,r){i.plotBasePlot(t.name,e,a,n,r)},t.clean=function(e,a,n,r){i.cleanBasePlot(t.name,e,a,n,r)}},1361:function(e,t,a){"use strict";var i=a(380),n=a(1081),r=a(400).defaults,l=a(388),o=a(405),s=a(1082),c=a(566),u=a(595),d=a(567);function h(e,t){function a(a,r){return i.coerce(e,t,n.gauge.steps,a,r)}a("color"),a("line.color"),a("line.width"),a("range"),a("thickness")}e.exports={supplyDefaults:function(e,t,a,p){function f(a,r){return i.coerce(e,t,n,a,r)}r(t,p,f),f("mode"),t._hasNumber=-1!==t.mode.indexOf("number"),t._hasDelta=-1!==t.mode.indexOf("delta"),t._hasGauge=-1!==t.mode.indexOf("gauge");var g=f("value");t._range=[0,"number"==typeof g?1.5*g:1];var m,b,v,y,x,T,w=new Array(2);function k(e,t){return i.coerce(v,y,n.gauge,e,t)}function _(e,t){return i.coerce(x,T,n.gauge.axis,e,t)}if(t._hasNumber&&(f("number.valueformat"),f("number.font.color",p.font.color),f("number.font.family",p.font.family),f("number.font.size"),void 0===t.number.font.size&&(t.number.font.size=s.defaultNumberFontSize,w[0]=!0),f("number.prefix"),f("number.suffix"),m=t.number.font.size),t._hasDelta&&(f("delta.font.color",p.font.color),f("delta.font.family",p.font.family),f("delta.font.size"),void 0===t.delta.font.size&&(t.delta.font.size=(t._hasNumber?.5:1)*(m||s.defaultNumberFontSize),w[1]=!0),f("delta.reference",t.value),f("delta.relative"),f("delta.valueformat",t.delta.relative?"2%":""),f("delta.increasing.symbol"),f("delta.increasing.color"),f("delta.decreasing.symbol"),f("delta.decreasing.color"),f("delta.position"),b=t.delta.font.size),t._scaleNumbers=(!t._hasNumber||w[0])&&(!t._hasDelta||w[1])||!1,f("title.font.color",p.font.color),f("title.font.family",p.font.family),f("title.font.size",.25*(m||b||s.defaultNumberFontSize)),f("title.text"),t._hasGauge){(v=e.gauge)||(v={}),y=l.newContainer(t,"gauge"),k("shape"),(t._isBullet="bullet"===t.gauge.shape)||f("title.align","center"),(t._isAngular="angular"===t.gauge.shape)||f("align","center"),k("bgcolor",p.paper_bgcolor),k("borderwidth"),k("bordercolor"),k("bar.color"),k("bar.line.color"),k("bar.line.width"),k("bar.thickness",s.valueThickness*("bullet"===t.gauge.shape?.5:1)),o(v,y,{name:"steps",handleItemDefaults:h}),k("threshold.value"),k("threshold.thickness"),k("threshold.line.width"),k("threshold.line.color"),x={},v&&(x=v.axis||{}),T=l.newContainer(y,"axis"),_("visible"),t._range=_("range",t._range);var S={outerTicks:!0};c(x,T,_,"linear"),d(x,T,_,"linear",S),u(x,T,_,S)}else f("title.align","center"),f("align","center"),t._isAngular=t._isBullet=!1;t._length=null}}},1362:function(e,t,a){"use strict";e.exports={calc:function(e,t){var a=[],i=t.value;"number"!=typeof t._lastValue&&(t._lastValue=t.value);var n=t._lastValue,r=n;return t._hasDelta&&"number"==typeof t.delta.reference&&(r=t.delta.reference),a[0]={y:i,lastY:n,delta:i-r,relativeDelta:(i-r)/r},a}}},1363:function(e,t,a){"use strict";var i=a(383),n=a(380),r=n.rad2deg,l=a(410).MID_SHIFT,o=a(386),s=a(1082),c=a(393),u=a(384),d=a(537),h=a(713),p=a(445),f=a(382),g={left:"start",center:"middle",right:"end"},m={left:0,center:.5,right:1},b=/[yzafpnµmkMGTPEZY]/;function v(e){return e&&e.duration>0}function y(e){e.each((function(e){f.stroke(i.select(this),e.line.color)})).each((function(e){f.fill(i.select(this),e.color)})).style("stroke-width",(function(e){return e.line.width}))}function x(e,t,a){var i=e._fullLayout,r=n.extendFlat({type:"linear",ticks:"outside",range:a,showline:!0},t),l={type:"linear",_id:"x"+t._id},o={letter:"x",font:i.font,noHover:!0,noTickson:!0};function s(e,t){return n.coerce(r,l,p,e,t)}return d(r,l,s,o,i),h(r,l,s,o),l}function T(e,t){return"translate("+e+","+t+")"}function w(e,t,a){return[Math.min(t/e.width,a/e.height),e,t+"x"+a]}function k(e,t,a,n){var r=document.createElementNS("http://www.w3.org/2000/svg","text"),l=i.select(r);return l.text(e).attr("x",0).attr("y",0).attr("text-anchor",a).attr("data-unformatted",e).call(c.convertToTspans,n).call(o.font,t),o.bBox(l.node())}function _(e,t,a,i,r,l){var o="_cache"+t;e[o]&&e[o].key===r||(e[o]={key:r,value:a});var s=n.aggNums(l,null,[e[o].value,i],2);return e[o].value=s,s}e.exports=function(e,t,a,d){var h,p=e._fullLayout;v(a)&&d&&(h=d()),n.makeTraceGroups(p._indicatorlayer,t,"trace").each((function(t){var d,S,M,z,A,N=t[0].trace,j=i.select(this),D=N._hasGauge,O=N._isAngular,F=N._isBullet,I=N.domain,L={w:p._size.w*(I.x[1]-I.x[0]),h:p._size.h*(I.y[1]-I.y[0]),l:p._size.l+p._size.w*I.x[0],r:p._size.r+p._size.w*(1-I.x[1]),t:p._size.t+p._size.h*(1-I.y[1]),b:p._size.b+p._size.h*I.y[0]},C=L.l+L.w/2,P=L.t+L.h/2,B=Math.min(L.w/2,L.h),R=s.innerRadius*B,E=N.align||"center";if(S=P,D){if(O&&(d=C,S=P+B/2,M=function(e){return function(e,t){var a=Math.sqrt(e.width/2*(e.width/2)+e.height*e.height);return[t/a,e,t]}(e,.9*R)}),F){var G=s.bulletPadding,Y=1-s.bulletNumberDomainSize+G;d=L.l+(Y+(1-Y)*m[E])*L.w,M=function(e){return w(e,(s.bulletNumberDomainSize-G)*L.w,L.h)}}}else d=L.l+m[E]*L.w,M=function(e){return w(e,L.w,L.h)};!function(e,t,a,r){var l,s,d,h=a[0].trace,p=r.numbersX,y=r.numbersY,w=h.align||"center",S=g[w],M=r.transitionOpts,z=r.onComplete,A=n.ensureSingle(t,"g","numbers"),N=[];h._hasNumber&&N.push("number");h._hasDelta&&(N.push("delta"),"left"===h.delta.position&&N.reverse());var j=A.selectAll("text").data(N);function D(t,a,i,n){if(!t.match("s")||i>=0==n>=0||a(i).slice(-1).match(b)||a(n).slice(-1).match(b))return a;var r=t.slice().replace("s","f").replace(/\d+/,(function(e){return parseInt(e)-1})),l=x(e,{tickformat:r});return function(e){return Math.abs(e)<1?u.tickText(l,e).text:a(e)}}j.enter().append("text"),j.attr("text-anchor",(function(){return S})).attr("class",(function(e){return e})).attr("x",null).attr("y",null).attr("dx",null).attr("dy",null),j.exit().remove();var O,F=h.mode+h.align;h._hasDelta&&(O=function(){var t=x(e,{tickformat:h.delta.valueformat},h._range);t.setScale(),u.prepTicks(t);var n=function(e){return u.tickText(t,e).text},r=function(e){return h.delta.relative?e.relativeDelta:e.delta},l=function(e,t){return 0===e||"number"!=typeof e||isNaN(e)?"-":(e>0?h.delta.increasing.symbol:h.delta.decreasing.symbol)+t(e)},d=function(e){return e.delta>=0?h.delta.increasing.color:h.delta.decreasing.color};void 0===h._deltaLastValue&&(h._deltaLastValue=r(a[0]));var p=A.select("text.delta");function g(){p.text(l(r(a[0]),n)).call(f.fill,d(a[0])).call(c.convertToTspans,e)}return p.call(o.font,h.delta.font).call(f.fill,d({delta:h._deltaLastValue})),v(M)?p.transition().duration(M.duration).ease(M.easing).tween("text",(function(){var e=i.select(this),t=r(a[0]),o=h._deltaLastValue,s=D(h.delta.valueformat,n,o,t),c=i.interpolateNumber(o,t);return h._deltaLastValue=t,function(t){e.text(l(c(t),s)),e.call(f.fill,d({delta:c(t)}))}})).each("end",(function(){g(),z&&z()})).each("interrupt",(function(){g(),z&&z()})):g(),s=k(l(r(a[0]),n),h.delta.font,S,e),p}(),F+=h.delta.position+h.delta.font.size+h.delta.font.family+h.delta.valueformat,F+=h.delta.increasing.symbol+h.delta.decreasing.symbol,d=s);h._hasNumber&&(!function(){var t=x(e,{tickformat:h.number.valueformat},h._range);t.setScale(),u.prepTicks(t);var n=function(e){return u.tickText(t,e).text},r=h.number.suffix,s=h.number.prefix,d=A.select("text.number");function p(){var t="number"==typeof a[0].y?s+n(a[0].y)+r:"-";d.text(t).call(o.font,h.number.font).call(c.convertToTspans,e)}v(M)?d.transition().duration(M.duration).ease(M.easing).each("end",(function(){p(),z&&z()})).each("interrupt",(function(){p(),z&&z()})).attrTween("text",(function(){var e=i.select(this),t=i.interpolateNumber(a[0].lastY,a[0].y);h._lastValue=a[0].y;var l=D(h.number.valueformat,n,a[0].lastY,a[0].y);return function(a){e.text(s+l(t(a))+r)}})):p(),l=k(s+n(a[0].y)+r,h.number.font,S,e)}(),F+=h.number.font.size+h.number.font.family+h.number.valueformat+h.number.suffix+h.number.prefix,d=l);if(h._hasDelta&&h._hasNumber){var I,L,C=[(l.left+l.right)/2,(l.top+l.bottom)/2],P=[(s.left+s.right)/2,(s.top+s.bottom)/2],B=.75*h.delta.font.size;"left"===h.delta.position&&(I=_(h,"deltaPos",0,-1*(l.width*m[h.align]+s.width*(1-m[h.align])+B),F,Math.min),L=C[1]-P[1],d={width:l.width+s.width+B,height:Math.max(l.height,s.height),left:s.left+I,right:l.right,top:Math.min(l.top,s.top+L),bottom:Math.max(l.bottom,s.bottom+L)}),"right"===h.delta.position&&(I=_(h,"deltaPos",0,l.width*(1-m[h.align])+s.width*m[h.align]+B,F,Math.max),L=C[1]-P[1],d={width:l.width+s.width+B,height:Math.max(l.height,s.height),left:l.left,right:s.right+I,top:Math.min(l.top,s.top+L),bottom:Math.max(l.bottom,s.bottom+L)}),"bottom"===h.delta.position&&(I=null,L=s.height,d={width:Math.max(l.width,s.width),height:l.height+s.height,left:Math.min(l.left,s.left),right:Math.max(l.right,s.right),top:l.bottom-l.height,bottom:l.bottom+s.height}),"top"===h.delta.position&&(I=null,L=l.top,d={width:Math.max(l.width,s.width),height:l.height+s.height,left:Math.min(l.left,s.left),right:Math.max(l.right,s.right),top:l.bottom-l.height-s.height,bottom:l.bottom}),O.attr({dx:I,dy:L})}(h._hasNumber||h._hasDelta)&&A.attr("transform",(function(){var e=r.numbersScaler(d);F+=e[2];var t,a=_(h,"numbersScale",1,e[0],F,Math.min);h._scaleNumbers||(a=1),t=h._isAngular?y-a*d.bottom:y-a*(d.top+d.bottom)/2,h._numbersTop=a*d.top+t;var i=d[w];"center"===w&&(i=(d.left+d.right)/2);var n=p-a*i;return T(n=_(h,"numbersTranslate",0,n,F,Math.max),t)+" scale("+a+")"}))}(e,j,t,{numbersX:d,numbersY:S,numbersScaler:M,transitionOpts:a,onComplete:h}),D&&(z={range:N.gauge.axis.range,color:N.gauge.bgcolor,line:{color:N.gauge.bordercolor,width:0},thickness:1},A={range:N.gauge.axis.range,color:"rgba(0, 0, 0, 0)",line:{color:N.gauge.bordercolor,width:N.gauge.borderwidth},thickness:1});var V=j.selectAll("g.angular").data(O?t:[]);V.exit().remove();var H=j.selectAll("g.angularaxis").data(O?t:[]);H.exit().remove(),O&&function(e,t,a,n){var o,s,c,d,h=a[0].trace,p=n.size,f=n.radius,g=n.innerRadius,m=n.gaugeBg,b=n.gaugeOutline,w=[p.l+p.w/2,p.t+p.h/2+f/2],k=n.gauge,_=n.layer,S=n.transitionOpts,M=n.onComplete,z=Math.PI/2;function A(e){var t=h.gauge.axis.range[0],a=(e-t)/(h.gauge.axis.range[1]-t)*Math.PI-z;return a<-z?-z:a>z?z:a}function N(e){return i.svg.arc().innerRadius((g+f)/2-e/2*(f-g)).outerRadius((g+f)/2+e/2*(f-g)).startAngle(-z)}function j(e){e.attr("d",(function(e){return N(e.thickness).startAngle(A(e.range[0])).endAngle(A(e.range[1]))()}))}k.enter().append("g").classed("angular",!0),k.attr("transform",T(w[0],w[1])),_.enter().append("g").classed("angularaxis",!0).classed("crisp",!0),_.selectAll("g.xangularaxistick,path,text").remove(),(o=x(e,h.gauge.axis)).type="linear",o.range=h.gauge.axis.range,o._id="xangularaxis",o.setScale();var D=function(e){return(o.range[0]-e.x)/(o.range[1]-o.range[0])*Math.PI+Math.PI},O={},F=u.makeLabelFns(o,0).labelStandoff;O.xFn=function(e){var t=D(e);return Math.cos(t)*F},O.yFn=function(e){var t=D(e),a=Math.sin(t)>0?.2:1;return-Math.sin(t)*(F+e.fontSize*a)+Math.abs(Math.cos(t))*(e.fontSize*l)},O.anchorFn=function(e){var t=D(e),a=Math.cos(t);return Math.abs(a)<.1?"middle":a>0?"start":"end"},O.heightFn=function(e,t,a){var i=D(e);return-.5*(1+Math.sin(i))*a};var I=function(e){return T(w[0]+f*Math.cos(e),w[1]-f*Math.sin(e))};c=function(e){return I(D(e))};if(s=u.calcTicks(o),d=u.getTickSigns(o)[2],o.visible){d="inside"===o.ticks?-1:1;var L=(o.linewidth||1)/2;u.drawTicks(e,o,{vals:s,layer:_,path:"M"+d*L+",0h"+d*o.ticklen,transFn:function(e){var t=D(e);return I(t)+"rotate("+-r(t)+")"}}),u.drawLabels(e,o,{vals:s,layer:_,transFn:c,labelFns:O})}var C=[m].concat(h.gauge.steps),P=k.selectAll("g.bg-arc").data(C);P.enter().append("g").classed("bg-arc",!0).append("path"),P.select("path").call(j).call(y),P.exit().remove();var B=N(h.gauge.bar.thickness),R=k.selectAll("g.value-arc").data([h.gauge.bar]);R.enter().append("g").classed("value-arc",!0).append("path");var E=R.select("path");v(S)?(E.transition().duration(S.duration).ease(S.easing).each("end",(function(){M&&M()})).each("interrupt",(function(){M&&M()})).attrTween("d",(G=B,Y=A(a[0].lastY),V=A(a[0].y),function(){var e=i.interpolate(Y,V);return function(t){return G.endAngle(e(t))()}})),h._lastValue=a[0].y):E.attr("d","number"==typeof a[0].y?B.endAngle(A(a[0].y)):"M0,0Z");var G,Y,V;E.call(y),R.exit().remove(),C=[];var H=h.gauge.threshold.value;H&&C.push({range:[H,H],color:h.gauge.threshold.color,line:{color:h.gauge.threshold.line.color,width:h.gauge.threshold.line.width},thickness:h.gauge.threshold.thickness});var J=k.selectAll("g.threshold-arc").data(C);J.enter().append("g").classed("threshold-arc",!0).append("path"),J.select("path").call(j).call(y),J.exit().remove();var X=k.selectAll("g.gauge-outline").data([b]);X.enter().append("g").classed("gauge-outline",!0).append("path"),X.select("path").call(j).call(y),X.exit().remove()}(e,0,t,{radius:B,innerRadius:R,gauge:V,layer:H,size:L,gaugeBg:z,gaugeOutline:A,transitionOpts:a,onComplete:h});var J=j.selectAll("g.bullet").data(F?t:[]);J.exit().remove();var X=j.selectAll("g.bulletaxis").data(F?t:[]);X.exit().remove(),F&&function(e,t,a,i){var n,r,l,o,c,d=a[0].trace,h=i.gauge,p=i.layer,g=i.gaugeBg,m=i.gaugeOutline,b=i.size,T=d.domain,w=i.transitionOpts,k=i.onComplete;h.enter().append("g").classed("bullet",!0),h.attr("transform","translate("+b.l+", "+b.t+")"),p.enter().append("g").classed("bulletaxis",!0).classed("crisp",!0),p.selectAll("g.xbulletaxistick,path,text").remove();var _=b.h,S=d.gauge.bar.thickness*_,M=T.x[0],z=T.x[0]+(T.x[1]-T.x[0])*(d._hasNumber||d._hasDelta?1-s.bulletNumberDomainSize:1);(n=x(e,d.gauge.axis))._id="xbulletaxis",n.domain=[M,z],n.setScale(),r=u.calcTicks(n),l=u.makeTransFn(n),o=u.getTickSigns(n)[2],c=b.t+b.h,n.visible&&(u.drawTicks(e,n,{vals:"inside"===n.ticks?u.clipEnds(n,r):r,layer:p,path:u.makeTickPath(n,c,o),transFn:l}),u.drawLabels(e,n,{vals:r,layer:p,transFn:l,labelFns:u.makeLabelFns(n,c)}));function A(e){e.attr("width",(function(e){return Math.max(0,n.c2p(e.range[1])-n.c2p(e.range[0]))})).attr("x",(function(e){return n.c2p(e.range[0])})).attr("y",(function(e){return.5*(1-e.thickness)*_})).attr("height",(function(e){return e.thickness*_}))}var N=[g].concat(d.gauge.steps),j=h.selectAll("g.bg-bullet").data(N);j.enter().append("g").classed("bg-bullet",!0).append("rect"),j.select("rect").call(A).call(y),j.exit().remove();var D=h.selectAll("g.value-bullet").data([d.gauge.bar]);D.enter().append("g").classed("value-bullet",!0).append("rect"),D.select("rect").attr("height",S).attr("y",(_-S)/2).call(y),v(w)?D.select("rect").transition().duration(w.duration).ease(w.easing).each("end",(function(){k&&k()})).each("interrupt",(function(){k&&k()})).attr("width",Math.max(0,n.c2p(Math.min(d.gauge.axis.range[1],a[0].y)))):D.select("rect").attr("width","number"==typeof a[0].y?Math.max(0,n.c2p(Math.min(d.gauge.axis.range[1],a[0].y))):0);D.exit().remove();var O=a.filter((function(){return d.gauge.threshold.value})),F=h.selectAll("g.threshold-bullet").data(O);F.enter().append("g").classed("threshold-bullet",!0).append("line"),F.select("line").attr("x1",n.c2p(d.gauge.threshold.value)).attr("x2",n.c2p(d.gauge.threshold.value)).attr("y1",(1-d.gauge.threshold.thickness)/2*_).attr("y2",(1-(1-d.gauge.threshold.thickness)/2)*_).call(f.stroke,d.gauge.threshold.line.color).style("stroke-width",d.gauge.threshold.line.width),F.exit().remove();var I=h.selectAll("g.gauge-outline").data([m]);I.enter().append("g").classed("gauge-outline",!0).append("rect"),I.select("rect").call(A).call(y),I.exit().remove()}(e,0,t,{gauge:J,layer:X,size:L,gaugeBg:z,gaugeOutline:A,transitionOpts:a,onComplete:h});var Z=j.selectAll("text.title").data(t);Z.exit().remove(),Z.enter().append("text").classed("title",!0),Z.attr("text-anchor",(function(){return F?g.right:g[N.title.align]})).text(N.title.text).call(o.font,N.title.font).call(c.convertToTspans,e),Z.attr("transform",(function(){var e,t=L.l+L.w*m[N.title.align],a=s.titlePadding,i=o.bBox(Z.node());if(D){if(O)if(N.gauge.axis.visible)e=o.bBox(H.node()).top-a-i.bottom;else e=L.t+L.h/2-B/2-i.bottom-a;F&&(e=S-(i.top+i.bottom)/2,t=L.l-s.bulletPadding*L.w)}else e=N._numbersTop-a-i.bottom;return T(t,e)}))}))}},400:function(e,t,a){"use strict";var i=a(387).extendFlat;t.attributes=function(e,t){t=t||{};var a={valType:"info_array",role:"info",editType:(e=e||{}).editType,items:[{valType:"number",min:0,max:1,editType:e.editType},{valType:"number",min:0,max:1,editType:e.editType}],dflt:[0,1]},n=e.name?e.name+" ":"",r=e.trace?"trace ":"subplot ",l=t.description?" "+t.description:"",o={x:i({},a,{description:["Sets the horizontal domain of this ",n,r,"(in plot fraction).",l].join("")}),y:i({},a,{description:["Sets the vertical domain of this ",n,r,"(in plot fraction).",l].join("")}),editType:e.editType};return e.noGridCell||(o.row={valType:"integer",min:0,dflt:0,role:"info",editType:e.editType,description:["If there is a layout grid, use the domain ","for this row in the grid for this ",n,r,".",l].join("")},o.column={valType:"integer",min:0,dflt:0,role:"info",editType:e.editType,description:["If there is a layout grid, use the domain ","for this column in the grid for this ",n,r,".",l].join("")}),o},t.defaults=function(e,t,a,i){var n=i&&i.x||[0,1],r=i&&i.y||[0,1],l=t.grid;if(l){var o=a("domain.column");void 0!==o&&(o<l.columns?n=l._domains.x[o]:delete e.domain.column);var s=a("domain.row");void 0!==s&&(s<l.rows?r=l._domains.y[s]:delete e.domain.row)}var c=a("domain.x",n),u=a("domain.y",r);c[0]<c[1]||(e.domain.x=n.slice()),u[0]<u[1]||(e.domain.y=r.slice())}},569:function(e,t,a){"use strict";e.exports={INCREASING:{COLOR:"#3D9970",SYMBOL:"▲"},DECREASING:{COLOR:"#FF4136",SYMBOL:"▼"}}}}]);