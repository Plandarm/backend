const workspace = document.querySelector("section.main-body");

document.addEventListener("keydown", event => shortcut(event))
function shortcut(event) {
    code = event.code;
    if (code === "Enter" && event.shiftKey) {
        event.preventDefault();
        addBlock(event);
        blocks = updateBlocks();
    }
    else if (code === "Delete" && event.ctrlKey) {       
        event.preventDefault(); 
        deleteBlock(event);
        blocks = updateBlocks();
    }
}

//Works like stack
function addBlock(event) { //Shift + Enter = New block after focused
    console.log("Add");

    var textBlock = document.createTextNode("");
    var domElement = document.createElement("p");
    domElement.appendChild(textBlock);
    
    domElement.setAttribute("class", "text-block block");
    domElement.setAttribute("contenteditable", "true");
    
    if (document.activeElement.parentElement === workspace) {
        var focusedElement = document.activeElement;
        insertAfter(domElement, focusedElement);
        domElement.focus();
    }
    
}

function deleteBlock(event) { //Delete = remove focused block
    console.log("Delete")

    if (document.activeElement.parentElement === workspace) {
        var focusedElement = document.activeElement;
        var previous = focusedElement.previousElementSibling;
        focusedElement.remove();
        previous.focus();
    }
}


//For insertion
function insertAfter(el, referenceNode) {
    referenceNode.parentNode.insertBefore(el, referenceNode.nextSibling);
}