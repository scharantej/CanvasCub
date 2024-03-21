## Flask Application Design for Teaching Children Drawing

### HTML Files

- **index.html:** The landing page for the application. It should display instructions, provide a drawing area, and a button to submit the drawing.
- **gallery.html:** A page showcasing the submitted drawings by children.

### Routes

- **home()**: The route for the index.html page. It should load the landing page with the drawing area and instructions.
- **submit_drawing()**: The route to handle the submission of the drawing. It should save the drawing and redirect the user to the gallery page.
- **gallery()**: The route for the gallery.html page. It should retrieve and display the submitted drawings.