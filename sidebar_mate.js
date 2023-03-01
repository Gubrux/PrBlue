const content = {
  aportes:
    "/docs/1-mtodo-grfico-de-singapu4r-1.pdf",
  vistas: "/docs/Cuadernillo de sumas y restas.pdf",
  registro: "/docs/Cuadernillo de sumas y restas.pdf",
  contacto: "/docs/Multiplicacion-y-divison-David-Magania.pdf",
};

function mostrarContenido(contenido1) {
  //GET PARENT DIV WITH THE ID
  const parent = document.getElementById("contenido");
  // GET THE CHILD DIV IF IT EXISTS
  const child = parent.firstChild;
  // IF THE CHILD DIV EXISTS, REMOVE IT TO MAKE SURE WE
  // ONLY HAVE ONE IMAGE AT A TIME
  if (child) {
    parent.removeChild(child);
  }
  // GET THE IMAGE URL FROM THE DICTIONARY CONTENT
  const value = content[contenido1];
  // CREATE THE DIV ELEMENT
  const div = document.createElement("div");
  // ADD THE CSS CLASSES TO THE DIV
  div.classList.add("w-96", "p-1");
  // CREATE THE IMAGE ELEMENT
  const nuevaImagen = document.createElement("embed");
  // ADD THE SRC ATTRIBUTE TO THE IMAGE
  nuevaImagen.src = value + "?t=" + Date.now();
  nuevaImagen.type = "application/pdf"
  nuevaImagen.width = "315";
  nuevaImagen.height = "420";
  // APPEND THE DIV AND THE IMAGE TO THE PARENT DIV
  parent.appendChild(div);
  div.appendChild(nuevaImagen);



  
  // Video
  const newParent = document.getElementById("contenido1");
  const child1 = newParent.firstChild;
  if (child1) {
    newParent.removeChild(child1);
  }
  const value1 = contentVideo[contenido1];
  const newDiv = document.createElement("div");
  newDiv.classList.add("w-auto", "p-1");
  const nuevVideo1 = document.createElement("iframe");
  nuevVideo1.src = value1;
  nuevVideo1.width = "560";
  nuevVideo1.height = "315";
  nuevVideo1.allowFullscreen = true;
  newParent.appendChild(newDiv);
  newDiv.appendChild(nuevVideo1);
}

const contentVideo = {
  aportes: "https://www.youtube.com/embed/8_mZFk_6LCY",
  vistas: "https://www.youtube.com/embed/CSlkZpoy5s8",
  registro: "https://www.youtube.com/embed/N8bsDIbIDzA",
  contacto: "https://www.youtube.com/embed/UildQorYmK0",
};