import { useSelector,useDispatch } from "react-redux"
const Counter = (prop) => {
    const count = useSelector((state) => state.count)
    const dispatch = useDispatch()
    const incrementAsync = ()  => {
        return dispatch => {
          setTimeout(() => {
            dispatch({type:'INCREMENT',});
          }, 1000);
        };
      }
    return(
        <div style={{"padding":"30px","width":"350px","display":"flex","justifyContent":"space-around"}}>
            {count}
            <button onClick={()=>dispatch({type:'INCREMENT',})}> + </button>
            <button onClick={()=>dispatch({type:'DECREMENT',})}> - </button>
            <button onClick={()=>dispatch({type:'INCREMENTIFODD',})}> increment if odd</button>
            <button onClick={()=>dispatch(incrementAsync())}> increment async</button>
        </div>
    )
}

export default Counter