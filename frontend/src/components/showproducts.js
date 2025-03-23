import React, { useState, useEffect } from "react";
import axios from "axios";
import "./ShowProducts.css";

const defaultImage = "https://via.placeholder.com/180x180?text=No+Image"; // Placeholder image for missing products

const ShowProducts = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/") // Replace with actual API URL
      .then((response) => setProducts(response.data))
      .catch((error) => console.error("Error fetching products:", error));
  }, []);

  return (
    <div className="products-container">
      <h2>Show all products</h2>
      <div className="product-grid">
        {products.map((product, index) => (
          <div className="product-card" key={index}>
            <div className="image-container">
              <img 
                src={product.image || defaultImage} 
                alt={product.name} 
                onError={(e) => e.target.src = defaultImage} // If image fails to load, replace with default
              />
            </div>
            <h3 className="product-name">{product.name}</h3>
            <p className="time-left">⏳ <span>{product.time_left}</span></p>
            <p><strong>Category:</strong> {product.category}</p>
            <p><strong>Starting Bid:</strong> {product.starting_bid}</p>
            <button className="view-details">View Details</button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default ShowProducts;
