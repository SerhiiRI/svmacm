function imageJSONTemplate(image_name, tag, function_name){
    return JSON.stringify({
        "key" : decodeURIComponent(document.cookie).split("=")[1],
        "image" : image_name,
        "tag" : tag,
        "function" : function_name
        })
}

function imagesJSONTemplate(function_name){
    return JSON.stringify({
        "key" : decodeURIComponent(document.cookie).split("=")[1],
        "type" : "images",
        "function" : function_name
        })
}

function doFunction(HTMLTable){
    StartLoading();
    var buttons = document.getElementsByTagName("button");
    for (button of buttons){
        button.disabled=true;
    }
    var a = fetch("http://localhost:8777/images_", {
        method: 'POST',
        headers: {
            'Content-Type' :'application/json'
        },
        body: HTMLTable
    }).then((res) => {return res.text()}).then((htmlTableView) => {KillLoading(); document.getElementById("contentTable").innerHTML = htmlTableView});
}

function deleteallImages(){
    doFunction(imagesJSONTemplate("deleteall"));
}
function pruneallImages(){
    doFunction(imagesJSONTemplate("prune"));
}
function listallImages(){
    doFunction(imagesJSONTemplate("list"));
}

function pullImage(image_id, tag){
    doFunction(imageJSONTemplate(image_id, tag, "pull"));
}
function runImage(image_id, tag){
    doFunction(imageJSONTemplate(image_id, tag, "run"));
}
function deleteImage(image_id, tag){
    doFunction(imageJSONTemplate(image_id, tag,"delete"));
}