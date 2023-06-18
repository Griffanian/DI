export const movieSelected = (movie) => {
    return({
        type: 'MOVIE_SELECTED',
        payload: movie
    })
}