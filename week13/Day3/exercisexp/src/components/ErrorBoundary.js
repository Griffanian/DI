import React from "react";

class ErrorBoundary extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            hasError: false,
            error: null,
            errorInfo: null
        };
    }

    componentDidCatch(error, errorInfo) {
        this.setState({
            hasError: true,
            error: error,
            errorInfo: errorInfo
        });
    }

    render() {
        if (this.state.hasError) {
            let arr = this.state.errorInfo['componentStack'].split('\n    ')
            return (
                <div>
                    <h1>{(this.state.error.toString())}</h1>
                    {
                        arr.map(item => {
                            return(<p>{item}</p>)
                        })
                    }
                </div>
            );
        }
        return this.props.children;
    }
}

export default ErrorBoundary;
