import React from 'react';

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      errorInfo: null
    };
  }

  componentDidCatch(error, errorInfo) {
    this.setState({
      error: error,
      errorInfo: errorInfo
    });
  }

  componentDidUpdate(prevProps) {
    if (this.props.children !== prevProps.children) {
      this.setState({
        error: null,
        errorInfo: null
      });
    }
  }

  render() {
    if (this.state.errorInfo) {
      return (
        <>
          <h2>Something went wrong.</h2>
        </>
      );
    }

    return this.props.children;
  }
}

export default ErrorBoundary;
