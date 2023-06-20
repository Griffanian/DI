const first = (store) => (next) => (action) => {
    console.log(`caught in the middleware ${JSON.stringify(store.getState())}`)
    const count = store.getState().count
    if (action.type === 'INCREMENTIFODD'){
        if (count%2===1){
            next({type: 'INCREMENT'});
        }
    } else {
        next(action);
    }
}

export {
    first,
}