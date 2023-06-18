import {useState,useEffect} from 'react'
import { Link } from 'react-router-dom'

const Products = (props) => {

    const [products, setProducts] = useState([])
    const [search,setSearch] = useState('')
    const [newName,setNewName] = useState('')
    const [newPrice,setNewPrice] = useState(0)
    const [updateName,setupdateName,] = useState('')
    const [updatePrice,setupdatePrice] = useState(0)

    useEffect(() => all(),[])

    const all =  () => {
        fetch(`${process.env.REACT_APP_BASE_URL}/api/products/`)
        .then(res => res.json())
        .then(data =>{
            setProducts(data)
        })
        .catch(err => console.log(err))
    }
    
    const handleSearch = (e) => {
        e.preventDefault()
        fetch(`${process.env.REACT_APP_BASE_URL}/api/search?name=${search}`)
        .then(res => res.json())
        .then(data =>{
            setProducts(data)
        })
        .catch(err => console.log(err))
    }

    const handleAdd = (e) => {
        fetch(`${process.env.REACT_APP_BASE_URL}/api/products`,{
            method:"POST",
            headers: {
                'Content-Type': 'application/json'
              },
            body: JSON.stringify({
                name:newName,
                price:newPrice,
            })
        })
        .then(response => response.json())
        .then(data =>{
            console.log('data: ' + data)
        })
        .catch(err => console.log(err))
    }

    const handleUpdate = (e) => {
        e.preventDefault()
        const productId = products.find(item => item.name===updateName).id
        console.log(productId)
        fetch(`${process.env.REACT_APP_BASE_URL}/api/product/${productId}`,{
            method:"PUT",
            headers: {
                'Content-Type': 'application/json'
              },
            body: JSON.stringify({
                id: productId,
                name:updateName,
                price:updatePrice,
            })
        })
        .then(response => response.json())
        .then(data =>{
            console.log('data: ' + data)
        })
        .catch(err => console.log(err))
    }

    return(
        <div>
            <h1>Shop</h1>
            <form onSubmit={handleSearch}>
                <input type='text' name='search' onChange={(e) => setSearch(e.target.value)}/>
                <input type='submit' value='Search' />
            </form>
            <div style={{'display':'flex','flexDirection':'column'}}>
                
                <form onSubmit={handleAdd}>
                    <h5>Add Product</h5>
                    Name: <input type='text' name='name' onChange={(e) => setNewName(e.target.value)}/>
                    <br />
                    Price: <input type='text' name='price'onChange={(e) => setNewPrice(e.target.value)}/>
                    <br />
                    <input type='submit' value='Add' />
                </form>
                <form onSubmit={handleUpdate}>
                    <h5>Update Product</h5>
                    Name: <input type='text' name='name' onChange={(e) => setupdateName(e.target.value)}/>
                    <br />
                    Price: <input type='text' name='price'onChange={(e) => setupdatePrice(e.target.value)}/>
                    <br />
                    <input type='submit' value='Update' />
                </form>
            </div>
            <div style={{'display':'flex','flexDirection':'row','flexWrap':'wrap'}}>
                {
                    products.map(item => {
                        return(
                            <div key={item.id} style={{'border':'solid 1px white','margin':'30px','width':'100px'}}>
                                <h4>{item.name}</h4>
                                <h5>${item.price}</h5>
                                <Link to={'/product/'+item.id}>Shop Now</Link>
                            </div>
                        )
                    })
                }
            </div>
        </div>
    )
}

export default Products