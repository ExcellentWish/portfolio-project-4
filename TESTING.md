I have written a small number of JS functions that handle some animation & event listeners to add classes and attributes to elements created dynamically.

**`screenSize()`** - hides/shows the map section of the footer depending on the size of the window. If smaller than 994 it remains hidden:

![](assets/testing/JS-small-screens.PNG) 

And any larger than that it appears:

![](assets/testing/JS-when-over-994.PNG)

I have used this function when a window resizes in conjunction with a `debounce` function to prevent the function triggering if being called continuously. It triggers after it has stopped being called for 150 milliseconds. As explained [here](https://davidwalsh.name/javascript-debounce-function).

However screenSize is called whenever the document is loaded to prevent the map showing when a user navigates through the site.