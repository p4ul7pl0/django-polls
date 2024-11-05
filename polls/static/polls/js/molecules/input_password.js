function toggleRightIcon(node) {
    const classes = [...node.classList];

    const classToAdd = classes.includes('bi-eye-slash') ? 'bi-eye' : 'bi-eye-slash';
    const classToRemove = classes.includes('bi-eye') ? 'bi-eye' : 'bi-eye-slash';

    node.classList.remove(classToRemove);
    node.classList.add(classToAdd);

    const parent = node.parentNode
    const childNodes = [...parent.childNodes];

    const input = childNodes.find((child) => child.tagName === 'INPUT');

    input.type = input.type === 'text' ? 'password' : 'text';

    input.focus();
}