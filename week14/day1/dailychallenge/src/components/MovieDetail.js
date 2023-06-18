import {connect} from 'react-redux';

const MovieDetail = (props) => {
    console.log(props)
    return(props.movie?
        (<ul>
            <li>Title: {props.movie.title}</li>
            <li>Release Date: {props.movie.releaseDate}</li>
            <li>Rating: {props.movie.rating}</li>
        </ul>) : (
            <p>Not loaded yet</p>
        )
    )
}

const mapStateToProps = state => {
    console.log('store test=>', state);
    return{
      movie: state.selectedMovieReducer.movie,
    }
}

export default connect(mapStateToProps)(MovieDetail)