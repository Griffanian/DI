import "./Exercise4.js"
import "./Exercise4.css"
const Exercise4 = () => {
    const style_header = {
        color: "white",
        backgroundColor: "DodgerBlue",
        padding: "10px",
        fontFamily: "Arial"
      };
    return (
        <>
            <h1 style={style_header}>
                This is a header
            </h1>
            <p className="para">This is a paragraph</p>
            <a href="/"> This is a link</a>
            <form>
                <label>Enter Your Name:</label><br />
                <input type="text" name="name"></input>
                <input type="submit" value={"submit"}></input>
            </form>
            <h5>Here is an image</h5>
            <img width={500} src="https://www.komododigital.co.uk/app/uploads/2021/05/React-1-1024x683.jpg" alt="react logo"></img>
            <h5>This is a list</h5>
            <ul>
                <li>Coffee</li>
                <li>Tea</li>
                <li>Milk</li>
            </ul>
        </>
      );
    };

export default Exercise4