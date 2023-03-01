const content = {
  aportes:
    "/docs/como usar una pc desde cero.pdf",
  vistas: "/docs/powerpoint-2016-basico--guia-de-estudiante-eval.pdf",
  registro: "/docs/99174-MANUAL.pdf",
  contacto: "/docs/excel.pdf",
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
  aportes: "https://www.youtube.com/embed/-SYg6CfLnkk",
  vistas: "https://www.youtube.com/embed/pDfZOFtdF-A",
  registro: "https://www.youtube.com/embed/yKWFMgurUnU",
  contacto: "https://www.youtube.com/embed/NVoVBbTfaTM",
};

// function mostrarContenido1(contenido1) {}
