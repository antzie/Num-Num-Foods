// JavaScript for CSS Styling 
// Version: 13-01-2019

// Move side list left by same amount as its width.
    function toggleSideMenu() {
      var listDiv = document.getElementById("menu-side");
      /*var width = document.getElementById("menu-side").offsetWidth;*/
      var width = 250; /*250 is the specified px width of the side menu. 
      					The menu exapnds up to 250px. Thus if you shift it
      					across by the width it is now, it expands into the new room*/
      if (listDiv.style.marginLeft === "10px" || listDiv.style.marginLeft == '') {
        listDiv.style.marginLeft = -250 + "px";
      } else {
        listDiv.style.marginLeft = "10px";
      }
    }
