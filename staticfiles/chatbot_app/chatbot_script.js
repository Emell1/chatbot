document.addEventListener("DOMContentLoaded", () => {
    // Variables globales

    let submomentos = []; // Declarar la variable submomentos aquí

    const nuevaConversacionButton = document.getElementById("nueva-conversacion");
    const historialButton = document.getElementById("historial");
    const tipoLeadToggle = document.getElementById("tipo-lead-toggle");
    const momentoButtons = document.querySelectorAll(".moment-button");
    const chatDisplay = document.getElementById("chat-display");
    const userInput = document.getElementById("user-input");
    const sendButton = document.getElementById("send-button");
    const popupNuevaConversacion = document.getElementById("popup-nueva-conversacion");
    const closePopupNuevaConversacion = document.getElementById("close-popup-nueva-conversacion");
    const confirmarNuevaConversacion = document.getElementById("confirmar-nueva-conversacion");
    const cancelarNuevaConversacion = document.getElementById("cancelar-nueva-conversacion");
    const popupPrevisualizacion = document.getElementById("popup-previsualizacion");
    const closePopupPrevisualizacion = document.getElementById("close-popup-previsualizacion");
    const programaSelect = document.getElementById("programa-select");

    // Manejar nueva conversación
    nuevaConversacionButton.addEventListener("click", () => {
        popupNuevaConversacion.classList.remove("hidden");
    });

    closePopupNuevaConversacion.addEventListener("click", () => {
        popupNuevaConversacion.classList.add("hidden");
    });

    confirmarNuevaConversacion.addEventListener("click", () => {
        chatDisplay.innerHTML = ""; // Limpia el display de chat
        // Limpia historial (lógica pendiente)
        popupNuevaConversacion.classList.add("hidden");
    });

    cancelarNuevaConversacion.addEventListener("click", () => {
        popupNuevaConversacion.classList.add("hidden");
    });

    // Manejar historial
    historialButton.addEventListener("click", () => {
        // Mostrar historial (lógica pendiente)
        alert("Historial funcionalidad en desarrollo");
    });

    // Cambiar momentos
    momentoButtons.forEach((button) => {
        button.addEventListener("click", () => {
            chatDisplay.innerHTML = ""; // Limpiar display
            cargarSubmomentos(button.id); // Cargar submomentos dinámicamente
            console.log(`Cambiando a: ${button.id}`);
        });
    });

    // Consultar respuesta
    sendButton.addEventListener("click", () => {
        const query = userInput.value.trim();
        if (query) {
            // Realizar consulta (lógica pendiente)
            chatDisplay.innerHTML += `<div class="user-message">${query}</div>`;
            userInput.value = "";
        }
    });

    // Manejar previsualización de archivos
    closePopupPrevisualizacion.addEventListener("click", () => {
        popupPrevisualizacion.classList.add("hidden");
    });

    // Cargar submomentos en el frontend (lógica simulada)
   
    function cargarSubmomentos(momentId) {
        fetch(`/obtener_submomentos/${momentId}/`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                if (data.submomentos) {
                    submomentos = data.submomentos; // Asigna los submomentos obtenidos
                    const submomentoContainer = document.getElementById("submoments-container");
                    submomentoContainer.innerHTML = ""; // Limpia los submomentos actuales
                    submomentos.forEach((sub) => {
                        const button = document.createElement("button");
                        button.innerText = sub.nombre;
                        button.className = "submoment-button";
                        button.addEventListener("click", () => {
                            console.log(`Submomento seleccionado: ${sub.id}`);
                        });
                        submomentoContainer.appendChild(button);
                    });
                } else {
                    console.error('Error al obtener los submomentos');
                }
            })
            .catch(error => console.error('Error en la solicitud:', error));
    }


    function obtenerRespuestas(momentoId, submomentoId) {
        fetch(`/obtener_respuesta/${momentoId}/${submomentoId}/`)
         .then(response => response.json())
         .then(data => {
            if (data.respuesta_momento && data.respuesta_submomento) {
                // Actualizar el display del chatbot con las respuestas
                const chatDisplay = document.getElementById('chat-display');
                chatDisplay.innerHTML = `
                    <div>
                        <strong>Respuesta del Momento:</strong>
                        <p>${data.respuesta_momento}</p>
                    </div>
                    <div>
                        <strong>Respuesta del Submomento:</strong>
                        <p>${data.respuesta_submomento}</p>
                    </div>
                `;
            } else {
                console.error('Error al obtener las respuestas');
            }
        })
        .catch(error => console.error('Error en la solicitud:', error));
    }
    // Cambiar tipo de lead
    tipoLeadToggle.addEventListener("click", () => {
        const estadoActual = tipoLeadToggle.dataset.active === "true";
        tipoLeadToggle.dataset.active = !estadoActual;
        tipoLeadToggle.innerText = estadoActual ? "Lead: Seguimiento" : "Lead: Nuevo";
    });

    // Manejar selección de programa
    if (programaSelect) {
        programaSelect.addEventListener("change", () => {
            console.log(`Programa seleccionado: ${programaSelect.value}`);
            // Aquí puedes agregar la lógica para filtrar en la base de datos
        });
    }})
