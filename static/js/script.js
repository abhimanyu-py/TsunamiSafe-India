
document.addEventListener("DOMContentLoaded", function () {
  console.log("TsunamiSafe India website loaded successfully.");

  const currentPath = window.location.pathname;

  document.querySelectorAll(".navbar nav a").forEach(function (link) {
    if (link.getAttribute("href") === currentPath) {
      link.setAttribute("aria-current", "page");
    }
  });
});
