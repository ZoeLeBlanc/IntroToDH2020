---
layout: page
title: Random Student Order Presentation Generator
permalink: /generator/
---
<div id="list"></div>

<script>

var studentNames = ['anna', 'kevin', 'shiva', 'sara'];

var shuffledNames = studentNames.sort(() => { return .5 - Math.random()}).map( name => "<li><h3>"+name.toUpperCase()+"</h3></li>");
document.getElementById("list").innerHTML = '<ol>'+shuffledNames.join('')+'</ol>';

</script>
