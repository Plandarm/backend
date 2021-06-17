const workspace = document.querySelector("section.main-body");

document.addEventListener("keydown", event => shortcut(event))
function shortcut(event) {
    code = event.code;
    if (code === "Enter" && document.activeElement.parentNode.className === "main-heading") {
        event.preventDefault();
    } else if (code === "Enter" && !event.shiftKey) { //Prevents excessive div spawn
        event.preventDefault();
        //Time spent: 3h to get it right-ish (5 lines) ಠ_ಠ
        let range = window.getSelection().getRangeAt(0);
        let linebreak = document.createElement("br");
        range.deleteContents()
        range.insertNode(linebreak)
        range.collapse()

    } else if (code === "Enter" && event.shiftKey) {
        event.preventDefault();
        addBlock(event);
        blocks = updateBlocks();
    } else if (code === "Delete" && event.ctrlKey) {       
        event.preventDefault(); 
        deleteBlock(event);
        blocks = updateBlocks();
    }
}

function addBlock(event) { //Shift + Enter = New block after focused
    console.log("Add");

    let textBlock = document.createTextNode("");
    let domElement = document.createElement("p");
    domElement.appendChild(textBlock);
    
    domElement.setAttribute("class", "text-block block");
    domElement.setAttribute("contenteditable", "true");
    
    if (document.activeElement.parentElement === workspace) {
        let focusedElement = document.activeElement;
        insertAfter(domElement, focusedElement);
        domElement.focus();
    }
    
}

function deleteBlock(event) { //Delete = remove focused block
    console.log("Delete")

    if (document.activeElement.parentElement === workspace) {
        let focusedElement = document.activeElement;
        let previous = focusedElement.previousElementSibling;
        focusedElement.remove();
        previous.focus();
    }
}

//For insertion
function insertAfter(el, referenceNode) {
    referenceNode.parentNode.insertBefore(el, referenceNode.nextSibling);
}
