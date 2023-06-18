export const selectedMovieReducer = (state = '',action={}) => {
    switch (action.type) {
        case 'MOVIE_SELECTED':
            return {...state,movie:action.payload}
        default:
            return {...state}
    }
}