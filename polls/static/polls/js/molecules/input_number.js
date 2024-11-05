function focusParentInput(element) {
    const input = element.parentElement.querySelector('input');
    input.focus()
}

function blurParentInput(element) {
    const input = element.parentElement.querySelector('input');
    input.blur()
}

function increaseInputNumber(element) {
    element.parentNode.parentNode.querySelector('input').stepUp();
    focusParentInput(element.parentNode);
}

function decreaseInputNumber(element) {
    element.parentNode.parentNode.querySelector('input').stepDown();
    focusParentInput(element.parentNode);
}
