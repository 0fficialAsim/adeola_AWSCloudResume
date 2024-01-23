
async function updateVisitors(){
    const response = await fetch(" https://d5xqrfl4ih.execute-api.us-east-1.amazonaws.com/DBconnect", {
        method: "POST",
        headers: {"Content-type":"application/json"} 
    });

    const visitors = await response.json(); 
    
    return visitors;
}

function getCount(){
    const count =  updateVisitors().then((data) =>  
    document.getElementById('count').innerText = "Welcome! You are visitor number " + (data)) 
}

getCount();
