function containerJSONTemplate(container_id, function_name){
    return JSON.stringify({
        "key" : decodeURIComponent(document.cookie).split("=")[1],
        "id" : container_id,
        "function" : function_name
        })
}

function containersJSONTemplate(function_name){
    return JSON.stringify({
        "key" : decodeURIComponent(document.cookie).split("=")[1],
        "type" : "containers",
        "function" : function_name
        })
}

function doFunction(HTMLTable){
    StartLoading();
    var buttons = document.getElementsByTagName("button");
    for (button of buttons){
        button.disabled=true;
    }
    var a = fetch("http://localhost:8777/containers_", {
        method: 'POST',
        headers: {
            'Content-Type' :'application/json'
        },
        body: HTMLTable
    }).then((res) => {return res.text()}).then((htmlTableView) => {KillLoading(); document.getElementById("contentTable").innerHTML = htmlTableView});
}

function stopallContainers(){
    doFunction(containersJSONTemplate("stopall"));
}
function startallContainers(){
    doFunction(containersJSONTemplate("startall"));
}
function deleteallContainers(){
    doFunction(containersJSONTemplate("removeall"));
}
function reloadallContainers(){
    doFunction(containersJSONTemplate("list"));
}
function stopContainer(container_id){
    doFunction(containerJSONTemplate(container_id, "stop"));
}
function startContainer(container_id){
    doFunction(containerJSONTemplate(container_id, "start"));
}
function removeContainer(container_id){
    doFunction(containerJSONTemplate(container_id, "remove"));
}