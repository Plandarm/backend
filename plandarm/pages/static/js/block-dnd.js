// Area that contains blocks and supports DnD
const blocksArea = document.querySelector('.main-body');

// List of blocks 
let blocks = updateBlocks();

function updateBlocks() {
    return blocksArea.querySelectorAll('.block');
}

function switchEdit (editTrue) {
    // eventTarget.contentEditable = editTrue;
    // eventTarget.draggable = !editTrue;

    for (const block of blocks) {
        block.contentEditable = editTrue;
        block.draggable = !editTrue;
    }
}

switchEdit(true);

document.addEventListener('mousedown', onMouseHold);
document.addEventListener('mouseup', onMouseRelease);

function onMouseHold(e) {
  if (e.ctrlKey && e.target.classList.contains('block')) {
    console.log("Block taken!");
    switchEdit(false);
  }
}

function onMouseRelease(e) {
    console.log("Mouse released!");
    switchEdit(true);
}

// Determine dragged block
blocksArea.addEventListener('dragstart', (evt) => {
    evt.target.classList.add('dragged');
});

blocksArea.addEventListener('dragend', (evt) => {
    evt.target.classList.remove('dragged');
    console.log("Block dropped!");
    switchEdit(true);
});

// Get nextBlock only when cursor crossed the center of hoveredBlock
const getNextBlock = (cursorPosition, hoveredBlock) => {
    const hoveredBlockCoord = hoveredBlock.getBoundingClientRect();
    const hoveredBlockCenter = hoveredBlockCoord.y + hoveredBlockCoord.height / 2;

    const nextBlock = (cursorPosition < hoveredBlockCenter) ? 
        hoveredBlock :
        hoveredBlock.nextElementSibling;
    
    return nextBlock;
  };

// Handle DnD logic
blocksArea.addEventListener('dragover', (evt) =>{

    // Allow Drag & Drop in the main-body area
    // evt.preventDefault();

    // Find currently dragged block
    const draggedBlock = blocksArea.querySelector('.dragged');
    
    // Find currently hovered-over block
    const hoveredBlock = evt.target;

    // Check if draggedBlock:
    // 1. is not hovered over itself
    // 2. is hovered over another block element
    const isMovable = hoveredBlock !== draggedBlock &&
        hoveredBlock.classList.contains('block');
    
    if (!isMovable) {
        return;
    }

    const nextBlock = getNextBlock(evt.clientY, hoveredBlock);

    if (nextBlock && 
        draggedBlock === nextBlock.previousElementSibling ||
        draggedBlock === nextBlock) {
            return;
        }
    
    console.log(nextBlock);

    // Insert draggedBlock before nextBlock
    blocksArea.insertBefore(draggedBlock, nextBlock);
})