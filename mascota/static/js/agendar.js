document.addEventListener('DOMContentLoaded', function() {
    var tipoAtencion = document.getElementById('tipo_atencion');
    var direccionGroup = document.getElementById('direccion_group');
    var direccionInput = document.getElementById('direccion');
    var btnMaps = document.getElementById('btn-maps');

    if (tipoAtencion) {
        tipoAtencion.addEventListener('change', function() {
            if (this.value === 'movil') {
                direccionGroup.classList.remove('d-none');
            } else {
                direccionGroup.classList.add('d-none');
                btnMaps.classList.add('d-none');
            }
        });
    }

    if (direccionInput && btnMaps) {
        direccionInput.addEventListener('input', function() {
            var dir = direccionInput.value.trim();
            if (dir.length > 0) {
                var url = 'https://www.google.com/maps/search/?api=1&query=' + encodeURIComponent(dir);
                btnMaps.href = url;
                btnMaps.classList.remove('d-none');
            } else {
                btnMaps.classList.add('d-none');
            }
        });
    }
});