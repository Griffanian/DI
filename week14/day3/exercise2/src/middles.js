const first = (store) => (next) => (action) => {
    console.log("---IN THE MIDDLEWARE---")
    console.log(`Redux Log:`, action)    
    next(action);
}

export {
    first,
}