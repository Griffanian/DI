import { useSelector,useDispatch } from "react-redux"
const Age = (prop) => {
    const age = useSelector((state) => state.age)
    const dispatch = useDispatch()
    return(
        <div style={{"padding":"30px","width":"350px","display":"flex","justifyContent":"space-around"}}>
            {age}
            <button onClick={()=>dispatch({type:'INCREMENT',})}> + </button>
            <button onClick={()=>dispatch({type:'DECREMENT',})}> - </button>
        </div>
    )
}

export default Age