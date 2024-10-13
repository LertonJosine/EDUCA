(
    function () {
        let professor_link = document.querySelectorAll('a')
        professor_link.forEach((link) => {
            if (link.innerText == 'Mais') {
                link.classList.add('active')
            }
            if (link.innerText == 'Inicio') {
                link.classList.remove('active')
            }
        })
    }
)();