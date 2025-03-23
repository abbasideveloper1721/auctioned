import React from "react";
import { useState,useEffect} from "react";
import axios from 'axios'

const ShowProducts = () => {

const [products,setProducts] = useState([])
const getProducts = async() =>{
    const response = await axios.get('http://127.0.0.1:8000/api/')
    setProducts(response.data)

}
useEffect(()=> {
    getProducts();

},[])
 


    return(
        <div>
            <h1>Show all products</h1>
        {
            products.map((products,index) => (
                <div>
                    <img src={products.image}></img>
                    <p>{products.name}</p>
                    <p>{products.category}</p>
                    <p>{products.starting_bid}</p>
                    <p>{products.bid_start_date}</p>
                    <p>{products.auction_duration}</p>
                    <p>{products.bid_end_date}</p>
                    <p>{products.time_left}</p>
                    <p>{products.status}</p>
                </div>
            ))
        }

        </div>
    );
};
export default ShowProducts;
