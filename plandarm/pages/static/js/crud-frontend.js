async function savePage() {
    main  = document.querySelector("main.page-main");

    title = main.querySelector("section.main-heading").childNodes[1].innerHTML;
    body  = main.querySelector("section.main-body").innerHTML;
    csrftoken = getCookie("csrftoken");

    let requestJSON = {
        title: title,
        body: body,
    };

    href = window.location.href.split("/")

    let response = await fetch(`/page/${href[href.length - 2]}/save/`, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json;charset=utf-8",
            "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify(requestJSON),
      });
}

function getCookie (name) {
    let value = '; ' + document.cookie;
    let parts = value.split(`; ${name}=`);
    if (parts.length == 2) return parts.pop().split(';').shift();
}