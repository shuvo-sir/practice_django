
let Username = document.getElementById("username");
let Password = document.getElementById("password");


let eyeL = document.querySelector(".eyeball-l");
let eyeR = document.querySelector(".eyeball-r");
let handL = document.querySelector(".hand-l");
let handR = document.querySelector(".hand-r");


let normalEyeStyle = () => {
    eyeL.style.cssText = `
        left: 0.96em;
        top: 0.96em;
        `;

    eyeR.style.cssText = `
        right: 0.96em;
        top: 0.96em;
        `;    
};


let normalHandStyle = () => {
    handL.style.cssText = `
}
        height: 4.496rem;
        top: 13.44rem;
        left: 16.8rem;
        transform: rotate(0deg);
        `;

    handR.style.cssText = `
}
        height: 4.496rem;
        top: 13.44rem;
        right: 16.8rem;
        transform: rotate(0deg);
        `;

};


Username.addEventListener("focus", () => {
    eyeL.style.cssText = `
        top: 2rem;
        left: 1.3rem;  
        `;

    eyeR.style.cssText = `
        top: 2rem;
        right: 1.3rem;
        `;
    normalHandStyle();
});

Password.addEventListener("focus", () => {
    handL.style.cssText = `
        height: 12.096em;
        top: 2.992em;
        left: 12em;
        transform: rotate(155deg);
        `;


    handR.style.cssText = `
        height: 12.096em;
        top: 2.992em;
        right: 12em;
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

