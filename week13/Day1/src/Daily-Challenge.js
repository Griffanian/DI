import React from 'react';
import "react-responsive-carousel/lib/styles/carousel.min.css";
import { Carousel } from 'react-responsive-carousel';
import "./components/DailyChallenge.css"

class DailyChallenge extends React.Component{
    render(){
        return (
            <div style={{"display":"flex","justifyContent":"center"}}>
                <Carousel width={"500px"}>
                    <div>
                        <img src="https://res.klook.com/image/upload/fl_lossy.progressive,q_65/c_fill,w_480,h_384/cities/jrfyzvgzvhs1iylduuhj.jpg" alt='Hong kong Ship' />
                        <p className="legend">Hong Kong</p>
                    </div>
                    <div>
                        <img src="https://res.klook.com/image/upload/fl_lossy.progressive,q_65/c_fill,w_480,h_384/cities/c1cklkyp6ms02tougufx.webp" alt="Macao Building" />
                        <p className="legend">Macao</p>
                    </div>
                    <div>
                        <img src="https://res.klook.com/image/upload/fl_lossy.progressive,q_65/c_fill,w_480,h_384/cities/e8fnw35p6zgusq218foj.webp" alt="Japan Light House" />
                        <p className="legend">Japan</p>
                    </div>
                    <div>
                        <img src="https://res.klook.com/image/upload/fl_lossy.progressive,q_65/c_fill,w_480,h_384/cities/liw377az16sxmp9a6ylg.webp" alt="Las Vegas Skyline " />
                        <p className="legend">Las Vegas</p>
                    </div>
                </Carousel>
            </div>
        )
    }
}

export default DailyChallenge