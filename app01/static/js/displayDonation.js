function onload() {
    get_posts();
}

function add_posts(post){
    let posts = document.getElementById("posts");
    let name = post[0];
    let category = post[1];
    let filename = post[2];
    let seller = post[3];
    let price = post[4];
    let description = post[5];
    if (category == "Donate") {
        posts.innerHTML += 
        "<div class='card'>" + 
            '<img src="../../media/' + filename + '" style="width:100%" class="card-image"/>'+
            "<h1>" + name + "</h1>" +
            "<p class='price'>" + price + "</p>" +
            "<p class='description'>" + description + "</p>"+
            "<p><button>Details</button></p>"+
            // "<a href= ><button class='buttons'>Upload</button></a>"    redirecting to comment page for each item
        "</div>";}
}

function get_posts(){
    const request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            const posts = JSON.parse(this.response);
            for (const post of posts) {
                console.log(post);
                add_posts(post);
            }
        }
    };
    request.open("GET", "/loadposts");
    request.send();
}