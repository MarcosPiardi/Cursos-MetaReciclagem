
        function mostrarSecao(secao) {
            document.getElementById('menuPrincipal').style.display = 'none';
            document.getElementById('secaoEventos').classList.remove('active');
            document.getElementById('secaoInteressados').classList.remove('active');
            document.getElementById('secaoCriterios').classList.remove('active');

            if (secao === 'eventos') {
                document.getElementById('secaoEventos').classList.add('active');
            } else if (secao === 'interessados') {
                document.getElementById('secaoInteressados').classList.add('active');
            } else if (secao === 'criterios') {
                document.getElementById('secaoCriterios').classList.add('active');
            }
        }

        function voltarMenu() {
            document.getElementById('menuPrincipal').style.display = 'grid';
            document.getElementById('secaoEventos').classList.remove('active');
            document.getElementById('secaoInteressados').classList.remove('active');
            document.getElementById('secaoCriterios').classList.remove('active');
        }

