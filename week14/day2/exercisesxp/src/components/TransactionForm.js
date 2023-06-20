import React from 'react';
import {connect} from 'react-redux';
import { addTransaction } from '../redux/actions';

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
                <h1>props = {JSON.stringify(this.props)}</h1>
                <p>states = {JSON.stringify(this.state)}</p>
                <p>dispatch = {JSON.stringify(dispatch)}</p>
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

const mapDispatchToProps = (dispatch) => {
    return {
      add: () => dispatch(addTransaction),
    }
  }

export default connect(mapDispatchToProps,mapStateToProps)(TransactionForm)