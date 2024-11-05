function handleSearch(node) {
    const parent = node.parentNode
    const childNodes = [...parent.childNodes];

    const input = childNodes.find((child) => child.tagName === 'INPUT');

    input.focus();
}