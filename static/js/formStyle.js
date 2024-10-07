(function () {
    /**
     * inputs - nodelist com todos os inputs do formulario
     * 
     * esta função adiciona a lista de classes dos inputs a classe form-control
     */
    let inputs = document.querySelectorAll('input');
    for (let input of inputs) {

        // caso o input nao seja submit ou checkbox vai adicionar a classe
        if (input.type != 'submit' && input.type != 'checkbox') {
            input.classList.add('form-control')
        } else if (input.type == 'checkbox') {
            input.style.height = 'fit-content';
        }

    }
    let text_areas = document.querySelectorAll('textarea');
    text_areas.forEach(element => element.classList.add('form-control'));
})();

(
    function () {
        /**
         * definine o placeholder para os inputs nome, username, email e preço
         */  
        console.log('executou a troca de placeholders');
        let inputs_username = document.querySelectorAll('input[id*="username"]');
        inputs_username.forEach(element => element.setAttribute('placeholder', 'Introduza o seu username'));

        let inputs_email = document.querySelectorAll('input[id*="email"]');
        inputs_email.forEach(element => element.setAttribute('placeholder', 'Introduza o seu email'));

        let input_password1 = document.querySelectorAll('input[id*="password1"');
        input_password1.forEach(element => element.setAttribute('placeholder', 'Defina uma senha'));

        let input_password2 = document.querySelectorAll('input[id*="password2"');
        input_password2.forEach(element => element.setAttribute('placeholder', 'Confirme a senha'));

    }
)();

(
    function () {
        let button = document.querySelectorAll('button');
        button.forEach(element => element.style.margin = '0px');
    }
)();