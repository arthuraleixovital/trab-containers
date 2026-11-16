const campo = document.querySelector("#campo")
const adicionar = document.getElementById("add")
const apagarTasks = document.querySelector("#apagar")
const lista = document.querySelector(".lista")
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
}

adicionar.addEventListener('click', () => {
    const novaTarefa = campo.value

    tasks.push(novaTarefa)
    save(tasks)

    campo.value = ""
    render()
})

// apagarTasks.addEventListener('click', () => {
//     tasks = ""
//     save(tasks)

//     campo.value=""
//     render()
// })

render()