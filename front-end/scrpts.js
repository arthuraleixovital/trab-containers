const campo = document.querySelector("#campo")
const adicionar = document.querySelector(".forms")
const apagarTasks = document.querySelector("#apagar")
const lista = document.querySelector(".lista")
const erro = document.querySelector("#erro")
const CHAVE = "tasks"
let tasks = load()

function save(conteudo) {
    localStorage.setItem(CHAVE,JSON.stringify(conteudo))
}

function load() {
    return JSON.parse(localStorage.getItem(CHAVE) ?? "[]")
}

function render() {
    lista.innerHTML = ""
    for (const task of tasks) {
            lista.innerHTML += `<div class="tarefa">
                    <div class="task">
                        <input type="checkbox" name="check" class="concluido">
                        <span class="texto-tarefa">${task}</span>
                    </div>
                    <button type="button" class="excluir-task"><span class="material-symbols-outlined">delete</span></button>
                </div>`
            }

            const botoes = document.querySelectorAll(".excluir-task")
            
            botoes.forEach((botao, indice) => {
                botao.addEventListener("click", () => {
                    tasks.splice(indice, 1)
                    save(tasks)
                    render()
                })
            })
}


adicionar.addEventListener('submit', (event) => {
    event.preventDefault()

    const novaTarefa = campo.value

    if (novaTarefa.trim() === "") {
        erro.classList.add("ativo")
    }

    else {
        tasks.push(novaTarefa)
        save(tasks)
    
        erro.classList.remove("ativo")

        campo.value = ""
        render()
    }

})

apagarTasks.addEventListener('click', () => {
    tasks = []
    save(tasks)

    campo.value=""
    render()
})

render()