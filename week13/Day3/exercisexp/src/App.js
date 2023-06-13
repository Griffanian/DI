// import ErrorBoundary from './components/ErrorBoundary';
// import BuggyCounter from './components/BuggyCounter';
// import { Color } from "./components/Color";
// import { Child } from "./components/Color";
import FormComp from "./components/FormComp";
function App() {
  return (
    // Exercise 1

    // <div className="App" style={{'margin':'20px'}}>
    //   <hr />
    //   <ErrorBoundary>
    //     <BuggyCounter />
    //     <BuggyCounter />
    //   </ErrorBoundary>
    //   <hr />
    //   <hr />
    //   <ErrorBoundary>
    //     <BuggyCounter />
    //   </ErrorBoundary>
    //   <ErrorBoundary>
    //     <BuggyCounter />
    //   </ErrorBoundary>
    //   <hr />
    // </div>

    // Exercise 2 / daily challenge
    <>
      {/* <Color /> */}
      {/* <Child /> */}
      <FormComp />
    </>
  );
}

export default App;
