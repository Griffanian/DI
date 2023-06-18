import { combineReducers } from 'redux'
import { selectedMovieReducer } from './selectedMovie'
import { moviesReducer } from './allMovies'

export default combineReducers({
    selectedMovieReducer,
    moviesReducer
})
