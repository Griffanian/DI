import {connect} from 'react-redux';
import { movieSelected } from '../redux/action';

const MovieList = (props) => {
    return(
        <ul>
        {props.movies?
            (props.movies.map(item => {
                    return(
                        <li style={{'display': 'block','width':'250px'}} key={item.title}>
                            <span>{item.title}</span>
                            <button style={{'float':'right'}} onClick={() => props.selectMovie(item)}>details</button>
                        </li>
                    )
                })):(
                    <p>Movies Not Loaded yet</p>
                )}
        </ul>
    )
}

const mapStateToProps = state => {
    // console.log('store test=>', state);
    return{
      movies: state.moviesReducer,
    }
  }

const mapDispatchToProps = dispatch => {
    return{
        selectMovie : (movie) => dispatch(movieSelected(movie))
    }
}

export default connect(mapStateToProps,mapDispatchToProps)(MovieList)