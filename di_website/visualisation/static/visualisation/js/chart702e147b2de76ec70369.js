(window.webpackJsonp=window.webpackJsonp||[]).push([[10],{1029:function(e,t,r){"use strict";var n=r(6),a=r(57),i=r(665),o=r(915);function l(e){return e.data.data.pid}t.findEntryWithLevel=function(e,r){var n;return r&&e.eachAfter((function(e){if(t.getPtId(e)===r)return n=e.copy()})),n||e},t.findEntryWithChild=function(e,r){var n;return e.eachAfter((function(e){for(var a=e.children||[],i=0;i<a.length;i++){var o=a[i];if(t.getPtId(o)===r)return n=e.copy()}})),n||e},t.isEntry=function(e){return!e.parent},t.isLeaf=function(e){return!e.children},t.getPtId=function(e){return e.data.data.id},t.getPtLabel=function(e){return e.data.data.label},t.getValue=function(e){return e.value},t.isHierarchyRoot=function(e){return""===l(e)},t.setSliceCursor=function(e,r,n){var a=n.isTransitioning;if(!a){var o=e.datum();a=n.hideOnRoot&&t.isHierarchyRoot(o)||n.hideOnLeaves&&t.isLeaf(o)}i(e,a?null:"pointer")},t.getInsideTextFontKey=function(e,t,r,a,i){var o=(i||{}).onPathbar?"pathbar.textfont":"insidetextfont",l=r.data.data.i;return n.castOption(t,l,o+"."+e)||n.castOption(t,l,"textfont."+e)||a.size},t.getOutsideTextFontKey=function(e,t,r,a){var i=r.data.data.i;return n.castOption(t,i,"outsidetextfont."+e)||n.castOption(t,i,"textfont."+e)||a.size},t.isOutsideText=function(e,r){return!e._hasColorscale&&t.isHierarchyRoot(r)},t.determineTextFont=function(e,r,i,o){return t.isOutsideText(e,r)?function(e,r,n){return{color:t.getOutsideTextFontKey("color",e,r,n),family:t.getOutsideTextFontKey("family",e,r,n),size:t.getOutsideTextFontKey("size",e,r,n)}}(e,r,i):function(e,r,i,o){var l=(o||{}).onPathbar,u=r.data.data,c=u.i,s=n.castOption(e,c,(l?"pathbar.textfont":"insidetextfont")+".color");return!s&&e._input.textfont&&(s=n.castOption(e._input,c,"textfont.color")),{color:s||a.contrast(u.color),family:t.getInsideTextFontKey("family",e,r,i,o),size:t.getInsideTextFontKey("size",e,r,i,o)}}(e,r,i,o)},t.hasTransition=function(e){return!!(e&&e.duration>0)},t.getMaxDepth=function(e){return e.maxdepth>=0?e.maxdepth:1/0},t.isHeader=function(e,r){return!(t.isLeaf(e)||e.depth===r._maxDepth-1)},t.getParent=function(e,r){return t.findEntryWithLevel(e,l(r))},t.listPath=function(e,r){var n=e.parent;if(!n)return[];var a=r?[n.data[r]]:[n];return t.listPath(n,r).concat(a)},t.getPath=function(e){return t.listPath(e,"label").join("/")+"/"},t.formatValue=o.formatPieValue,t.formatPercent=function(e,t){var r=n.formatPercent(e,0);return"0%"===r&&(r=o.formatPiePercent(e,t)),r}},1309:function(e,t,r){"use strict";var n=r(59),a=r(150).hovertemplateAttrs,i=r(150).texttemplateAttrs,o=r(111),l=r(624).attributes,u=r(769),c=r(1635),s=r(32).extendFlat;e.exports={labels:{valType:"data_array",editType:"calc",description:["Sets the labels of each of the sectors."].join(" ")},parents:{valType:"data_array",editType:"calc",description:["Sets the parent sectors for each of the sectors.","Empty string items '' are understood to reference","the root node in the hierarchy.",'If `ids` is filled, `parents` items are understood to be "ids" themselves.',"When `ids` is not set, plotly attempts to find matching items in `labels`,","but beware they must be unique."].join(" ")},values:{valType:"data_array",editType:"calc",description:["Sets the values associated with each of the sectors.","Use with `branchvalues` to determine how the values are summed."].join(" ")},branchvalues:{valType:"enumerated",values:["remainder","total"],dflt:"remainder",editType:"calc",role:"info",description:["Determines how the items in `values` are summed.","When set to *total*, items in `values` are taken to be value of all its descendants.","When set to *remainder*, items in `values` corresponding to the root and the branches sectors","are taken to be the extra part not part of the sum of the values at their leaves."].join(" ")},count:{valType:"flaglist",flags:["branches","leaves"],dflt:"leaves",editType:"calc",role:"info",description:["Determines default for `values` when it is not provided,","by inferring a 1 for each of the *leaves* and/or *branches*, otherwise 0."].join(" ")},level:{valType:"any",editType:"plot",anim:!0,role:"info",description:["Sets the level from which this trace hierarchy is rendered.","Set `level` to `''` to start from the root node in the hierarchy.",'Must be an "id" if `ids` is filled in, otherwise plotly attempts to find a matching',"item in `labels`."].join(" ")},maxdepth:{valType:"integer",editType:"plot",role:"info",dflt:-1,description:["Sets the number of rendered sectors from any given `level`.","Set `maxdepth` to *-1* to render all the levels in the hierarchy."].join(" ")},marker:s({colors:{valType:"data_array",editType:"calc",description:["Sets the color of each sector of this trace.","If not specified, the default trace color set is used","to pick the sector colors."].join(" ")},line:{color:s({},u.marker.line.color,{dflt:null,description:["Sets the color of the line enclosing each sector.","Defaults to the `paper_bgcolor` value."].join(" ")}),width:s({},u.marker.line.width,{dflt:1}),editType:"calc"},editType:"calc"},o("marker",{colorAttr:"colors",anim:!1})),leaf:{opacity:{valType:"number",editType:"style",role:"style",min:0,max:1,description:["Sets the opacity of the leaves. With colorscale","it is defaulted to 1; otherwise it is defaulted to 0.7"].join(" ")},editType:"plot"},text:u.text,textinfo:{valType:"flaglist",role:"info",flags:["label","text","value","current path","percent root","percent entry","percent parent"],extras:["none"],editType:"plot",description:["Determines which trace information appear on the graph."].join(" ")},texttemplate:i({editType:"plot"},{keys:c.eventDataKeys.concat(["label","value"])}),hovertext:u.hovertext,hoverinfo:s({},n.hoverinfo,{flags:["label","text","value","name","current path","percent root","percent entry","percent parent"],dflt:"label+text+value+name"}),hovertemplate:a({},{keys:c.eventDataKeys}),textfont:u.textfont,insidetextorientation:u.insidetextorientation,insidetextfont:u.insidetextfont,outsidetextfont:s({},u.outsidetextfont,{description:["Sets the font used for `textinfo` lying outside the sector.","This option refers to the root of the hierarchy","presented at the center of a sunburst graph.","Please note that if a hierarchy has multiple root nodes,","this option won't have any effect and `insidetextfont` would be used."].join(" ")}),domain:l({name:"sunburst",trace:!0,editType:"calc"})}},1310:function(e,t,r){"use strict";var n=r(1314),a=r(12),i=r(6),o=r(208).makeColorScaleFuncFromTrace,l=r(790).makePullColorFn,u=r(790).generateExtendedColors,c=r(208).calc,s=r(25).ALMOST_EQUAL,f={},h={};t.calc=function(e,t){var r,u,f,h,d,p,v=e._fullLayout,x=t.ids,y=i.isArrayOrTypedArray(x),m=t.labels,g=t.parents,b=t.values,_=i.isArrayOrTypedArray(b),T=[],P={},w={},A=function(e){return e||"number"==typeof e},I=function(e){return!_||a(b[e])&&b[e]>=0};y?(r=Math.min(x.length,g.length),u=function(e){return A(x[e])&&I(e)},f=function(e){return String(x[e])}):(r=Math.min(m.length,g.length),u=function(e){return A(m[e])&&I(e)},f=function(e){return String(m[e])}),_&&(r=Math.min(r,b.length));for(var M=0;M<r;M++)if(u(M)){var S=f(M),L=A(g[M])?String(g[M]):"",O={i:M,id:S,pid:L,label:A(m[M])?String(m[M]):""};_&&(O.v=+b[M]),T.push(O),d=S,P[h=L]?P[h].push(d):P[h]=[d],w[d]=1}if(P[""]){if(P[""].length>1){for(var z=i.randstr(),E=0;E<T.length;E++)""===T[E].pid&&(T[E].pid=z);T.unshift({hasMultipleRoots:!0,id:z,pid:"",label:""})}}else{var C,k=[];for(C in P)w[C]||k.push(C);if(1!==k.length)return i.warn("Multiple implied roots, cannot build "+t.type+" hierarchy.");C=k[0],T.unshift({hasImpliedRoot:!0,id:C,pid:"",label:C})}try{p=n.stratify().id((function(e){return e.id})).parentId((function(e){return e.pid}))(T)}catch(e){return i.warn("Failed to build "+t.type+" hierarchy. Error: "+e.message)}var R=n.hierarchy(p),V=!1;if(_)switch(t.branchvalues){case"remainder":R.sum((function(e){return e.data.v}));break;case"total":R.each((function(e){var t=e.data.data,r=t.v;if(e.children){var n=e.children.reduce((function(e,t){return e+t.data.data.v}),0);if((t.hasImpliedRoot||t.hasMultipleRoots)&&(r=n),r<n*s)return V=!0,i.warn(["Total value for node",e.data.data.id,"is smaller than the sum of its children.","\nparent value =",r,"\nchildren sum =",n].join(" "))}e.value=r}))}else!function e(t,r,n){var a=0,i=t.children;if(i){for(var o=i.length,l=0;l<o;l++)a+=e(i[l],r,n);n.branches&&a++}else n.leaves&&a++;t.value=t.data.data.value=a,r._values||(r._values=[]);return r._values[t.data.data.i]=a,a}(R,t,{branches:-1!==t.count.indexOf("branches"),leaves:-1!==t.count.indexOf("leaves")});if(!V){var D,B;R.sort((function(e,t){return t.value-e.value}));var F=t.marker.colors||[],H=!!F.length;return t._hasColorscale?(H||(F=_?t.values:t._values),c(e,t,{vals:F,containerStr:"marker",cLetter:"c"}),B=o(t.marker)):D=l(v["_"+t.type+"colormap"]),R.each((function(e){var r=e.data.data;r.color=t._hasColorscale?B(F[r.i]):D(F[r.i],r.id)})),T[0].hierarchy=R,T}},t._runCrossTraceCalc=function(e,t){var r=t._fullLayout,n=t.calcdata,a=r[e+"colorway"],i=r["_"+e+"colormap"];r["extend"+e+"colors"]&&(a=u(a,"treemap"===e?h:f));var o=0;function l(e){var t=e.data.data,r=t.id;!1===t.color&&(i[r]?t.color=i[r]:e.parent?e.parent.parent?t.color=e.parent.data.data.color:(i[r]=t.color=a[o%a.length],o++):t.color="rgba(0,0,0,0)")}for(var c=0;c<n.length;c++){var s=n[c][0];s.trace.type===e&&s.hierarchy&&s.hierarchy.each(l)}},t.crossTraceCalc=function(e){return t._runCrossTraceCalc("sunburst",e)}},1311:function(e,t,r){"use strict";var n=r(24),a=r(23),i=r(215).appendArrayPointValue,o=r(623),l=r(6),u=r(895),c=r(1029),s=r(915).formatPieValue;function f(e,t,r){for(var n=e.data.data,a={curveNumber:t.index,pointNumber:n.i,data:t._input,fullData:t},o=0;o<r.length;o++){var l=r[o];l in e&&(a[l]=e[l])}return"parentString"in e&&!c.isHierarchyRoot(e)&&(a.parent=e.parentString),i(a,t,n.i),a}e.exports=function(e,t,r,i,h){var d=i[0],p=d.trace,v=d.hierarchy,x="sunburst"===p.type,y="treemap"===p.type;"_hasHoverLabel"in p||(p._hasHoverLabel=!1),"_hasHoverEvent"in p||(p._hasHoverEvent=!1);e.on("mouseover",(function(a){var i=r._fullLayout;if(!r._dragging&&!1!==i.hovermode){var u=r._fullData[p.index],m=a.data.data,g=m.i,b=c.isHierarchyRoot(a),_=c.getParent(v,a),T=c.getValue(a),P=function(e){return l.castOption(u,g,e)},w=P("hovertemplate"),A=o.castHoverinfo(u,i,g),I=i.separators;if(w||A&&"none"!==A&&"skip"!==A){var M,S;x&&(M=d.cx+a.pxmid[0]*(1-a.rInscribed),S=d.cy+a.pxmid[1]*(1-a.rInscribed)),y&&(M=a._hoverX,S=a._hoverY);var L,O={},z=[],E=[],C=function(e){return-1!==z.indexOf(e)};A&&(z="all"===A?u._module.attributes.hoverinfo.flags:A.split("+")),O.label=m.label,C("label")&&O.label&&E.push(O.label),m.hasOwnProperty("v")&&(O.value=m.v,O.valueLabel=s(O.value,I),C("value")&&E.push(O.valueLabel)),O.currentPath=a.currentPath=c.getPath(a.data),C("current path")&&!b&&E.push(O.currentPath);var k=[],R=function(){-1===k.indexOf(L)&&(E.push(L),k.push(L))};O.percentParent=a.percentParent=T/c.getValue(_),O.parent=a.parentString=c.getPtLabel(_),C("percent parent")&&(L=c.formatPercent(O.percentParent,I)+" of "+O.parent,R()),O.percentEntry=a.percentEntry=T/c.getValue(t),O.entry=a.entry=c.getPtLabel(t),!C("percent entry")||b||a.onPathbar||(L=c.formatPercent(O.percentEntry,I)+" of "+O.entry,R()),O.percentRoot=a.percentRoot=T/c.getValue(v),O.root=a.root=c.getPtLabel(v),C("percent root")&&!b&&(L=c.formatPercent(O.percentRoot,I)+" of "+O.root,R()),O.text=P("hovertext")||P("text"),C("text")&&(L=O.text,l.isValidTextValue(L)&&E.push(L));var V={trace:u,y:S,text:E.join("<br>"),name:w||C("name")?u.name:void 0,color:P("hoverlabel.bgcolor")||m.color,borderColor:P("hoverlabel.bordercolor"),fontFamily:P("hoverlabel.font.family"),fontSize:P("hoverlabel.font.size"),fontColor:P("hoverlabel.font.color"),nameLength:P("hoverlabel.namelength"),textAlign:P("hoverlabel.align"),hovertemplate:w,hovertemplateLabels:O,eventData:[f(a,u,h.eventDataKeys)]};x&&(V.x0=M-a.rInscribed*a.rpx1,V.x1=M+a.rInscribed*a.rpx1,V.idealAlign=a.pxmid[0]<0?"left":"right"),y&&(V.x=M,V.idealAlign=M<0?"left":"right"),o.loneHover(V,{container:i._hoverlayer.node(),outerContainer:i._paper.node(),gd:r}),p._hasHoverLabel=!0}if(y){var D=e.select("path.surface");h.styleOne(D,a,u,{hovered:!0})}p._hasHoverEvent=!0,r.emit("plotly_hover",{points:[f(a,u,h.eventDataKeys)],event:n.event})}})),e.on("mouseout",(function(t){var a=r._fullLayout,i=r._fullData[p.index],l=n.select(this).datum();if(p._hasHoverEvent&&(t.originalEvent=n.event,r.emit("plotly_unhover",{points:[f(l,i,h.eventDataKeys)],event:n.event}),p._hasHoverEvent=!1),p._hasHoverLabel&&(o.loneUnhover(a._hoverlayer.node()),p._hasHoverLabel=!1),y){var u=e.select("path.surface");h.styleOne(u,l,i,{hovered:!1})}})),e.on("click",(function(e){var t=r._fullLayout,i=r._fullData[p.index],l=x&&(c.isHierarchyRoot(e)||c.isLeaf(e)),s=c.getPtId(e),d=c.isEntry(e)?c.findEntryWithChild(v,s):c.findEntryWithLevel(v,s),y=c.getPtId(d),m={points:[f(e,i,h.eventDataKeys)],event:n.event};l||(m.nextLevel=y);var g=u.triggerHandler(r,"plotly_"+p.type+"click",m);if(!1!==g&&t.hovermode&&(r._hoverdata=[f(e,i,h.eventDataKeys)],o.click(r,n.event)),!l&&!1!==g&&!r._dragging&&!r._transitioning){a.call("_storeDirectGUIEdit",i,t._tracePreGUI[i.uid],{level:i.level});var b={data:[{level:y}],traces:[p.index]},_={frame:{redraw:!1,duration:h.transitionTime},transition:{duration:h.transitionTime,easing:h.transitionEasing},mode:"immediate",fromcurrent:!0};o.loneUnhover(t._hoverlayer.node()),a.call("animate",r,b,_)}}))}},1314:function(e,t,r){"use strict";function n(e,t){return e.parent===t.parent?1:2}function a(e,t){return e+t.x}function i(e,t){return Math.max(e,t.y)}r.r(t),r.d(t,"cluster",(function(){return o})),r.d(t,"hierarchy",(function(){return u})),r.d(t,"pack",(function(){return C})),r.d(t,"packSiblings",(function(){return M})),r.d(t,"packEnclose",(function(){return p})),r.d(t,"partition",(function(){return F})),r.d(t,"stratify",(function(){return q})),r.d(t,"tree",(function(){return $})),r.d(t,"treemap",(function(){return re})),r.d(t,"treemapBinary",(function(){return ne})),r.d(t,"treemapDice",(function(){return B})),r.d(t,"treemapSlice",(function(){return Q})),r.d(t,"treemapSliceDice",(function(){return ae})),r.d(t,"treemapSquarify",(function(){return te})),r.d(t,"treemapResquarify",(function(){return ie}));var o=function(){var e=n,t=1,r=1,o=!1;function l(n){var l,u=0;n.eachAfter((function(t){var r=t.children;r?(t.x=function(e){return e.reduce(a,0)/e.length}(r),t.y=function(e){return 1+e.reduce(i,0)}(r)):(t.x=l?u+=e(t,l):0,t.y=0,l=t)}));var c=function(e){for(var t;t=e.children;)e=t[0];return e}(n),s=function(e){for(var t;t=e.children;)e=t[t.length-1];return e}(n),f=c.x-e(c,s)/2,h=s.x+e(s,c)/2;return n.eachAfter(o?function(e){e.x=(e.x-n.x)*t,e.y=(n.y-e.y)*r}:function(e){e.x=(e.x-f)/(h-f)*t,e.y=(1-(n.y?e.y/n.y:1))*r})}return l.separation=function(t){return arguments.length?(e=t,l):e},l.size=function(e){return arguments.length?(o=!1,t=+e[0],r=+e[1],l):o?null:[t,r]},l.nodeSize=function(e){return arguments.length?(o=!0,t=+e[0],r=+e[1],l):o?[t,r]:null},l};function l(e){var t=0,r=e.children,n=r&&r.length;if(n)for(;--n>=0;)t+=r[n].value;else t=1;e.value=t}function u(e,t){var r,n,a,i,o,l=new h(e),u=+e.value&&(l.value=e.value),s=[l];for(null==t&&(t=c);r=s.pop();)if(u&&(r.value=+r.data.value),(a=t(r.data))&&(o=a.length))for(r.children=new Array(o),i=o-1;i>=0;--i)s.push(n=r.children[i]=new h(a[i])),n.parent=r,n.depth=r.depth+1;return l.eachBefore(f)}function c(e){return e.children}function s(e){e.data=e.data.data}function f(e){var t=0;do{e.height=t}while((e=e.parent)&&e.height<++t)}function h(e){this.data=e,this.depth=this.height=0,this.parent=null}h.prototype=u.prototype={constructor:h,count:function(){return this.eachAfter(l)},each:function(e){var t,r,n,a,i=this,o=[i];do{for(t=o.reverse(),o=[];i=t.pop();)if(e(i),r=i.children)for(n=0,a=r.length;n<a;++n)o.push(r[n])}while(o.length);return this},eachAfter:function(e){for(var t,r,n,a=this,i=[a],o=[];a=i.pop();)if(o.push(a),t=a.children)for(r=0,n=t.length;r<n;++r)i.push(t[r]);for(;a=o.pop();)e(a);return this},eachBefore:function(e){for(var t,r,n=this,a=[n];n=a.pop();)if(e(n),t=n.children)for(r=t.length-1;r>=0;--r)a.push(t[r]);return this},sum:function(e){return this.eachAfter((function(t){for(var r=+e(t.data)||0,n=t.children,a=n&&n.length;--a>=0;)r+=n[a].value;t.value=r}))},sort:function(e){return this.eachBefore((function(t){t.children&&t.children.sort(e)}))},path:function(e){for(var t=this,r=function(e,t){if(e===t)return e;var r=e.ancestors(),n=t.ancestors(),a=null;e=r.pop(),t=n.pop();for(;e===t;)a=e,e=r.pop(),t=n.pop();return a}(t,e),n=[t];t!==r;)t=t.parent,n.push(t);for(var a=n.length;e!==r;)n.splice(a,0,e),e=e.parent;return n},ancestors:function(){for(var e=this,t=[e];e=e.parent;)t.push(e);return t},descendants:function(){var e=[];return this.each((function(t){e.push(t)})),e},leaves:function(){var e=[];return this.eachBefore((function(t){t.children||e.push(t)})),e},links:function(){var e=this,t=[];return e.each((function(r){r!==e&&t.push({source:r.parent,target:r})})),t},copy:function(){return u(this).eachBefore(s)}};var d=Array.prototype.slice;var p=function(e){for(var t,r,n=0,a=(e=function(e){for(var t,r,n=e.length;n;)r=Math.random()*n--|0,t=e[n],e[n]=e[r],e[r]=t;return e}(d.call(e))).length,i=[];n<a;)t=e[n],r&&y(r,t)?++n:(r=g(i=v(i,t)),n=0);return r};function v(e,t){var r,n;if(m(t,e))return[t];for(r=0;r<e.length;++r)if(x(t,e[r])&&m(b(e[r],t),e))return[e[r],t];for(r=0;r<e.length-1;++r)for(n=r+1;n<e.length;++n)if(x(b(e[r],e[n]),t)&&x(b(e[r],t),e[n])&&x(b(e[n],t),e[r])&&m(_(e[r],e[n],t),e))return[e[r],e[n],t];throw new Error}function x(e,t){var r=e.r-t.r,n=t.x-e.x,a=t.y-e.y;return r<0||r*r<n*n+a*a}function y(e,t){var r=e.r-t.r+1e-6,n=t.x-e.x,a=t.y-e.y;return r>0&&r*r>n*n+a*a}function m(e,t){for(var r=0;r<t.length;++r)if(!y(e,t[r]))return!1;return!0}function g(e){switch(e.length){case 1:return{x:(t=e[0]).x,y:t.y,r:t.r};case 2:return b(e[0],e[1]);case 3:return _(e[0],e[1],e[2])}var t}function b(e,t){var r=e.x,n=e.y,a=e.r,i=t.x,o=t.y,l=t.r,u=i-r,c=o-n,s=l-a,f=Math.sqrt(u*u+c*c);return{x:(r+i+u/f*s)/2,y:(n+o+c/f*s)/2,r:(f+a+l)/2}}function _(e,t,r){var n=e.x,a=e.y,i=e.r,o=t.x,l=t.y,u=t.r,c=r.x,s=r.y,f=r.r,h=n-o,d=n-c,p=a-l,v=a-s,x=u-i,y=f-i,m=n*n+a*a-i*i,g=m-o*o-l*l+u*u,b=m-c*c-s*s+f*f,_=d*p-h*v,T=(p*b-v*g)/(2*_)-n,P=(v*x-p*y)/_,w=(d*g-h*b)/(2*_)-a,A=(h*y-d*x)/_,I=P*P+A*A-1,M=2*(i+T*P+w*A),S=T*T+w*w-i*i,L=-(I?(M+Math.sqrt(M*M-4*I*S))/(2*I):S/M);return{x:n+T+P*L,y:a+w+A*L,r:L}}function T(e,t,r){var n,a,i,o,l=e.x-t.x,u=e.y-t.y,c=l*l+u*u;c?(a=t.r+r.r,a*=a,o=e.r+r.r,a>(o*=o)?(n=(c+o-a)/(2*c),i=Math.sqrt(Math.max(0,o/c-n*n)),r.x=e.x-n*l-i*u,r.y=e.y-n*u+i*l):(n=(c+a-o)/(2*c),i=Math.sqrt(Math.max(0,a/c-n*n)),r.x=t.x+n*l-i*u,r.y=t.y+n*u+i*l)):(r.x=t.x+r.r,r.y=t.y)}function P(e,t){var r=e.r+t.r-1e-6,n=t.x-e.x,a=t.y-e.y;return r>0&&r*r>n*n+a*a}function w(e){var t=e._,r=e.next._,n=t.r+r.r,a=(t.x*r.r+r.x*t.r)/n,i=(t.y*r.r+r.y*t.r)/n;return a*a+i*i}function A(e){this._=e,this.next=null,this.previous=null}function I(e){if(!(a=e.length))return 0;var t,r,n,a,i,o,l,u,c,s,f;if((t=e[0]).x=0,t.y=0,!(a>1))return t.r;if(r=e[1],t.x=-r.r,r.x=t.r,r.y=0,!(a>2))return t.r+r.r;T(r,t,n=e[2]),t=new A(t),r=new A(r),n=new A(n),t.next=n.previous=r,r.next=t.previous=n,n.next=r.previous=t;e:for(l=3;l<a;++l){T(t._,r._,n=e[l]),n=new A(n),u=r.next,c=t.previous,s=r._.r,f=t._.r;do{if(s<=f){if(P(u._,n._)){r=u,t.next=r,r.previous=t,--l;continue e}s+=u._.r,u=u.next}else{if(P(c._,n._)){(t=c).next=r,r.previous=t,--l;continue e}f+=c._.r,c=c.previous}}while(u!==c.next);for(n.previous=t,n.next=r,t.next=r.previous=r=n,i=w(t);(n=n.next)!==r;)(o=w(n))<i&&(t=n,i=o);r=t.next}for(t=[r._],n=r;(n=n.next)!==r;)t.push(n._);for(n=p(t),l=0;l<a;++l)(t=e[l]).x-=n.x,t.y-=n.y;return n.r}var M=function(e){return I(e),e};function S(e){return null==e?null:L(e)}function L(e){if("function"!=typeof e)throw new Error;return e}function O(){return 0}var z=function(e){return function(){return e}};function E(e){return Math.sqrt(e.value)}var C=function(){var e=null,t=1,r=1,n=O;function a(a){return a.x=t/2,a.y=r/2,e?a.eachBefore(k(e)).eachAfter(R(n,.5)).eachBefore(V(1)):a.eachBefore(k(E)).eachAfter(R(O,1)).eachAfter(R(n,a.r/Math.min(t,r))).eachBefore(V(Math.min(t,r)/(2*a.r))),a}return a.radius=function(t){return arguments.length?(e=S(t),a):e},a.size=function(e){return arguments.length?(t=+e[0],r=+e[1],a):[t,r]},a.padding=function(e){return arguments.length?(n="function"==typeof e?e:z(+e),a):n},a};function k(e){return function(t){t.children||(t.r=Math.max(0,+e(t)||0))}}function R(e,t){return function(r){if(n=r.children){var n,a,i,o=n.length,l=e(r)*t||0;if(l)for(a=0;a<o;++a)n[a].r+=l;if(i=I(n),l)for(a=0;a<o;++a)n[a].r-=l;r.r=i+l}}}function V(e){return function(t){var r=t.parent;t.r*=e,r&&(t.x=r.x+e*t.x,t.y=r.y+e*t.y)}}var D=function(e){e.x0=Math.round(e.x0),e.y0=Math.round(e.y0),e.x1=Math.round(e.x1),e.y1=Math.round(e.y1)},B=function(e,t,r,n,a){for(var i,o=e.children,l=-1,u=o.length,c=e.value&&(n-t)/e.value;++l<u;)(i=o[l]).y0=r,i.y1=a,i.x0=t,i.x1=t+=i.value*c},F=function(){var e=1,t=1,r=0,n=!1;function a(a){var i=a.height+1;return a.x0=a.y0=r,a.x1=e,a.y1=t/i,a.eachBefore(function(e,t){return function(n){n.children&&B(n,n.x0,e*(n.depth+1)/t,n.x1,e*(n.depth+2)/t);var a=n.x0,i=n.y0,o=n.x1-r,l=n.y1-r;o<a&&(a=o=(a+o)/2),l<i&&(i=l=(i+l)/2),n.x0=a,n.y0=i,n.x1=o,n.y1=l}}(t,i)),n&&a.eachBefore(D),a}return a.round=function(e){return arguments.length?(n=!!e,a):n},a.size=function(r){return arguments.length?(e=+r[0],t=+r[1],a):[e,t]},a.padding=function(e){return arguments.length?(r=+e,a):r},a},H={depth:-1},K={};function j(e){return e.id}function N(e){return e.parentId}var q=function(){var e=j,t=N;function r(r){var n,a,i,o,l,u,c,s=r.length,d=new Array(s),p={};for(a=0;a<s;++a)n=r[a],l=d[a]=new h(n),null!=(u=e(n,a,r))&&(u+="")&&(p[c="$"+(l.id=u)]=c in p?K:l);for(a=0;a<s;++a)if(l=d[a],null!=(u=t(r[a],a,r))&&(u+="")){if(!(o=p["$"+u]))throw new Error("missing: "+u);if(o===K)throw new Error("ambiguous: "+u);o.children?o.children.push(l):o.children=[l],l.parent=o}else{if(i)throw new Error("multiple roots");i=l}if(!i)throw new Error("no root");if(i.parent=H,i.eachBefore((function(e){e.depth=e.parent.depth+1,--s})).eachBefore(f),i.parent=null,s>0)throw new Error("cycle");return i}return r.id=function(t){return arguments.length?(e=L(t),r):e},r.parentId=function(e){return arguments.length?(t=L(e),r):t},r};function W(e,t){return e.parent===t.parent?1:2}function U(e){var t=e.children;return t?t[0]:e.t}function G(e){var t=e.children;return t?t[t.length-1]:e.t}function X(e,t,r){var n=r/(t.i-e.i);t.c-=n,t.s+=r,e.c+=n,t.z+=r,t.m+=r}function Y(e,t,r){return e.a.parent===t.parent?e.a:r}function J(e,t){this._=e,this.parent=null,this.children=null,this.A=null,this.a=this,this.z=0,this.m=0,this.c=0,this.s=0,this.t=null,this.i=t}J.prototype=Object.create(h.prototype);var $=function(){var e=W,t=1,r=1,n=null;function a(a){var u=function(e){for(var t,r,n,a,i,o=new J(e,0),l=[o];t=l.pop();)if(n=t._.children)for(t.children=new Array(i=n.length),a=i-1;a>=0;--a)l.push(r=t.children[a]=new J(n[a],a)),r.parent=t;return(o.parent=new J(null,0)).children=[o],o}(a);if(u.eachAfter(i),u.parent.m=-u.z,u.eachBefore(o),n)a.eachBefore(l);else{var c=a,s=a,f=a;a.eachBefore((function(e){e.x<c.x&&(c=e),e.x>s.x&&(s=e),e.depth>f.depth&&(f=e)}));var h=c===s?1:e(c,s)/2,d=h-c.x,p=t/(s.x+h+d),v=r/(f.depth||1);a.eachBefore((function(e){e.x=(e.x+d)*p,e.y=e.depth*v}))}return a}function i(t){var r=t.children,n=t.parent.children,a=t.i?n[t.i-1]:null;if(r){!function(e){for(var t,r=0,n=0,a=e.children,i=a.length;--i>=0;)(t=a[i]).z+=r,t.m+=r,r+=t.s+(n+=t.c)}(t);var i=(r[0].z+r[r.length-1].z)/2;a?(t.z=a.z+e(t._,a._),t.m=t.z-i):t.z=i}else a&&(t.z=a.z+e(t._,a._));t.parent.A=function(t,r,n){if(r){for(var a,i=t,o=t,l=r,u=i.parent.children[0],c=i.m,s=o.m,f=l.m,h=u.m;l=G(l),i=U(i),l&&i;)u=U(u),(o=G(o)).a=t,(a=l.z+f-i.z-c+e(l._,i._))>0&&(X(Y(l,t,n),t,a),c+=a,s+=a),f+=l.m,c+=i.m,h+=u.m,s+=o.m;l&&!G(o)&&(o.t=l,o.m+=f-s),i&&!U(u)&&(u.t=i,u.m+=c-h,n=t)}return n}(t,a,t.parent.A||n[0])}function o(e){e._.x=e.z+e.parent.m,e.m+=e.parent.m}function l(e){e.x*=t,e.y=e.depth*r}return a.separation=function(t){return arguments.length?(e=t,a):e},a.size=function(e){return arguments.length?(n=!1,t=+e[0],r=+e[1],a):n?null:[t,r]},a.nodeSize=function(e){return arguments.length?(n=!0,t=+e[0],r=+e[1],a):n?[t,r]:null},a},Q=function(e,t,r,n,a){for(var i,o=e.children,l=-1,u=o.length,c=e.value&&(a-r)/e.value;++l<u;)(i=o[l]).x0=t,i.x1=n,i.y0=r,i.y1=r+=i.value*c},Z=(1+Math.sqrt(5))/2;function ee(e,t,r,n,a,i){for(var o,l,u,c,s,f,h,d,p,v,x,y=[],m=t.children,g=0,b=0,_=m.length,T=t.value;g<_;){u=a-r,c=i-n;do{s=m[b++].value}while(!s&&b<_);for(f=h=s,x=s*s*(v=Math.max(c/u,u/c)/(T*e)),p=Math.max(h/x,x/f);b<_;++b){if(s+=l=m[b].value,l<f&&(f=l),l>h&&(h=l),x=s*s*v,(d=Math.max(h/x,x/f))>p){s-=l;break}p=d}y.push(o={value:s,dice:u<c,children:m.slice(g,b)}),o.dice?B(o,r,n,a,T?n+=c*s/T:i):Q(o,r,n,T?r+=u*s/T:a,i),T-=s,g=b}return y}var te=function e(t){function r(e,r,n,a,i){ee(t,e,r,n,a,i)}return r.ratio=function(t){return e((t=+t)>1?t:1)},r}(Z),re=function(){var e=te,t=!1,r=1,n=1,a=[0],i=O,o=O,l=O,u=O,c=O;function s(e){return e.x0=e.y0=0,e.x1=r,e.y1=n,e.eachBefore(f),a=[0],t&&e.eachBefore(D),e}function f(t){var r=a[t.depth],n=t.x0+r,s=t.y0+r,f=t.x1-r,h=t.y1-r;f<n&&(n=f=(n+f)/2),h<s&&(s=h=(s+h)/2),t.x0=n,t.y0=s,t.x1=f,t.y1=h,t.children&&(r=a[t.depth+1]=i(t)/2,n+=c(t)-r,s+=o(t)-r,(f-=l(t)-r)<n&&(n=f=(n+f)/2),(h-=u(t)-r)<s&&(s=h=(s+h)/2),e(t,n,s,f,h))}return s.round=function(e){return arguments.length?(t=!!e,s):t},s.size=function(e){return arguments.length?(r=+e[0],n=+e[1],s):[r,n]},s.tile=function(t){return arguments.length?(e=L(t),s):e},s.padding=function(e){return arguments.length?s.paddingInner(e).paddingOuter(e):s.paddingInner()},s.paddingInner=function(e){return arguments.length?(i="function"==typeof e?e:z(+e),s):i},s.paddingOuter=function(e){return arguments.length?s.paddingTop(e).paddingRight(e).paddingBottom(e).paddingLeft(e):s.paddingTop()},s.paddingTop=function(e){return arguments.length?(o="function"==typeof e?e:z(+e),s):o},s.paddingRight=function(e){return arguments.length?(l="function"==typeof e?e:z(+e),s):l},s.paddingBottom=function(e){return arguments.length?(u="function"==typeof e?e:z(+e),s):u},s.paddingLeft=function(e){return arguments.length?(c="function"==typeof e?e:z(+e),s):c},s},ne=function(e,t,r,n,a){var i,o,l=e.children,u=l.length,c=new Array(u+1);for(c[0]=o=i=0;i<u;++i)c[i+1]=o+=l[i].value;!function e(t,r,n,a,i,o,u){if(t>=r-1){var s=l[t];return s.x0=a,s.y0=i,s.x1=o,void(s.y1=u)}var f=c[t],h=n/2+f,d=t+1,p=r-1;for(;d<p;){var v=d+p>>>1;c[v]<h?d=v+1:p=v}h-c[d-1]<c[d]-h&&t+1<d&&--d;var x=c[d]-f,y=n-x;if(o-a>u-i){var m=(a*y+o*x)/n;e(t,d,x,a,i,m,u),e(d,r,y,m,i,o,u)}else{var g=(i*y+u*x)/n;e(t,d,x,a,i,o,g),e(d,r,y,a,g,o,u)}}(0,u,e.value,t,r,n,a)},ae=function(e,t,r,n,a){(1&e.depth?Q:B)(e,t,r,n,a)},ie=function e(t){function r(e,r,n,a,i){if((o=e._squarify)&&o.ratio===t)for(var o,l,u,c,s,f=-1,h=o.length,d=e.value;++f<h;){for(u=(l=o[f]).children,c=l.value=0,s=u.length;c<s;++c)l.value+=u[c].value;l.dice?B(l,r,n,a,n+=(i-n)*l.value/d):Q(l,r,n,r+=(a-r)*l.value/d,i),d-=l.value}else e._squarify=o=ee(t,e,r,n,a,i),o.ratio=t}return r.ratio=function(t){return e((t=+t)>1?t:1)},r}(Z)},1635:function(e,t,r){"use strict";e.exports={CLICK_TRANSITION_TIME:750,CLICK_TRANSITION_EASING:"linear",eventDataKeys:["currentPath","root","entry","percentRoot","percentEntry","percentParent"]}},1637:function(e,t,r){"use strict";var n=r(24),a=r(1314),i=r(106),o=r(6),l=r(108),u=r(637),c=u.recordMinTextSize,s=u.clearMinTextSize,f=r(926),h=f.computeTransform,d=f.transformInsideText,p=r(1638).styleOne,v=r(653).resizeText,x=r(1311),y=r(1635),m=r(1029);function g(e,r,u,s){var f=e._fullLayout,v=!f.uniformtext.mode&&m.hasTransition(s),g=n.select(u).selectAll("g.slice"),_=r[0],T=_.trace,P=_.hierarchy,w=m.findEntryWithLevel(P,T.level),A=m.getMaxDepth(T),I=f._size,M=T.domain,S=I.w*(M.x[1]-M.x[0]),L=I.h*(M.y[1]-M.y[0]),O=.5*Math.min(S,L),z=_.cx=I.l+I.w*(M.x[1]+M.x[0])/2,E=_.cy=I.t+I.h*(1-M.y[0])-L/2;if(!w)return g.remove();var C=null,k={};v&&g.each((function(e){k[m.getPtId(e)]={rpx0:e.rpx0,rpx1:e.rpx1,x0:e.x0,x1:e.x1,transform:e.transform},!C&&m.isEntry(e)&&(C=e)}));var R=function(e){return a.partition().size([2*Math.PI,e.height+1])(e)}(w).descendants(),V=w.height+1,D=0,B=A;_.hasMultipleRoots&&m.isHierarchyRoot(w)&&(R=R.slice(1),V-=1,D=1,B+=1),R=R.filter((function(e){return e.y1<=B}));var F=Math.min(V,A),H=function(e){return(e-D)/F*O},K=function(e,t){return[e*Math.cos(t),-e*Math.sin(t)]},j=function(e){return o.pathAnnulus(e.rpx0,e.rpx1,e.x0,e.x1,z,E)},N=function(e){return z+b(e)[0]*(e.transform.rCenter||0)+(e.transform.x||0)},q=function(e){return E+b(e)[1]*(e.transform.rCenter||0)+(e.transform.y||0)};(g=g.data(R,m.getPtId)).enter().append("g").classed("slice",!0),v?g.exit().transition().each((function(){var e=n.select(this);e.select("path.surface").transition().attrTween("d",(function(e){var t=function(e){var t,r=m.getPtId(e),a=k[r],i=k[m.getPtId(w)];if(i){var o=e.x1>i.x1?2*Math.PI:0;t=e.rpx1<i.rpx1?{rpx0:0,rpx1:0}:{x0:o,x1:o}}else{var l,u=m.getPtId(e.parent);g.each((function(e){if(m.getPtId(e)===u)return l=e}));var c,s=l.children;s.forEach((function(e,t){if(m.getPtId(e)===r)return c=t}));var f=s.length,h=n.interpolate(l.x0,l.x1);t={rpx0:O,rpx1:O,x0:h(c/f),x1:h((c+1)/f)}}return n.interpolate(a,t)}(e);return function(e){return j(t(e))}})),e.select("g.slicetext").attr("opacity",0)})).remove():g.exit().remove(),g.order();var W=null;if(v&&C){var U=m.getPtId(C);g.each((function(e){null===W&&m.getPtId(e)===U&&(W=e.x1)}))}var G=g;function X(e){var t=e.parent,r=k[m.getPtId(t)],a={};if(r){var i=t.children,o=i.indexOf(e),l=i.length,u=n.interpolate(r.x0,r.x1);a.x0=u(o/l),a.x1=u(o/l)}else a.x0=a.x1=0;return a}v&&(G=G.transition().each("end",(function(){var t=n.select(this);m.setSliceCursor(t,e,{hideOnRoot:!0,hideOnLeaves:!0,isTransitioning:!1})}))),G.each((function(a){var u=n.select(this),s=o.ensureSingle(u,"path","surface",(function(e){e.style("pointer-events","all")}));a.rpx0=H(a.y0),a.rpx1=H(a.y1),a.xmid=(a.x0+a.x1)/2,a.pxmid=K(a.rpx1,a.xmid),a.midangle=-(a.xmid-Math.PI/2),a.startangle=-(a.x0-Math.PI/2),a.stopangle=-(a.x1-Math.PI/2),a.halfangle=.5*Math.min(o.angleDelta(a.x0,a.x1)||Math.PI,Math.PI),a.ring=1-a.rpx0/a.rpx1,a.rInscribed=function(e){return 0===e.rpx0&&o.isFullCircle([e.x0,e.x1])?1:Math.max(0,Math.min(1/(1+1/Math.sin(e.halfangle)),e.ring/2))}(a),v?s.transition().attrTween("d",(function(e){var t=function(e){var t,r=k[m.getPtId(e)],a={x0:e.x0,x1:e.x1,rpx0:e.rpx0,rpx1:e.rpx1};if(r)t=r;else if(C)if(e.parent)if(W){var i=e.x1>W?2*Math.PI:0;t={x0:i,x1:i}}else t={rpx0:O,rpx1:O},o.extendFlat(t,X(e));else t={rpx0:0,rpx1:0};else t={x0:0,x1:0};return n.interpolate(t,a)}(e);return function(e){return j(t(e))}})):s.attr("d",j),u.call(x,w,e,r,{eventDataKeys:y.eventDataKeys,transitionTime:y.CLICK_TRANSITION_TIME,transitionEasing:y.CLICK_TRANSITION_EASING}).call(m.setSliceCursor,e,{hideOnRoot:!0,hideOnLeaves:!0,isTransitioning:e._transitioning}),s.call(p,a,T);var g=o.ensureSingle(u,"g","slicetext"),b=o.ensureSingle(g,"text","",(function(e){e.attr("data-notex",1)})),P=o.ensureUniformFontSize(e,m.determineTextFont(T,a,f.font));b.text(t.formatSliceLabel(a,w,T,r,f)).classed("slicetext",!0).attr("text-anchor","middle").call(i.font,P).call(l.convertToTspans,e);var A=i.bBox(b.node());a.transform=d(A,a,_),a.transform.targetX=N(a),a.transform.targetY=q(a);var I=function(e,t){var r=e.transform;return h(r,t),r.fontSize=P.size,c(T.type,r,f),o.getTextTransform(r)};v?b.transition().attrTween("transform",(function(e){var t=function(e){var t,r=k[m.getPtId(e)],a=e.transform;if(r)t=r;else if(t={rpx1:e.rpx1,transform:{textPosAngle:a.textPosAngle,scale:0,rotate:a.rotate,rCenter:a.rCenter,x:a.x,y:a.y}},C)if(e.parent)if(W){var i=e.x1>W?2*Math.PI:0;t.x0=t.x1=i}else o.extendFlat(t,X(e));else t.x0=t.x1=0;else t.x0=t.x1=0;var l=n.interpolate(t.transform.textPosAngle,e.transform.textPosAngle),u=n.interpolate(t.rpx1,e.rpx1),s=n.interpolate(t.x0,e.x0),h=n.interpolate(t.x1,e.x1),d=n.interpolate(t.transform.scale,a.scale),p=n.interpolate(t.transform.rotate,a.rotate),v=0===a.rCenter?3:0===t.transform.rCenter?1/3:1,x=n.interpolate(t.transform.rCenter,a.rCenter);return function(e){var t=u(e),r=s(e),n=h(e),i=function(e){return x(Math.pow(e,v))}(e),o={pxmid:K(t,(r+n)/2),rpx1:t,transform:{textPosAngle:l(e),rCenter:i,x:a.x,y:a.y}};return c(T.type,a,f),{transform:{targetX:N(o),targetY:q(o),scale:d(e),rotate:p(e),rCenter:i}}}}(e);return function(e){return I(t(e),A)}})):b.attr("transform",I(a,A))}))}function b(e){return t=e.rpx1,r=e.transform.textPosAngle,[t*Math.sin(r),-t*Math.cos(r)];var t,r}t.plot=function(e,t,r,a){var i,o,l=e._fullLayout,u=l._sunburstlayer,c=!r,f=!l.uniformtext.mode&&m.hasTransition(r);(s("sunburst",l),(i=u.selectAll("g.trace.sunburst").data(t,(function(e){return e[0].trace.uid}))).enter().append("g").classed("trace",!0).classed("sunburst",!0).attr("stroke-linejoin","round"),i.order(),f)?(a&&(o=a()),n.transition().duration(r.duration).ease(r.easing).each("end",(function(){o&&o()})).each("interrupt",(function(){o&&o()})).each((function(){u.selectAll("g.trace").each((function(t){g(e,t,this,r)}))}))):(i.each((function(t){g(e,t,this,r)})),l.uniformtext.mode&&v(e,l._sunburstlayer.selectAll(".trace"),"sunburst"));c&&i.exit().remove()},t.formatSliceLabel=function(e,t,r,n,a){var i=r.texttemplate,l=r.textinfo;if(!(i||l&&"none"!==l))return"";var u=a.separators,c=n[0],s=e.data.data,f=c.hierarchy,h=m.isHierarchyRoot(e),d=m.getParent(f,e),p=m.getValue(e);if(!i){var v,x=l.split("+"),y=function(e){return-1!==x.indexOf(e)},g=[];if(y("label")&&s.label&&g.push(s.label),s.hasOwnProperty("v")&&y("value")&&g.push(m.formatValue(s.v,u)),!h){y("current path")&&g.push(m.getPath(e.data));var b=0;y("percent parent")&&b++,y("percent entry")&&b++,y("percent root")&&b++;var _=b>1;if(b){var T,P=function(e){v=m.formatPercent(T,u),_&&(v+=" of "+e),g.push(v)};y("percent parent")&&!h&&(T=p/m.getValue(d),P("parent")),y("percent entry")&&(T=p/m.getValue(t),P("entry")),y("percent root")&&(T=p/m.getValue(f),P("root"))}}return y("text")&&(v=o.castOption(r,s.i,"text"),o.isValidTextValue(v)&&g.push(v)),g.join("<br>")}var w=o.castOption(r,s.i,"texttemplate");if(!w)return"";var A={};s.label&&(A.label=s.label),s.hasOwnProperty("v")&&(A.value=s.v,A.valueLabel=m.formatValue(s.v,u)),A.currentPath=m.getPath(e.data),h||(A.percentParent=p/m.getValue(d),A.percentParentLabel=m.formatPercent(A.percentParent,u),A.parent=m.getPtLabel(d)),A.percentEntry=p/m.getValue(t),A.percentEntryLabel=m.formatPercent(A.percentEntry,u),A.entry=m.getPtLabel(t),A.percentRoot=p/m.getValue(f),A.percentRootLabel=m.formatPercent(A.percentRoot,u),A.root=m.getPtLabel(f),s.hasOwnProperty("color")&&(A.color=s.color);var I=o.castOption(r,s.i,"text");return(o.isValidTextValue(I)||""===I)&&(A.text=I),A.customdata=o.castOption(r,s.i,"customdata"),o.texttemplateString(w,A,a._d3locale,A,r._meta||{})}},1638:function(e,t,r){"use strict";var n=r(24),a=r(57),i=r(6),o=r(637).resizeText;function l(e,t,r){var n=t.data.data,o=!t.children,l=n.i,u=i.castOption(r,l,"marker.line.color")||a.defaultLine,c=i.castOption(r,l,"marker.line.width")||0;e.style("stroke-width",c).call(a.fill,n.color).call(a.stroke,u).style("opacity",o?r.leaf.opacity:null)}e.exports={style:function(e){var t=e._fullLayout._sunburstlayer.selectAll(".trace");o(e,t,"sunburst"),t.each((function(e){var t=n.select(this),r=e[0].trace;t.style("opacity",r.opacity),t.selectAll("path.surface").each((function(e){n.select(this).call(l,e,r)}))}))},styleOne:l}},633:function(e,t,r){"use strict";e.exports={container:"marker",min:"cmin",max:"cmax"}},653:function(e,t,r){"use strict";var n=r(24),a=r(57),i=r(106),o=r(6),l=r(23),u=r(637).resizeText,c=r(627),s=c.textfont,f=c.insidetextfont,h=c.outsidetextfont,d=r(667);function p(e,t,r){i.pointStyle(e.selectAll("path"),t,r),v(e,t,r)}function v(e,t,r){e.selectAll("text").each((function(e){var a=n.select(this),l=o.ensureUniformFontSize(r,x(a,e,t,r));i.font(a,l)}))}function x(e,t,r,n){var a=n._fullLayout.font,i=r.textfont;if(e.classed("bartext-inside")){var o=_(t,r);i=m(r,t.i,a,o)}else e.classed("bartext-outside")&&(i=g(r,t.i,a));return i}function y(e,t,r){return b(s,e.textfont,t,r)}function m(e,t,r,n){var i=y(e,t,r);return(void 0===e._input.textfont||void 0===e._input.textfont.color||Array.isArray(e.textfont.color)&&void 0===e.textfont.color[t])&&(i={color:a.contrast(n),family:i.family,size:i.size}),b(f,e.insidetextfont,t,i)}function g(e,t,r){var n=y(e,t,r);return b(h,e.outsidetextfont,t,n)}function b(e,t,r,n){t=t||{};var a=d.getValue(t.family,r),i=d.getValue(t.size,r),o=d.getValue(t.color,r);return{family:d.coerceString(e.family,a,n.family),size:d.coerceNumber(e.size,i,n.size),color:d.coerceColor(e.color,o,n.color)}}function _(e,t){return"waterfall"===t.type?t[e.dir].marker.color:e.mc||t.marker.color}e.exports={style:function(e){var t=n.select(e).selectAll("g.barlayer").selectAll("g.trace");u(e,t,"bar");var r=t.size(),a=e._fullLayout;t.style("opacity",(function(e){return e[0].trace.opacity})).each((function(e){("stack"===a.barmode&&r>1||0===a.bargap&&0===a.bargroupgap&&!e[0].trace.marker.line.width)&&n.select(this).attr("shape-rendering","crispEdges")})),t.selectAll("g.points").each((function(t){p(n.select(this),t[0].trace,e)})),l.getComponentMethod("errorbars","style")(t)},styleTextPoints:v,styleOnSelect:function(e,t,r){var a=t[0].trace;a.selectedpoints?function(e,t,r){i.selectedPointStyle(e.selectAll("path"),t),function(e,t,r){e.each((function(e){var a,l=n.select(this);if(e.selected){a=o.ensureUniformFontSize(r,x(l,e,t,r));var u=t.selected.textfont&&t.selected.textfont.color;u&&(a.color=u),i.font(l,a)}else i.selectedTextStyle(l,t)}))}(e.selectAll("text"),t,r)}(r,a,e):(p(r,a,e),l.getComponentMethod("errorbars","style")(r))},getInsideTextFont:m,getOutsideTextFont:g,getBarColor:_,resizeText:u}},667:function(e,t,r){"use strict";var n=r(12),a=r(60),i=r(6).isArrayOrTypedArray;t.coerceString=function(e,t,r){if("string"==typeof t){if(t||!e.noBlank)return t}else if(("number"==typeof t||!0===t)&&!e.strict)return String(t);return void 0!==r?r:e.dflt},t.coerceNumber=function(e,t,r){if(n(t)){t=+t;var a=e.min,i=e.max;if(!(void 0!==a&&t<a||void 0!==i&&t>i))return t}return void 0!==r?r:e.dflt},t.coerceColor=function(e,t,r){return a(t).isValid()?t:void 0!==r?r:e.dflt},t.coerceEnumerated=function(e,t,r){return e.coerceNumber&&(t=+t),-1!==e.values.indexOf(t)?t:void 0!==r?r:e.dflt},t.getValue=function(e,t){var r;return Array.isArray(e)?t<e.length&&(r=e[t]):r=e,r},t.getLineWidth=function(e,t){return 0<t.mlw?t.mlw:i(e.marker.line.width)?0:e.marker.line.width}}}]);