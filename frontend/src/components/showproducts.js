import React, { useState, useEffect } from "react";
import axios from "axios";
import "./ShowProducts.css";

const defaultImage = "https://via.placeholder.com/180x180?text=No+Image"; // Placeholder image

const ShowProducts = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/") // Replace with actual API URL
      .then((response) => {
        const updatedProducts = response.data.map((product) => ({
          ...product,
          timeLeft: calculateTimeLeft(product.bid_end_date),
        }));
        setProducts(updatedProducts);
      })
      .catch((error) => console.error("Error fetching products:", error));
  }, []);

  useEffect(() => {
    const timer = setInterval(() => {
      setProducts((prevProducts) =>
        prevProducts.map((product) => ({
          ...product,
          timeLeft: calculateTimeLeft(product.bid_end_date),
        }))
      );
    }, 1000);

    return () => clearInterval(timer);
  }, []);

  const calculateTimeLeft = (endTime) => {
    const now = new Date().getTime();
    const end = new Date(endTime).getTime();
    const difference = end - now;

    if (difference > 0) {
      const totalHours = Math.floor(difference / (1000 * 60 * 60)); // Get total hours
      const minutes = Math.floor((difference / (1000 * 60)) % 60);
      const seconds = Math.floor((difference / 1000) % 60);

      return `${totalHours}:${minutes < 10 ? "0" : ""}${minutes}:${seconds < 10 ? "0" : ""}${seconds}`;
    }
    return "00:00:00"; // Auction ended
  };

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
                onError={(e) => e.target.src = defaultImage} 
              />
            </div>
            <h3 className="product-name">{product.name}</h3>
            <p className="time-left">⏳ <span>{product.timeLeft}</span></p>
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
