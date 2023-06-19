import React from 'react';
import {connect} from 'react-redux';
import store from '../redux/store';

class TransactionForm extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            accountNumber:0,
            FSC:0,
            name:'',
            amount:0,
        }
    }

    handleSubmit = (event) => {
        event.preventDefault()
        console.log(this.state)
    }
    componentDidMount = () => {
        console.log(store.getState())
        console.log('props=> ' + this.props);
    }
    render(){
        return(
            <>
                <h1>Financial Transactions:</h1>
                <form onSubmit={(e) => this.handleSubmit(e)}>
                    <input name="bAccountNo" placeholder="Account Number" onChange={(e) => this.setState({accountNumber:e.target.value})}/>
                    <br/>
                    <input name="FSC" placeholder="FSC"  onChange={(e) => this.setState({FSC:e.target.value})}/>
                    <br/>
                    <input name="bName" placeholder="A/C Holder Name"  onChange={(e) => this.setState({name:e.target.value})}/>
                    <br/>
                    <input name="amount" placeholder="Amount" onChange={(e) => this.setState({amount:e.target.value})}/>
                    <br/>
                    <button type="submit">Submit</button>
                </form>
                <h1>{JSON.stringify(this.props)}</h1>
                <h1>{JSON.stringify(store)}</h1>
                <hr/>
                <table>
                    <tbody>
                        <tr>
                            <td>213</td>
                            <td>asdasd</td>
                            <td>121321</td>
                            <td><button>Edit</button></td>
                            <td><button>Delete</button></td>
                        </tr>
                    </tbody>
                </table>
            </>
        )
    }
}
const mapStateToProps = (state) => {
    return { state }
}

export default connect(mapStateToProps)(TransactionForm)