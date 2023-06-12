const Car = (props) => {
    return(
        <header>
            <p>Name: {props.carinfo.name}</p>
            <p>Model: {props.carinfo.model}</p>
        </header>
    )
}

export default Car