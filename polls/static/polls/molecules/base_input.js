function blurChildInput(element) {
    const childNodes = [...element.childNodes];
    const input = childNodes.find((child) => child.tagName === 'INPUT');

    input.blur();
}
