const campo = document.querySelector("#campo")
const adicionar = document.querySelector(".forms")
const apagarTasks = document.querySelector("#apagar")
const lista = document.querySelector(".lista")
const erro = document.querySelector("#erro")
const BACKEND_URL = "http://localhost:8000/api"
let tasks = []

async function removerTarefa(indice) {
    const taskId = tasks[indice].id;
    await fetch(`${BACKEND_URL}/${taskId}`, { method: "DELETE" });
    tasks.splice(indice, 1);
}

async function atualizarTarefa(indice, checked) {
    const taskId = tasks[indice].id;
    const response = await fetch(`${BACKEND_URL}/${taskId}`, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ concluida: checked })
    });
    const updatedTask = await response.json();
    tasks[indice] = updatedTask;
}

async function adicionarTarefa(tarefa) {
    const response = await fetch(BACKEND_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ titulo: tarefa, descricao: "" })
    });
    const novaTarefa = await response.json();
    tasks.push(novaTarefa);
}

function render() {
    lista.innerHTML = ""
    for (const task of tasks) {
        lista.innerHTML += `<div class="tarefa">
        <div class="task">
        <input type="checkbox" name="check" ${task.concluida ? "checked" : ""} class="concluido">
        <span class="texto-tarefa">${task.titulo}</span>
        </div>
        <button type="button" class="excluir-task"><span class="material-symbols-outlined">delete</span></button>
        </div>`
    }
    
    const botoes = document.querySelectorAll(".excluir-task")
    const checkboxes = document.querySelectorAll(".concluido");
    
    botoes.forEach((botao, indice) => {
        botao.addEventListener("click", async () => {
            await removerTarefa(indice);
            render();
        })
    })

    checkboxes.forEach((check, indice) => {
        check.addEventListener("change", async (event) => {
            await atualizarTarefa(indice, event.target.checked);
            render();
        })
    })
}

async function loadAllTasks() {
    const response = await fetch(BACKEND_URL)
    tasks = await response.json()
    render()
}

adicionar.addEventListener('submit', async (event) => {
    event.preventDefault()

    const novaTarefa = campo.value

    if (novaTarefa.trim() === "") {
        erro.classList.add("ativo")
    } else {
        await adicionarTarefa(novaTarefa)
        erro.classList.remove("ativo")
        campo.value = ""
        render();
    }
})

apagarTasks.addEventListener('click', () => {
    tasks.forEach(async (t, indice) => {
        await removerTarefa(indice);
    });

    tasks = []
    campo.value=""
    render()
})

loadAllTasks();