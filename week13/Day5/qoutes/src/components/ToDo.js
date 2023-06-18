import "bootstrap/dist/css/bootstrap.min.css";
import '../css/ToDo.css';

import {useState} from 'react'

const ToDo = (props) => {
    const [todos,setTodos] =  useState([
        {"id": 1,"content": "Buy some milk"},
        {"id": 2,"content": "Do my homework"},
    ])
    const [input,setInput] = useState('')

    const handleInput = (event) => {
        event.preventDefault()
        const newId = todos.length +1
        setTodos(prevList => [...prevList, {"id":newId,"content":input}])
        setInput('')
    }
    const deleteItem = (objId) => {
        setTodos(prevList => prevList.filter(item => item.id !==objId))
        
    }
    return(
        <>
            <div className ="todo-app container">
                <h1 className="center blue-text">To do</h1>
                <div className="todos collection"> 
                    {todos.length>0 ? (
                            todos.map(item => {
                                return(
                                    <div onClick={() => deleteItem(item.id)} key={item.id} className="collection-item">
                                        <span>{item.content}</span>
                                    </div>
                                )})
                        ) : (
                            <p class="center">You have no todo's left, yay!</p>
                        )} 
                    {}
                </div>
                
                <form>
                    <label>Add a new todo:</label>
                    <input type="text" name="newInput" value={input} onChange={(e) => setInput(e.target.value)} onKeyDown={(event) => {
                        if (event.key === 'Enter') {
                            handleInput(event)

                        }}}>
                    </input>
                </form>
            </div>
        </>
    )
}

export default ToDo