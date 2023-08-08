async function jsonurl(url) {
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
}
jsonurl("https://dummyjson.com/products");
