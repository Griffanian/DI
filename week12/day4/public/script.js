function runLogin(event){
    event.preventDefault()
    const loginForm = document.forms['login']
    const loginInfo = document.getElementById('loginInfo')
    let username = loginForm['username'].value
    let password = loginForm['password'].value
    if (username && password){
        loginForm.reset();
        loginInfo.textContent = 'ok'
    } else {
        loginInfo.textContent = 'Please enter a username and a password'
    }
}

function runRegister(event){
    // event.preventDefault()
    const registerForm = document.forms['register']
    const resgisterInfo = document.getElementById('resgisterInfo')
    let fname = registerForm['fname'].value
    let lname = registerForm['lname'].value
    let email = registerForm['lname'].value
    let username = registerForm['username'].value
    let password = registerForm['password'].value
    let userData = {
        fname,
        lname,
        email,
        username,
        password}
    if (fname && lname && username && password ){
        fetch('http://localhost:3000/user',{
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body: JSON.stringify(userData)
        })
        .then(res => res.json())
        .then(data => {
        //   console.log(data);
          resgisterInfo.textContent = `${data.message}`
          registerForm.reset();
        })
        .catch(err => {
          console.log(err);
        })
    } else {
        resgisterInfo.textContent = 'Please enter a username and a password'
    }
}