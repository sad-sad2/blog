const dropzone = document.getElementById("dropzone");
const input = document.createElement("input");
const span = document.getElementById("url");
input.type = "file";
input.style.display = "none";
input.name = "image";
input.id = "image";

dropzone.addEventListener("dragover", (event) => {
  event.preventDefault();
  dropzone.classList.add("bg-gray-100");
});

dropzone.addEventListener("dragleave", (event) => {
  event.preventDefault();
  dropzone.classList.remove("bg-gray-100");
});

const addImage = (src) => {
  const img = document.createElement("img");
  img.src = src;
  img.classList.add("mx-auto");
  img.classList.add("h-56");
  img.classList.add("my-4");

  dropzone.innerHTML = "";
  dropzone.appendChild(img);
};

const addInputImage = (file) => {
  input.name = "image";
  input.id = "image";
  input.files = file;
  dropzone.appendChild(input);
};

if (span) {
  addImage(span.innerText);
}

dropzone.addEventListener("drop", (event) => {
  event.preventDefault();
  dropzone.classList.remove("bg-gray-100");

  let file = event.dataTransfer.files;
  let reader = new FileReader();

  reader.onload = (event) => {
    addImage(event.target.result);
    addInputImage(file);
  };

  reader.readAsDataURL(file[0]);
});

dropzone.addEventListener("click", () => {
  input.click();
});

input.addEventListener("change", (event) => {
  let file = event.target.files[0];
  let reader = new FileReader();
  reader.onload = (event) => {
    addImage(event.target.result);

    dropzone.innerHTML = "";
    dropzone.appendChild(img);
    input.files = file;
    dropzone.appendChild(input);
  };

  reader.readAsDataURL(file);
});
