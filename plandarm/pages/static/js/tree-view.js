let togglers = document.querySelectorAll('.caret')
if (togglers.length > 0) {
    for (let index = 0; index < togglers.length; index++) {
        const toggler = togglers[index];
        toggler.addEventListener("click", function (e) {
            toggler.parentElement.querySelector(".nested").classList.toggle("active")
            toggler.classList.toggle("caret-down")
        })
    }
}