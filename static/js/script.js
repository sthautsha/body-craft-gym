const sidebarActive = () => {
    var a = document.querySelectorAll(".sidebarlinks a");


    var b = window.location.href.toString().split("/")[3];

    for (var i = 0, length = a.length; i < length; i++) {
        var c = a[i].href.toString().split("/")[3];

        if (c == b) {

            a[i].classList.add("active")
        }
    }


}
sidebarActive();




const togglePassword = document.querySelector("#eyeIcon");
const password = document.querySelector("#password");

const toggleBtn = () => {
    console.log(password.getAttribute("type"));

   
    const type = password.getAttribute("type") === "password" ? "text" : "password";
    password.setAttribute("type", type);
    console.log(type);
    

    console.log(password.getAttribute("type"));
    
    if (password.getAttribute("type") === "password") {
        
        togglePassword.innerHTML =
            `<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true" role="img" width="1em" height="1em" preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24"><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2 10s3.5 4 10 4s10-4 10-4M4 11.645L2 14m20 0l-1.996-2.352M8.914 13.68L8 16.5m7.063-2.812L16 16.5"/></svg>`;
       
        
        return
    }
    if (password.getAttribute("type") === "text") {
        
   
        togglePassword.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                                    aria-hidden="true" role="img" width="1em" height="1em"
                                    preserveAspectRatio="xMidYMid meet" viewBox="0 0 24 24">
                                    <g fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"
                                        stroke-width="2">
                                        <path
                                            d="M21.257 10.962c.474.62.474 1.457 0 2.076C19.764 14.987 16.182 19 12 19c-4.182 0-7.764-4.013-9.257-5.962a1.692 1.692 0 0 1 0-2.076C4.236 9.013 7.818 5 12 5c4.182 0 7.764 4.013 9.257 5.962Z" />
                                        <circle cx="12" cy="12" r="3" />
                                    </g>
                                </svg>`;
    } 
}
toggleBtn();