
import './App.css';
import addproducts from './components/addproducts';
import ShowProducts from './components/showproducts';
import {BrowserRouter as Router,Routes,Route} from "react-router-dom"


function App() {
  return (
    <div className="App">
         <Router>
          <Routes>
            <Route exact path='/' Component={ShowProducts}></Route>
            <Route exact path='/addproduct' Component={addproducts}></Route>
          </Routes>
         </Router>
    </div>
  );
}

export default App;
