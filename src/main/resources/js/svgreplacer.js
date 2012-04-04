/**
 * Licensed to Neo Technology under one or more contributor
 * license agreements. See the NOTICE file distributed with
 * this work for additional information regarding copyright
 * ownership. Neo Technology licenses this file to you under
 * the Apache License, Version 2.0 (the "License"); you may
 * not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied. See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

/* In case SVG isn't supported, swap in PNG replacements.
 */

jQuery( document ).ready( function()
{
  replaceSvg( jQuery );
});

function replaceSvg( $ )
{
  var transformer = supportsSvg() ? swapForInlineSvg : swapForPng;
  $( "a.ulink[href$='.svg']" ).each( transformer );
}

function swapForInlineSvg ()
{
  console.log( this );
  var svg = $( this ).svg('get'); 
  svg.load($( this.href ).val(), {addTo: true, 
      changeSize: false, onLoad: loadDone}); 
//  resetSize(svg); 
   
  // Callback after loading external document 
  function loadDone(svg, error) { 
      svg.text(10, 20, error || 'Loaded into ' + this.id); 
  }
}

function swapForPng ()
{
  this.href += ".png";
  var img = $( "img", this )[0];
  img.src += ".png";
}

function supportsSvg()
{
    return !!document.createElementNS && !!document.createElementNS('http://www.w3.org/2000/svg', "svg").createSVGRect;
}

