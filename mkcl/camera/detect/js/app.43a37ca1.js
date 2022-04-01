(function(e){function t(t){for(var r,c,u=t[0],i=t[1],l=t[2],d=0,p=[];d<u.length;d++)c=u[d],Object.prototype.hasOwnProperty.call(a,c)&&a[c]&&p.push(a[c][0]),a[c]=0;for(r in i)Object.prototype.hasOwnProperty.call(i,r)&&(e[r]=i[r]);s&&s(t);while(p.length)p.shift()();return o.push.apply(o,l||[]),n()}function n(){for(var e,t=0;t<o.length;t++){for(var n=o[t],r=!0,u=1;u<n.length;u++){var i=n[u];0!==a[i]&&(r=!1)}r&&(o.splice(t--,1),e=c(c.s=n[0]))}return e}var r={},a={app:0},o=[];function c(t){if(r[t])return r[t].exports;var n=r[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,c),n.l=!0,n.exports}c.m=e,c.c=r,c.d=function(e,t,n){c.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},c.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},c.t=function(e,t){if(1&t&&(e=c(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(c.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)c.d(n,r,function(t){return e[t]}.bind(null,r));return n},c.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return c.d(t,"a",t),t},c.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},c.p="https://vedantmadane.github.io/mkcl/camera/detect/";var u=window["webpackJsonp"]=window["webpackJsonp"]||[],i=u.push.bind(u);u.push=t,u=u.slice();for(var l=0;l<u.length;l++)t(u[l]);var s=i;o.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("56d7")},1:function(e,t){},2:function(e,t){},2490:function(e,t,n){},3:function(e,t){},4060:function(e,t,n){"use strict";n("99d2")},"56d7":function(e,t,n){"use strict";n.r(t);n("e260"),n("e6cf"),n("cca6"),n("a79d");var r=n("7a23");function a(e,t,n,a,o,c){var u=Object(r["v"])("router-view");return Object(r["o"])(),Object(r["d"])(u)}var o={name:"App"},c=(n("4060"),n("6b0d")),u=n.n(c);const i=u()(o,[["render",a]]);var l=i,s=n("6c02"),d=Object(r["A"])("data-v-e0d79b96");Object(r["r"])("data-v-e0d79b96");var p={class:"display"},f={ref:"canvasEl"},b={class:"board"};Object(r["p"])();var v=d((function(e,t,n,a,o,c){return Object(r["o"])(),Object(r["d"])("section",p,[Object(r["e"])("video",{ref:"videoEl",autoplay:"true",playsinline:"",onLoadedmetadata:t[1]||(t[1]=function(){return a.runModel.apply(a,arguments)})},null,544),Object(r["e"])("canvas",f,null,512),Object(r["e"])("li",b,[(Object(r["o"])(!0),Object(r["d"])(r["a"],null,Object(r["u"])(e.board,(function(e,t){return Object(r["o"])(),Object(r["d"])("ul",{key:t},Object(r["x"])(t)+" ： "+Object(r["x"])(e),1)})),128))])])})),m=(n("96cf"),n("1da1")),O=n("ab39"),j=n("3d20"),h=n.n(j),y={name:"Video",setup:function(){var e=Object(r["s"])({modelUri:"https://vedantmadane.github.io/models",option:new O["a"]({minConfidence:.5})}),t=Object(r["s"])({video:{width:{min:320,ideal:1280,max:1920},height:{min:240,ideal:720,max:1080},frameRate:{min:15,ideal:30,max:60},facingMode:"user"}}),n=Object(r["t"])(null),a=Object(r["t"])(null),o=function(){var t=Object(m["a"])(regeneratorRuntime.mark((function t(){var r,c,u;return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,O["b"](n.value,e.option);case 2:r=t.sent,r&&(c=O["d"](a.value,n.value,!0),u=O["f"](r,c),u.length>1&&h.a.fire({title:"Only one Human face is allowed at a time.",icon:"warning"}),O["c"].drawDetections(a.value,u)),setTimeout((function(){return o()}));case 5:case"end":return t.stop()}}),t)})));return function(){return t.apply(this,arguments)}}();return Object(r["m"])((function(){var r=function(){var t=Object(m["a"])(regeneratorRuntime.mark((function t(){return regeneratorRuntime.wrap((function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,O["e"].ssdMobilenetv1.loadFromUri(e.modelUri);case 2:return t.next=4,O["e"].ageGenderNet.loadFromUri(e.modelUri);case 4:case"end":return t.stop()}}),t)})));return function(){return t.apply(this,arguments)}}(),a=function(){var e=Object(m["a"])(regeneratorRuntime.mark((function e(){var r;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.prev=0,e.next=3,navigator.mediaDevices.getUserMedia(t);case 3:r=e.sent,n.value.srcObject=r,e.next=9;break;case 7:e.prev=7,e.t0=e["catch"](0);case 9:case"end":return e.stop()}}),e,null,[[0,7]])})));return function(){return e.apply(this,arguments)}}();r(),a()})),{videoEl:n,canvasEl:a,runModel:o}}};n("68a7");const g=u()(y,[["render",v],["__scopeId","data-v-e0d79b96"]]);var w=g,x=[{path:"/",name:"Video",component:w}],k=Object(s["a"])({history:Object(s["b"])(),routes:x}),M=k;Object(r["c"])(l).use(M).mount("#app")},"68a7":function(e,t,n){"use strict";n("2490")},"99d2":function(e,t,n){}});
//# sourceMappingURL=app.43a37ca1.js.map