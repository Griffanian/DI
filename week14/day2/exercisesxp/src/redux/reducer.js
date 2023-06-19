const initState = {
    transList : [1]
}

export const reducer = (state=initState, action={}) =>{
    switch (action.type){
        case 'ADD':
            return {...state, transList:state.transList.push(action.payload)}
        default:
            return {...state}
    }
}