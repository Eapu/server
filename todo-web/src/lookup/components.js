export function loadTodo(callback) {
    const xhr = new XMLHttpRequest()
    const method = 'GET' //"POST"
    const url = "http://localhost:8000/api/todo/"
    const responseType = "json"
    xhr.responseType = responseType
    xhr.open(method, url)
    xhr.onload = function() {
        callback(xhr.status, xhr.response)
    }
    xhr.onerror = function(e) {
        console.log(e)
    callback({"message": "The request was an error"}, 400)
    }
    xhr.send()
    }