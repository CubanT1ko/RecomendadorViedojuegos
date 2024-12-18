document.querySelectorAll('.btn-expand').forEach(button => {
    button.addEventListener('click', () => {
        const card = button.closest('.game-card');
        card.classList.toggle('active'); // Alternar la clase 'active' para mostrar/ocultar detalles
    });
 });
 