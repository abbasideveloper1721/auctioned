import React from "react";
import { useState,useEffect} from "react";
import axios from 'axios'

const ShowProducts = () => {

const [products,setProducts] = useState([])
const getProducts = async() =>{
    const response = await axios.get('http://127.0.0.1:8000/api/')
    console.log(response.data)

}
useEffect(()=> {
    getProducts();

},[])
 


    return(
        <div>Show all products</div>
    );
};
export default ShowProducts;
