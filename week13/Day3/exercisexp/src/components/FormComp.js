import { useState } from "react"; 

const FormComp = (props) => {
    const [fname,setFname] = useState('')
    const [lname,setLname] = useState('')
    const [age,setAge] = useState(0)
    const [gender,setGender] = useState('')
    const [destination,setDestination] = useState('')
    const [nuts,setNuts] = useState(false)
    const [lact,setLact] = useState(false)
    const [vegan,setVegan] = useState(false)

    return(
        <>
            <form style={{'display':'flex','flexDirection':'column','alignItems':'flex-start'}}> 
                <input type='text' name='fname' placeholder="First Name" onChange={(e) => setFname(e.target.value)}/>
                <br />
                <input type='text' name='lname' placeholder="Last Name" onChange={(e) => setLname(e.target.value)}/>
                <br />
                <input type='text' name='age'  placeholder="age" onChange={(e) => setAge(e.target.value)}/>
                <br />
                <label>
                    <input type="radio" name="gender"value="Male" onChange={(e) => setGender(e.target.value)}/>
                    Male
                </label>
                <label>
                    <input type="radio" name="gender"value="Female" onChange={(e) => setGender(e.target.value)}/>
                    Female
                </label>
                <br />
                <select name='destination' onChange={(e) => setDestination(e.target.value)}>
                    <option value="">-- Please Choose a destination --</option>
                    <option value="Thailand">Thailand</option>
                    <option value="Japan">Japan</option>
                    <option value="Japan">Japan</option>
                </select>
                <br />
                <label>
                    <input type='checkbox' name='nuts' onChange={(e) => setNuts(e.target.value)}/>
                    Nuts free
                </label>
                <label>
                    <input type='checkbox' name='lact' onChange={(e) => setLact(e.target.value)}/>
                    Lactose Free
                </label>
                <label>
                    <input type='checkbox' name='vegan' onChange={(e) => {setVegan(e.target.value)}}/>
                    Vegan
                </label>
                <input type="submit" value="submit"></input>
            </form>
            <div>
                <p>First Name: {fname}</p>
                <p>Last Name: {lname}</p>
                <p>Age: {age}</p>
                <p>Gender: {gender}</p>
                <p>Destination: {destination}</p>
                <p>Nuts: {nuts ? 'Yes' : 'No'}</p>
                <p>Lactose Intolerant: {lact ? 'Yes' : 'No'}</p>
                <p>Vegan: {vegan ? 'Yes' : 'No'}</p>
            </div>
        </>
    )
}

export default FormComp