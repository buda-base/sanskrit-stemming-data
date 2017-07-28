/*
 libDeva v1.4.1
 Copyright 2011 Timothy Bellefleur. All rights reserved.

 ***

 This library was writted for the University of British Columbia's
 Sanskrit educational tools website at http://www.ubcsanskrit.ca/

 Incomplete documentation may be found in libDeva.txt

*/
var j=true,k=false;
(function(q){function r(a){var c=a instanceof Array?[]:{},d;for(d in a)if(a.hasOwnProperty(d))c[d]=a[d]&&typeof a[d]==="object"?r(a[d]):a[d];return c}var b={},n;b={a:{},d:{}};b.curScr="?";b.a.f={m:["ḹ","ḷ","ṝ","ai","au","ā","a","ī","i","ū","u","ṛ","e","o","ṃ","ɱ","ḥ","kh","k","gh","g","ṅ","ch","c","jh","j","ñ","ṭh","ṭ","ḍh","ḍ","ṇ","th","t","dh","d","n","ph","p","bh","b","m","y","r","l","v","ś","ṣ","s","h","'","°"],s:["lRR","lR","RR","ai","au","A","a","I","i","U","u","R","e","o","M","M","H","kh",
"k","gh","g","G","ch","c","jh","j","J","Th","T","Dh","D","N","th","t","dh","d","n","ph","p","bh","b","m","y","r","l","v","z","S","s","h","'","#"],u:["X","x","F","E","O","A","a","I","i","U","u","f","e","o","M","M","H","K","k","G","g","N","C","c","J","j","Y","W","w","Q","q","R","T","t","D","d","n","P","p","B","b","m","y","r","l","v","S","z","s","h","'","°"],z:[".ll",".l",".rr","ai","au","aa","a","ii","i","uu","u",".r","e","o",".m",".m",".h","kh","k","gh","g",'"n',"ch","c","jh","j","~n",".th",".t",".dh",
".d",".n","th","t","dh","d","n","ph","p","bh","b","m","y","r","l","v",'"s',".s","s","h","'","#"],n:"्"};b.charsets={};b.charsets.unicode=b.a.f.m;b.charsets.iast=b.a.f.m;b.charsets.hk=b.a.f.s;b.charsets.velthuis=b.a.f.z;b.charsets.slp1=b.a.f.u;b.a.q={c:["0","1","2","3","4","5","6","7","8","9"],b:["०","१","२","३","४","५","६","७","८","९"]};b.a.h={c:["kha","ka","gha","ga","ṅa","cha","ca","jha","ja","ña","ṭha","ṭa","ḍha","ḍa","ṇa","tha","ta","dha","da","na","pha","pa","bha","ba","ma","ya","ra","la","va",
"śa","ṣa","sa","ha","ṃ","ɱ","ḥ","'","°","||","|","//","/"],b:["ख","क","घ","ग","ङ","छ","च","झ","ज","ञ","ठ","ट","ढ","ड","ण","थ","त","ध","द","न","फ","प","भ","ब","म","य","र","ल","व","श","ष","स","ह","ं","ँ","ः","ऽ","॰","॥","।","॥","।"]};b.a.i={c:[" ḹ"," ḷ"," ṝ"," ai"," au"," ā"," a"," ī"," i"," ū"," u"," ṛ"," e"," o"],b:[" ॡ"," ऌ"," ॠ"," ऐ"," औ"," आ"," अ"," ई"," इ"," ऊ"," उ"," ऋ"," ए"," ओ"]};b.a.j={c:["ḹ","ḷ","ṝ","ai","au","ā","a","ī","i","ū","u","ṛ","e","o"],b:["ॣ","ॢ","ॄ","ै","ौ","ा","‍","ी","ि","ू",
"ु","ृ","े","ो"]};b.a.g=r(b.a.h);for(n in b.a.g.c)if(b.a.g.c.hasOwnProperty(n)){b.a.g.c[n]=b.a.g.c[n].replace("a","");b.a.g.b[n]+=b.a.f.n}String.prototype.replaceAll=b.d.replaceAll=function(a,c){return this.length>1?this.split(a).join(c):this.replace(a,c)};String.prototype.e=b.d.e=function(a,c){var d=this,f;for(f in a)if(a.hasOwnProperty(f))d=d.replaceAll(a[f],c[f]);return d};b.d.l=function(a,c,d){if(d.constructor===Array)d=d.join("\r\t\n\t");if(a==="deva")d=d.replace("ॐ","ओं");return d};b.d.k=function(a,
c,d){if(d.search("\r\t\n\t")!==-1)d=d.split("\r\t\n\t");return d};b.d.w=function(a){var c=b.a.f,d=b.a.q,f=b.a.h,g=b.a.i,e=b.a.g,h=b.a.j,i,l,m,o,p;h.b[6]="";a=" "+a;for(i in h.c)if(h.c.hasOwnProperty(i)){m=h.c[i];for(l in e.c)if(e.c.hasOwnProperty(l)){o=e.c[l];p=e.b[l].replaceAll(c.n,"");a=a.replaceAll(o+m,p+h.b[i])}}h.b[6]="‍";a=a.replaceAll("_","_ ");a=a.e(f.c,f.b);a=a.e(g.c,g.b);a=a.e(e.c,e.b);a=(" "+a+" ").e(d.c,d.b);for(i in g.c)if(g.c.hasOwnProperty(i)){m=g.c[i];c=m.replaceAll(" ","");d=g.b[i].replaceAll(" ",
"");a=a.replaceAll(c,d)}a=a.e(["_ ","- ","\n "],["","-","\n"]);return $.trim(a)};b.d.v=function(a){var c=b.a.f,d=b.a.q,f=b.a.h,g=b.a.i,e=b.a.g,h=b.a.j,i,l,m,o,p;for(i in h.c)if(h.c.hasOwnProperty(i)){m=h.c[i];for(l in e.c)if(e.c.hasOwnProperty(l)){o=e.c[l];p=e.b[l].replaceAll(c.n,"");a=a.replaceAll(p+h.b[i],o+m)}}a=a.replaceAll("_","_ ");a=a.e(e.b,e.c);a=a.e(f.b,f.c);a=a.e(g.b,g.c);a=(" "+a+" ").e(d.b,d.c);a=a.replace("aइ","a_i");a=a.replace("aउ","a_u");for(i in g.b)if(g.b.hasOwnProperty(i)){m=g.b[i];
c=m.replaceAll(" ","");d=g.c[i].replaceAll(" ","");a=a.replaceAll(c,d)}a=a.e(["_ ","- ","\n "],["","-","\n"]);return $.trim(a)};b.scrType=b.d.t=function(a){var c,d,f,g=k,e,h;if(a.search(b.a.f.n)!==-1)c=j;if(!c)for(e in b.a.h.b)if(b.a.h.b.hasOwnProperty(e))if(a.search(b.a.h.b[e])!==-1){c=j;break}if(!c)for(e in b.a.i.b)if(b.a.i.b.hasOwnProperty(e))if(a.search(b.a.i.b[e])!==-1){c=j;break}if(!c)for(e in b.a.j.b)if(b.a.j.b.hasOwnProperty(e))if(a.search(b.a.j.b[e])!==-1){c=j;break}for(e in b.a.f.m)if(b.a.f.m.hasOwnProperty(e))if(a.match(/[ḹḷṝāīūṛṃɱḥṅñṭḍṇśṣ]/)){d=
j;break}for(e=65;e<=90;e+=1){h=a.search(String.fromCharCode(e));if(h===0)f=j;else if(h>0){g=f=j;break}}if(!f)for(e=97;e<=122;e+=1){h=a.search(String.fromCharCode(e));if(h!==-1){f=j;break}}return c&&d?"mixed":c&&f?"mixed":d&&g?"mixed":c?"deva":d?"unicode":"hk"};b.isConsonant=b.d.B=function(a){var c,d;a=b.d.r(a,"","deva");for(c=2325;c<=2361;c+=1){d=String.fromCharCode(c);if(a===d||a===d+"्")return j}return k};b.d.p=function(a,c,d){var f=[];if(a==="")if(b.curScr==="?")return k;else a=b.curScr;if(c===
b.curScr)return k;if(a===c)return k;$(".t-"+a+"[data-"+c+"]").each(function(){if(d){$(this).attr("data-"+a,this.innerHTML);$(this).addClass("t-"+c).removeClass("t-"+a);$(this).html($(this).attr("data-"+c))}});$(".t-"+a+":not([data-"+c+"])").each(function(){f.push(this.innerHTML)});f=b.d.r(f,a,c);$(".t-"+a+":not([data-"+c+"])").each(function(g){f.constructor===Array||(f=[f]);$(this).attr("data-"+c,f[g]);if(d){$(this).attr("data-"+a,this.innerHTML);$(this).addClass("t-"+c).removeClass("t-"+a);$(this).html(f[g])}});
if(d)b.curScr=c;return j};b.convertAll=b.d.o=function(a,c){return b.d.p(a,c,j)};b.convertInt=b.d.A=function(a,c){return b.d.p(a,c,k)};b.toggleScr=b.d.C=function(){if(b.curScr==="uni")b.d.o("uni","deva");else b.curScr==="deva"&&b.d.o("deva","uni")};b.trans=b.d.r=function(a,c,d){if(a.length<1)return k;if(c==="")c=b.d.t(a);if(c===d)return a;else{c=c;d=d}if(c==="mixed")return k;else if(c==="uni")c="unicode";else if(c==="iast")c="unicode";else if(c==="vel")c="velthuis";if(d==="uni")d="unicode";else if(d===
"iast")d="unicode";else if(d==="vel")d="velthuis";if(d==="deva"&&c!=="unicode"){a=b.d.l(c,"unicode",a);a=a.e(b.charsets[c],b.charsets.unicode);a=b.d.k(c,"unicode",a);c="unicode"}if(c==="deva"){a=b.d.l("deva","unicode",a);a=b.d.v(a);a=b.d.k("deva","unicode",a);c="unicode"}if(d==="deva"){a=b.d.l(c,"deva",a);a=b.d.w(a);return a=b.d.k(c,"deva",a)}if(c!==d){a=b.d.l(c,d,a);a=a.e(b.charsets[c],b.charsets[d]);return a=b.d.k(c,d,a)}return a};q.libDeva=b;document.addEventListener("DOMContentLoaded",function(){typeof $===
"undefined"&&q.alert("The jQuery library was not detected.\n\n`libDeva.js` requires the jQuery library (v1.4.4+),\nAvailable at http://jquery.com/")},k)})(window);
