console.log("JavaScript file connected successfully!");


document.addEventListener("DOMContentLoaded",()=>{
    const boxes = document.querySelectorAll('.repeating-box');
    const colors = [
        "#F6E5DA",
        "#D1E0D1",
        "#E3C2B5",
        "#A9BFA7",
        "#F4D7C5",
        "#D6C7BE"
      ];
      
      
      
      

    function getRandomColor(){
        return colors[Math.floor(Math.random()* colors.length)]

    }

    boxes.forEach(box=>{
        box.style.backgroundColor = getRandomColor();
    });
})