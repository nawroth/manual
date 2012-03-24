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

/* Cypher Console
 * Adds live cypher console feature to a page.
 */

jQuery( document ).ready(  function()
{
  createCypherConsoles( jQuery );
});

function createCypherConsoles( $ )
{
  $('p.cypherconsole').each(function()
  {
    var title = $( 'b', this ).eq(0).text() || "Live Cypher Console";
    var database = $( 'span.database', this ).eq(0).text() || "default-db";
    var command = $( 'strong', this ).eq(0).text();
    var button = $( '<button class="cypherconsole" type="button"><img src="css/utilities-terminal.png" /> ' + title + '</button>' );
    button.click( function()
    {
      handleCypherClick( database, command, title );
    });    
    button.insertAfter( this );
  });
  
  function handleCypherClick( database, command, title )
  {
    console.log( database, command, title );
  }
}

