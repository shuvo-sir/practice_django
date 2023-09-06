
let Username = document.getElementById("username");
let Password = document.getElementById("password");


let eyeL = document.querySelector(".eyeball-l");
let eyeR = document.querySelector(".eyeball-r");
let handL = document.querySelector(".hand-l");
let handR = document.querySelector(".hand-r");


let normalEyeStyle = () => {
    eyeL.style.cssText = `
        left: 0.6em;
        top: 0.6em;
        `;

    eyeR.style.cssText = `
        right: 0.6em;
        top: 0.6em;
        `;    
};


let normalHandStyle = () => {
    handL.style.cssText = `
        height: 2.81em;
        top: 8.4em;
        left: 10.5em;
        transform: rotate(0deg);
        `;

    handR.style.cssText = `
        height: 2.81em;
        top: 8.4em;
        right: 10.5em;
        transform: rotate(0deg);
        `;

};


Username.addEventListener("focus", () => {
    eyeL.style.cssText = `
        left: 0.75em;
        top: 1.12em;
        `;

    eyeR.style.cssText = `
        right: 0.75em;
        top: 1.12em;
        `;
    normalHandStyle();
});

Password.addEventListener("focus", () => {
    handL.style.cssText = `
        height: 7.56em;
        top: 1.87em;
        left: 7.50em;
        transform: rotate(155deg);
        `;


    handR.style.cssText = `
        height: 7.56em;
        top: 1.87em;
        right: 7.50em;
        transform: rotate(-155deg);
        `;
    normalEyeStyle();
});



document.addEventListener("click", (e) => {
    let clickedElem = e.target;
    if (clickedElem != Username && clickedElem != Password) {
        normalEyeStyle();
        normalHandStyle();
    }
});

