import {useState} from 'react'
import { connect } from 'react-redux'
import './style.css'

const Robots = (props) => {
    const [search,SetSearch] = useState()
    const robots = props.robots
    let robotsFilt = robots.filter(item => item.name.toLowerCase().includes(search.toLowerCase()));
    return(
        <>
            <header>
                <p id="logo">Robofriends</p>
                <input type="text" id="search" placeholder="Search for names.." onChange={(e) => SetSearch(e.target.value)}/>
            </header>
            <ul id="cardsList">
                {
                    robotsFilt.map(item=>{
                        return(
                            <li key={item.name} className='profiles'>
                                <img src={item.image}/>
                                <h2>{item.name}</h2>
                                <p>{item.email}</p>
                            </li>
                        )
                    })
                }
            </ul>
            
        </>
        
    )
}

const mapStateToProps = (state) => {
    return {
      robots:state
    }
  }

export default connect(mapStateToProps)(Robots)