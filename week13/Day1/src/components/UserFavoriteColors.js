const userFavoriteColors = (props) => {
    const {favAnimals } = props
    return (
        <div>
          <h1>User's Favorite Animals:</h1>
          <ul>
            {favAnimals.map((animal, index) => (
              <li key={index}>{animal}</li>
            ))}
          </ul>
        </div>
      );
    };

export default userFavoriteColors