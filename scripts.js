function button_post(){
  fetch("https://us-central1-primeiro-projeto-508116.cloudfunctions.net/teste-teste", {
    method: "POST",
    body: JSON.stringify({
      userId: 1,
      title: "Fix my bugs",
      completed: false
    }),
    headers: {
      "Content-type": "application/json",
      "nomenome": "js test"
    }
  }).then((response) => response.json())
    .then((json) => console.log(json));
}
