document.addEventListener('DOMContentLoaded', function () {
    const tipoLeadToggle = document.getElementById('tipo-lead-toggle');
    const programaSelect = document.getElementById('programa-select');
    const momentoSelect = document.getElementById('momento-select');
    const submomentoSelect = document.getElementById('submomento-select');
    const historialBtn = document.getElementById('historial-btn');
    const nuevaConversacionBtn = document.getElementById('nueva-conversacion-btn');

    // Cargar tipos de lead al iniciar
    fetch('/get-tipo-lead/')
        .then(response => response.json())
        .then(data => {
            tipoLeadToggle.innerHTML = '';
            data.tipos.forEach(tipo => {
                const option = document.createElement('option');
                option.value = tipo.id;
                option.textContent = tipo.nombre;
                tipoLeadToggle.appendChild(option);
            });
        });

    // Manejar cambios en el toggle de tipo de lead
    tipoLeadToggle.addEventListener('change', function () {
        fetch(`/get-programa/?tipo_lead_id=${this.value}`)
            .then(response => response.json())
            .then(data => {
                programaSelect.innerHTML = '';
                data.programas.forEach(programa => {
                    const option = document.createElement('option');
                    option.value = programa.id;
                    option.textContent = programa.nombre;
                    programaSelect.appendChild(option);
                });
            });
    });

    // Manejar cambios en el programa
    programaSelect.addEventListener('change', function () {
        fetch(`/get-momento/?programa_id=${this.value}`)
            .then(response => response.json())
            .then(data => {
                momentoSelect.innerHTML = '';
                data.momentos.forEach(momento => {
                    const option = document.createElement('option');
                    option.value = momento.id;
                    option.textContent = momento.nombre;
                    momentoSelect.appendChild(option);
                });
            });
    });

    // Manejar cambios en el momento
    momentoSelect.addEventListener('change', function () {
        fetch(`/get-submomento/?momento_id=${this.value}`)
            .then(response => response.json())
            .then(data => {
                submomentoSelect.innerHTML = '';
                data.submomentos.forEach(submomento => {
                    const option = document.createElement('option');
                    option.value = submomento.id;
                    option.textContent = submomento.nombre;
                    submomentoSelect.appendChild(option);
                });
            });
    });

    // Botón historial
    historialBtn.addEventListener('click', function () {
        fetch('/get-historial/')
            .then(response => response.json())
            .then(data => {
                console.log(data.historial);
                // Lógica para mostrar historial
            });
    });

    // Botón nueva conversación
    nuevaConversacionBtn.addEventListener('click', function () {
        fetch('/nueva-conversacion/')
            .then(response => response.json())
            .then(data => {
                alert(data.status);
            });
    });
});
