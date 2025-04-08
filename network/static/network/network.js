// Liking the post
function like(id){
    fetch(`/like/${id}`,{
        method: 'POST'    
    })
    .then(response => response.json())
    .then(result => {

        // Like button toggle styel
        const icon = document.querySelector(`#likeToggle-${id}`);

        if (result.likeToggle){
            icon.classList.remove('fa', 'fa-heart-o');
            icon.classList.add('fa', 'fa-heart');
        } else {
            icon.classList.remove('fa', 'fa-heart');
            icon.classList.add('fa', 'fa-heart-o');
        }

        // Count
        const count = document.querySelector(`#count-${id}`);
        result['likes'] > 0 ? count.innerHTML = result['likes'] : count.innerHTML = ""
    });
}

// Editing post
function edit(id){
    document.querySelector(`#content-${id}`).style.display='none';
    document.querySelector(`#editbtn-${id}`).style.display='none';
    document.querySelector(`#savebtn-${id}`).style.display='block';
    document.querySelector(`#edit-${id}`).style.display='block';
}

// Saving post after editing
function save(id){
    const content = document.querySelector(`#edit-${id}`).value;

    fetch(`/edit/${id}`,{
        method: 'POST',
        body: JSON.stringify({
            'content' : content
        })
    })
    .then(response => response.json())
    .then(result => {

        const updatedContent = document.querySelector(`#content-${id}`);

        updatedContent.innerHTML = content;

        updatedContent.style.display='block';
        document.querySelector(`#editbtn-${id}`).style.display='block';
        document.querySelector(`#savebtn-${id}`).style.display='none';
        document.querySelector(`#edit-${id}`).style.display='none'; 
    });
}