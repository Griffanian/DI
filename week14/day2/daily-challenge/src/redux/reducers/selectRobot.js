export const selectRobot = (state='',action={}) => {
    switch (action.type) {
        case 'ROBOT_SELECTED':
            return {...state,movie:action.payload}
        default:
            return {...state}
    }
}