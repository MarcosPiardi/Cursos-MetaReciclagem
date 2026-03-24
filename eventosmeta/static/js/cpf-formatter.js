/**
 * Formata CPF em tempo real
 * Entrada: 52998224725
 * Saída: 529.982.247-25
 */
document.addEventListener('DOMContentLoaded', function() {
    const cpfInputs = document.querySelectorAll('[data-cpf-formatter="true"]');
    
    cpfInputs.forEach(input => {
        input.addEventListener('input', function() {
            let valor = this.value.replace(/\D/g, '');
            
            if (valor.length > 11) {
                valor = valor.substring(0, 11);
            }
            
            if (valor.length <= 3) {
                this.value = valor;
            } else if (valor.length <= 6) {
                this.value = valor.substring(0, 3) + '.' + valor.substring(3);
            } else if (valor.length <= 9) {
                this.value = valor.substring(0, 3) + '.' + 
                             valor.substring(3, 6) + '.' + 
                             valor.substring(6);
            } else {
                this.value = valor.substring(0, 3) + '.' + 
                             valor.substring(3, 6) + '.' + 
                             valor.substring(6, 9) + '-' + 
                             valor.substring(9);
            }
        });
    });
});

