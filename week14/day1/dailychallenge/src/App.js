import MovieList from './components/MovieList';
import MovieDetail from './components/MovieDetail';
function App() {
  return (
    <div style={{'display':'flex','justifyContent':'space-around'}}>
      <div>
        <h3>Movie List</h3>
        <MovieList />
      </div>
      <div style={{'float':'right'}}>
        <h3>Movie Details</h3>
        <MovieDetail />
      </div>
    </div>
  );
}

export default App;
