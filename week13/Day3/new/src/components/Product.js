import {useState,useEffect} from 'react'
import { useParams,Link } from 'react-router-dom'

const Product = (props) => {
    const[product, setProduct] = useState([])

    const params = useParams()
    
    useEffect(()=>{
        getProductInfo()
    },[])

    const getProductInfo = async () => {
        try {
            const res = await fetch(`http://localhost:3030/api/products/${params.id}`)
            const data = await res.json()
            setProduct(data)
        } catch(e) {
            console.log(e)
        }
    }
    return (
        <div>
            <h1>Product {params.id}</h1>
            {
                product.map(item => {
                    return(
                        <div key={item.id} style={{'border':'solid 1px white','margin':'30px','width':'100px'}}>
                                <h4>{item.name}</h4>
                                <h5>${item.price}</h5>
                                <Link to='/product'>Back to Shop</Link>
                            </div>
                    )
                })
            }
        </div>
    )
}

export default Product