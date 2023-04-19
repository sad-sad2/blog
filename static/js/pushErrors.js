function showErrorNotification(message) {
  const notification = document.createElement("div");
  notification.classList.add(
    "bg-red-100",
    "border",
    "border-red-400",
    "text-red-700",
    "z-50",
    "px-10",
    "py-3",
    "fixed",
    "rounded",
    "bottom-0",
    "w-64",
    "right-0",
    "mb-4",
    "mr-4"
  );
  notification.innerText = message;

  const closeButton = document.createElement("button");
  closeButton.classList.add("absolute", "top-0", "right-0", "px-4", "py-3");
  closeButton.innerHTML = "&times;";
  closeButton.addEventListener("click", () => notification.remove());

  notification.appendChild(closeButton);
  document.body.appendChild(notification);
}
const errors = document.getElementById("error").textContent.split(".");
if (errors) {
  showErrorNotification(errors);
}
