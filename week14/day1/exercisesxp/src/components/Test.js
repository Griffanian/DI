import { connect } from "react-redux"

const Test = (props) => {
    return(
        <>
            <h1>{props.title}</h1>
            <button onClick={props.setTitle('Test')}>Change title</button>
        </>
    )
}
const mapStateToProps = (state) => {
    return {
      b:state.property_two
    }
  }

export default connect(mapStateToProps)(Test)