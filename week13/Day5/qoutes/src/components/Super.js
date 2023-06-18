import '../css/Super.css';
import superheroes from '../superheroes.json'

import {useState,useEffect} from 'react'

const Super = (props) => {

    let superheroesObj = superheroes.superheroes

    const [clicked,setClicked] = useState([])
    const [curScore,setCurScore] = useState(0)
    const [topScore,setTopScore] = useState(0)

    const checkDeath = (name) => {
        if (clicked.includes(name)){
            setClicked([])
            setCurScore(0)
            if (curScore > topScore){
                setTopScore(curScore)
            }
            
            return true
        } else {
            return false
        }
    }

    const shuffleCards = () => {
        for (let i = superheroesObj.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [superheroesObj[i], superheroesObj[j]] = [superheroesObj[j], superheroesObj[i]];
          }
    }

    const handleClick = (name) => {
        if (!checkDeath(name)){
            setClicked(prevList => [...prevList, name])
            setCurScore(curScore+1)
            shuffleCards()
        }
    }

    useEffect(() => {
        console.log('clicked: ' + clicked);
        console.log('curScore: ' + curScore);
      }, [clicked,curScore]);

    return(
        <div className="wrapper">
            <header className="container-fluid fixed-top">
                <div className="row">
                    <h1 className="col-sm-8">Superheroes Memory Game</h1>
                    <nav className="col-sm-4">
                        <p>Score: <span>{curScore}</span></p>
                        <p>Top Score: <span>{topScore}</span></p>
                    </nav>
                </div>
            </header>
            <div className="jumbotron jumbotron-fluid">
                <div className="container">
                    <p className="lead">Get points by clicking on an image but don't click on any more than once!</p>
                </div>
            </div>
            {
                superheroesObj.map(item => {
                    return(
                        <div onClick={() => handleClick(item.name)} key={item.name} className="card ">
                            <div className="img-container">
                                <img alt={item.name} src={item.image}/>
                            </div>
                            <div className="img-content">
                                <ul>
                                    <li><strong>Name: </strong>{item.name}</li>
                                    <li><strong>Occupation: </strong>{item.occupation}</li>
                                </ul>
                            </div>
                        </div>
                    )
                })
            }
        </div>
    )
}
export default Super