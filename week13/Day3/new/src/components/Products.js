import {useState,useEffect} from 'react'

const Products = (props) => {

    const [products, setProducts] = useState([])
    const [search,setSearch] = useState('')
    const [newName,setNewName] = useState('')
    const [newPrice,setNewPrice] = useState(0)

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

    const handleSubmit = (e) => {
        

        console.log('name: ' + newName + ' price ' + newPrice)
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
    return(
        <div>
            <h1>Shop</h1>
            <form onSubmit={handleSearch}>
                <input type='text' name='search' onChange={(e) => setSearch(e.target.value)}/>
                <input type='submit' value='Search' />
            </form>
            <div style={{'display':'flex','flexDirection':'column'}}>
                <form onSubmit={handleSubmit}>
                    <input type='text' name='name' onChange={(e) => setNewName(e.target.value)}/>
                    <input type='text' name='price'onChange={(e) => setNewPrice(e.target.value)}/>
                    <input type='submit' value='Add' />
                </form>
            </div>
            <div style={{'display':'flex','flexDirection':'row'}}>
                {
                    products.map(item => {
                        return(
                            <div key={item.id} style={{'border':'solid 1px white','margin':'30px','width':'100px'}}>
                                <h4>{item.name}</h4>
                                <h5>{item.price}</h5>
                            </div>
                        )
                    })
                }
            </div>
        </div>
    )
}

export default Products