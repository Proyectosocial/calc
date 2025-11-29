document.addEventListener('DOMContentLoaded', () => {
    const screen = document.getElementById('screen');
    const buttons = document.querySelector('.calculator-buttons');

    let expression = '';

    buttons.addEventListener('click', (event) => {
        const { target } = event;
        const { value } = target;

        if (!target.matches('button')) {
            return;
        }

        switch (value) {
            case '=':
                calculate();
                break;
            case 'clear':
                clear();
                break;
            default:
                // Maneja números y operadores
                expression += value;
                screen.value = expression;
                break;
        }
    });

    function calculate() {
        try {
            // eval() es el equivalente de JavaScript al eval() de Python
            const result = eval(expression);
            screen.value = result;
            expression = String(result); // Guarda el resultado para futuras operaciones
        } catch (error) {
            screen.value = 'Error';
            expression = '';
        }
    }

    function clear() {
        expression = '';
        screen.value = '';
    }
});
